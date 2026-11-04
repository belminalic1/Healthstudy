# Healthstudy, Statistisk dataanalys

## Syfte
Analys av en hälsostudie med 800 deltagare och utreda olika frågor:

** Del 1 frågor
- Hur ser deltagarnas ålder, vikt, längd, blodtryck och kolesterol ut
- Hur stor del av deltagarna har sjukdomen, och stämmer det med simuleringen?
- Imom vilket intervall ligger det genomsnittliga systoliska blodtrycket?
- Har rökare högre medelblodtryck än icke-rökare?

** Del 2
- Kan systoliskt blodtryck förutsägas utifrån ålder och vikt?
- Vilka ytterligare samnband finns i datan?

## Data
Dataset (CSV): health_study_dataset.csv
Kolumner: age (år), sex (M/F), height (cm), weight (kg), systolic_bp (mmHg), cholesterol (mmol/L), smoker (Yes/No), disease (0/1).

## Miljö
- Python 3.13.7
- Paket och versioner finns i "requirements.txt"

## Kom igång
```bash
# Skapa och aktivera virtuell miljö (Windows, Git Bash)
python - venv .venv
source .venv/Scripts/activate

# Installera paketen
python -m pip install -r requirements.txt

Öppna sedan "analysis.ipynb", välj ".venv" som kernel och kör **Restart & Run All**.

## Struktur

Healthstudy/

- "data/"
    - "health_study_dataset.csv"
- "src/" funktioner och klasser
- "analysis.ipynb"
- "README.md"
- "requirements.txt"
- ".gitignore"

## Branches
- "del1" Grundläggande analys och statistik
- "del2" Fördjupning och pipeline

## Resultat
*Fylls i när analysen är klar