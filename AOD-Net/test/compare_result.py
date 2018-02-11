import os;
from skimage.measure import compare_ssim;
import matplotlib.pyplot as plt;
import numpy as np;
import cv2;
import pandas as pd;

def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2);
	err /= float(imageA.shape[0] * imageA.shape[1]);
	return err;

haze_path="/workspace/AOD-Net/data/Haze/";
non_haze_path="/workspace/AOD-Net/data/Non-Haze/";
haze_result="/workspace/AOD-Net/data/result_haze/";
non_haze_result="/workspace/AOD-Net/data/result_non-haze/";
daftar_haze=os.listdir(haze_path);
daftar_non_haze=os.listdir(non_haze_path);

mse_value = list();
ssim_value = list();

for i in range(0,len(daftar_haze)):
	nama_file=daftar_haze[i];
	nama_file=nama_file[:-4];
	imageA=cv2.imread(haze_path+nama_file+'.jpg');
	imageB=cv2.imread(haze_result+nama_file+'_AOD-Net.jpg');
	grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY);
	grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY);
	m = mse(grayA, grayB);
	mse_value.append(m);
	s = compare_ssim(grayA, grayB);
	ssim_value.append(s);

output = pd.DataFrame(daftar_haze);
output['mse_value'] = mse_value;
output['ssim_value'] = ssim_value;

output.to_csv('output_aod_haze.csv',index=False);

mse_value = list();
ssim_value = list();

for i in range(0,len(daftar_non_haze)):
	nama_file=daftar_non_haze[i];
	nama_file=nama_file[:-4];
	imageA=cv2.imread(non_haze_path+nama_file+'.jpg');
	imageB=cv2.imread(non_haze_result+nama_file+'_AOD-Net.jpg');
	grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY);
	grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY);
	m = mse(grayA, grayB);
	mse_value.append(m);
	s = compare_ssim(grayA, grayB);
	ssim_value.append(s);

output = pd.DataFrame(daftar_non_haze);
output['mse_value'] = mse_value;
output['ssim_value'] = ssim_value;

output.to_csv('output_aod_non-haze.csv',index=False);
