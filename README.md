# Installation
---

# Install miniconda
Install miniconda from [here](https://docs.anaconda.com/miniconda/miniconda-install/)

# Create the environment
Load the environment from yml file: `conda env create -f audio_acuprec2.yml 

Active the environment with `conda activate myenv`

For execute the program, use `python main.py` or main.py directly

Important variables for the script are:
- location: denomination of three characters of the place in we are recording audio
- system_device: system in we are working 
- device_sel: selected input/ouput device
- t_on: time for record
- t_off: time off doing nothing
- fs: frequency sample
