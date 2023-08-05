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
import time

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
import seaborn as sns

import ipywidgets as widgets
from ipywidgets import interactive, fixed, HBox, VBox, interact_manual, Label
from ipyfilechooser import FileChooser
from IPython.display import HTML, Markdown, display, clear_output

import manipylator
from manipylator.controller import Controller
import manipylator.utils as utils
import manipylator.signals as signals
import manipylator.analysis as analysis


# useful color list for plotting
color_list = [c['color'] for c in list(plt.rcParams['axes.prop_cycle'])] + sns.color_palette("Set1", n_colors=9,desat=.5)


def printmd(string):
    """
    Display Markdown formarted string in a notebook
    """
    display(Markdown(string))


def generate_show_pos(controller,output):
    """
    A function wrapper that generates a function to be passed to Widget on_click method
    controller: controller.Controller object 
    output: ipywidgets.Output object
    """

    def show_pos(obj):
        """
        a function used to show the stage position when button clicked
        """
        output.clear_output()
        pos = controller.get_pos(print_pos=False)
        with output:
            print('raw position = {} um\n'.format(pos))
            print('transformed position = {} um\n'.format(controller.stage_pos))

    return show_pos



def make_basic_dashboard(controller_dict, virtual):
    """
    Make a dashboard to control the position and the servo of the connected controllers
    controller_dict: dict of controller.Controller object 
    virtual: bool if True controller are virtual
    """

    # initialize lists of widgets and labels for each controller
    interactive_mover_list = []
    interactive_servo_list = []
    pos_wid_list = []
    out_list = []
    label = []
    controller_list = []

    # loop over list of controllers
    for i, key in enumerate(controller_dict.keys()):

        # get controller info
        controller = controller_dict[key]
        min_bound = controller.stage_min_bound
        max_bound = controller.stage_max_bound
        init_pos = controller.get_pos()

        # raw stage position controller
        interactive_mover = interactive(controller.move,
                                        pos=widgets.FloatSlider(value=init_pos, min=min_bound, max=max_bound, step=0.1,
                                                                description='position:')
        
                                        )
        # if virtual stage disable servo
        if virtual:  
            interactive_servo = interactive(controller.set_servo,
                                            status=widgets.ToggleButton(value=True, description='Servo', disabled=True),
                                            verbose=fixed(False)
                                            )
        else:
            interactive_servo = interactive(controller.set_servo,
                                            status=widgets.ToggleButton(value=True, description='Servo'),
                                            verbose=fixed(False)
                                            )

        
        # show position button
        out = widgets.Output()  # output to display position
        pos_wid = widgets.Button(value=True, description='Show position')  # button widget
        show_pos = generate_show_pos(controller,out)  # function to show position when button click
        pos_wid.on_click(show_pos)


        # store widgets, outputs and labels
        controller_list.append(controller)
        interactive_mover_list.append(interactive_mover)
        interactive_servo_list.append(interactive_servo)
        pos_wid_list.append(pos_wid)
        out_list.append(out)
        label.append(Label(key))


    # display all widgets, outputs and labels
    for i in range(len(controller_dict.keys())):
        display(HBox([label[i], interactive_mover_list[i], interactive_servo_list[i], VBox([pos_wid_list[i], out_list[i]])]))


def run_chirp(controller, parameters, saving_dir):
    """
    Run a chirp assay with a controller.
    controller: manipylator.Controller object
    parameters: dict of parameters used to overwrite default_parameters
    saving_dir: str, path to saving directory
    """

    # get parameters
    default_parameters = {'x0': 100,  # half amplitude um
                          'center_position': 250,  # um
                          'low_angular_freq': 0.1,  # rad/sec
                          'high_angular_freq': 0.5,  # rad/sec
                          'total_time': 20,  # sec
                          'num_points': 20,  # number of points
                          'tuckey_wind': 0.15,  # tuckey window parameter see doi:10.1103/PhysRevX.8.041042
                          'polarity': -1,  # to change sign of signal
                          'cst_points': [0, 0],  # number of constant points before and after the signal [before,after]
                          'print_pos': True,  # print the position of stage
                          'correction_time': 0.05,  # time to compensate for code execution (in sec). Typically=0.05
                          'out_fn': None,  # if False: not saving, if None: saving with date and time as filename
                          }

    # fill missing parameters with default_parameters                 
    for k in default_parameters.keys():
        if k not in parameters.keys():
            parameters[k] = default_parameters[k]

    # checking outdata filemane
    out_fn, param_fn = utils.make_filenames(parameters['out_fn'],saving_dir)

    # make chirp signal
    x, dt = signals.make_tuckey_chirp(x0=parameters['x0'],
                                      off=parameters['center_position'],
                                      w1=parameters['low_angular_freq'],
                                      w2=parameters['high_angular_freq'],
                                      T=parameters['total_time'],
                                      N=parameters['num_points'],
                                      polarity=parameters['polarity'],
                                      r=parameters['tuckey_wind'],
                                      cst_num_steps=parameters['cst_points'],
                                      saving_dir=saving_dir,
                                      )

    # make run button to start experiment
    start_chirp_wid = widgets.Button(value=True, description='Run chirp')

    def start_chirp(obj):
        """
        make a function used to run the assay when button clicked
        """
        if param_fn is not False: 
            # save experiment parameters
            param_dict = {'amplitude': parameters['x0'],
                          'center_position': parameters['center_position'],
                          'low_angular_freq': parameters['low_angular_freq'],
                          'high_angular_freq': parameters['high_angular_freq'],
                          'total_time': parameters['total_time'],
                          'num_points': parameters['num_points'],
                          'polarity': parameters['polarity'],
                          'tuckey_window': parameters['tuckey_wind'],
                          'cst_points': parameters['cst_points'],
                          'correction_time': parameters['correction_time'],
                          't0': '',
                          }
            utils.write_dict(param_dict, param_fn)

        # run experiment
        try:
            controller.move_sequence(x, dt, print_pos=parameters['print_pos'], saving_dir=saving_dir,
                                     correction_time=parameters['correction_time'], out_fn=out_fn)
        except KeyboardInterrupt:
            print("chirp interrupted. Saving data...")
            controller.export_move_seq_data(saving_dir=saving_dir, out_fn=out_fn)

    # display run button
    start_chirp_wid.on_click(start_chirp)
    display(start_chirp_wid)

    print('low angular frequency: period = {:.2f} s'.format(2 * np.pi / parameters['low_angular_freq']))
    print('high angular frequency: period = {:.2f} s'.format(2 * np.pi / parameters['high_angular_freq']))


def get_sweep_parameters(controller, sweep_num=1, rate_def='time', steps_def='freq'): 
    """
    Display widgets to select sweep parameters
    controller: manipylator.Controller object
    sweep_num: int number of successive sweeps
    rate_def: str, definition for sweep rate in total time ('time') or speed ('speed')
    steps_def: str, definition for number of steps in total number ('total') or frequency ('freq')
    """
    
    boundaries_list = []
    rate_list = []
    unit_list = []
    steps_list = []
    row_list = []

    for i in range(sweep_num):
        
        # step boundaries
        boundaries_wid = widgets.FloatRangeSlider(value=[controller.stage_min_bound, controller.stage_max_bound],
                                                min=controller.stage_min_bound,max=controller.stage_max_bound,
                                                description='boundaries:',
                                                )
        boundaries_list.append(boundaries_wid)

        # definition of rate by total time or speed
        if rate_def == 'time':
            rate_descr = 'step duration:'
            units = ['sec','min', 'hr']
            rate_unit = 'sec'
            rate_value = 10
        elif rate_def == 'speed': 
            rate_descr = 'step rate:'
            units = ['um/sec','um/min', 'um/hr']
            rate_unit = 'um/sec'
            rate_value = 1

        rate_wid = widgets.BoundedFloatText(value=rate_value,min=0,max=1e5,description=rate_descr,)
        rate_list.append(rate_wid)

        unit_wid = widgets.Dropdown(options=units,value=rate_unit,description='unit:')
        unit_list.append(unit_wid)

        # definition of number of steps by total number or frequency
        if steps_def == 'total':
            steps_wid = widgets.BoundedIntText(value=100,min=1,max=1e5,description='total number of steps (#):',)
        elif steps_def == 'freq':
            steps_wid = widgets.BoundedFloatText(value=1,min=0,max=100,step=0.001,description='frequency (Hz):',)
        steps_list.append(steps_wid)
        

        row = HBox([boundaries_wid,rate_wid,unit_wid,steps_wid])
        row_list.append(row)

    display(VBox(row_list))

    sweep_widgets = {'boundaries_list':boundaries_list,'rate_list':rate_list,'unit_list':unit_list,'steps_list':steps_list}

    return sweep_widgets


def run_sweep(controller, parameters, saving_dir, plot='show'):
    """
    Run linear sweeps between boundaries
    controller: manipylator.Controller object
    parameters: dict of parameters used to overwrite default_parameters
    saving_dir: str, path to saving directory
    plot: str or bool, show plot if 'show', save if 'save', don't plot if False
    """

    # get parameters
    default_parameters = {'sweep_num': 1,  # number of successive sweeps
                          'boundaries': [[controller.stage_min_bound, controller.stage_max_bound]],  # list of boundaris in um
                          'rate_def': 'time',  # definition for sweep rate in total time ('time') or speed ('speed')
                          'steps_def': 'freq',  # definition for number of steps in total number ('total') or frequency ('freq')
                          'time_unit': ['s'],  # time unit used for sweep rate
                          'rate': [10],  # sweep time or sweep speed dependeing on rate_def
                          'num_steps': [10],  # number of steps or step frequency depending steps_def
                          'print_pos': True,  # print the position of stage
                          'correction_time': 0.05,  # time to compensate for code execution (in sec). Typically=0.05
                          'out_fn': None,  # if False: not saving, if None: saving with date and time as filename
                          }

    # fill missing parameters with default_parameters                 
    for k in default_parameters.keys():
        if k not in parameters.keys():
            parameters[k] = default_parameters[k]

    # checking outdata filemane
    out_fn, param_fn = utils.make_filenames(parameters['out_fn'],saving_dir)

    # convert rate and steps
    boundaries_list = []
    duration_list = []
    speed_list = []
    num_steps_list = []
    for i in range(parameters['sweep_num']):
        # boudaries
        bounds = parameters['boundaries'][i]
        boundaries_list.append(bounds)
        # convert duration
        if parameters['rate_def'] == 'speed': 
            duration = np.abs((bounds[1] - bounds[0]) / parameters['rate'][i])
        else: 
            duration = parameters['rate'][i]
        # scale duration to sec
        if parameters['time_unit'][i] == 'min':
            duration *= 60
        elif parameters['time_unit'][i] == 'hr':
            duration *= 3600
        duration_list.append(duration)
        speed_list.append(np.abs((bounds[1] - bounds[0]) / duration))
        # convert steps
        num_steps = int(parameters['num_steps'][i] * duration) if parameters['steps_def'] == 'freq' else parameters['num_steps'][i]
        num_steps_list.append(num_steps)

    # make sweep positions
    sweep = signals.make_linear_sweep_series(boundaries_list,duration_list,num_steps_list,plot)
    if sweep['pos'].min() < controller.stage_min_bound or sweep['pos'].max() > controller.stage_max_bound: 
        print("WARNING: some positions are out of stage range: sweep_min = {}, sweep_max = {}".format(sweep['pos'].min(),sweep['pos'].max()))

    # make run button
    run_sweep_wid = widgets.Button(value=True, description='Run sweep')

    def start_sweep(obj):
        """
        make a function used to run the assay when button clicked
        """

        param_dict = {'boundaries':boundaries_list,
                     'duration':duration_list,
                     'num_steps':num_steps_list,
                     'rate':speed_list,
                     'correction_time':parameters['correction_time'],
                     't0':'',
                    }
        utils.write_dict(param_dict,param_fn)
        
        # run experiment
        try:
            controller.move_sequence(sweep['pos'].tolist(),sweep['dt'].tolist(),saving_dir=saving_dir,
                                     print_pos=parameters['print_pos'],out_fn=out_fn,
                                     correction_time=parameters['correction_time'],)
        except KeyboardInterrupt:
            print("sweep interrupted. Saving data...")
            controller.export_move_seq_data(saving_dir=saving_dir,out_fn=out_fn)
        
    run_sweep_wid.on_click(start_sweep)
    display(run_sweep_wid)

    return sweep


def get_tip_parameters(saving_dir):
    """
    Display widgets to select tip parameters
    saving_dir: str, saving directory
    """

    # directory
    printmd("**Choose image directory where tip images will be saved**")
    fc_image = FileChooser(saving_dir)
    
    fc_image.use_dir_icons = True
    display(fc_image)

    # lengthscale
    printmd("**Set image lengthscale (um/px)**")
    lengthscale_wid = widgets.FloatText(value=1.0)
    display(lengthscale_wid)

    # detection method
    printmd("**Choose your tip detection method**")
    printmd("""The pattern matching methods tries to fit a reference pattern (defined by a region of interest) 
    in an image. The Hough transform detects circles of a given radius in an image (works only of circular tips)""")
    method_wid = widgets.ToggleButtons(options=['pattern matching', 'Hough transform'],value='pattern matching',
                                    description='Method:',tooltips=['Crosscorrelation pattern matching', 'Hough circle transform']
                                    )
    display(method_wid)

    # update tip ROI 
    printmd("**Update tip pattern at each time step (if not, keep the initial pattern). Only relevant for the pattern mathcing method.**")
    update_pattern_wid = widgets.Checkbox(value=True,description='Update pattern')
    display(update_pattern_wid)

    # tip filename filter
    printmd("**Filter tip files based on their names.**")
    fn_filter_wid = widgets.widgets.Text(value='',placeholder='name must contain',description='Filter:')
    display(fn_filter_wid)

    tip_widgets = {'fc_image':fc_image,
                    'lengthscale_wid':lengthscale_wid,
                    'method_wid':method_wid,
                    'update_pattern_wid':update_pattern_wid,
                    'fn_filter_wid':fn_filter_wid,
                    }

    return tip_widgets


def tune_detection_parameters(controller):
    """
    Display interactive plot to tune tip detection parameters
    """

    tip_fn = controller.get_last_tip_image()

    if controller.tip_method == "pattern":
        
        printmd("**Select the region of interest (ROI) you want to track**")
        
        image = imread(tip_fn)
        h,w = image.shape

        interactive_wid = interactive(utils.select_ROI,
                                             x_range=widgets.IntRangeSlider(min=0,max=w,value=[0,w],continuous_update=False),
                                             y_range=widgets.IntRangeSlider(min=0,max=h,value=[0,h],continuous_update=False),
                                             intensity_range=widgets.IntRangeSlider(min=0,max=255,value=[0,255],continuous_update=False),
                                             frame=widgets.IntSlider(min=0,max=0,value=0,continuous_update=False,disabled=True),
                                             stack=widgets.Checkbox(value=False,disabled=True),
                                             fn=tip_fn,
                                             continuous_update=False
                                            )

    elif controller.tip_method == "hough_circle":

        printmd("**Tune to the Hough transform parameters to detect the tip**")

        interactive_wid = interactive(analysis.tune_detect_bead,
                                             radius=widgets.IntSlider(min=0,max=1000,value=150),
                                             radius_err=widgets.FloatSlider(min=0.001,max=0.2,value=0.05,step=1e-3),
                                             blur=widgets.IntSlider(min=1,max=50,value=6),
                                             low_threshold=widgets.IntSlider(min=0,max=255,value=5),
                                             high_threshold=widgets.IntSlider(min=0,max=255,value=10),
                                             fn=tip_fn,
                                             stack=False,
                                            )

    display(interactive_wid)

    return interactive_wid


def save_detection_parameters(controller, interactive_wid):
    """
    Display interactive plot to tune tip detection parameters
    controller: manipylator.Controller object
    interactive_wid: ipywidgets.interactive object, output of tune_detection_parameters
    """

    if controller.tip_method == "pattern":
        # get ROI
        image = imread(controller.get_last_tip_image())
        x_range = interactive_wid.children[1].value
        y_range = interactive_wid.children[2].value
        frame = interactive_wid.children[3].value
        ROI = image[y_range[0]:y_range[1], x_range[0]:x_range[1]]
        
        # plot ROI
        fig, ax = plt.subplots()
        ax.imshow(ROI, cmap=plt.cm.gray, aspect='equal')
        ax.set_title("Selected ROI")
        plt.show(fig)
        
        #store ROI
        controller.tip_pattern = ROI
        printmd("this ROI will be use to track the tip")

    elif controller.tip_method == "hough_circle":   
        # get tuned segmentation parameters
        controller.tip_radius = interactive_wid.children[1].value
        controller.tip_radius_err = interactive_wid.children[2].value
        controller.tip_blur = interactive_wid.children[3].value
        controller.tip_low_threshold = interactive_wid.children[4].value
        controller.tip_high_threshold = interactive_wid.children[5].value

        printmd("""The following parameters will be used to detect the tip by Hough transform:  
        - tip radius (px) = {}  
        - tip radius errror (%) = {}  
        - gaussian blur (px) = {}  
        - low threshold = {}  
        - high threshold = {}  
        """.format(controller.tip_radius,controller.tip_radius_err,controller.tip_blur,controller.tip_low_threshold,controller.tip_high_threshold))


def initialize_deflection(controller,deflection_sign=1):
    """
    Initialize deflection with current offset
    controller: manipylator.Controller object
    deflection_sign: int, 1 or -1 to control the sign of the deflection
    """

    # check deflection sign
    if deflection_sign != 1 and deflection_sign != -1: 
        print('WARNING: invalid deflection sign ({}), must be +1 or -1. Using +1'.format(deflection_sign))
        deflection_sign = 1

    # get offset
    offset = controller.get_offset(plot_seg=False)

    # initialize deflection
    printmd("""Initializing deflection with current offset between tip and stage position:  
    - image position = {} $\mu m$  
    - stage transformed position = {} $\mu m$  
    - offset = {} $\mu m$
    """.format(offset['tip_pos'][controller.tip_axis],offset['stage_pos'],offset['offset']))

    
    controller.define_deflection(offset['offset'],deflection_sign)

    # calculate deflection range
    transformed_max = controller.transform_stage_pos(controller.stage_max_bound)
    transformed_min = controller.transform_stage_pos(controller.stage_min_bound)
    deflection_bound_1 = deflection_sign * (offset['stage_pos'] - transformed_max)
    deflection_bound_2 = deflection_sign * (offset['stage_pos'] - transformed_min)
    deflection_min = min(deflection_bound_1,deflection_bound_2)
    deflection_max = max(deflection_bound_1,deflection_bound_2)

    # show deflection
    show_def_wid = widgets.Button(description='Show deflection')
    show_def_out = widgets.Output()

    def show_def(obj):
        show_def_out.clear_output()
        deflection, pos_dict = controller.get_deflection(show_detection=False)
        with show_def_out:
            print('deflection = {} um\n'.format(deflection))
        
    show_def_wid.on_click(show_def)

    #set deflection
    set_def_button = widgets.Button(description='Apply deflection')
    set_def_wid = widgets.FloatText(min=-1e6, max=1e6, value=0)

    def set_def(obj): 
        print("applying deflection...                            ", flush=True, end='\r')  # print blanks to erase potential error message from move
        controller.set_deflection_(set_def_wid.value)
        
    set_def_button.on_click(set_def)
    #set_def_wid = interactive(controller.set_deflection_, {'manual': True}, target_def=widgets.FloatText(min=-1e6, max=1e6, value=0) )
    #set_def_wid.children[1].description = 'Apply deflection'
    

    printmd("**Deflection dashboard**")
    printmd("Warning: with the current tip position, only deflections between {} and {} are available.".format(deflection_min,deflection_max))

    display(VBox([HBox([show_def_wid,show_def_out]),HBox([set_def_wid,set_def_button])]))


def get_force_sequence(step_num,deflection_range=[-500,500]):
    """
    step_num: int, number of steps
    """

    printmd("""Choose series of constant setpoints and their duration. 
            Optionally, introduce a linear ramp before the step. 
            If ramp duration is 0, there is no ramp. """)

    run_list = []
    setpoint_list = []
    duration_list = []
    ramp_duration_list =[]

    # steps
    for i in range(step_num):
        # run step
        run_wid = widgets.Checkbox(value=True,description='Run step')
        run_list.append(run_wid)
        # step setpoint
        setpoint_wid = widgets.BoundedFloatText(value=50,min=deflection_range[0],max=deflection_range[1],step=0.1,description='Setpoint: ')
        setpoint_list.append(setpoint_wid)
        # step duration
        duration_wid = widgets.BoundedFloatText(value=1000,min=0,max=1e6,step=0.1,description='Duration: ')
        duration_list.append(duration_wid)
        # ramp duration
        ramp_duration_wid = widgets.BoundedFloatText(value=0,min=0,max=1e6,step=0.1,description='Ramp duration: ')
        ramp_duration_list.append(ramp_duration_wid)
        display(HBox([run_wid,setpoint_wid,duration_wid,ramp_duration_wid]))
    
    # relax sequence at the end
    # run step
    run_wid = widgets.Checkbox(value=True,description='Relax step')
    run_list.append(run_wid)
    # step setpoint
    setpoint_wid = widgets.BoundedFloatText(value=0,min=deflection_range[0],max=deflection_range[1],step=0.1,description='Setpoint: ',disabled=True)
    setpoint_list.append(setpoint_wid)
    # step duration
    duration_wid = widgets.BoundedFloatText(value=1000,min=0,max=1e6,step=0.1,description='Duration: ')
    duration_list.append(duration_wid)
    # ramp duration
    ramp_duration_wid = widgets.BoundedFloatText(value=0,min=0,max=1e6,step=0.1,description='Ramp duration: ')
    ramp_duration_list.append(ramp_duration_wid)
    display(HBox([run_wid,setpoint_wid,duration_wid,ramp_duration_wid]))

    force_widgets = {'run_list':run_list,
                    'setpoint_list':setpoint_list,
                    'duration_list':duration_list,
                    'ramp_duration_list':ramp_duration_list,
                    }

    return force_widgets


def run_force_sequence(controller, parameters, saving_dir):
    """
    Run sequence of controlled force steps
    controller: manipylator.Controller object
    parameters: dict of parameters used to overwrite default_parameters
    saving_dir: str, path to saving directory
    """

    # get parameters
    default_parameters = {'PID_param': [1,0,0],  # PID parameters
                          'PID_freq': 2,  # PID computation frequence
                          'plotting_freq': 0.2,  # plotting frequency
                          'force_widgets': {'run_list':[],'setpoint_list':[],'duration_list':[],'ramp_duration_list':[]},  # list of widgets
                          'out_fn': None,  # if False: not saving, if None: saving with date and time as filename
                          }

    # fill missing parameters with default_parameters                 
    for k in default_parameters.keys():
        if k not in parameters.keys():
            parameters[k] = default_parameters[k]

    # checking outdata filemane
    out_fn, param_fn = utils.make_filenames(parameters['out_fn'],saving_dir)


    # initialize live figure
    fig,axes = plt.subplots(4,1,figsize=(8,18))
    lines = [plt.Line2D([0], [0], color=color_list[i]) for i in range(3)]
    labels = ['measured', 'correction', 'setpoint']
    axes[0].legend(lines, labels)
    for ax in axes:
        ax.set_xlabel('time (sec)')
    axes[0].set_title('PID control')
    axes[0].set_ylabel(r'deflection ($\mu m$)')
    axes[1].set_title('stage transformed position')
    axes[1].set_ylabel(r'position ($\mu m$)')
    axes[2].set_title('tip position')
    axes[2].set_ylabel(r'position ($\mu m$)')
    axes[3].set_title('tip intensity')
    axes[3].set_ylabel(r'mean intensity')
    fig.tight_layout()
    fig.show()


    # extract deflection sequence parameters
    # unpack widgets
    run_list = parameters['force_widgets']['run_list']
    setpoint_list = parameters['force_widgets']['setpoint_list']
    duration_list = parameters['force_widgets']['duration_list']
    ramp_duration_list = parameters['force_widgets']['ramp_duration_list']
    
    # list of steps in the sequence
    deflection_sequence = []

    for i in range(len(run_list)): 
        if run_list[i].value:
            # if there's a ramp, add it to sequence before constant step
            if ramp_duration_list[i].value > 0: 
                prev_setpoint = 0 if i == 0 else setpoint_list[i-1].value
                
                # add ramp to sequence
                deflection_sequence.append({'setpoint':[prev_setpoint,setpoint_list[i].value],
                                             'duration':ramp_duration_list[i].value,
                                             'ramp': True, 
                                            })
            # add constant step
            deflection_sequence.append({'setpoint':setpoint_list[i].value,
                                        'duration':duration_list[i].value,
                                        'ramp': False, 
                                        })
            

    # run PID
    run_wid = widgets.Button(value=True, description='Run PID sequence')

    def run_seq(obj):
        
        # save experiment parameters
        param_dict = {'PID_param':parameters['PID_param'],
                     'PID_freq':parameters['PID_freq'],
                     'setpoint_list': [e['setpoint'] for e in deflection_sequence],
                     'duration_list': [e['duration'] for e in deflection_sequence],
                    }
        utils.write_dict(param_dict,param_fn)
        
        try:
            controller.control_deflection(deflection_sequence,fig=fig,PID_param=parameters['PID_param'],
                                        PID_freq=parameters['PID_freq'],plotting_freq=parameters['plotting_freq'],
                                        saving_dir=saving_dir,out_fn=parameters['out_fn'])
        except KeyboardInterrupt:
            print("PID control interrupted. Saving data PID sequence data...")
            controller.export_PID_data(saving_dir=saving_dir,out_fn=parameters['out_fn'])
        
    run_wid.on_click(run_seq)
    display(run_wid)


