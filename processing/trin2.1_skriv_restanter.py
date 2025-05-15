# Her vil jeg skrive NY data til API'et ved hjælp af en POST kommando - i modsætning til en PUT kommando, der opdaterer eksisterende data.
import requests

# Det data, jeg vil tilføje til "CRM-systemet". MockAPI tilføjer automatisk et fortløbende ID til hver post.
ny_restant = {
    "Navn": "Dennis Bager",
    "E-mail": "dennis@example.com",
    "Medlemskab": "Standard",
    "Indmeldelsesdato": "07-10-2006",
    "Betalingskanal": "Girokort",
    "Betalingsfrekvens": "Kvartalsvis",
    "SenestFejledeBetaling": "01-04-2025",
    "Status": "Ingen betaling",
    "subscriptionId": "123abc456def",
    "GirokortSendt": "25-03-2005",
}

# URL til API-endpoint
url = "https://6821b8aa259dad2655b05a09.mockapi.io/DVF/restanter"
response = requests.post(url, json=ny_restant)

# Tjek om request var succesfuld (statuskode 201)
if response.status_code == 201:
    print("Ny restant oprettet:")
    print(response.json())
else:
    print(f"Noget gik galt. Status: {response.status_code}")
    print(response.text)