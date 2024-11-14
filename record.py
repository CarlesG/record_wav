#!/usr/bin/env python3
"""
Script for recording audio from a device
record.py can act like a terminal command due to argparse
The parameters are next:
    record.py -h : help for the command
    parameters:
        --path: path to save files and log.txt file. default: actual directory
        -h: prints the help
        location: term for the location (normally 3 characters) 
        system_device: could be WIN or LIN
        device_sel: select input/output device 
        t_on: time recording
        t_off: time waiting
        fs: adquisition sample rate
"""
import datetime
import time
import sounddevice as sd
import soundfile as sf
import argparse

parser = argparse.ArgumentParser(
                    prog = 'record.py',
                    description = 'Script for record audio:')
parser.add_argument('--path', required = False,  help = 'path to save', default = './')
parser.add_argument('location', help = 'location', default = 'BCA')
parser.add_argument('system_device', help = 'System: JETSON or WIN', default = 'WIN')
parser.add_argument('device_sel', type = int,  help = 'Selected input/output device')
parser.add_argument('t_on', type = float, help = 'T on recording [s]')
parser.add_argument('t_off', type = float,  help = 'T off of pause [s]')
parser.add_argument('fs', type = int, help = 'sampling frequency (Hz)')
args = parser.parse_args()

# %%-----INPUT VARIABLES--------
path = args.path
location = args.location 
system_device = args.system_device 
device_sel = args.device_sel
extension = '.wav'
fs = args.fs 
duration_on = args.t_on  
duration_off = args.t_off 
list_devices = sd.query_devices()
#--------------------------------

# Select the output device
sd.default.device =  device_sel 

with open(path + 'log.txt', 'a') as log_file:
    start_time = datetime.datetime.now().strftime("[%Y%m%d_%H%M%S]")
    data_log = start_time + ": Starting program for recording"
    log_file.write(data_log + "\n")
    print(data_log)
log_file.close()
i = 1
while True:
    with open(path + 'log.txt', 'a') as log_file:
        date_start = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        file_name = location + '_' + system_device + '_' + date_start + extension
        data_recorded = sd.rec(int(duration_on * fs), fs, channels = 1, blocking = True)
        date_end = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        sf.write(path + file_name, data_recorded, fs)
        data_log = "   + Start time: " + date_start + " -- " + "End time: " + date_end
        log_file.write(data_log + "\n")     
        print("   [" + str(i) + "] Start time: " + date_start + " -- " + "End time: " + date_end)
        i = i + 1
    log_file.close()
    time.sleep(int(duration_off))
