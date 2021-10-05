# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 08:34:08 2021

@author: sebja
"""

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy.stats import norm
import imageio
import os

kappa = 2
theta = 10
sigma = 0.25
X0 = 9.8

# time grid
T = 2
NdT = 1_000
t = np.linspace(0,T,NdT)
dt = t[1]-t[0]


def SimOU(t, kappa, theta, sigma, Nsims):
    
    NdT = len(t)
    dt = t[1]-t[0]
    sqrt[t_idx]dt = np.sqrt(dt)
    
    # store the paths across simulations
    X = np.zeros((Nsims, NdT))
    
    # initial condition
    X[:,0] = X0

    # step through time
    for i in range(len(t)-1):

        # Euler discretization of  dX_t = kappa(theta - X_t) dt + sigma dW_t
        X[:,i+1] = X[:,i] + kappa*(theta - X[:,i]) * dt +  sigma * sqrt[t_idx]dt * np.random.randn(Nsims)

    return X

X = SimOU(t, kappa, theta, sigma, Nsims=10_000)

#%%
Y = 10*np.cumsum((X[0,:]-np.mean(X[0,:]))*dt)
Z = np.cumsum(Y*dt)

#%%
t_idx = np.where(t>=1.25)[0][0]

def MakeTrace(slope, name):
    
    y_min = np.min(Y)- np.abs(min(Y))*0.2
    y_max = np.max(Y)+ np.abs(max(Y))*0.3

    z_min = np.min(Z)- np.abs(min(Z))*0.2
    # z_max = np.max(Z)+ np.abs(max(Z))*0.3
    z_max = np.max(Z) +0.03
    
    filenames = []
    for i,t_ in enumerate(np.linspace(0,2,50)):
        
        
        filename = f'{i}.png'
        filenames.append(filename)    
    
        t_idx = np.where(t>=t_)[0][0]
        
        x = np.linspace(t[t_idx]-1,t[t_idx]+1,101)
        
        plt.subplot(1,2,1)
        plt.plot(t, Y)
        plt.scatter(t[t_idx],Y[t_idx],s=80,marker='o',color='r')
        plt.plot(x, slope*(x-t[t_idx])+Y[t_idx],'r', alpha=0.5)
        plt.plot(x, -slope*(x-t[t_idx])+Y[t_idx],'r', alpha=0.5)
        
        
        plt.fill_between(x, ((x<t[t_idx])-1*(x>=t[t_idx]))*slope*(x-t[t_idx])+Y[t_idx], y_min+ 0*x, color='y', alpha=0.5)
        
        plt.fill_between(x, y_max +0*x, ((x>=t[t_idx])-1*(x<t[t_idx]))*slope*(x-t[t_idx])+Y[t_idx],  color='y', alpha=0.5)
    
        plt.ylim([y_min,y_max])
        plt.xlim([0,2])
        plt.title(r"$\partial_\theta\ell(\theta)$",fontsize=16)
        plt.xticks([])
        plt.yticks([])        
        
        plt.subplot(1,2,2)
        plt.plot(t, Z)
        plt.scatter(t[t_idx],Z[t_idx],s=80,marker='o',color='r')
        plt.plot(x, slope*(x-t[t_idx])**2+Y[t_idx]*(x-t[t_idx])+Z[t_idx],'r', alpha=0.5)
        plt.plot(x, -slope*(x-t[t_idx])**2+Y[t_idx]*(x-t[t_idx])+Z[t_idx],'r', alpha=0.5)
        
        
        plt.fill_between(x, slope*(x-t[t_idx])**2+(x-t[t_idx])*Y[t_idx]+Z[t_idx], z_max+ 0*x, color='y', alpha=0.5)
        
        plt.fill_between(x, -slope*(x-t[t_idx])**2+(x-t[t_idx])*Y[t_idx]+Z[t_idx], z_min+ 0*x, color='y', alpha=0.5)
    
        plt.ylim([z_min,z_max])
        plt.xlim([0,2])        
        plt.title(r"$\ell(\theta)$",fontsize=16)
        plt.xticks([])
        plt.yticks([])
        
        plt.tight_layout(pad=2)
        # plt.show()
        plt.savefig(filename)
        plt.close()
    
    # build gif
    with imageio.get_writer('mygif.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
            
    # Remove files
    for filename in set(filenames):
        os.remove(filename)
        
    os.rename('mygif.gif', name)