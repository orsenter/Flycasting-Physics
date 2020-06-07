#-*- coding: utf-8 -*-
import numpy as np
import sys
#compare_equal_raitio_Rajeff_bass_bug contains the diameter and length  values
#for the Moray equal ratio Bass Bug design and the Rajeff Bass Bug design
#ratio design
#these data files will be evaluated in the Plot_Leader program to produce
#multiple designs on on plot
tit_leader=('Compare Moray Example to Equal Ratio Design')
#DIA len1 len2 len3 len4 %data for Moray equal ratio and Rajeff Bass Bug designs
dia_len=np.array([
        [32.00,   31.50 ,    0.00 ],	
    [30.86,    0.00 ,    33.28 ],	
    [26.00,   21.50 ,     0.00 ],	
    [24.63,    0.00 ,    17.81 ],	
    [22.00,   14.50 ,     0.00 ],	
    [19.66,    0.00 ,    16.04 ],	
    [18.00,   11.50 ,     0.00 ],	
    [15.69,    0.00 ,    10.92 ],	
    [14.00,    9.00 ,     0.00 ],	
    [12.53,    0.00 ,     9.43 ],	
    [10.00,   10.00 ,    10.52]	 
    ])
dia_match_tip_8=37.;
m=dia_len.shape[0]
print('m=',m)
n = len(dia_len[0]) #for list
print('n=',n)
ndesign=n-1;
for idesign in range(1,n,1):
    x=dia_len[:,idesign]
    ind_use=np.argwhere(x)
    muse=len(ind_use);
    if idesign==1:
        dia_section_1=dia_len[ind_use,0]
        len_section_1=x[ind_use]
        end_section_1=np.cumsum(len_section_1)
    if idesign==2:
        dia_section_2=dia_len[ind_use,0]
        len_section_2=x[ind_use]
        end_section_2=np.cumsum(len_section_2)

#str_leader_material='Nylon 6 s.g.={:3.2f} Ey={:0.3}gpsi Ey={:4.2f}GPa breaking strength={:0.3g}psi'.format(s_g,E_y_psi,E_y_gpa,E_tensile)
dia_row=np.transpose(dia_section_1)
(m,n)=dia_row.shape
str_1=''
for i in range(n):  
    str_1=str_1+ '{:6.1f}'.format(dia_row[0,i])
str_dia_1='Dia_example=[' +str_1 +'] mils'  
print(str_dia_1) 
len_row=np.transpose(len_section_1)
(m,n)=len_row.shape
str_1=''
for i in range(n):  
    str_1=str_1+ '{:6.1f}'.format(len_row[0,i])
str_len_1='Len_example=[' +str_1 +'] inches'  
print(str_len_1)   
dia_row=np.transpose(dia_section_2)
(m,n)=dia_row.shape
str_2=''
for i in range(n):  
    str_2=str_2+ '{:6.1f}'.format(dia_row[0,i])
str_dia_2='Dia_equal_r=[' +str_2 +'] mils'  
print(str_dia_2) 
len_row=np.transpose(len_section_2)
(m,n)=len_row.shape
str_2=''
for i in range(n):  
    str_2=str_2+ '{:6.1f}'.format(len_row[0,i])
str_len_2='Len_equal_r=[' +str_2 +'] inches'  
print(str_len_2)  
                       


# lable=setstr(32*ones(1,16));
str_label_1='[Moray Example]'
str_label_2='[Equal_ratio]'
xmin=0;xmax=100;
ymin=5;ymax=45;
#now save the data in a text output file using pickle
import pickle
filename = 'example_equal_ratio_data'
outfile = open(filename,'wb')
pickle.dump(dia_match_tip_8,outfile)
pickle.dump(tit_leader,outfile)
pickle.dump(dia_section_1,outfile)
pickle.dump(len_section_1,outfile)
pickle.dump(end_section_1,outfile)
pickle.dump(dia_section_2,outfile)
pickle.dump(len_section_2,outfile)
pickle.dump(end_section_2,outfile)
pickle.dump(str_dia_1,outfile)
pickle.dump(str_len_1,outfile)
pickle.dump(str_dia_2,outfile)
pickle.dump(str_len_2,outfile)
pickle.dump(str_label_1,outfile)
pickle.dump(str_label_2,outfile)
pickle.dump(xmin,outfile)
pickle.dump(xmax,outfile)
pickle.dump(ymin,outfile)
pickle.dump(ymax,outfile)
outfile.close()