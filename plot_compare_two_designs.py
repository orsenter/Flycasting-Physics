# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:28:20 2020

@author: aAa
"""


#plot_compare_two_designs will compare the shape and linear mass density profiles of 
#two different leader designs


#read in relevant pickle data file to get data for two different leader designs
#when using pickle making sure to load in the same order they were dumped to the file
#I miss the MATLAB save and load simplicity
import math
import numpy as np
print ('numpy.__version__ is ', np.__version__)
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import array
import pickle
import pandas as pd
import tkinter as tk
from tkinter.font import Font
root = tk.Tk()
text = tk.Text(root)
myFont = Font(family="Courier", size=11)
text.configure(font=myFont)
print ('pandas.__version__ is ', pd.__version__)
#filename = 'bass_bug_data'
filename = 'example_equal_ratio_data'
infile = open(filename,'rb')
dia_match_tip_8=pickle.load(infile)
tit_leader=pickle.load(infile)
dia_section_1=pickle.load(infile)
len_section_1=pickle.load(infile)
end_section_1=pickle.load(infile)
dia_section_2=pickle.load(infile)
len_section_2=pickle.load(infile)
end_section_2=pickle.load(infile)
str_dia_1=pickle.load(infile)
str_len_1=pickle.load(infile)
str_dia_2=pickle.load(infile)
str_len_2=pickle.load(infile)
str_label_1=pickle.load(infile)
str_label_2=pickle.load(infile)
xmin=pickle.load(infile)
xmax=pickle.load(infile)
ymin=pickle.load(infile)
ymax=pickle.load(infile)
infile.close()
pi=math.pi
d2r=pi/180
r2d=180/pi
wt_fly_line=8
dia_match_tip=dia_match_tip_8;
str_match="leader diameter to match tip of {} wt fly line={:2.1f} mils".format(wt_fly_line,dia_match_tip);
end_section_1=np.reshape(end_section_1,(6,1))
end_section_2=np.reshape(end_section_2,(6,1))
start_section_1=end_section_1-len_section_1
start_section_2=end_section_2-len_section_2
mid_section_1=(start_section_1+end_section_1)/2
mid_section_2=(start_section_2+end_section_2)/2

#now compute fine grained x_fit_1 and y_fit_1 values
x1=[start_section_1[0],end_section_1[0]]
y1=[dia_section_1[0],dia_section_1[0]]
n_pt_array=np.round(len_section_1[0]*10 +1,0)
n_pt_int=int(n_pt_array)
x_fit_1=np.linspace(x1[0], x1[1], num=n_pt_int, endpoint=True)
y_fit_1=np.full((n_pt_int,1),y1[0])  #fill the y_fit_1 array with constant diameter value
muse=len(len_section_1)
for i in range(1,muse):
    x1=[start_section_1[i],end_section_1[i]]
    y1=[dia_section_1[i],dia_section_1[i]]
    n_pt_array=np.round(len_section_1[i]*10 +1,0)
    n_pt_int=int(n_pt_array)
    x_fit=np.linspace(x1[0], x1[1], num=n_pt_int, endpoint=True)
    y_fit=np.full((n_pt_int,1),y1[0])  
    x_fit_1=np.concatenate((x_fit_1,x_fit),axis=0) #concatenate columns
    y_fit_1=np.concatenate((y_fit_1,y_fit),axis=0)
    #get fourth order polynomial fit to y_fit_1 values
x_fit_1_unique,indices=np.unique(x_fit_1, return_index=True)
coeffs=np.polyfit(x_fit_1_unique, y_fit_1[indices,0], 4)
y_fit_1_poly = np.polyval(coeffs, x_fit_1_unique)   
    
#now compute fine grained x_fit_2 and y_fit_2 values
x2=[start_section_2[0],end_section_2[0]]
y2=[dia_section_2[0],dia_section_2[0]]
n_pt_array=np.round(len_section_2[0]*10 +1,0)
n_pt_int=int(n_pt_array)
x_fit_2=np.linspace(x2[0], x2[1], num=n_pt_int, endpoint=True)
y_fit_2=np.full((n_pt_int,1),y2[0])  #fill the y_fit_2 array with constant diameter value
muse=len(len_section_2)
for i in range(1,muse):
    x2=[start_section_2[i],end_section_2[i]]
    y2=[dia_section_2[i],dia_section_2[i]]
    n_pt_array=np.round(len_section_2[i]*10 +1,0)
    n_pt_int=int(n_pt_array)
    # x_fit=np.resize(x_fit,(n_pt_int,1)) 
    # y_fit=np.resize(y_fit,(n_pt_int,1))
    x_fit=np.linspace(x2[0], x2[1], num=n_pt_int, endpoint=True)
    y_fit=np.full((n_pt_int,1),y2[0])  
    x_fit_2=np.concatenate((x_fit_2,x_fit),axis=0) #concatenate columns
    y_fit_2=np.concatenate((y_fit_2,y_fit),axis=0)
    #get fourth order polynomial fit to y_fit_2 values
    #get unique x_fit_1 values
x_fit_2_unique,indices=np.unique(x_fit_2, return_index=True)
coeffs = np.polyfit(x_fit_2_unique, y_fit_2[indices,0], 4)
y_fit_2_poly = np.polyval(coeffs, x_fit_2_unique)   
fig, ax = plt.subplots(figsize=(8,6)) #figsize is in inches
ax.plot(0,dia_match_tip,'ko')
str_match=r'leader diameter to match $\rho_{{l}}$ of {} wt fly line={:2.0f} mils'.format(wt_fly_line,dia_match_tip)
#the r prefix is necessary at the start of the string so the \ character used in LaTex is preserved
str_rho_l=r'$\rho_{{l}}$'
ax.text(2,dia_match_tip, str_match,
        verticalalignment='center', horizontalalignment='left',
        color='k', fontsize=12)
ax.plot(mid_section_1,dia_section_1,'b*')
ax.plot(x_fit_1,y_fit_1,color='b')
ax.plot(x_fit_1_unique,y_fit_1_poly,'b')
ax.text(80,dia_section_1[3], str_label_1,
        verticalalignment='center', horizontalalignment='left',
        color='b', fontsize=14)
ax.text(5,44, str_dia_1,
        verticalalignment='center', horizontalalignment='left',
        color='b', fontsize=10,fontname='monospace')
ax.text(5,42.8, str_len_1,
        verticalalignment='center', horizontalalignment='left',
        color='b', fontsize=10,fontname='monospace')

ax.plot(mid_section_2,dia_section_2,'r*')
ax.plot(x_fit_2,y_fit_2,'r')
ax.plot(x_fit_2_unique,y_fit_2_poly,'r')
ax.text(75,dia_section_2[4], str_label_2,
        verticalalignment='top', horizontalalignment='right',
        color='r', fontsize=14)
ax.text(5,41.6, str_dia_2,
        verticalalignment='center', horizontalalignment='left',
        color='r', fontsize=10,fontname='monospace')
ax.text(5,40.4, str_len_2,
        verticalalignment='center', horizontalalignment='left',
        color='r', fontsize=10,fontname='monospace')
        
ax.set_xlabel(r'$\bf{{Length - inches}}$', fontsize=12)
#ax.set_xlabel('Length - inches', fontsize=12)
ax.set_ylabel(r'$\bf{{Diameter - mils}}$', fontsize=12)
ax.set_title(tit_leader, fontsize=13)
ax.set_ylim([ymin,ymax])
ax.set_xlim([xmin,xmax])
ax.grid()
plt.savefig('bass_bug.jpg', DPI=300)
plt.show()
plt.close("all") #this will erase the figure like a clf in Matlab but it will keep the window open for future plots

#now plot the linear mass density
s_g=1.14   #specific gravity of Nylon 6 leader material
E_y_psi=250000.   #Youngs modulus in psi when wet
#1 gigapascal [GPa] = 145037.73773 psi [psi]
E_y_gpa=E_y_psi/145037.73
E_tensile=60000.   #tensile (breaking) strength in psi
# s_g=1.76#specific gravity of Pure Flurocarbon leader material
# E_y_psi=100000.   #Youngs modulus in psi when wet for Flurocarbon
#1 gigapascal [GPa] = 145037.73773 psi [psi]
# E_y_gpa=E_y_psi/145037.73
rho_vol=1000.*s_g;  #volume mass density in kg/m.^3
dia_m_1=y_fit_1/1000./39.37   #dia in m
rho_l_1=rho_vol*pi/4*np.square(dia_m_1)  #linear mass density in kg/m
str_leader_material='Nylon 6 s.g.={:3.2f} Ey={:0.3}gpsi Ey={:4.2f}GPa breaking strength={:0.3g}psi'.format(s_g,E_y_psi,E_y_gpa,E_tensile)
x_meter_1=x_fit_1/39.37
(x_meter_1_unique,indices)=np.unique(x_meter_1, return_index=True)
coeffs=np.polyfit(x_meter_1_unique, rho_l_1[indices,0], 4)
rho_l_1_poly = np.polyval(coeffs, x_meter_1_unique)#returns a vector
x_meter_1_unique=x_meter_1_unique[:,np.newaxis]
rho_l_1_poly=rho_l_1_poly[:,np.newaxis]#convert vector to ndarray   
dia_m_1=y_fit_1/1000./39.37   #dia in m
rho_l_1=rho_vol*pi/4*np.square(dia_m_1)  #linear mass density in kg/m

dia_m_2=y_fit_2/1000./39.37   #dia in m
rho_l_2=rho_vol*pi/4*np.square(dia_m_2)  #linear mass density in kg/m
x_meter_2=x_fit_2/39.37
x_meter_2_unique,indices=np.unique(x_meter_2, return_index=True)
coeffs=np.polyfit(x_meter_2_unique, rho_l_2[indices,0], 4)
rho_l_2_poly = np.polyval(coeffs, x_meter_2_unique)
x_meter_2_unique=x_meter_2_unique[:,np.newaxis]
rho_l_2_poly=rho_l_2_poly[:,np.newaxis]#

fig, ax = plt.subplots(figsize=(8,6)) #figsize is in inches
ax.plot(x_meter_1,1000.*rho_l_1,'b')#convert to g/m^3
ax.plot(x_meter_1_unique,1000*rho_l_1_poly,'b')#convert to g/m^3
ax.plot(x_meter_2,1000.*rho_l_2,'r')#convert to g/m^3
ax.plot(x_meter_2_unique,1000*rho_l_2_poly,'r')#convert to g/m^3
(mpoints,n)=x_meter_1_unique.shape
n_mrk=int(.65*mpoints)
ax.text(x_meter_1_unique[n_mrk,0]+.15,1000*rho_l_1_poly[n_mrk,0], str_label_1,
        verticalalignment='top', horizontalalignment='left',
        color='b', fontsize=14)
ax.text(x_meter_2_unique[n_mrk,0]-.1,1000*rho_l_2_poly[n_mrk,0], str_label_2,
        verticalalignment='top', horizontalalignment='right',
        color='r', fontsize=14)

ax.set_xlabel(r'$\bf{{Length - meters}}$', fontsize=12)
ax.set_ylabel(r'$\bf{{\rho_{{l}} - g/m}}$', fontsize=12)
tit_rho=(r'$\rho_{{l}}$  of Moray Equal Ratio Design compared to $\rho_{{l}}$ of Rajeff Bass Bug Design')
ax.set_title(tit_rho, fontsize=13)
plt.savefig('bass_bug_rho_l.jpg', DPI=300)
plt.show()
plt.close("all") #this will erase the figure like a clf in Matlab but it will keep the window open for future plots