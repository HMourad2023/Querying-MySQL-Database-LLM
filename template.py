from pathlib import Path
import os
import logging
from typing import List

logging.basicConfig(level=logging.INFO,format="[%(asctime)s]: %(message)s:")

list_of_files: List[str] = [
    "src/__init.py__",
    "src/config.py",
    "src/database.py",
    "src/query.py",
    "src/utils.py",
    "src/generate.py",
    "app.py",
    "params.yaml",
    ".env",
    "images/",
    "notebooks/experiments.ipynb"
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)  
        logging.info(f"Creating directory {filedir} for the file :{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as file:
            pass
        logging.info(f"creating empty file : {filepath}")
    else:
        logging.info(f"{filename} already exists")
        
            