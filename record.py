#!/usr/bin/python3
"""
Script for recording audio from a device

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
parser.add_argument('t_on', type = float, help = 'T on recording')
parser.add_argument('t_off', type = float,  help = 'T off of pause')
parser.add_argument('fs', type = float, help = 'sampling frequency (Hz)')
args = parser.parse_args()

# %%-----INPUT VARIABLES--------
path = args.path
location = 'BCA'
system_device = 'JETSON'
extension = '.wav'
fs = args.fs 
duration_on = args.t_on  
duration_off = args.t_off 
list_devices = sd.query_devices()
#--------------------------------

with open(path + 'log.txt', 'a') as log_file:
    start_time = datetime.datetime.now().strftime("[%Y%m%d_%H%M%S]")
    data_log = start_time + ": Starting program for recording"
    log_file.write(data_log + "\n")
    print(data_log)
log_file.close()

while True:
    with open(path + 'log.txt', 'a') as log_file:
        date_start = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        file_name = location + '_' + system_device + '_' + date_start + extension
        data_recorded = sd.rec(int(duration_on * fs), fs, channels = 1, blocking = True)
        date_end = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        sf.write(path + file_name, data_recorded, fs)
        data_log = "   + Start time: " + date_start + " -- " + "End time: " + date_end
        log_file.write(data_log + "\n")     
        print("   + Start time: " + date_start + " -- " + "End time: " + date_end)
    log_file.close()
    time.sleep(int(duration_off))
