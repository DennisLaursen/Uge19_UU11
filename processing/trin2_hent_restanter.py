#Her vil jeg forsøge at hente data fra et API og vise det i terminalen. Jeg har brugt mockapi.io.
import requests

# URL til API-endpoint
url = "https://6821b8aa259dad2655b05a09.mockapi.io/DVF/restanter"

try:
    # Send GET-request til API
    response = requests.get(url)

    # Tjek om request var succesfuld (statuskode 200)
    if response.status_code == 200:
        data = response.json()  # Parse JSON-data
        print("Data hentet fra API:")
        for item in data:
            print(item)
    else:
        print(f"Fejl ved hentning af data. Statuskode: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Der opstod en fejl ved forespørgslen: {e}")