#!/usr/bin/python3
import subprocess
import os
# input variables for script of recording
t_on = 5 * 60
t_off = 5 * 60 
fs = 44000
print(os.getcwd())
if __name__ == '__main__':
     subprocess.call(["python3", "record.py", str(t_on), str(t_off), str(fs)])

