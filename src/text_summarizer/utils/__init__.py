import os
import yaml
from text_summarizer.logging import logger
from ensure import ensure_annotations
from pathlib import Path
from typing import Dict


def read_yaml(yaml_file_path) -> Dict:
    """
    reads yaml file and returns.

    Args:
        yaml_file_path: path or str like input

    Raises:
        e: any errors

    Returns:
        data: Dict type
    """
    try:
        with open(yaml_file_path) as yaml_file:
            data = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {yaml_file_path} loaded successfully")
            return data
    except Exception as e:
        raise e
    
    
@ensure_annotations
def create_directories(dirs_path: list):
    """
    creates a list of directories.

    Args:
        dirs_path (list): list of path of directories
    
    returns:
        None
    """
    for dir_path in dirs_path:
        os.makedirs(dir_path, exist_ok=True)
        logger.info(f"directory created at: {dir_path}")


