import torch
import pickle
import numpy as np
import pandas as pd
import glob
import os

'''
best_checkpoint_path = get_best_checkpoint_path('models/son_height_regression_model', monitor='val_loss', mode='min')
best_checkpoint_path = get_best_checkpoint_path('models/iris_species_classification_model', monitor='val_accuracy', mode='max')
'''
def get_best_checkpoint_path(checkpoint_directory, monitor='val_loss', mode='min', default_best_checkpoint_path='models/son_height_regression_model/son_height_regression_model.ckpt'):
    checkpoint_file_names = glob.glob(os.path.join(checkpoint_directory, '*.ckpt'))
    #print(checkpoint_file_names) #['models/son_height_regression_model/son_height_regression_model-epoch=29-val_loss=0.00.ckpt', 'models/son_height_regression_model/son_height_regression_model-epoch=29-val_loss=0.00-v1.ckpt']
    best_checkpoint_path = None
    def sort_func(checkpoint_file_name, monitor=monitor):
        for token in checkpoint_file_name.split('-'):
            if '=' in token:
                li = token.split('=')
                name = li[0]
                value = li[1]
                if '.ckpt' in value:
                    value = value.split('.ckpt')[0]
                if name == monitor:
                    return float(value)
    checkpoint_file_names.sort(key=sort_func)
    try:
        if mode == 'min':
            best_checkpoint_path = checkpoint_file_names[0]
        elif mode == 'max':
            best_checkpoint_path = checkpoint_file_names[-1]
    except:
        best_checkpoint_path = default_best_checkpoint_path 
    return best_checkpoint_path
