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
import datetime as DT
import pickle

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny
from skimage.draw import circle_perimeter, line, disk
from skimage.io import imread
from skimage.color import gray2rgb
from skimage import img_as_ubyte
from skimage.feature import match_template
import seaborn as sns

from scipy.interpolate import interp1d
from lmfit import Parameters, Model

import multiprocessing
from joblib import Parallel, delayed

import manipylator
import manipylator.utils as utils
 

# current directory used as default argument
cwd = os.getcwd()

# useful color list for plotting
color_list = [c['color'] for c in list(plt.rcParams['axes.prop_cycle'])] + sns.color_palette("Set1", n_colors=9,desat=.5)



def tune_detect_bead(fn,radius=10,radius_err=0.05,blur=3,low_threshold=10,high_threshold=15,frame=0,stack=True): 
    """
    Method to tune paramater to detect a bead as circle in a 2D image using the Hough circle transform
    The detected radius is computed with some margin of error given by radius_err
    The input image can be a stack or an image
    """

    # Load picture and detect edges
    if stack:
        stack = imread(fn)
        image = stack[frame]
    else: 
        image = imread(fn)

    image = img_as_ubyte(image) #convert to 8bit
    edges = canny(image, sigma=blur, low_threshold=low_threshold, high_threshold=high_threshold)

    # Detect array of radii
    hough_radii = np.arange(int(radius-radius_err*radius), int(radius+radius_err*radius)+1)
    hough_res = hough_circle(edges, hough_radii)

    # Select the most prominent circle
    accums, cx, cy, radii = hough_circle_peaks(hough_res, hough_radii,total_num_peaks=1)
    if len(cy)==0:
        raise Exception("No circle detected. Aborting...")
    center_y = cy[0] 
    center_x = cx[0] 
    radius = radii[0]

    fig,axes = plt.subplots(1,2,figsize=(12,24))
    
    # convert images to rgb
    image = gray2rgb(image)
    edges = img_as_ubyte(edges)  # binary to grayscale
    edges = gray2rgb(edges)  # grayscale to rgb 
    
    # draw detection on image as a circle in and a cross
    for i in np.arange(-1,2): #draw 3 px thick lines
        #draw circle
        circy, circx = circle_perimeter(center_y, center_x, radius+i,
                                        shape=image.shape)
        image[circy, circx] = utils.hex_to_rgb(color_list[0])
        edges[circy, circx] = utils.hex_to_rgb(color_list[0])

        #draw center cross
        rr, cc = line(center_y+i, center_x-5, center_y+i, center_x+5)
        rr_, cc_ = line(center_y-5, center_x+i, center_y+5, center_x+i)
        image[rr, cc] = utils.hex_to_rgb(color_list[1])
        image[rr_, cc_] = utils.hex_to_rgb(color_list[1])

    axes[0].imshow(edges, aspect='equal')
    axes[1].imshow(image, aspect='equal')
    plt.show(fig)

    return [center_x, center_y, radius]


def detect_bead(method="hough_circle",seg_param={},fn=None,image=None,outdir=None,out_fn=None,plot_seg=True,debug=False,save_image=True,dpi=300): 
    """
    Detect a bead using alternative segmentation methods:
    - if method is "hough_circle", it is detected as circle in a 2D image using the Hough circle transform. The detected radius is computed with some margin of error given by radius_err
    - if method is "pattern", it uses a pattern recognition based on an input image
    The segmentation parameters and input are given by a dict seg_param
    """

    # check segmentation parameters based on segmentation method
    if method=="hough_circle":
        if "radius" not in seg_param.keys():
            raise Exception("radius not in seg_param. At least the radius should be give. Aborting...")
        seg_param_default = {'radius_err':0.05,'blur':3,'low_threshold':10,'high_threshold':15}
        for param in ["radius_err","blur","low_threshold","high_threshold"]:
            if param not in seg_param.keys():
                seg_param[param] = seg_param_default[param]

    elif method=="pattern":
        if "pattern" not in seg_param.keys():
            raise Exception("pattern not in seg_param. An input pattern must be given to perform pattern recognition. Aborting...")
        pattern = img_as_ubyte(seg_param["pattern"])  # convert to 8bit
        patthern_h,patthern_w = pattern.shape

    else: 
        raise Exception("This segmentation is not supported, use: hough_circle or pattern. Aborting...")

    # Load picture and detect edges
    if image is None:
        image = imread(fn)
    image = img_as_ubyte(image) #convert to 8bit

    # Detect
    if method=="hough_circle":
        edges = canny(image, sigma=seg_param["blur"], low_threshold=seg_param["low_threshold"], high_threshold=seg_param["high_threshold"]) # edge detection
        hough_radii = np.arange(int(seg_param["radius"]-seg_param["radius_err"]*seg_param["radius"]), int(seg_param["radius"]+seg_param["radius_err"]*seg_param["radius"])) # array of radii
        hough_res = hough_circle(edges, hough_radii) #hough transform
        accums, cx, cy, radii = hough_circle_peaks(hough_res, hough_radii,total_num_peaks=1) # Select the most prominent circle

        # store detected circle
        if len(radii)>0:
            # center of the detected ROI
            center_y = cy[0] 
            center_x = cx[0] 
            radius = radii[0]
            # measure mean intensity in the detected ROI 
            rr, cc = disk((center_y, center_x), radius)
            detected_ROI = image[rr,cc]
            mean_intensity = detected_ROI.sum()/detected_ROI.size
            detected_dict = {"center_y":center_y,"center_x":center_x,"radius":radius}
        else: 
            raise Exception("No circle detected. Aborting...")

    elif method=="pattern":
        result = match_template(image, pattern)
        ij = np.unravel_index(np.argmax(result), result.shape)
        x, y = ij[::-1]  # position of the top-left corner of the detected pattern
        # center of the detected ROI
        center_x = x + patthern_w/2
        center_y = y + patthern_h/2
        # measure mean intensity in the detected ROI 
        detected_ROI = image[y:y+patthern_h, x:x+patthern_w]
        mean_intensity = detected_ROI.sum()/detected_ROI.size
        detected_dict = {"center_y":center_y,"center_x":center_x,'mean_intensity':mean_intensity, "detected_ROI":detected_ROI}

    if plot_seg:
        # set figure size
        n,m = image.shape

        if debug:
            fig,axes = plt.subplots(1,2,figsize=(12,24))
        else:    
            fig,ax = plt.subplots(frameon=False)
        
        image = gray2rgb(image)
        
        # draw detection on image as a circle in and a cross
        for i in np.arange(-1,2): #draw 3 px thick lines
            # draw center cross
            rr, cc = line(int(center_y+i), int(center_x-5), int(center_y+i), int(center_x+5))
            rr_, cc_ = line(int(center_y-5), int(center_x+i), int(center_y+5), int(center_x+i))
            image[rr, cc] = utils.hex_to_rgb(color_list[1])
            image[rr_, cc_] = utils.hex_to_rgb(color_list[1])

            # draw circle if hough_circle
            if method=="hough_circle":
                circy, circx = circle_perimeter(int(center_y), int(center_x), int(radius+i),
                                                shape=image.shape)
                image[circy, circx] = utils.hex_to_rgb(color_list[0])

        if debug and method=="hough_circle":
            axes[0].imshow(edges, cmap=plt.cm.gray, aspect='equal')
            axes[1].imshow(image, aspect='equal')
            plt.show(fig)
        else:
            ax.imshow(image, aspect='equal')
            ax.axis('off')

        if save_image:
            # prepare outdata directory
            if outdir is None:
                if fn is not None: 
                    outdir = osp.join(osp.dirname(fn),'outdata')
                else: 
                    outdir = cwd
            if not osp.exists(outdir):
                os.mkdir(outdir)
            if out_fn is None:
                if fn is not None:
                    out_fn = osp.split(fn)[1]
                else: 
                    out_fn = 'detected_bead.png'
            fig.savefig(osp.join(outdir,out_fn),dpi=dpi) #save to same dpi as input
            plt.close(fig)

    return detected_dict


def track_bead(stack_fn,method="hough_circle",seg_param={},stack=None,outdir=None,save_image=True): 
    """
    Detect bead using detect_bead for all frames of a stack using one of the methods: hough_circle and pattern
    """

    if stack is None:
        stack = imread(stack_fn)
    frame_num = stack.shape[0]

    # check segmentation parameters based on segmentation method
    if method=="hough_circle":
        if "radius" not in seg_param.keys():
            raise Exception("radius not in seg_param. At least the radius should be give. Aborting...")
        seg_param_default = {'radius_err':0.05,'blur':3,'low_threshold':10,'high_threshold':15}
        for param in ["radius_err","blur","low_threshold","high_threshold"]:
            if param not in seg_param.keys():
                seg_param[param] = seg_param_default[param]
    elif method=="pattern":
        if "pattern" not in seg_param.keys():
            raise Exception("pattern not in seg_param. An input pattern must be given to perform pattern recognition. Aborting...")
    else: 
        raise Exception("This segmentation is not supported, use: hough_circle or pattern. Aborting...")

    # outdata dataframe
    columns = ['frame','cx','cy','radius'] if method=="hough_circle" else ['frame','cx','cy']
    df_out = pd.DataFrame(columns=columns)
    
    for frame in range(frame_num):
        sys.stdout.write("\033[K")  # go back to previous line
        print('processing image {}/{}'.format(frame, frame_num - 1), flush=True, end='\r')

        img = stack[frame]
        out_fn = '{:04d}.png'.format(frame)
        detected_dict = detect_bead(method,seg_param,fn=stack_fn,image=img,out_fn=out_fn,outdir=outdir,save_image=save_image)
        detected_param = [frame,detected_dict['center_x'],detected_dict['center_y'],detected_dict['radius']] if  method=="hough_circle" else [frame,detected_dict['center_x'],detected_dict['center_y']]
        df_out.loc[frame,:] = detected_param

    df_out.to_csv(osp.join(outdir,'tip_pos.csv'))

    return df_out


def detect_bead_wrapper(image,frame,arg_dict):
    """
    Wrapper function to use detect_bead in a parallel computing
    """

    method = arg_dict["method"]

    if method=="hough_circle":
        default_arg = {'radius':50,
                    'radius_err':0.05,
                    'blur':10,
                    'low_threshold':10,
                    'high_threshold':15,
                    'outdir':None,
                    'plot_seg':True,
                    'debug':False,
                    'save_image':True,
                    'dpi':300,
                    }
        # add default agrument if missing 
        for k in default_arg.keys():
            if k not in arg_dict.keys():
                arg_dict[k] = default_arg[k]
        seg_param = {k:arg_dict[k] for k in ['radius','radius_err','blur','low_threshold','high_threshold']}
    elif method=="pattern":
        seg_param = {"pattern":arg_dict["pattern"]}

    out_fn = '{:04d}.png'.format(frame)
    data_list = detect_bead(method=method,seg_param=seg_param,fn=None,image=image,outdir=arg_dict["outdir"],out_fn=out_fn,
                            plot_seg=arg_dict["plot_seg"],debug=arg_dict["debug"],save_image=arg_dict["save_image"],dpi=arg_dict["dpi"])

    # export data
    pickle_dir = osp.join(arg_dict["outdir"],'data')
    if not osp.exists(pickle_dir): 
        os.mkdir(pickle_dir)
    pickle_fn = osp.join(pickle_dir, '{:04d}.p'.format(frame))
    pickle.dump(data_list, open(pickle_fn, "wb"))


def parallel_track_bead(stack_fn,arg_dict,stack=None): 
    """
    Track bead using detect_bead for all frames of a stack using parallel computing
    """

    method = arg_dict["method"]
    if method not in ["hough_circle","pattern"]: 
        raise Exception("Segmentation method missing use: hough_circle or pattern. Aborting...")

    if method=="hough_circle":
        default_arg = {'radius':50,
                    'radius_err':0.05,
                    'blur':10,
                    'low_threshold':10,
                    'high_threshold':15,
                    'outdir':None,
                    'plot_seg':True,
                    'debug':False,
                    'save_image':True,
                    'dpi':300,
                    }
        # add default agrument if missing 
        for k in default_arg.keys():
            if k not in arg_dict.keys():
                arg_dict[k] = default_arg[k]

    # get stack
    if stack is None:
        stack = imread(stack_fn)
    frame_num = stack.shape[0]

    # run parallel computing
    print('Running parallel detection over {} frames'.format(frame_num))
    Parallel(n_jobs=multiprocessing.cpu_count(),verbose=10)(delayed(detect_bead_wrapper)(image,frame,arg_dict) for frame,image in enumerate(stack))

    # read data
    pickle_dir = osp.join(arg_dict["outdir"],'data')
    columns = ['frame','cx','cy','radius'] if method=="hough_circle" else ['frame','cx','cy']
    df_out = pd.DataFrame(columns=columns)

    for frame in range(frame_num):
        pickle_fn = osp.join(pickle_dir, '{:04d}.p'.format(frame))
        detected_dict = pickle.load(open(pickle_fn, "rb"))
        detected_param = [frame,detected_dict['center_x'],detected_dict['center_y'],detected_dict['radius']] if  method=="hough_circle" else [frame,detected_dict['center_x'],detected_dict['center_y']]
        df_out.loc[frame,:] = detected_param

    df_out.to_csv(osp.join(arg_dict["outdir"],'tip_pos.csv'))

    return df_out



### Experiment analysis methods

def compute_canti_stiffness(canti_length,k_ref=0.2378,L_ref=14.5):
    """ 
    Compute cantilever stiffness based on its length using calibration data
    k_ref=k_tilde/L_ref^3 k_ref= 0.2378 mN/mm and L_ref=14.5mm for 20200716 calibration 
    """
    k_tilde=k_ref*(L_ref)**3 
    k=k_tilde/(canti_length)**3
    return k


def compute_deflection(exp,outdir,num_points=1024,plot_data=True,tracking_method='automated',save_data=True,moving_avg=None,add_fixed_pts=False,stage_orientation=-1):
    """
    Sync stage and tip data to compute deflection
    """
    exp_dir = osp.join(exp['root_dir'],exp['exp_dir'])
    fn_tip = exp['fn_tip']
    fn_stage = exp['fn_stage']
    date = exp['date']
    t0_tip = exp['t0_tip']
    dt = exp['frame_interval']
    lengthscale = exp['lengthscale']
    sign = exp['sign']

    #get data 
    if tracking_method == 'kymo':
        df_tip = pd.read_csv(osp.join(exp_dir,fn_tip),delimiter='\t',names=['frame','pos'])
    else:
        df_tip = pd.read_csv(osp.join(exp_dir,fn_tip))
        df_tip = df_tip[['frame','cx']]
        df_tip.columns = ['frame','pos']
        df_tip['pos'] = df_tip['pos']*lengthscale

    # check if several stage files
    if type(fn_stage) is list: 
        df_list = [pd.read_csv(osp.join(exp_dir,fn),index_col=0) for fn in fn_stage]
        df_stage = pd.concat(df_list,ignore_index=True)
    else: 
        df_stage = pd.read_csv(osp.join(exp_dir,fn_stage),index_col=0)

    # sync stage and tip
    t0 = df_stage.loc[0,'timestamp']  # experiment time zero defined as first movement
    df_tip['t_raw'] = df_tip['frame'] * dt
    df_tip['timestamp'] = utils.convert_to_timestamp(date=date,time=t0_tip) + df_tip['t_raw']
    df_tip['t_ref'] = df_tip['timestamp'] - t0

    if add_fixed_pts:  # add constant points for stage position at the end
        # get timestamp after last stage timepoint
        tf = df_stage["timestamp"].iloc[-1]  # last stage timestamp        
        timestamp_end = df_tip[df_tip['timestamp'] > tf]['timestamp'].values
        # concatenate df_stage
        time_list = [DT.datetime.fromtimestamp(ts) for ts in timestamp_end]
        formatted_time = [t.strftime("%H:%M:%S.%f") for t in time_list]
        set_pos_f = df_stage["set_pos"].iloc[-1]  # last set position
        true_pos_f = df_stage["true_pos"].iloc[-1]  # last true position
        stage_end_dict = {'set_pos': np.ones(len(timestamp_end)) * set_pos_f,  # list of constant positions
                        'true_pos': np.ones(len(timestamp_end)) * true_pos_f,  # list of constant positions
                        'time': formatted_time,
                        'timestamp': timestamp_end,
                        }
        df_stage_end = pd.DataFrame(stage_end_dict)  # df of constant positions after stage last movement 

        df_stage = pd.concat([df_stage,df_stage_end],ignore_index=True)  # concatenated stage positions
    
    # relative time
    df_stage['t_ref'] = df_stage['timestamp']-t0

    # center and orient (stage and image axes' orientation are opposite)
    df_stage['centered_pos'] = stage_orientation * (df_stage['true_pos'] - df_stage.loc[0,'true_pos'])
    df_tip['centered_pos'] = df_tip['pos'] - df_tip.loc[0,'pos']
    if moving_avg is not None:
        df_tip['centered_pos'] = df_tip['centered_pos'].rolling(moving_avg,min_periods=0).mean()

    # interpolate positions and compare
    f_tip = interp1d(df_tip['t_ref'].values,df_tip['centered_pos'].values)
    f_stage = interp1d(df_stage['t_ref'].values,df_stage['centered_pos'].values)

    T = min(df_tip['t_ref'].max(),df_stage['t_ref'].max())
    t = np.linspace(0,T,num_points)
    tip_reg = f_tip(t)
    stage_reg = f_stage(t)

    # compute deflection
    deflection = stage_reg - tip_reg  # defined so if tip is lagging behind, deflection is positive for a movement towards the right
    deflection *= sign  # adjust sign if need be (make deflection positive if movement towards the left)

    if plot_data:
        # plot_raw
        fig,ax = plt.subplots()
        df_tip.plot(x='t_ref',y='centered_pos',ax=ax,color=color_list[0],label='tip')
        df_stage.plot(x='t_ref',y='centered_pos',ax=ax,color=color_list[1],label='stage')
        ax.set_xlabel('time (sec)')
        ax.set_ylabel(r'centered position ($\mu m$)')
        fig.tight_layout()
        fig.savefig(osp.join(outdir,'synced_stage_tip.png'),dpi=300)

        # plot deflection
        fig,ax = plt.subplots()
        ax.plot(t,deflection)
        ax.set_xlabel('time (sec)')
        ax.set_ylabel(r'deflection ($\mu m$)')
        fig.tight_layout()
        fig.savefig(osp.join(outdir,'deflection.png'),dpi=300)

        plt.close('all')

    if save_data:
        df_tip.to_csv(osp.join(outdir,'tip.csv'))
        df_stage.to_csv(osp.join(outdir,'stage.csv'))

    return {'t':t, 'deflection':deflection, 'tip_reg':tip_reg, 'stage_reg':stage_reg}


def analyze_chirp(exp_dir,exp=None,plot_data=True,tracking_method='kymo',save_data=True,moving_avg=None,num_points=1024,add_fixed_pts=False,stage_orientation=-1):
    """
    Analyze chirp experiment by computing stress, strain and their Fourier transform
    """
    outdir = osp.join(exp_dir,'outdata')
    if not osp.exists(outdir):
        os.mkdir(outdir)

    # get exp parameters
    if exp is None: 
        info_fn = osp.join(exp_dir,'info.csv')
        if osp.exists(info_fn):
            exp = utils.load_dict(info_fn)
        else: 
            raise Exception('No experiment dict given. Aborting...')
    contact_area = exp['contact_area']
    contact_perimeter = 2 * np.sqrt(np.pi * contact_area)  # circle approximation
    canti_length = exp['canti_length']
    k = compute_canti_stiffness(canti_length)

    # compute deflection
    defl_dict = compute_deflection(exp,outdir,num_points=num_points,plot_data=plot_data,tracking_method=tracking_method,save_data=save_data,moving_avg=moving_avg,add_fixed_pts=add_fixed_pts,stage_orientation=stage_orientation)
    t = defl_dict['t']
    deflection = defl_dict['deflection']
    tip_reg = defl_dict['tip_reg']

    force = - deflection*k # in uN / minus sign: force on tissue

    if contact_area is not None:
        stress = force / contact_perimeter # 2D stress

        # compute G*
        T = np.max(t)
        gamma_ = np.fft.fft(tip_reg)
        sigma_ = np.fft.fft(stress)
        G_star = sigma_/gamma_
        G_p = np.real(G_star)
        G_s = np.imag(G_star)
        #xf  =  np.linspace(0.0, 1.0*num_points/(2.0*T), num_points//2)
        xf = np.fft.fftfreq(num_points, d=T/num_points) #frequencies
        xf = xf*2*np.pi #angular frequencies
        df_Gstar = pd.DataFrame({'omega':xf[0:num_points//2],'gamma_star_mod':np.abs(gamma_)[0:num_points//2],'sigma_star_mod':np.abs(sigma_)[0:num_points//2],'Gp':G_p[0:num_points//2],'Gs':G_s[0:num_points//2]})  # remove redundant frequencies


    if plot_data:
        # remove non-relevant high frequencies 
        df_Gstar_zoom = df_Gstar[df_Gstar['omega'] < exp['w1']]

        # plot force
        fig,ax=plt.subplots()
        ax.plot(t,force)
        ax.set_xlabel('time (sec)')
        ax.set_ylabel(r'force ($\mu N$)')
        fig.tight_layout()
        fig.savefig(osp.join(outdir,'force.png'),dpi=300)

        if contact_area is not None:
            # plot stress
            fig,ax=plt.subplots()
            ax.plot(t,stress)
            ax.set_xlabel('time (sec)')
            ax.set_ylabel(r'2D stress (N/m)')
            fig.tight_layout()
            fig.savefig(osp.join(outdir,'stress.png'),dpi=300)

            # plot FFT
            fig,ax=plt.subplots()
            ax.plot(df_Gstar['omega'].values,df_Gstar['gamma_star_mod'].values,color=color_list[0],label=r"$\vert\gamma^\star \vert$")
            ax.plot(df_Gstar['omega'].values,df_Gstar['sigma_star_mod'].values,color=color_list[1],label=r"$\vert\sigma^\star \vert$")
            ax.legend(frameon=False)
            #ax.set_xscale('log')
            ax.set_ylabel(r"TF modulus")
            ax.set_xlabel(r"$\omega$ (rad/s)")
            fig.tight_layout()
            fig.savefig(osp.join(outdir,'raw_TF.png'),dpi=300)

            # plot zoomed FFT
            fig,ax=plt.subplots()
            ax.plot(df_Gstar_zoom['omega'].values,df_Gstar_zoom['gamma_star_mod'].values,color=color_list[0],label=r"$\vert\gamma^\star \vert$")
            ax.plot(df_Gstar_zoom['omega'].values,df_Gstar_zoom['sigma_star_mod'].values,color=color_list[1],label=r"$\vert\sigma^\star \vert$")
            ax.legend(frameon=False)
            #ax.set_xscale('log')
            ax.set_ylabel(r"TF modulus")
            ax.set_xlabel(r"$\omega$ (rad/s)")
            fig.tight_layout()
            fig.savefig(osp.join(outdir,'raw_TF_zoom.png'),dpi=300)

            # plot full Gstar
            fig,ax=plt.subplots()
            ax.plot(df_Gstar['omega'].values[1:],df_Gstar['Gp'].values[1:],color=color_list[0],label=r"G'")  # not plotting 1 data point because non-zero
            ax.plot(df_Gstar['omega'].values,df_Gstar['Gs'].values,color=color_list[1],label=r"G''")
            ax.legend(frameon=False)
            #ax.set_xscale('log')
            ax.set_ylabel(r"G',G'' (N/m)")
            ax.set_xlabel(r"$\omega$ (rad/s)")
            fig.tight_layout()
            fig.savefig(osp.join(outdir,'G_star.png'),dpi=300)

            # plot zoomed Gstar 
            fig,ax=plt.subplots()
            ax.plot(df_Gstar_zoom['omega'].values[1:],df_Gstar_zoom['Gp'].values[1:],color=color_list[0],label=r"G'")  # not plotting 1 data point because non-zero
            ax.plot(df_Gstar_zoom['omega'].values,df_Gstar_zoom['Gs'].values,color=color_list[1],label=r"G''")
            ax.legend(frameon=False)
            #ax.set_xscale('log')
            ax.set_ylabel(r"G',G'' (N/m)")
            ax.set_xlabel(r"$\omega$ (rad/s)")
            fig.tight_layout()
            fig.savefig(osp.join(outdir,'G_star_zoom.png'),dpi=300)

        plt.close('all')

    if save_data:
        if contact_area is not None:
            df_out = pd.DataFrame({'t':t,'tip_interpol':tip_reg,'deflection':deflection,'force':force,'stress':stress})
        else: 
            df_out = pd.DataFrame({'t':t,'tip_interpol':tip_reg,'deflection':deflection,'force':force})
        df_out.to_csv(osp.join(outdir,'deflection.csv'))

        df_Gstar.to_csv(osp.join(outdir,'G_star.csv'))

    return df_out


def analyze_sweep(exp_dir,exp=None,plot_data=True,tracking_method='kymo',save_data=True,moving_avg=None,num_points=1024,add_fixed_pts=False,stage_orientation=-1):
    """
    Analyze free sweep experiment by plotting deflection, force and stress over time 
    """

    outdir = osp.join(exp_dir,'outdata')
    if not osp.exists(outdir):
        os.mkdir(outdir)

    # get exp parameters
    if exp is None: 
        info_fn = osp.join(exp_dir,'info.csv')
        if osp.exists(info_fn):
            exp = utils.load_dict(info_fn)
        else: 
            raise Exception('No experiment dict given. Aborting...')
    contact_area = exp['contact_area']
    canti_length = exp['canti_length']
    k = compute_canti_stiffness(canti_length)

    # compute deflection
    defl_dict = compute_deflection(exp,outdir,num_points=num_points,plot_data=plot_data,tracking_method=tracking_method,save_data=save_data,moving_avg=moving_avg,add_fixed_pts=add_fixed_pts,stage_orientation=stage_orientation)
    t = defl_dict['t']
    deflection = defl_dict['deflection']
    tip_reg = defl_dict['tip_reg']

    force = deflection * k  #in uN
    if contact_area is not None:
        stress = (force/contact_area)*1e6 #in Pa

    if plot_data:
        # plot force
        fig,ax=plt.subplots()
        ax.plot(t,force)
        ax.set_xlabel('time (sec)')
        ax.set_ylabel(r'force ($\mu N$)')
        fig.tight_layout()
        fig.savefig(osp.join(outdir,'force.png'),dpi=300)

        if contact_area is not None:
            # plot stress
            fig,ax=plt.subplots()
            ax.plot(t,stress)
            ax.set_xlabel('time (sec)')
            ax.set_ylabel(r'stress (Pa)')
            fig.tight_layout()
            fig.savefig(osp.join(outdir,'stress.png'),dpi=300)

        plt.close('all')

    if save_data:
        if contact_area is not None:
            df_out = pd.DataFrame({'t':t,'tip_interpol':tip_reg,'deflection':deflection,'force':force,'stress':stress})
        else: 
            df_out = pd.DataFrame({'t':t,'tip_interpol':tip_reg,'deflection':deflection,'force':force})
        df_out.to_csv(osp.join(outdir,'deflection.csv'))

    return df_out


def fit_creep(df,relax_time=None,vary_beta=False,guess={'delta':100,'tau':100,'rate':0.1,'beta':1},fitrange=[None,None],
    saving_dir=cwd,print_report=False,plot_fit=True,plot_fn=None,export_data_pts=True):
    """
    Fit a creep experiment with potentially 
    df: pandas.DataFrame with columns: t,pos
    relax_time: starting time of relaxation phase, if None only creep
    vary_beta: vary beta parameter
    guess: initial guess for fitting function
    fitrange: list of maximum time for fitting: [creep_lim,relax_lim]. If None, no limit
    """

    # fitting model
    func = lambda t,delta,tau,rate,beta:delta*(1-beta*np.exp(-t/tau))+rate*t
    model = Model(func)
    p = model.make_params(delta=guess['delta'],tau=guess['tau'],rate=guess['rate'],beta=guess['beta'])
    p['beta'].set(min=0,max=1,vary=vary_beta)
    p['tau'].set(min=1e-10,max=5000)
    p['delta'].set(min=0)
    p['rate'].set(min=0)

    fit_relax = False
    if relax_time is not None:
        fit_relax = True
        ind_relax = df.iloc[(df['t']-relax_time).abs().argsort()].index[0]  # get index of closest t to relax_time
        df1 = df.loc[0:ind_relax,:]
        df2 = df.loc[ind_relax:,:].reset_index(drop=True)
    else: 
        df1 = df


    fit_output = {}

    # creep fit
    if fitrange[0] is not None:
        df1 = df1[df1['t']<fitrange[0]]
    best1 = model.fit(df1['pos'].values,t=df1['t'].values,params=p)
    x_fit1 = df1['t'].values
    y_fit1 = best1.best_fit
    if print_report:
        print(best1.fit_report())

    fit_output['creep_fit']={'fit_report':best1.fit_report(),
                            'delta':best1.best_values['delta'],
                            'tau':best1.best_values['tau'],
                            'beta':best1.best_values['beta'],
                            'rate':best1.best_values['rate'], 
                            }
    if export_data_pts:
        fitparam_fn = osp.join(saving_dir,'creep_fitparam.csv') if plot_fn is None else plot_fn[:-4]+'_fitparam.csv'
        utils.write_dict(fit_output['creep_fit'],fitparam_fn)

    # relax fit
    if fit_relax:
        df2['t_'] = df2['t'] - df2.loc[0,'t']  # reset time to zero 
        if fitrange[1] is not None:
            df2 = df2[df2['t_']<fitrange[1]]
        df2['pos'] = df2.loc[0,'pos'] - df2['pos']  # reset offset and change sign
        best2 = model.fit(df2['pos'].values,t=df2['t_'].values,params=p)  # fit
        if print_report:
            print(best2.fit_report())
        
        # transform fitted curve
        x_fit2 = df2['t'].values
        y_fit2 = - best2.best_fit  # invert
        y_fit2 += df.loc[ind_relax,'pos']  # offset

        fit_output['relax_fit']={'fit_report':best2.fit_report(),
                                'delta':best2.best_values['delta'],
                                'tau':best2.best_values['tau'],
                                'beta':best2.best_values['beta'],
                                'rate':best2.best_values['rate'], 
                                }
        if export_data_pts:
            fitparam_fn = osp.join(saving_dir,'creep_fitparam_relax.csv') if plot_fn is None else plot_fn[:-4]+'_fitparam_relax.csv'
            utils.write_dict(fit_output['relax_fit'],fitparam_fn)


    # plot_fit
    if plot_fit:
        fig,ax = plt.subplots(figsize=(4,3))
        df.plot(x='t',y='pos',ax=ax,legend=None)
        ax.plot(x_fit1,y_fit1, ls='--', color=color_list[1])
        if fit_relax:
            ax.plot(x_fit2,y_fit2, ls='--', color=color_list[1])
        ax.set_xlabel('time (sec)')
        ax.set_ylabel(r'tip position ($\mu m$)')
        fig.tight_layout()
        plot_fn = osp.join(saving_dir,'creep.png') if plot_fn is None else plot_fn
        fig.savefig(plot_fn,dpi=300)

    # export plot data points
    if export_data_pts:
        #save raw data points
        df_raw = df[['t','pos']]
        plot_pts_fn = osp.join(saving_dir,'creep.csv') if plot_fn is None else plot_fn[:-4]+'.csv'
        df_raw.to_csv(plot_pts_fn)

        #save fit data points
        x = np.concatenate((x_fit1,x_fit2)) if fit_relax else x_fit1
        y = np.concatenate((y_fit1,y_fit2)) if fit_relax else y_fit1
        df_fit = pd.DataFrame({'t':x,'fit':y})
        plot_fit_fn = osp.join(saving_dir,'creep_fit.csv') if plot_fn is None else plot_fn[:-4]+'_fit.csv'
        df_raw.to_csv(plot_fit_fn)


    return fit_output


def analyze_creep(exp_dir,exp=None,use_retrack=True,plot_PID=True,vary_beta=False,guess={'delta':100,'tau':100,'rate':0.1,'beta':1},print_report=False,
    outlier_lim=None,moving_avg=None,plot_fit=True,dont_fit=False): 
    """
    Analyze a creep experiment by fitting it
    use_retrack: bool if False position from PID file
    outlier_lim: list [low_outlier, high_outlier]: remove points out of these limits
    moving_avg: if None, no moving average, if int perform moving average with window size given by moving_avg
    """

    outdir = osp.join(exp_dir,'outdata')
    if not osp.exists(outdir):
        os.mkdir(outdir)

    # get exp parameters
    if exp is None: 
        info_fn = osp.join(exp_dir,'info.csv')
        if osp.exists(info_fn):
            exp = utils.load_dict(info_fn)
        else: 
            raise Exception('No experiment dict given. Aborting...')

    PID_fn_list = exp['PID_fn_list']
    fn_tip = exp['fn_tip']
    #t0_tip = exp['t0_tip']
    #contact_area = exp['contact_area']
    relax_time = exp['relax_time']
    dt = exp['frame_interval']
    canti_length = exp['canti_length']
    lengthscale = exp['lengthscale']
    sign = exp['sign']
    k = compute_canti_stiffness(canti_length)

    # get data 
    df_list = [pd.read_csv(osp.join(exp_dir,fn)) for fn in PID_fn_list]
    df_PID = pd.concat(df_list,ignore_index=True)
    df_PID['relative_time'] = df_PID['timestamp'] - df_PID.loc[0,'timestamp']

    if use_retrack:
        df_tip = pd.read_csv(osp.join(exp_dir,fn_tip))
        df_tip = df_tip[['frame','cx']]
        df_tip.columns = ['frame','pos']  # rename
        #scale
        df_tip['pos'] = df_tip['pos'] * lengthscale
        df_tip['t'] = df_tip['frame'] * dt
    else:
        tip_pos_col = 'tip_pos_x' if 'tip_pos_x' in df_PID.columns else 'tip_pos'  # make compatible between old and new column names
        df_tip = df_PID[['relative_time',tip_pos_col]]
        df_tip.columns = ['t','pos']  # rename

    # fit
    # prepare data
    if exp['t0_tip'] is not None: 
        df_tip = df_tip[df_tip['t'] >= exp['t0_tip']].reset_index(drop=True)
    df_tip['pos'] = df_tip['pos'] - df_tip.loc[0,'pos']  # center
    df_tip['pos'] = sign * df_tip['pos']  # orient
    if outlier_lim is not None:
        if outlier_lim[0] is not None:
            df_tip = df_tip[df_tip['pos'] > outlier_lim[0]]
        elif outlier_lim[1] is not None:
            df_tip = df_tip[df_tip['pos'] < outlier_lim[1]]
    if moving_avg is not None:
        df_tip['pos'] = df_tip['pos'].rolling(moving_avg,min_periods=0).mean()

    plot_fn = osp.join(outdir,'creep.png')

    if dont_fit:
        fig,ax = plt.subplots()
        df_tip.plot(x='t',y='pos',ax=ax,legend=None)
        ax.set_xlabel('time (sec)')
        ax.set_ylabel(r'tip position ($\mu m$)')
        fig.tight_layout()
        fig.savefig(plot_fn,dpi=300)

        fit_output = None
    else: 
        fit_output = fit_creep(df_tip,relax_time=relax_time,vary_beta=vary_beta,guess=guess,saving_dir=outdir,print_report=print_report,plot_fit=plot_fit,plot_fn=plot_fn)

    if plot_PID: 
        fig,axes = plt.subplots(3,1, figsize=(8,15))
        labels = ['measured', 'correction', 'setpoint']
        params = ['measured_def', 'applied_def', 'setpoint']
        for i in range(3):
            axes[0].plot(df_PID['relative_time'].values,df_PID[params[i]].values, color=color_list[i], label=labels[i])
        axes[0].set_xlabel('time (sec)')
        axes[0].set_title('PID control')
        axes[0].set_ylabel(r'deflection ($\mu m$)')
        axes[0].legend(frameon=False)

        axes[1].plot(df_PID['relative_time'].values,df_PID['stage_pos'].values)
        axes[1].set_title('stage transformed position')
        axes[1].set_ylabel(r'position ($\mu m$)')

        axes[2].plot(df_PID['relative_time'].values,df_PID['tip_intensity'].values)
        axes[2].set_title('tip intensity')
        axes[2].set_ylabel(r'mean intensity')

        fig.tight_layout()
        fig.savefig(osp.join(outdir,'PID.png'),dpi=300) 

    return fit_output


def get_creep_outdata(dirdata,debug=False): 
    """
    Get creep assay outdata of series of experiments on a specific date given by dirdata name
    """
    col = ['date','exp','creep_fn','creep_fit_fn','delta','tau','rate','delta_relax','tau_relax','rate_relax',
           'canti_id','canti_length','canti_stiffness','contact_area',
           'set_deflection','set_force','set_stress','relax_time','sign']
    
    df_out = pd.DataFrame(columns=col)
    dir_list = []
    for d in os.listdir(dirdata):
        if osp.isdir(osp.join(dirdata,d)) and d!='outdata':
            dir_list.append(d)
    
    root_dir,date = osp.split(dirdata)

    i = 0
    for d in dir_list: 
        if debug: 
            print(d)
        info = utils.load_dict(osp.join(dirdata,d,'info.csv'))
        if debug: 
            print(info)
        
        df_out.loc[i,'date'] = date
        df_out.loc[i,'exp'] = osp.join(date,d)
        df_out.loc[i,'canti_id'] = info['canti_id']
        df_out.loc[i,'canti_length'] = info['canti_length']
        canti_stiffness = compute_canti_stiffness(info['canti_length'])
        df_out.loc[i,'canti_stiffness'] = canti_stiffness
        df_out.loc[i,'contact_area'] = info['contact_area']
        df_out.loc[i,'set_deflection'] = info['set_deflection']
        df_out.loc[i,'relax_time'] = info['relax_time']
        df_out.loc[i,'sign'] = info['sign']
        set_force = info['set_deflection'] * canti_stiffness
        df_out.loc[i,'set_force'] = set_force
        df_out.loc[i,'set_stress'] = set_force / info['contact_area']
        
        creep_fn = osp.join(dirdata,d,'outdata','creep.csv')
        if osp.exists(creep_fn): 
            df_out.loc[i,'creep_fn'] = osp.join(date,d,'outdata','creep.csv') # relative path
        
        creep_fit_fn = osp.join(dirdata,d,'outdata','creep_fit.csv')
        if osp.exists(creep_fit_fn): 
            df_out.loc[i,'creep_fit_fn'] = osp.join(date,d,'outdata','creep_fit.csv') # relative path
        
        creep_fitparam_fn = osp.join(dirdata,d,'outdata','creep_fitparam.csv')
        if osp.exists(creep_fitparam_fn): 
            creep_fitparam = utils.load_dict(creep_fitparam_fn)
            df_out.loc[i,'delta'] = creep_fitparam['delta']
            df_out.loc[i,'tau'] = creep_fitparam['tau']
            df_out.loc[i,'rate'] = creep_fitparam['rate']

        creep_fitparam_relax_fn = osp.join(dirdata,d,'outdata','creep_fitparam_relax.csv')
        if osp.exists(creep_fitparam_relax_fn): 
            creep_fitparam_relax = utils.load_dict(creep_fitparam_relax_fn)
            df_out.loc[i,'delta_relax'] = creep_fitparam_relax['delta']
            df_out.loc[i,'tau_relax'] = creep_fitparam_relax['tau']
            df_out.loc[i,'rate_relax'] = creep_fitparam_relax['rate']
            
        i+=1
        
    return df_out


def get_sweep_outdata(dirdata,debug=False): 
    """
    Get sweep assay outdata of series of experiments on a specific date given by dirdata name
    """
    col = ['date','exp','deflection_fn','canti_id','canti_length',
           'canti_stiffness','contact_area','strain_rate']
    
    df_out = pd.DataFrame(columns=col)
    dir_list = []
    for d in os.listdir(dirdata):
        if osp.isdir(osp.join(dirdata,d)) and d!='outdata':
            dir_list.append(d)
    
    root_dir,date = osp.split(dirdata)

    i = 0
    for d in dir_list: 
        if debug: 
            print(d)
        info = utils.load_dict(osp.join(dirdata,d,'info.csv'))
        if debug: 
            print(info)
        
        df_out.loc[i,'date'] = date
        df_out.loc[i,'exp'] = osp.join(date,d)
        df_out.loc[i,'canti_id'] = info['canti_id']
        df_out.loc[i,'canti_length'] = info['canti_length']
        canti_stiffness = compute_canti_stiffness(info['canti_length'])
        df_out.loc[i,'canti_stiffness'] = canti_stiffness
        df_out.loc[i,'contact_area'] = info['contact_area']
#        df_out.loc[i,'strain_rate'] = info['strain_rate'] ## get sweep_rate from param file instead if need be
        
        if osp.exists(osp.join(dirdata,d,'outdata','deflection.csv')): 
            df_out.loc[i,'deflection_fn'] = osp.join(date,d,'outdata','deflection.csv') # relative path
            
        i+=1
        
    return df_out


def get_chirp_outdata(dirdata,debug=False): 
    """
    Get chirp assay outdata of series of experiments on a specific date given by dirdata name
    """
    col = ['date','exp','deflection_fn','G_star_fn','canti_id','canti_length',
           'canti_stiffness','contact_area','w0','w1']
    
    df_out = pd.DataFrame(columns=col)
    dir_list = []
    for d in os.listdir(dirdata):
        if osp.isdir(osp.join(dirdata,d)) and d!='outdata':
            dir_list.append(d)
    
    root_dir,date = osp.split(dirdata)

    i = 0
    for d in dir_list: 
        if debug: 
            print(d)
        info = utils.load_dict(osp.join(dirdata,d,'info.csv'))
        if debug: 
            print(info)
        
        df_out.loc[i,'date'] = date
        df_out.loc[i,'exp'] = osp.join(date,d)
        df_out.loc[i,'canti_id'] = info['canti_id']
        df_out.loc[i,'canti_length'] = info['canti_length']
        canti_stiffness = compute_canti_stiffness(info['canti_length'])
        df_out.loc[i,'canti_stiffness'] = canti_stiffness
        df_out.loc[i,'contact_area'] = info['contact_area']
        df_out.loc[i,'w0'] = info['w0']
        df_out.loc[i,'w1'] = info['w1']
        
        for fn in ['deflection.csv','G_star.csv']:
            fn_path = osp.join(dirdata,d,'outdata',fn)
            if osp.exists(fn_path): 
                df_out.loc[i,fn[:-4]+'_fn'] = fn_path # relative path
            
        i+=1
        
    return df_out


def plot_pooled_Gstar(df_all,root_dir,label=None,color_code=None,):
    """
    Plot all Gstar together
    """

    color_code_label = {'canti_stiffness':'cantilever stiffness (N/m)',
                        'contact_area': r'contact_area $(\mu m^2)$'
                        }

    outdir = osp.join(root_dir,'outdata')
    if not osp.exists(outdir):
        os.mkdir(outdir)

    fig1,ax1 = plt.subplots() # G'
    fig2,ax2 = plt.subplots() # G''

    if color_code is not None:
        if color_code in df_all.columns:
            cmap = plt.get_cmap('plasma')
            norm = plt.Normalize(df_all[color_code].min(), df_all[color_code].max())
            lab = color_code_label[color_code] if color_code in color_code_label.keys() else color_code
            utils.plot_cmap(outdir, lab, 'plasma', df_all[color_code].min(), df_all[color_code].max(),suffix='_'+color_code)
        else: 
            print("WARNING: {} not a supported parameter".format(color_code))
            color_code = None
    
    i = 0
    for ind in df_all.index:
        fn = osp.join(root_dir,df_all.loc[ind,'G_star_fn'])
        df = pd.read_csv(fn,index_col=0)
        df_zoom = df[df['omega'] < df_all.loc[ind,'w1']]

        if label is not None:
            if label in df_all.columns: 
                label_ = df_all.loc[ind,label]
            else: 
                print("WARNING: {} not a supported parameter".format(label))
                label_ = None

        if color_code is None:
            color = color_list[i%len(color_list)]
        else: 
            color = cmap(norm(df_all.loc[ind,color_code]))
        # plot
        ax1.plot(df_zoom['omega'].values[1:],df_zoom['Gp'].values[1:],color=color,label=label_)  # not plotting 1 data point because non-zero
        ax2.plot(df_zoom['omega'].values,df_zoom['Gs'].values,color=color,label=label_)

        i += 1

    if label is not None:
        ax1.legend(frameon=False)
        ax2.legend(frameon=False)
    #ax.set_xscale('log')
    ax1.set_ylabel(r"G' (N/m)")
    ax2.set_ylabel(r"G'' (N/m)")
    ax1.set_xlabel(r"$\omega$ (rad/s)")
    ax2.set_xlabel(r"$\omega$ (rad/s)")
    fig1.tight_layout()
    fig2.tight_layout()
    suffix = '_'+color_code if color_code is not None else ''
    fig1.savefig(osp.join(outdir,'all_Gp'+suffix+'.png'),dpi=300)
    fig2.savefig(osp.join(outdir,'all_Gs'+suffix+'.png'),dpi=300)

    plt.close('all')


def batch_analyze_chirp(df_all,root_dir): 
    """
    Run analysis on a database given by df_all
    """
    for ind in df_all.index:
        exp_dir = fn = osp.join(root_dir,df_all.loc[ind,'exp'])

        # load info
        info_fn = osp.join(exp_dir,'info.csv')
        if osp.exists(info_fn):
            exp = utils.load_dict(info_fn)
            exp['root_dir'] = root_dir   # adding root_dir to exp info
            analyze_chirp(osp.join(root_dir,exp['exp_dir']),exp=exp,plot_data=True,tracking_method='automated',save_data=True)
        else: 
            print('WARNING: {} does not exist'.format(info_fn))