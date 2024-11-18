import os, sys
from pathlib import Path
import logging

while True:
    project_name = input("Enter your project name: ")
    if project_name != "":
        break

files_list = [
    f'{project_name}/__init__.py',
    f'{project_name}/components/__init__.py',
    f'{project_name}/config/__init__.py',
    f'{project_name}/constants/__init__.py',
    f'{project_name}/entity/__init__.py',
    f'{project_name}/exception/__init__.py',
    f'{project_name}/logger/__init__.py',
    f'{project_name}/pipeline/__init__.py',
    f'{project_name}/utils/__init__.py',
    f'config/config.yaml',
    'schema.yaml',
    'app.py',
    'main.py',
    'logs.py',
    'exception.py',
    'setup.py'
]

for filepath in files_list:
    file_path=Path(filepath)
    filedir,filename=os.path.split(file_path)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, "w") as f:
            pass
    else:
        logging.imfo("file is already present at: {file_path}")