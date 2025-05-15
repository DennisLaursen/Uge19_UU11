# Her vil jeg opdatere eksisterende data i API'et ved hjælp af en PUT kommando. Dette skal illustrere en opfølgning på restanten.
import requests
from datetime import datetime

# ID på den restant vi skal opdatere
restant_id = 3  # <-- Dette skal på sigt gøres dynamisk, så den korrekte restant/medlem vælges

# MockAPI endpoint
url = f"https://6821b8aa259dad2655b05a09.mockapi.io/DVF/restanter/{restant_id}"

# Dags dato i dansk format
dato = datetime.now().strftime("%d-%m-%Y")

# Opdaterer kolonnen "Status" med en besked om at der er sendt en e-mail til medlemmet, samt datoen for mailen
opdatering = {
    "Status": f"E-mail sendt ({dato})"
}

# Send PUT-request
response = requests.put(url, json=opdatering)

# Resultat
if response.status_code == 200:
    print("Status opdateret:")
    print(response.json())
else:
    print(f"Noget gik galt! Statuskode: {response.status_code}")
    print(response.text)