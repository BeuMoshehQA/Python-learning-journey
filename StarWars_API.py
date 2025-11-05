import requests

def fetch_data(option):
    url = f"https://swapi.dev/api/{option}/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Accedemos a la lista real de resultados
        results = data.get("results", [])
        print(f"Successfully fetched {len(results)} entities")
        return results

    except requests.HTTPError as e:
        print(f"Error fetching data: {e}")
        return None

option = input("Enter an option (e.g., 'people' or 'planets'): ").strip().lower()
data = fetch_data(option)

if data:
    for entity in data:
        print(entity["name"])
else:
    print("Unable to download data")