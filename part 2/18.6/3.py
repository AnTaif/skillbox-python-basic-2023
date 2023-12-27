import requests
import json
import os

def get_pilot_info(pilot_url):
    pilot_response = requests.get(pilot_url)
    pilot_data = pilot_response.json()

    planet_url = pilot_data['homeworld']
    planet_response = requests.get(planet_url)
    planet_data = planet_response.json()

    pilot_info = {
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'weight': pilot_data['mass'],
        'homeworld': pilot_data['homeworld'],
        'homeworld_info': {
            'name': planet_data['name'],
            'url': planet_url
        }
    }

    return pilot_info

def get_millennium_falcon_info():
    falcon_url = "https://swapi.dev/api/starships/10/"
    falcon_response = requests.get(falcon_url)
    falcon_data = falcon_response.json()

    pilots_info = []

    for pilot_url in falcon_data['pilots']:
        pilot_info = get_pilot_info(pilot_url)
        pilots_info.append(pilot_info)

    falcon_info = {
        'name': falcon_data['name'],
        'max_speed': falcon_data['max_atmosphering_speed'],
        'class': falcon_data['starship_class'],
        'pilots': pilots_info
    }

    return falcon_info

millennium_falcon_info = get_millennium_falcon_info()

print("Информация о Millennium Falcon:")
print(json.dumps(millennium_falcon_info, indent=2))

path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'millennium_falcon_info.json')

with open(path, 'w') as json_file:
    json.dump(millennium_falcon_info, json_file, indent=2)
