import http.client
import json


###################################################################################3333333

import http.client

conn = http.client.HTTPSConnection("league-of-legends-galore.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "a090edb962msh33e48e25717eff7p1c3b18jsn791b4f22ecb3",
    'X-RapidAPI-Host': "league-of-legends-galore.p.rapidapi.com"
}

conn.request("GET", "/api/randomChamp", headers=headers)

res = conn.getresponse()
data = res.read()




def get_champion_details(champion_name):
    conn = http.client.HTTPSConnection("league-of-legends-galore.p.rapidapi.com")
    headers = {
        "X-RapidAPI-Key": "a090edb962msh33e48e25717eff7p1c3b18jsn791b4f22ecb3",  # Replace with your actual API key
        "X-RapidAPI-Host": "league-of-legends-galore.p.rapidapi.com"
    }
    if champion_name == "random":
        url = "/api/randomChamp"
    else:
        url = f"/api/selectChamp?name={champion_name}"
    conn.request("GET", url, headers=headers)


    
    res = conn.getresponse()
    if res.status == 200:
            data = res.read().decode("utf-8")
            data = json.loads(data)  # Parse JSON response

            if len(data) > 0:  # Check if champion found
                champion_data = data[0]
                return {
                    "Name": champion_data["champName"],
                    "Release Date": champion_data["releaseDate"],
                    "HP": champion_data["HP"]
                }
            else:
                print(f"Champion '{champion_name}' not found.")
                return None
    else:
            print(f"API error: {res.status} - {res.reason}")
            return None

    
champion_name = " "

while champion_name != "q":

    champion_name = input("Select a Champ or type Random. (Q to quit) ").lower()
    if champion_name == "q":
        print("Cya")
    else:
        champion_details = get_champion_details(champion_name)
        if champion_details is not None:
            print(f"\nChampion Details:\nName: {champion_details['Name']}")
            print(f"Release Date: {champion_details['Release Date']}")
            print(f"HP: {champion_details['HP']}")
        else:
            print("Invalid champion name or API error. Please try again.")
    

