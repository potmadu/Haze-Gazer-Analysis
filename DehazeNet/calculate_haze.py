import os;
import DehazeNet;
import numpy as np;
import pandas as pd;

img_path = 'Non-Haze/'
daftar = os.listdir(img_path);

A_min = list();
A_avg = list();
A_max = list();

te_min = list();
te_avg = list();
te_max = list();

t_min = list();
t_avg = list();
t_max = list();

for i in range(0,len(daftar)):
    nama_file=img_path+daftar[i]
    TE = DehazeNet.getTe(nama_file)
    T = DehazeNet.getT(nama_file,TE)
    A = DehazeNet.getA(nama_file)
    A_min.append(np.amin(A))
    A_avg.append(np.average(A))
    A_max.append(np.amax(A))
    te_min.append(np.amin(TE))
    te_avg.append(np.average(TE))
    te_max.append(np.amax(TE))
    t_min.append(np.amin(T))
    t_avg.append(np.average(T))
    t_max.append(np.amax(T))

output = pd.DataFrame(daftar);

output['A_min'] = A_min;
output['A_avg'] = A_avg;
output['A_max'] = A_max;

output['te_min'] = te_min;
output['te_avg'] = te_avg;
output['te_max'] = te_max;

output['t_min'] = t_min;
output['t_avg'] = t_avg;
output['t_max'] = t_max;

output.to_csv('output_dehazenet-non-haze.csv',index=False);

