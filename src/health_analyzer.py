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
    
    def plot_histogram(self, kolumn, titel, xlabel):
        """ Gör ett histogram för en kolumn med en linje vid medelvärdet.
        Kolumn: kolumnamn
        Titel: grafens titel
        xlabel: text under x-axeln """
    
        plt.hist(self.df[kolumn], bins=20)
        plt.axvline(self.df[kolumn].mean(), color="red",    
            linestyle="--", label="Medelvärde")
        plt.title(titel)
        plt.xlabel(xlabel)
        plt.ylabel("Antal deltagare")
        plt.legend()
        plt.grid(True)
        plt.show()