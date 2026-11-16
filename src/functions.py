import numpy as np
import pandas as pd
from scipy import stats

def load_data(path):
    """ Läser in datasetet från en csv fil och returnerar det som en Dataframe.
    path: sökväg till filen """
    
    df = pd.read_csv(path)
    return df

def simulate_disease(p, n):
    """ Simulerar n personer där var och en är sjuk med sannolikheten p.
    Retunerar andelen sjuka i simuleringen.
    p: sannolikheten att vara sjuk
    n: antal personer att simulera """

    simulering = np.random.random(n) < p
    return simulering.mean()

def ci_normal(data, z=1.96):
    """ Beräknar ett konfidensintervall för medelvärdet med normalapproximation.
    Returnerar medelvärde, nedre gräns och övre gräns.
    data: värden ur datasetet
    z: z_värde, 1,96 ger 95 % konfidensintervall (v6, upp 13) """
    medel = data.mean()
    se = data.std() / np.sqrt(len(data)) #v6 upp 15, standard fel
    nedre = medel - z * se 
    ovre = medel + z * se
    return medel, nedre, ovre
