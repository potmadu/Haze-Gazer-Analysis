import os;
import DehazeNet;

img_path = 'img_haze/'
daftar = os.listdir("img_haze/");

for i in range(0,len(daftar)-1):
	nama_file=img_path+daftar[i];
	DehazeNet.Dehaze(nama_file);

