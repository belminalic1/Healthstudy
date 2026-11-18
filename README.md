# Healthstudy, Statistisk dataanalys

## Syfte
Analys av en hälsostudie med 800 deltagare och besvara olika frågor:

**Del 1**
- Hur ser deltagarnas ålder, vikt, längd, blodtryck och kolesterol ut?
- Hur stor del av deltagarna har sjukdomen, och stämmer det med simuleringen?
- Inom vilket intervall ligger det genomsnittliga systoliska blodtrycket?
- Har rökare högre medelblodtryck än icke-rökare?

**Del 2**
- Kan blodtrycket förklaras av ålder och vikt?
- Hur hänger blodtrycket ihop med åldern?

## Data
"data/health_study_dataset.csv" - 800 deltagare

Kolumner:
- "id" - deltagarnas id
- "age" (år), "sex" (M/F)
- "height" (cm), "weight" (kg)
- "systolic_bp" (mmHg), "cholesterol" (mmol/L)
- "smoker" (Yes/No), "disease" (0/1)

## Miljö
- Python 3.13.7
- Paket och versioner finns i "requirements.txt"

## Kom igång
```bash
# Skapa och aktivera virtuell miljö (Windows, Git Bash)
python -m venv .venv
source .venv/Scripts/activate

# Installera paketen
python -m pip install -r requirements.txt
```

Öppna sedan "analysis.ipynb", välj ".venv" som kernel och kör **Restart & Run All**.

## Struktur
- "data/"
    - "health_study_dataset.csv"
- "src/" 
    - "functions.py" - funktioner för inläsning, simulering, konfidensintervall och t-test
    - "health_analyzer.py" – klassen "HealthAnalyzer" för beskrivande statistik och grafer
- "analysis.ipynb" - analysen
- "README.md"
- "requirements.txt"
- ".gitignore"

## Branches
- "del1" Grundläggande analys och statistik
- "del2" Fördjupning och pipeline

## Resultat 

**Del 1**
- Deltagarna är 18-90 år och medelblodtrycket är cirka 149 mmHg.
- 5,9 procent har sjukdomen. Simuleringen med samma risk gav 6,5 procent.
- 95 % konfidensintervall för medelblodtrycket: 148,3 - 150,1 mmHg.
- Rökare har 0,47 mmHg högre medelblodtryck, men skillnaden går inte att skilja från slumpmässig variation (p = 0,33).

**Del 2**
- Ålder och vikt förklarar cirka 40 % av variationen i blodtrycket (R² = 0,41).
- Blodtrycket ökar med cirka 0,54 mmHg per år och 0,18 mmHg per kg. NumPy och scikit-learn ger samma resultat.
- Blodtrycket stiger tydligt med åldern, och nästan alla över 65 år har över 140 mmHg.