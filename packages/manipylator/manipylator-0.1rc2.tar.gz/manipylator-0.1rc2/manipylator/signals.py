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
import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

 
# current directory used as default argument
cwd = os.getcwd()


def make_linear_sweep(boundaries=[0,500],duration=None,speed=None,num_steps=50):
    """Create an array of positions sweeping a range with a linear motion within the boundaries. 
    The motion's speed can be passed by speed or computed by the total time. If both are given duration is default. 
    The number of steps is given by num_steps.
    """
    if duration is None and speed is None:
        print("ERROR: at duration or speed must be passed")
        return -1
        
    pos_list = np.linspace(boundaries[0],boundaries[1],num_steps)
    dx = (boundaries[1]-boundaries[0])/num_steps
    
    if duration is not None:
        dt = duration/num_steps
    else:
        tot_range = np.abs(boundaries[1]-boundaries[0])
        duration = tot_range/speed 
        dt = duration/num_steps
    
    return {'pos':pos_list,'dt':dt,'dx':dx,'duration':duration}


def make_linear_sweep_series(boundaries_list=[],duration_list=[],num_steps_list=[],plot='show',saving_dir=cwd,out_fn=None):
    """
    Make a series of successive linear sweeps calling make_linear_sweep. Each argument is a list of arguments passed to make_linear_sweep
    """

    # check that all list of arguments have the same length
    if len(boundaries_list) != len(duration_list) or len(boundaries_list) != len(num_steps_list):
        raise Exception("ERROR: list of arguments don't have the same length")
    
    df_list = []

    for i in range(len(boundaries_list)): 
        sweep_dict = make_linear_sweep(boundaries=boundaries_list[i],duration=duration_list[i],num_steps=num_steps_list[i])
        df_list.append(pd.DataFrame(sweep_dict))

    df_out = pd.concat(df_list,ignore_index=True)

    # plot
    if plot is not False:
        # cumulate intervals to get time
        df_out['t'] = np.cumsum(df_out['dt'].values) - df_out['dt'].values[0]
        # plot filename
        if out_fn is None:
            plot_fn=osp.join(saving_dir,time.strftime("%Y%m%d_%H-%M-%S")+'.png')
        else: 
            plot_fn=osp.join(saving_dir,out_fn[:-4]+'.png')
        fig,ax=plt.subplots()
        df_out.plot.scatter('t','pos',ax=ax)
        ax.set_ylabel(r'displacement $(\mu m)$')
        ax.set_xlabel(r'time (sec)')
        fig.tight_layout()
        if plot=="save":
            fig.savefig(plot_fn,dpi=300)
        elif plot=="show":
            plt.show(fig)

    return df_out


def make_chirp(x0=200,off=250,w1=0.05,w2=0.5,T=500,N=1000,plot='show',cst_num_steps=[0,0],saving_dir=cwd,out_fn=None):
    """
    Create a chirp motion defined in Geri et al. 2018. 
    x0: half amplitude in um. w1=low frequency in rad/s. w2=high frequency in rad/s.
    T:total time in sec. off: offset in um. N: number of points
    cst_num_steps: number of constant points to add at start and end of signal
    """

    dt=T/N
    print('step interval = {} sec'.format(dt))
    
    #gererate points
    t=np.linspace(0,T,N)
    x=x0*np.sin((w1*T/np.log(w2/w1))*(np.exp(np.log(w2/w1)*t/T)-1))+off

    #append constant points at start and end
    x_start = np.ones(cst_num_steps[0])*off
    x_end = np.ones(cst_num_steps[1])*off
    t_start = np.arange(-cst_num_steps[0]*dt,0,dt)
    t_end = np.arange(T+dt,T+cst_num_steps[1]*dt,dt)
    x = np.concatenate((x_start,x,x_end))
    t = np.concatenate((t_start,t,t_end))
    
    if plot is not False:
        if out_fn is None:
            plot_fn=osp.join(saving_dir,time.strftime("%Y%m%d_%H-%M-%S")+'.png')
        else: 
            plot_fn=osp.join(saving_dir,out_fn[:-4]+'.png')
        fig,ax=plt.subplots()
        ax.plot(t,x)
        ax.set_ylabel(r'displacement $(\mu m)$')
        ax.set_xlabel(r'time (sec)')
        fig.tight_layout()
        if plot=="save":
            fig.savefig(plot_fn,dpi=300)
        elif plot=="show":
            plt.show(fig)

    return x,dt


def make_tuckey_chirp(x0=200,off=250,w1=0.05,w2=0.5,T=500,N=1024,polarity=-1,r=0.15,plot='show',cst_num_steps=[0,0],saving_dir=cwd,out_fn=None):
    """
    Create a chirp with tuckey window (see Eq. 5 from Geri et al. 2018)
    x0: amplitude in microns
    off: offset in microns (ie. central point position)
    polarity: controls sign of first oscillation (-1 or 1)
    w1 = 0.05
    w2 = 0.5
    T: total time in sec
    N: number of points (use a multiple of 2^n)
    r: tapering parameter in [0-1], best: 0.1-0.15
    cst_num_steps: number of constant points to add at start and end of signal
    plot: "show", "save" or False
    saving_dir: saving directory
    """
    
    dt=T/N
    print('step interval = {} sec'.format(dt))

    # time windows boundaries
    t1_min = 0
    t1_max = r*T/2
    t2_min = r*T/2
    t2_max = T - r*T/2
    t3_min = T - r*T/2
    t3_max = T

    # number of points in windows
    N1 = np.int(r*N/2)
    N2 = np.int(N - r*N)
    N3 = np.int(r*N/2)
    N_rest = N - (N1 + N2 + N3)
    N2 += N_rest #if the rounding operation leads to a mismatch give the missing points to the central window (not ideal but easier)

    # time windows
    t1 = np.linspace(t1_min,t1_max,N1)
    t2 = np.linspace(t2_min,t2_max,N2)
    t3 = np.linspace(t3_min,t3_max,N3)

    #prefactors
    phi1 = w1*T/np.log(w2/w1)
    phi2 = np.log(w2/w1)
    a_1 = np.cos(np.pi/r*(t1/T - r/2))**2
    a_3 = np.cos(np.pi/r*(t3/T - 1 + r/2))**2

    # amplitude windows
    x1 = a_1*np.sin(phi1*(np.exp(phi2*t1/T)-1))
    x2 = np.sin(phi1*(np.exp(phi2*t2/T)-1))
    x3 = a_3*np.sin(phi1*(np.exp(phi2*t3/T)-1))

    # concatenate windows
    t = np.concatenate((t1,t2,t3))
    x = np.concatenate((x1,x2,x3))
    
    if polarity != 1 and polarity != -1:
        print("Warning: polarity needs to be 1 or -1")
    x_final = polarity*x0*x + off

    #append constant points at start and end
    x_start = np.ones(cst_num_steps[0])*off
    x_end = np.ones(cst_num_steps[1])*off
    t_start = np.arange(-cst_num_steps[0]*dt,0,dt)
    t_end = np.arange(T+dt,T+(cst_num_steps[1]+1)*dt,dt)
    x_final = np.concatenate((x_start,x_final,x_end))
    t = np.concatenate((t_start,t,t_end))

    if plot is not False:
        if out_fn is None:
            plot_fn=osp.join(saving_dir,time.strftime("%Y%m%d_%H-%M-%S")+'.png')
        else: 
            plot_fn=osp.join(saving_dir,out_fn[:-4]+'.png')
        fig,ax = plt.subplots()
        ax.plot(t,x_final)
        ax.set_ylabel(r'displacement $(\mu m)$')
        ax.set_xlabel(r'time (sec)')
        fig.tight_layout()
        if plot=="save":
            fig.savefig(plot_fn,dpi=300)
        elif plot=="show":
            plt.show(fig)


    return x_final,dt

    