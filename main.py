

import re
import string
import random
import pyfiglet
import os


os.system('color 4')

print(pyfiglet.figlet_format('RandomCode', width = 100))

# load the file

script_path = input('your script path here : ')
python_file_content = open(script_path, 'r', errors='ignore').read()

# extract functions names and variables names and parametrs

def extract_functions_names(python_file_content : str):
    regx = "(def [a-zA-z0-9]+)"
    functions_names = re.findall(regx, python_file_content, re.IGNORECASE)
    return [str(name).replace('def', '').strip() for name in functions_names]


def extract_variables_names(python_file_content : str):
    regx = "([a-zA-Z0-9]+)(\s=|\.s=)"
    variables_names = re.findall(regx, python_file_content, re.IGNORECASE)
    variables_names = [str(name[0]).replace('=', '') for name in variables_names]
    return variables_names


def extract_parameters_names(python_file_content : str):
    regx = "\([a-zA-Z0-9 ,]+\)"
    parameters_names = re.findall(regx, python_file_content, re.IGNORECASE)
    parameters_names = [str(name).replace('(', '').replace(')', '').strip() for name in parameters_names]
    return parameters_names





# create random names for funtions and variables

def generate_random_name():
    name_len = random.randint(5, 8)
    return ''.join([random.choice(string.ascii_letters) for _ in range(name_len)])




# generate random name for varebles
variables_names = {}
for var_name in extract_variables_names(python_file_content):
    variables_names[var_name] = generate_random_name()


# generate random names for parameters
parameters_names = {}
for parameter_name in extract_parameters_names(python_file_content):
    if ',' in parameter_name:
        for p in parameter_name.split(','):
            p = p.strip()
            if p in variables_names:
                parameters_names[p] = variables_names[p]
            else:
                parameters_names[p] = generate_random_name()
    else:
        if parameter_name in variables_names:
            parameters_names[parameter_name] = variables_names[parameter_name]
        
    
# replace old names with new names

for var_name in variables_names:
    python_file_content = python_file_content.replace(var_name, variables_names[var_name])
    
for parameter_name in parameters_names:
    python_file_content = python_file_content.replace(parameter_name, parameters_names[parameter_name])

# generate random name for functions
functions_names = {}
for func_name in extract_functions_names(python_file_content):
    functions_names[func_name] = generate_random_name()
    
for func_name in functions_names:
    python_file_content = python_file_content.replace(func_name, functions_names[func_name])



python_file = open('out/script.py', 'w')
python_file.write(python_file_content)
print('done ;)')
