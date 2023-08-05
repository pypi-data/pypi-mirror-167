##########################################################################
# Manipylator - a Python-driven manipulator controller                   #
# Authors: Arthur Michaut                                                #
# Copyright 2020-2022 Institut Pasteur and CNRS–UMR3738                  #
# See the COPYRIGHT file for details                                     #
#                                                                        #
# This file is part of manipylator package.                              #
#                                                                        #
# Manipylator is free software: you can redistribute it and/or modify    #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# Manipylator is distributed in the hope that it will be useful,         #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the           #
# GNU General Public License for more details .                          #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with Manipylator (COPYING).                                      #
# If not, see <https://www.gnu.org/licenses/>.                           #
##########################################################################

import os.path as osp
import os
import sys
import datetime
import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pipython import GCSDevice, pitools
from simple_pid import PID

from manipylator.analysis import detect_bead


# current directory used as default argument
cwd = os.getcwd()

# useful color list for plotting
color_list = [c['color'] for c in list(plt.rcParams['axes.prop_cycle'])] + sns.color_palette("Set1", n_colors=9,desat=.5)


def get_stage_prop(kind='piezo'):
    """
    Export properties of stages for 2 kinds of PI stage.
    - M110.1DG1 referred as 'stepper'
    - P-625.1CD referred as 'piezo'
    """

    if kind == 'piezo':
        stage_properties = {'controller_name': 'E-709',
                            'USB_serialnum': '0120040211',
                            'stage_axis': 'X',
                            'stage_max_bound': 500,  # in um
                            'stage_min_bound': 0,  # in um
                            'stage_orientation': -1,  # orientation with respect to image
                            'stage_scaling': 1,  # scaling to convert to the stage natural unit
                            'stage_name': None,  # stages arg in pitools.startup
                            'stage_refmodes': None,  # refmodes arg in pitools.startup
                            }
    elif kind == 'stepper':
        stage_properties = {'controller_name': 'C-863.11',
                            'USB_serialnum': '0205500017',
                            'stage_axis': '1',
                            'stage_max_bound': 5000,
                            # in um -> needs to converted to mm as mm is the natural unit of the stage
                            'stage_min_bound': 0,  # in um
                            'stage_orientation': -1,  # orientation with respect to image
                            'stage_scaling': 0.001,  # scaling to convert to the stage natural unit
                            'stage_name': 'M-110.1DG1',  # stages arg in pitools.startup
                            'stage_refmodes': 'FNL',  # refmodes arg in pitools.startup
                            }
    else:
        stage_properties = None
        raise Exception('Error: {} is not a supported kind of stage. Supported kinds: piezo, stepper')

    return stage_properties


class Controller:
    """
    A class with extended methods to control a PI stage and apply controlled deflections
    """

    def __init__(self, stage_properties, tip_properties=None):
        """
        A controller is defined by the PI device properties. Optionally, the deflection can be controlled by tracking the device's tip
        """
        # stage parameters
        self.pidevice = None  # pidevice to be initialize by connect()
        self.controller_name = stage_properties['controller_name']
        self.USB_serialnum = stage_properties['USB_serialnum']
        self.stage_axis = stage_properties['stage_axis']
        self.stage_max_bound = stage_properties['stage_max_bound']
        self.stage_min_bound = stage_properties['stage_min_bound']
        self.stage_orientation = stage_properties['stage_orientation']  # orientation with respect to image
        self.stage_scaling = stage_properties['stage_scaling']  # scaling to convert to the stage natural unit
        self.stage_name = stage_properties['stage_name']  # stages arg in pitools.startup
        self.stage_refmodes = stage_properties['stage_refmodes']  ## refmodes arg in pitools.startup
        self.virtual = False  # make a virtual stage
        self.stage_raw_pos = None  # stage raw position (output of get_pos())
        self.stage_pos = None  # transformed stage position (output of transform_stage_pos(pos))
        self.move_seq_data = None  # a dict to store positions when move_sequence is called

        # initialize tip parameters
        self.tip_dir = None  # directory to tip image
        self.tip_fn_filter = None  # some keyword filtering in image filename
        self.tip_last_fn = None  # last file of tip image
        self.tip_radius = None  # tip radius in px
        self.tip_radius_err = None  # radius error
        self.tip_blur = None  # gaussian blur before canny
        self.tip_low_threshold = None  # canny filter low threshold
        self.tip_high_threshold = None  # canny filter high threshold
        self.tip_axis = 'x'  # axis of tip movement in image ('x' or 'y')
        self.tip_lengthscale = None  # image pixel size in um/px
        self.offset_0 = None  # offset for deflection = 0
        self.sign = None  # sign of deflection
        self.PID_data = None  # a dict collecting data when a PID controller is run
        self.tip_pos = None  # tip position in scaled data update by get_offset()
        self.tip_pattern = None  # a 2D numpy array being the ROI of a 8bit image
        self.tip_method = None  # tip detection method: "pattern" or "hough_circle"
        self.tip_intensity = None  # tip mean intensity 
        self.update_tip_pattern = False  # update tip_pattern with last detected 

        # set tip parameters if given
        if tip_properties is not None:
            for k in tip_properties.keys():
                setattr(self,k,tip_properties[k])


    def update_properties(self, stage_properties=None, tip_properties=None):
        """
        Update controller properties with dict of properties
        """
        if stage_properties is not None:
            for k in tip_properties.keys():
                setattr(self,k,stage_properties[k])

        if tip_properties is not None:
            for k in tip_properties.keys():
                setattr(self,k,tip_properties[k])


    def connect(self, virtual=False):
        """
        Method to connect PI device
        """
        if not virtual:
            pidevice = GCSDevice(self.controller_name)
            pidevice.ConnectUSB(serialnum=self.USB_serialnum)
            pitools.startup(pidevice, stages=self.stage_name, refmodes=self.stage_refmodes)
            self.pidevice = pidevice
            print('connected: {}'.format(pidevice.qIDN().strip()))
            self.set_servo('on')
            self.stage_raw_pos = self.get_pos()
        else:
            self.virtual = True
            self.stage_raw_pos = 0
            print('Running a virtual stage')

        # initialize transformed stage pos
        self.stage_pos = self.transform_stage_pos(self.stage_raw_pos)
        print('Stage raw position: {} um. \nStage transformed position: {} um.'.format(self.stage_raw_pos,
                                                                                       self.stage_pos))


    def check_connection(self):
        """
        Method to check stage connection
        """
        if self.pidevice is None:
            raise Exception("ERROR: no device conntected. Aborting")


    def set_servo(self, status, verbose=True):
        """Set servo on or off. status is a string or a boolean"""

        # check status
        if type(status) is str:
            if status == 'on' or status == 'off':
                status = 1 if status == 'on' else 0
            else:
                print("Error: invalid value for status. It needs to be a boolean or a string 'on' or 'off'")

        # set servo
        if not self.virtual:
            self.check_connection()

            # get status before setting new
            svo_status_before = 'on' if self.pidevice.qSVO(self.stage_axis)[self.stage_axis] else 'off'

            # set servo
            self.pidevice.SVO(self.stage_axis, status)

            # get status after setting new
            svo_status_after = 'on' if self.pidevice.qSVO(self.stage_axis)[self.stage_axis] else 'off'

            if verbose:
                print('servo was {}, it is now {}'.format(svo_status_before, svo_status_after))

        else:
            if verbose:
                print('virtual servo set to {}'.format(status))


    def get_pos(self, print_pos=False, store_pos=True):
        """
        Get current position. 
        Store positions in attributes if store_pos=True 
        """
        if not self.virtual:
            # measure position
            self.check_connection()
            pos = self.pidevice.qPOS(self.stage_axis)[self.stage_axis]
            pos /= self.stage_scaling  # convert from stage natural unit to um

            if store_pos:
                self.stage_raw_pos = pos
                self.stage_pos = self.transform_stage_pos(pos)
        else:
            pos = self.stage_raw_pos
            if store_pos:
                self.stage_pos = self.transform_stage_pos(pos)

        if print_pos:
            print('position = {} um'.format(pos))
        return pos


    def move(self, pos):
        """
        Move stage to a position 
        pos: float, position in the stage referential (raw_pos) in um
        """

        # ensure pos is stage range
        if pos >= self.stage_min_bound and pos <= self.stage_max_bound:
            if not self.virtual:
                #self.check_connection()
                pos_scaled = pos * self.stage_scaling  # transform to stage natural unit
                self.pidevice.MOV(self.stage_axis, pos_scaled)
                pitools.waitontarget(self.pidevice)  # time waitontarget function
            else:
                self.stage_raw_pos = pos
        else:
            print("Warning: movement out of boundaries. Not moving...", flush=True, end='\r')


    def transform_stage_pos(self, pos):
        """
        Transform a stage position to put it in the same referential as the image
        pos: float, position to transform
        """

        if self.stage_orientation == -1:  # if opposed orientation, transform position
            pos_ = abs(pos - self.stage_max_bound)
        
        elif self.stage_orientation == 1: # if same orientation, don't transform
            pos_ = float(pos)

        else: 
            raise Exception('ERROR: invalid stage orientation ({}), must be +1 or -1'.format(self.stage_orientation))

        return pos_


    def move_sequence(self, pos_list, dt=0, print_pos=False, out_fn=None, saving_dir=cwd, correction_time=0,
                      ow_out_fn=False):
        """
        Move stage along a list of N positions given by pos_list. pos_list can be a single position. positions in um
        The interval between movements is given by dt. dt can be a list of intervals of length N-1. time intervals in sec
        List of positions and times can be saved in a csv file if out_fn is not False. out_fn can be used to pass the file name
        """

        # if pos_list is a number
        if type(pos_list) is float or type(pos_list) is int:
            pos_list = [pos_list]  # transform to list

        # check boundaries
        pos_list = np.array(pos_list)
        if pos_list.min() < self.stage_min_bound or pos_list.max() > self.stage_max_bound:
            raise Exception('ERROR: pos_list contains positions out of the stage range. Aborting...')

        # check dt type
        if type(dt) is list:
            # check that list lengths are consistent
            if len(dt) == len(pos_list) - 1:
                dt.append(0)  # add a zero-wait interval at the end so lists have same length
            elif len(dt) == len(pos_list):
                pass  # last interval will happen after the last movement
            else:
                raise Exception(
                    "ERROR: pos_list and dt have not compatible lengths ({},{})".format(len(pos_list), len(dt)))

        elif type(dt) is float or type(dt) is int:
            dt = np.ones(len(pos_list)) * dt
        else:
            raise Exception("ERROR: dt must be a list or a number")

        # initialize data to be stored
        self.move_seq_data = {'set_pos': [],
                              'true_pos': [],
                              'time': [],
                              }

        # moving sequence
        for i, p in enumerate(pos_list):
            time_ = datetime.datetime.now()  # get current time
            self.move(p)

            # store position and time
            curr_pos = self.get_pos()
            self.move_seq_data['set_pos'].append(p)
            self.move_seq_data['true_pos'].append(curr_pos)
            self.move_seq_data['time'].append(time_)

            if print_pos:
                sys.stdout.write("\033[K")  # go back to previous line
                print('step {}/{}: position = {}'.format(i + 1, len(pos_list), curr_pos), flush=True, end='\r')

            # impose wait time
            wait_time = dt[i] - correction_time if dt[i] - correction_time > 0 else 0  # correction time: either subtract the computing time 50ms, or use real time
            time.sleep(wait_time)

            # export data
        out_df = self.export_move_seq_data(saving_dir=saving_dir, out_fn=out_fn, ow_out_fn=ow_out_fn)

        return out_df


    def export_move_seq_data(self, saving_dir=cwd, out_fn=None, ow_out_fn=False):
        """
        Export data generated during a moving sequence by running move_sequence
        saving_dir: saving directory
        out_fn: outdata filename. if str: full path of file, if None: file named with current_time, if False: no file will be saved
        ow_out_fn: bool, to allow overwriting outdata file
        """

        if self.move_seq_data is None:
            raise Exception("ERROR: no moving sequence data available. Aborting...")

        if len(self.move_seq_data['set_pos']) == 0:
            raise Exception("ERROR: empty moving sequence data. Aborting...")

        # store in df
        timestamp_list = [t.timestamp() for t in self.move_seq_data['time']]
        time_list = [t.strftime("%H:%M:%S.%f") for t in self.move_seq_data['time']]
        out_df = pd.DataFrame(
            {'set_pos': self.move_seq_data['set_pos'], 'true_pos': self.move_seq_data['true_pos'], 'time': time_list,
             'timestamp': timestamp_list})

        if out_fn is not False:
            # if no out file name, use a unique name it with time
            if out_fn is None:
                out_fn = osp.join(saving_dir, self.move_seq_data['time'][0].strftime("%Y%m%d_%H-%M-%S") + '.csv')
            # if file name already exists, add unique suffix with time
            if osp.exists(out_fn) and not ow_out_fn:
                out_fn = out_fn[:-4] + '_' + self.move_seq_data['time'][0].strftime("%Y%m%d_%H-%M-%S") + '.csv'

            out_df.to_csv(out_fn)
            print('Saving data to: {}'.format(out_fn))

        return out_df


    def get_last_tip_image(self):
        """
        Get the latest file in image directory. Files can be filtered with self.tip_fn_filter
        """
        if self.tip_dir is None:
            raise Exception("ERROR: no directory given for tip image. Aborting...")

        fn_list = []
        for fn in os.listdir(self.tip_dir):
            if not osp.isdir(osp.join(self.tip_dir, fn)):  # dont use directories
                if self.tip_fn_filter in fn:  # filter based on name
                    if not fn.startswith('.'):
                        fn_list.append(osp.join(self.tip_dir, fn))

        if len(fn_list) == 0:
            raise Exception('ERROR: there is no image in {}, please acquire at least one.'.format(self.tip_dir))
        else:
            latest_fn = max(fn_list, key=osp.getctime)
            path = osp.join(self.tip_dir, latest_fn)

        self.tip_last_fn = path

        return path

    def get_offset(self, plot_seg=False):
        """
        Get offset between stage position and tip position (both in um)
        """

        # get tip image
        tip_fn = self.get_last_tip_image()

        # prepare tip detection
        seg_param = {}  # segmentation parameter
        if self.tip_method == "pattern":
            if self.tip_pattern is None:
                raise Exception("No reference pattern to detect the tip. Aborting...")
            seg_param["pattern"] = self.tip_pattern

        elif self.tip_method == "hough_circle":
            for k in ['radius', 'radius_err', 'blur', 'low_threshold', 'high_threshold']:
                seg_param[k] = getattr(self, 'tip_' + k)

        else:
            raise Exception("Segmentation method missing use: hough_circle or pattern. Aborting...")

        # detect tip center
        detected_dict = detect_bead(self.tip_method, seg_param, fn=tip_fn, save_image=False, plot_seg=plot_seg)

        # update tip pattern
        if self.update_tip_pattern:
            self.tip_pattern = detected_dict['detected_ROI']

        # update tip intensity
        self.tip_intensity = detected_dict['mean_intensity']

        # update tip position
        tip_pos = {'x': detected_dict['center_x'] * self.tip_lengthscale,
                   'y': detected_dict['center_y'] * self.tip_lengthscale}
        self.tip_pos = tip_pos

        # get stage position
        stage_raw_pos = self.get_pos(store_pos=True)  # get position and update self.stage_pos and self.stage_raw_pos

        # offset
        if self.tip_axis == 'x': 
            offset = tip_pos['x'] - self.stage_pos 
        elif self.tip_axis == 'y': 
            offset = tip_pos['y'] - self.stage_pos
        else: 
            raise Exception("ERROR: tip_axis ({}) is not supported, must be 'x' or 'y'.".format(self.tip_axis))

        return {'offset': offset, 'tip_pos': tip_pos, 'stage_pos': self.stage_pos}


    def set_offset(self, target_offset, dont_calc=False, pos_dict=None):
        """
        Move stage to reach target offset (tip_pos - stage_pos).
        """

        if not dont_calc:
            pos_dict = self.get_offset()

        if self.tip_axis == 'x': 
            target_stage_pos = pos_dict['tip_pos']['x'] - target_offset
        elif self.tip_axis == 'y': 
            target_stage_pos = pos_dict['tip_pos']['y'] - target_offset
        else: 
            raise Exception("ERROR: tip_axis ({}) is not supported, must be 'x' or 'y'.".format(self.tip_axis))
        
        raw_stage_pos = self.transform_stage_pos(target_stage_pos)

        self.move(raw_stage_pos)

        return {'target_stage_pos': target_stage_pos, 'raw_stage_pos': raw_stage_pos}


    def define_deflection(self, offset_0, sign):
        """
        Define deflection by setting offset_O and sign
        """

        self.offset_0 = offset_0
        self.sign = sign


    def get_deflection(self,show_detection=False):
        """
        Get deflection by setting an offset with respect to the reference offset offset_0. deflection = offset - offset_0
        The sign of the deflection can be inverted using sign=+/-1
        """

        if self.sign is None or self.offset_0 is None:
            raise Exception('ERROR: offset_0 and sign are not defined')

        offset_dict = self.get_offset(plot_seg=show_detection)
        deflection = self.sign * (offset_dict['offset'] - self.offset_0)

        return deflection, offset_dict


    def set_deflection(self, target_def, dont_calc=False, pos_dict=None):
        """
        Set deflection target_def by setting an offset with respect to the reference offset offset_0. target_def = offset - offset_0
        The sign of the deflection can be inverted using sign=+/-1
        """
        if self.sign is None or self.offset_0 is None:
            raise Exception('ERROR: offset_0 and sign are not defined')

        target_offset = self.offset_0 + target_def / self.sign
        self.set_offset(target_offset, dont_calc=dont_calc, pos_dict=pos_dict)


    def set_deflection_(self, target_def):
        """
        Set deflection target_def by setting an offset with respect to the reference offset offset_0. target_def = offset - offset_0
        The sign of the deflection can be inverted using sign=+/-1
        Simple version of set_deflection to make it usable by a widget
        """
        if self.sign is None or self.offset_0 is None:
            raise Exception('ERROR: offset_0 and sign are not defined')

        target_offset = self.offset_0 + target_def / self.sign
        self.set_offset(target_offset, dont_calc=False, pos_dict=None)


    def control_deflection(self, target_sequence=[], PID_param=[5, 0.01, 0.1], fig=None, PID_freq=1, plotting_freq=1,
                           saving_dir=cwd, out_fn=None):
        """
        Control deflection using a PID controller. The sequence of deflections is given by target_sequence a list of target_dict: [target_dict, ...]
        target_dict = {'setpoint':setpoint, 'duration':duration, 'ramp':False} if the target deflection is constant of value setpoint
        target_dict = {'setpoint':[setpoint1,setpoint2], 'duration':duration, 'ramp':True} if the target deflection is a linear ramp between setpoint1 and setpoint2
        setpoint in um, duration in sec, or 'inf' if as long as possible
        fig: a Matplotlib figure to interactively plot the data
        PID_freq: PID computing frequency in Hz 
        plotting_freq: plotting frequency in Hz (a computing-intensive step, avoid going >1Hz)
        saving_dir: path to saving directory
        out_fn: path to PID data file
        """

        # PID controller updating PID_freq
        period = 1.0 / PID_freq

        # checking deflection definition
        if self.sign is None or self.offset_0 is None:
            raise Exception('ERROR: offset_0 and sign are not defined')

        # prepare sequence
        if len(target_sequence) == 0:
            raise Exception(
                "ERROR: empty sequence of deflection. Must be: [{'setpoint':setpoint1, 'duration':duration1}, ...]")

        # convert to list if single target
        if type(target_sequence) is dict:
            target_sequence = [target_sequence]

        cumulated_duration = []  # cumulated duration of each deflection 
        last_inf = False  # boolean to add an infinite loop at the end
        for i, target in enumerate(target_sequence):
            # check element
            if "setpoint" not in target.keys() or "duration" not in target.keys():
                excpt_msg = "ERROR: target {} deflection not valid. Must be: {'setpoint':setpoint1, 'duration':duration1}".format(i)
                raise Exception(excpt_msg)

            if target['duration'] == 'inf':
                last_inf = True
                break  # don't look at following targets if infinite duration
            else:
                if type(target['duration']) is float or type(target['duration']) is int:
                    cumulated_duration.append(target['duration'])
                else:
                    raise Exception("ERROR: target {} deflection not valid. Must be float or int".format(i))
        cumulated_duration = list(np.cumsum(cumulated_duration))
        if last_inf:
            cumulated_duration.append('inf')

        # initialization of PID
        setpoint = target_sequence[0]["setpoint"] if not target_sequence[0]['ramp'] else target_sequence[0]["setpoint"][
            0]
        pid = PID(PID_param[0], PID_param[1], PID_param[2], setpoint=setpoint)
        # pid.output_limits = offset_lims #what are the limits: stage position, bead detectons. maybe get the limits from
        # IMPORTANT: think about having a detector of tip getting to close from the edge image

        # unpack axes to plot
        if fig is not None:
            ax1 = fig.axes[0]
            ax2 = fig.axes[1]
            ax3 = fig.axes[2]
            ax4 = fig.axes[3]

        # Keep track of values for plotting
        self.PID_data = {'setpoint': [],
                         'relative_time': [],
                         'timestamp': [],
                         'measured_def': [],
                         'applied_def': [],
                         'stage_pos': [],
                         'tip_pos_x': [],
                         'tip_pos_y': [],
                         'tip_intensity': [],
                         }

        # running PID sequence 
        current_target_ind = 0  # index in target_sequence
        current_cumulated_time = 0  # cumulated time of previous steps
        running = True  # running boolean
        prev_plotting_time = 0  # previous time used to plot
        next_plotting_time = 1 / plotting_freq  # next time used to plot

        start_time = time.time()

        # initialize PID_data before running
        curr_def, offset_dict = self.get_deflection()
        self.PID_data['setpoint'].append(pid.setpoint)
        self.PID_data['timestamp'].append(start_time)
        self.PID_data['relative_time'].append(0)
        self.PID_data['measured_def'].append(curr_def)
        self.PID_data['applied_def'].append(0)
        self.PID_data['stage_pos'].append(self.stage_pos)
        self.PID_data['tip_pos_x'].append(self.tip_pos['x'])
        self.PID_data['tip_pos_y'].append(self.tip_pos['y'])
        self.PID_data['tip_intensity'].append(self.tip_intensity)

        # PID controller loop
        while running:
            current_time = time.time()
            relative_time = current_time - start_time

            # compute correction
            curr_def, offset_dict = self.get_deflection()
            def_increment = pid(curr_def)

            # save data
            self.PID_data['setpoint'].append(pid.setpoint)
            self.PID_data['timestamp'].append(current_time)
            self.PID_data['relative_time'].append(relative_time)
            self.PID_data['measured_def'].append(curr_def)
            self.PID_data['applied_def'].append(def_increment)
            self.PID_data['stage_pos'].append(self.stage_pos)
            self.PID_data['tip_pos_x'].append(self.tip_pos['x'])
            self.PID_data['tip_pos_y'].append(self.tip_pos['y'])
            self.PID_data['tip_intensity'].append(self.tip_intensity)

            # apply correction
            self.set_deflection(curr_def + def_increment, dont_calc=True, pos_dict=offset_dict)

            # plot data  ## consider plotting with a different frequency
            if fig is not None:
                if relative_time > next_plotting_time:  # don't plot during interval defined by plotting_freq
                    ax1.plot(self.PID_data['relative_time'], self.PID_data['measured_def'], color=color_list[0])
                    ax1.plot(self.PID_data['relative_time'], self.PID_data['applied_def'], color=color_list[1])
                    ax1.plot(self.PID_data['relative_time'], self.PID_data['setpoint'], color=color_list[2])
                    ax2.plot(self.PID_data['relative_time'], self.PID_data['stage_pos'], color=color_list[0])
                    if self.tip_axis == 'x':
                        ax3.plot(self.PID_data['relative_time'], self.PID_data['tip_pos_x'], color=color_list[0])
                        ax3.set_title(r'tip position = {:.1f} $\mu m$'.format(self.PID_data['tip_pos_x'][-1]))
                    elif self.tip_axis == 'y':
                        ax3.plot(self.PID_data['relative_time'], self.PID_data['tip_pos_y'], color=color_list[0])
                        ax3.set_title(r'tip position = {:.1f} $\mu m$'.format(self.PID_data['tip_pos_y'][-1]))
                    ax4.plot(self.PID_data['relative_time'], self.PID_data['tip_intensity'], color=color_list[0])
                    ax2.set_title(r'stage raw position = {:.1f} $\mu m$'.format(self.PID_data['stage_pos'][-1]))
                    ax4.set_title(r'tip intensity = {:.1f}'.format(self.PID_data['tip_intensity'][-1]))
                    fig.canvas.draw()
                    # update plotting times
                    prev_plotting_time = next_plotting_time
                    next_plotting_time = prev_plotting_time + 1 / plotting_freq

            # update setpoint
            if cumulated_duration[current_target_ind] != 'inf':  # if not infinite loop
                if relative_time > cumulated_duration[current_target_ind]:  # switch to next target
                    current_target_ind += 1
                    if current_target_ind >= len(cumulated_duration):  # if last point has been reached, terminate
                        running = False
                    else:
                        current_cumulated_time = cumulated_duration[
                            current_target_ind - 1]  # update current_cumulated_time
                        target = target_sequence[current_target_ind]
                        if target['ramp']:
                            if target['duration'] == 'inf':
                                raise Exception(
                                    'step {} cannot be a ramp of infinite duration'.format(current_target_ind))
                            # ramp setpoint calculation: setpoint = setpoint1 + (setpoint2-setpoint1)/step_duration * (relative_time - current_cumulated_time)
                            pid.setpoint = target['setpoint'][0] + (target['setpoint'][1] - target['setpoint'][0]) * (
                                        relative_time - current_cumulated_time) / target['duration']
                        else:
                            pid.setpoint = target['setpoint']
                else:
                    target = target_sequence[current_target_ind]
                    if target['ramp']:
                        if target['duration'] == 'inf':
                            raise Exception('step {} cannot be a ramp of infinite duration'.format(current_target_ind))
                        # ramp setpoint calculation: setpoint = setpoint1 + (setpoint2-setpoint1)/step_duration * (relative_time - current_cumulated_time)
                        pid.setpoint = target['setpoint'][0] + (target['setpoint'][1] - target['setpoint'][0]) * (
                                    relative_time - current_cumulated_time) / target['duration']
                    else:
                        pid.setpoint = target['setpoint']

            # sleep so PID isn't always computing
            while (time.time() - current_time) < period:
                time.sleep(0.001)  # precision here 

        # export PID_data at the end
        print("PID control over. Saving data PID sequence data...")
        self.export_PID_data(saving_dir=saving_dir, out_fn=out_fn)


    def export_PID_data(self, saving_dir=cwd, out_fn=None, ow_out_fn=False):
        """
        Export data from a PID control sequence to a csv file 
        """
        if self.PID_data is None:
            raise Exception("ERROR: no PID data available. Aborting...")

        out_df = pd.DataFrame(self.PID_data)

        if out_df.shape[0] == 0:
            raise Exception("ERROR: empty PID data. Aborting...")

        if out_fn is not False:
            formatted_first_time = datetime.datetime.fromtimestamp(out_df.loc[0, 'timestamp']).strftime(
                "%Y%m%d_%H-%M-%S")
            # if no out file name, use a unique name it with time
            if out_fn is None:
                out_fn = osp.join(saving_dir, formatted_first_time + '.csv')
            # if file name already exists, add unique suffix with time
            if osp.exists(out_fn) and not ow_out_fn:
                out_fn = out_fn[:-4] + '_' + formatted_first_time + '.csv'
            out_df.to_csv(out_fn)
            print('Saving data to: {}'.format(out_fn))

        return out_df


    def set_deflection_sequence(self, def_list, dt=0, print_=False, out_fn=None, saving_dir=cwd, correction_time=0,
                                ow_out_fn=False):
        """
        Apply a list of N deflections given by def_list. def_list can be a single deflection.
        The interval between movements is given by dt. dt can be a list of intervals of length N-1. time intervals in sec
        Data can be saved in a csv file if out_fn is not False. out_fn can be used to pass the file name
        """

        # if def_list is a number
        if type(def_list) is float or type(def_list) is int:
            def_list = [def_list]  # transform to list

        # check dt type
        if type(dt) is list:
            # check that list lengths are consistent
            if len(dt) == len(def_list) - 1:
                dt.append(0)  # add a zero-wait interval at the end so lists have same length
            elif len(dt) == len(def_list):
                pass  # last interval will happen after the last movement
            else:
                raise Exception(
                    "ERROR: def_list and dt have not compatible lengths ({},{})".format(len(def_list), len(dt)))

        elif type(dt) is float or type(dt) is int:
            dt = np.ones(len(def_list)) * dt
        else:
            raise Exception("ERROR: dt must be a list or a number")

        # moving
        true_def_list = []
        time_list = []
        for i, deflection in enumerate(def_list):
            time_ = datetime.datetime.now()  # get current time
            self.set_deflection(deflection)

            # store position and time
            curr_def, pos_dict = self.get_deflection()
            true_def_list.append(curr_def)
            time_list.append(time_)

            if print_:
                print('current deflection = {:.2f}, time = {}:{}:{}:{}'.format(curr_def, time_.hour, time_.minute,
                                                                               time_.second, time_.microsecond))

            # impose wait time
            # correction time: either subtract the computing time 50ms, or use real time
            wait_time = dt[i] - correction_time if dt[i] - correction_time > 0 else 0
            time.sleep(wait_time)

            # store in df
        timestamp_list = [t.timestamp() for t in time_list]
        time_list_ = [t.strftime("%H:%M:%S.%f") for t in time_list]
        out_df = pd.DataFrame(
            {'set_def': def_list, 'true_def': true_def_list, 'time': time_list_, 'timestamp': timestamp_list})

        if out_fn is not False:
            # if no out file name, use a unique name it with time
            if out_fn is None:
                out_fn = osp.join(saving_dir, time_list[0].strftime("%Y%m%d_%H-%M-%S") + '.csv')
            # if file name already exists, add unique suffix with time
            if osp.exists(out_fn) and not ow_out_fn:
                out_fn = out_fn[:-4] + '_' + time_list[0].strftime("%Y%m%d_%H-%M-%S") + '.csv'
            out_df.to_csv(out_fn)

        return out_df
