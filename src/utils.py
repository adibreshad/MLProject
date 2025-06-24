import os 
import sys
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException


def save_object(obj, file_path):
    """
    Save an object to a file using pickle.
    
    Parameters:
    obj: The object to save.
    file_path: The path where the object will be saved.
    """
    
    try:
        dir_path= os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        print(f"Error saving object: {e}")
        raise CustomException(e, sys)   