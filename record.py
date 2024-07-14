# -*- coding: utf-8 -*-
"""
Script for recording audio from a device

"""
import datetime
import time
import sounddevice as sd
import soundfile as sf

with open('log.txt', 'a') as log_file:
    start_time = datetime.datetime.now().strftime("[%Y%m%d_%H%M%S]")
    data_log = start_time + ": Starting program for recording"
    log_file.write(data_log + "\n")
    print(data_log)
log_file.close()

# %%-----INPUT VARIABLES-----
location = 'BCA'
system_device = 'JETSON'
extension = '.wav'
fs = 44100 # sample rate
duration_on = 10  # duration of recording
duration_off =  2
list_devices = sd.query_devices()
#-------------------------

#print(list_devices)

# %% Recording
# Para saber que dispositivos tenemos disponibles de audio: 
# python3 -m sounddevices

while True:
    date_start = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    file_name = location + '_' + system_device + '_' + date_start + extension
    #myrecording = sd.rec(int(duration_on * fs), samplerate=fs, channels=2)
    date_end = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    time.sleep(duration_off)
    with open('log.txt', 'a') as log_file:
        data_recorded = sd.rec(int(duration_on * fs), fs, channels = 1, blocking = True)
        sf.write(file_name, data_recorded, fs)
        data_log = "   - Start time: " + date_start + " -- " + "End time: " + date_end
        log_file.write(data_log + "\n")     
        print("   - Start time: " + date_start + " -- " + "End time: " + date_end)
    log_file.close()
    sd.wait(int(duration_off))
    
