import pandas as pd
from datetime import datetime
import os
import sys

# Tjek om filen findes
filsti = "data/restantliste_screenet.csv"

if not os.path.exists(filsti):
    print("restantliste_screenet.csv endnu ikke genereret. Start med at køre indledende_trin.py koden først.")
    sys.exit(1)

# Indlæs data
df = pd.read_csv("data\restantliste_screenet.csv", sep=";", encoding="utf-8")
df["Senest fejlede betaling"] = pd.to_datetime(df["Senest fejlede betaling"], dayfirst=True)

# Funktion til at flette mail
def generer_mail(navn, dato, kanal):
    if kanal == "Dankort/VISA" or kanal == "MasterCard":
        skabelonfil = "templates/betalingskort.txt"
    elif kanal == "MobilePay":
        skabelonfil = "templates/mobilepay.txt"
    elif kanal == "Girokort":
        skabelonfil = "templates/girokort.txt"
    elif kanal == "Betalingsservice":
        skabelonfil = "templates/betalingsservice.txt"
    else:
        print(f"Ukendt kanal: {kanal} – springer over.")
        return None

    with open(skabelonfil, encoding="utf-8") as f:
        tekst = f.read()
    
    tekst = tekst.replace("{{navn}}", navn)
    tekst = tekst.replace("{{dato}}", dato.strftime("%d-%m-%Y"))
    tekst = tekst.replace("{{link}}", "https://fornyelse.vegetarisk.dk")  # placeholder

    return tekst

# Generér mails
for index, row in df.iterrows():
    mail = generer_mail(row["Navn"], row["Senest fejlede betaling"], row["Betalingskanal"])
    if mail:
        print(f"\n--- MAIL TIL: {row['Navn']} ({row['E-mail']}) ---\n")
        print(mail)
        print("\n-------------------------\n")