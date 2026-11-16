import numpy as np
import pandas as pd
from scipy import stats

def load_data(path):
    """ Läser in datasetet från en csv fil och returnerar det som en Dataframe.
    path: sökväg till filen """
    
    df = pd.read_csv(path)
    return df
