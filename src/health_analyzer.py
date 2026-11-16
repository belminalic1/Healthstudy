import matplotlib.pyplot as plt # grafer

class HealthAnalyzer:
    """ Gör beskrivande analys och grafer för hälsodata. """
    
    def __init__(self, df):
        
        """ Sparar datasetet i klassen så alla metoder kan använda det.
        df = dataset """
        
        self.df = df # spara data i objektet
        
    def describe(self, kolumner):
        
        """ Returnerar tabell med medel, median, min och max för valda kolumner.
        Kolumner: lista med kolumnnamn """
    
        tabell = self.df[kolumner].agg(["mean", "median", "min", "max"])
        
        return tabell.T.round(1)