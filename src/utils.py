import os 
import sys
import numpy as np
import pandas as pd
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score
from src.logger import logging
from sklearn.model_selection import GridSearchCV

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
    

def evaluate_model(X_train, y_train, X_test, y_test, models,params):
    """
    Evaluate multiple models and return their performance metrics.
    
    Parameters:
    """
    try:
        report= {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = params[list(models.keys())[i]]
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)
            #model.fit(X_train, y_train)
            y_test_pred = model.predict(X_test)
            train_model_score= r2_score(y_test, y_test_pred)
            test_model_score= r2_score(y_train, model.predict(X_train))
            report[list(models.keys())[i]] = test_model_score
        return report
    except Exception as e:
        
        raise CustomException(e, sys)