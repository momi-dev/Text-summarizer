import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="Textsummarizer"

list_files=[
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirments.txt",
    "setup.py",
    "research/trials.ipynb",
    

]

for paths in list_files:
    paths=Path(paths)
    filedir,filename=os.path.split(paths)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)  
        logging.info(f"creating directory:{filedir} for the file {filename}")
    
    if (not os.path.exists(paths)) or (os.path.getsize(paths==0)):
        with open(paths,"w") as f:
            pass
        logging.info(f"creating empty file:{paths}")
    
    else:
        logging.info(f"{filename} is already exist")
        