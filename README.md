# Installation
---

# Install miniconda
Install miniconda from [here](https://docs.anaconda.com/miniconda/miniconda-install/)

# Create the environment
Load the environment from yml file: `conda env create -f audio_acuprec2.yml 

Active the environment with `conda activate myenv`

For execute the program, use `python main.py` or main.py directly

Important variables for the script are:
- location: denomination of three characters of the place, only use 3 characters
- system_device: system in we are working, only use 3 characters
- device_sel: selected input/ouput device
- t_on: time for record
- t_off: time off doing nothing
- fs: frequency sample

# Executing the program

To execute the main `$> main` directly or:

```python3 main.py```

Also we can do it directly with the terminal

```main```

We can use separetely the `record.py` script like terminal command:

```$> record.py -h --path location system_device device_sel t_on t_off fs```
