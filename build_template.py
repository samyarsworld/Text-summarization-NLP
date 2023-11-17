import os
import logging

# Setup information level (e.g., WARNING, ERROR, CRITICAL) logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_title = "text_summarizer"

# Project structure initialization
files_and_dirs = [
    "setup.py",
    "requirements.txt",
    "app.py",
    "main.py",
    f"src/{project_title}/__init__.py",
    f"src/{project_title}/components/__init__.py",
    f"src/{project_title}/utils/__init__.py",
    f"src/{project_title}/logging/__init__.py",
    f"src/{project_title}/config_manager/__init__.py",
    f"src/{project_title}/pipeline/__init__.py",
    "config/config.yaml",
    "parameters.yaml",
    "testing/test.ipynb",
    "Dockerfile",
    ".github/workflows/.gitkeep",
]

logging.info(f"Initializing project template started:")
for path in files_and_dirs:
    dir, file = os.path.split(path)

    if dir and not os.path.exists(dir):
        print(dir)
        os.makedirs(dir, exist_ok=True)
        logging.info(f"Creating directory:{dir}")

    if path and not os.path.exists(path):
        with open(path, "w") as f:
            logging.info(f"Creating the file {file}")

logging.info(f"Initializing project template finished:")

