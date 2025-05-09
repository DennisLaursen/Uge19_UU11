import pandas as pd
from datetime import datetime, timedelta
import os

def forbered_restantskema(filsti: str, gem_som: str = None) -> pd.DataFrame:
    # Læs CSV-filen
    df = pd.read_csv(filsti, sep=';', encoding='utf-8')
    
    # Konverter datoer til datetime-format
    df['Senest fejlede betaling'] = pd.to_datetime(df['Senest fejlede betaling'], format='%d-%m-%Y', errors='coerce')
    df['Indmeldelsesdato'] = pd.to_datetime(df['Indmeldelsesdato'], format='%d-%m-%Y', errors='coerce')
    
    # Tilføj kolonne hvis den ikke findes
    if "Senest screenet" not in df.columns:
        df['Senest screenet'] = ""
    
    #Tilføj dags dato
    today = datetime.today().strftime('%d-%m-%Y')
    df["Senest screenet"] = today

    #Slet restanter der er ældre end 3 måneder
    df['Senest fejlede betaling'] = pd.to_datetime(df['Senest fejlede betaling'], format='%d-%m-%Y', errors='coerce')
    cutoff_date = datetime.today() - timedelta(days=90)
    gamle = df[df['Senest fejlede betaling'] < cutoff_date]
    for _, row in gamle.iterrows():
        print(f"Slettet pga. mere end 3 mdr. gammel: Medl.nr. {row['Medl.nr.']}")
    df = df[df['Senest fejlede betaling'] >= cutoff_date]

    # Fjern dubletter
    før = len(df)
    df = df.drop_duplicates(subset=['Medl.nr.'], keep='first')
    efter = len(df)
    if før > efter:
        print(f"Slettet {før - efter} dublet baseret på Medl.nr.")
    
    # Gem som ny fil
    if gem_som is None:
        mappe, filnavn = os.path.split(filsti)
        gem_som = os.path.join(mappe, "restantliste_screenet.csv")
    df.to_csv(gem_som, sep=';', encoding='utf-8', index=False)
    print(f"Listen er screenet og gemt som {gem_som}")

    return df

df = forbered_restantskema('data/restantliste.csv')