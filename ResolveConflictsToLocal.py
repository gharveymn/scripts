import glob
import os

for filename in glob.iglob('**/*-DESKTOP-7398PIN*', recursive=True):
	os.remove(filename.replace('-DESKTOP-7398PIN',''))
	os.rename(filename,filename.replace('-DESKTOP-7398PIN',''))