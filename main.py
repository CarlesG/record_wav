#!/usr/bin/python3
import subprocess

# input variables for script of recording
system_device = 'WIN'
location = 'BCA'
folder  = "data/"
t_on = 10 
t_off = 10 
fs = 44000
if __name__ == '__main__':
     subprocess.call(["python3", "record.py", "--path", folder, system_device, location,  str(t_on), str(t_off), str(fs)])

