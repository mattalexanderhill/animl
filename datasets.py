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
        tgz.extractall(os.path.dirname(local))

def load_housing_data():
    return pd.read_csv(os.path.join(LOCAL_ROOT, 'housing', 'housing.csv'))

def load_pokemon_data():
    return pd.read_csv(os.path.join(LOCAL_ROOT, 'pokemon', 'pokemon.csv'))
