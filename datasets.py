import os
import tarfile
from urllib import request
import pandas as pd

REMOTE_ROOT = 'https://raw.githubusercontent.com/ageron/handson-ml/master/'
LOCAL_ROOT  = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets')

def fetch_housing_data():
    remote = REMOTE_ROOT + 'datasets/housing/housing.tgz'
    local  = os.path.join(LOCAL_ROOT, 'housing', 'housing.tgz')
    if not os.path.isdir(os.path.dirname(local)):
        os.makedirs(os.path.dirname(local))
    request.urlretrieve(remote, local)
    with tarfile.open(local) as tgz:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tgz, os.path.dirname(local))

def load_housing_data():
    return pd.read_csv(os.path.join(LOCAL_ROOT, 'housing', 'housing.csv'))

def load_pokemon_data():
    return pd.read_csv(os.path.join(LOCAL_ROOT, 'pokemon', 'pokemon.csv'))

def load_country_classifier_data():
    return pd.read_csv(os.path.join(LOCAL_ROOT, 'country_classifier', 'predictions.csv'))
