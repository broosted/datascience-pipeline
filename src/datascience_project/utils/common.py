import os
import yaml
from src.datascience_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    
    Args:
        path_to_yaml (Path): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file
    """
    try:
        with open(path_to_yaml) as yaml_file:
            print(path_to_yaml)
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
    
            
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            



@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data
    
    Args:
        path (Path): path to save json file
        data (dict): data to save in json file
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json file
    
    Args:
        path (Path): path to load json file
    """
    with open(path, "r") as f:
        data = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(data)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file
    
    Args:
        data (Any): data to save in binary file
        path (Path): path to save binary file
    """
    joblib.dump(data, path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary file
    
    Args:
        path (Path): path to load binary file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data







