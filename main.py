#!/usr/bin/python3
import subprocess

# input variables for script of recording
system_device = 'WIN'
location = 'BCA'
device_sel = 2 
folder  = "data/"
t_on = 10 
t_off = 10 
fs = 44000
if __name__ == '__main__':
     subprocess.call(["python3", "record.py", "--path", folder, location, system_device, str(device_sel), str(t_on), str(t_off), str(fs)])
