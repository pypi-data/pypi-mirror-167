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
import datetime
import time

import numpy as np
import matplotlib.pyplot as plt
import csv
import matplotlib as mpl
from skimage.io import imread
from skimage import img_as_ubyte
from skimage.exposure import rescale_intensity
import seaborn as sns

from IPython.display import Markdown, display

from scipy.optimize import curve_fit
 
 
# useful color list for plotting
color_list = [c['color'] for c in list(plt.rcParams['axes.prop_cycle'])] + sns.color_palette("Set1",n_colors=9,desat=.5)


def printmd(string):
    """
    print text using Markdown formatting in notebook
    """
    display(Markdown(string))


def hex_to_rgb(value):
    """
    transform color hex code to rgb, from https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python
    """

    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def convert_to_timestamp(time,date):
    """convert a date and time with respective format %Y-%m-%d and %H:%M:%S.%f to a timestamp with millisecond precision"""
    concat=date+' '+time 
    return datetime.datetime.strptime(concat,"%Y:%m:%d %H:%M:%S.%f").timestamp()


def write_dict(dicts, filename, dict_names=None):
    """Write a dict or a list of dict into a csv file."""
    if type(dicts) is dict:
        dicts = [dicts]

    if type(dict_names) is list:
        if len(dicts) != len(dict_names):
            print("Warning: the name list doesn't match the dict list. Not printing names")
            dict_names = None

    with open(filename, "w+") as f:
        w = csv.writer(f)
        for i, d in enumerate(dicts):
            if type(d) is dict:
                if dict_names is not None:
                    f.write(dict_names[i] + '\n')
                for key, val in d.items():
                    w.writerow([key, val])
                f.write('\n')


def load_dict(filename):
    """Read a csv file and returns a converted dict"""
    if not filename.endswith('.csv'): 
        raise Exception("ERROR: No csv file passed. Aborting...")

    if not osp.exists(filename): 
        raise Exception("ERROR: File does not exist. Aborting...")

    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {}
        for rows in reader:
            if len(rows)>0:
                if rows[1] == '':
                    mydict[rows[0]] = None
                else:
                    try: 
                        mydict[rows[0]] = eval(rows[1]) #if needs conversion
                    except:
                        mydict[rows[0]] = rows[1] #if string

    return mydict


def fit_lin(data,fitxrange=None,zero_intercept=False):
    """This function performs a linear fit. Some fitting range can be specified with fitxrange. It returns the fir parameters, the error the fitted curve in a list"""
    x0=data[:,0]
    #prepare subdata
    if fitxrange:
        if type(fitxrange) is list:
            xmin = fitxrange[0]; xmax = fitxrange[1]
            if xmin is None:
                xmin = data[0,0]
            if xmax is None:
                xmax = data[-1,0]
        elif fitxrange <= 1:
            xmax = fitxrange*data[-1,0]
            xmin = data[0,0]
        else:
            print("WARNING: no valid fitxrange provided")
        data = data[(data[:,0]<=xmax) & (data[:,0]>=xmin)]
    
    #fiting function
    if zero_intercept:
        f=lambda x,a:a*x
    else:
        f=lambda x,a,b:a*x+b

    #initialize output
    fit_dict = {'parameters':None,
                'errors': None,
                'fitted': None, 
                'x_fit': None,
                'fitted_tot': None,
                'Rsq': None,
                'success': False}
    #fit
    if data.shape[0]>1:
        try:
            parameters,covar = curve_fit(f,data[:,0],data[:,1])
            if zero_intercept:
                fitted=f(data[:,0],parameters[0]) #fitted y-data on the fitxrange interval
                fitted_tot=f(x0,parameters[0])  #fitted y-data on the total interval
            else:
                fitted=f(data[:,0],parameters[0],parameters[1])
                fitted_tot=f(x0,parameters[0],parameters[1])
            #Rsquared
            ymean=0 if zero_intercept else np.mean(data[:,1])
            Stot=np.square(data[:,1]-ymean).sum()
            Sres=np.square(data[:,1]-fitted).sum()
            Rsq=1-Sres/Stot
            
            #store fit data
            fit_dict['parameters'] = parameters
            fit_dict['errors'] = np.sqrt(np.diag(covar))
            fit_dict['fitted'] = fitted
            fit_dict['x_fit'] = data[:,0]
            fit_dict['fitted_tot'] = fitted_tot
            fit_dict['Rsq'] = Rsq
            fit_dict['success'] = True
            
        except RuntimeError:
            print("Fit failed")

    return fit_dict


def plot_cmap(plot_dir, label, cmap, vmin, vmax, suffix=''):
    """ Plot colormap given by cmap with boundaries vmin and vmax."""

    fig = plt.figure(figsize=(8, 3))
    ax = fig.add_axes([0.05, 0.80, 0.9, 0.15])
    norm = plt.Normalize(vmin=vmin, vmax=vmax)
    cb = mpl.colorbar.ColorbarBase(ax, cmap=plt.get_cmap(cmap), norm=norm, orientation='horizontal')
    ax.tick_params(labelsize=16)
    cb.set_label(label=label, size=24)
    filename = osp.join(plot_dir, 'colormap'+suffix+'.png')
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close(fig)


def select_ROI(fn,x_range,y_range,frame=0,intensity_range=[0,255],stack=True):
    """
    Select ROI on an image based on x_range, y_range. Useful to be passed to an interactive widget method
    If stack is True, a stack must be passed. 
    """
    
    # select image
    if not stack:
        image = imread(fn)
    else:
        stack = imread(fn)
        if frame < 0 or frame > len(stack) - 1:
            raise ValueError("frame must be an integer between {} and {}".format(0,len(stack) - 1))
        image = stack[frame]

    # convert to 8 bit and set intensity
    h,w = image.shape
    image = img_as_ubyte(image)
    image = rescale_intensity(image,in_range=(intensity_range[0],intensity_range[1]))
    
    # plot
    fig, ax = plt.subplots(figsize=(12,12))
    ax.imshow(image, cmap=plt.cm.gray)
    rect = plt.Rectangle((x_range[0], y_range[0]), x_range[1]-x_range[0], y_range[1]-y_range[0],lw=2,edgecolor=color_list[0], facecolor='none')
    ax.add_patch(rect)
    center_y = y_range[0] + (y_range[1] - y_range[0])/2
    center_x = x_range[0] + (x_range[1] - x_range[0])/2
    ax.plot([x_range[0],x_range[1]],[center_y,center_y],color=color_list[1],lw=2) # plot central y line
    ax.plot([center_x,center_x],[y_range[0],y_range[1]],color=color_list[1],lw=2) # plot central x line
    ax.axis([0, w, h, 0])
    plt.show(fig)

    # return ROI
    ROI = image[y_range[0]:y_range[1], x_range[0]:x_range[1]]

    return ROI


def make_filenames(out_fn,saving_dir):
    """
    Check outdata filename and create if None, create it using date and time. Make parameters filename. 
    out_fn: str or None or False
    saving_dir: str, saving directory
    """

    if out_fn is False:
        # don't do anything, False is used to prevent from saving
        return False, False

    elif out_fn is None:
        # if not given, use date_time.csv 
        date_time_str = time.strftime("%Y%m%d_%H-%M-%S")
        out_fn = osp.join(saving_dir, date_time_str + '.csv')
        param_fn = osp.join(saving_dir, date_time_str + '_param.csv')

        printmd("**WARNING: No outfile name given!**")
        printmd("Positions data will be saved to: {}".format(out_fn))
        printmd("Parameters will be saved to: {}".format(param_fn))
    
    elif type(out_fn) is str:
        out_fn = osp.join(saving_dir, out_fn)
        # if already exists, don't overwrite and add date_time to filename
        if osp.exists(out_fn):
            printmd("**ERROR: {} already exists!**".format(out_fn))
            out_fn = out_fn[:-4] + '_' + time.strftime("%Y%m%d_%H-%M-%S") + '.csv'

        # param file
        param_fn = osp.join(saving_dir, out_fn[:-4] + '_param.csv')

        printmd("Positions data will be saved to: {}".format(out_fn))
        printmd("Parameters will be saved to: {}".format(param_fn))

    return out_fn, param_fn
