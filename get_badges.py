from flask import Flask
from flask import request
import requests

app = Flask(__name__)  # Flask constructor


# A decorator used to tell the application
# which URL is associated function
@app.route('/badges/<placeid>', methods=['GET'])
# def hello():
#     return 'HELLO'


def get_universe_id(placeid):
    print(placeid)
    places = f"https://apis.roblox.com/universes/v1/places/{placeid}/universe"
    response = requests.get(places)

    # Parse the JSON response into a Python dictionary or list
    data = response.json()

    print(data['universeId'])
    universe_id = data['universeId']
    # get_badges(universe_id)

    return get_game_data(universe_id)

def get_badges(universe_id):
    badges = f"https://badges.roblox.com/v1/universes/{universe_id}/badges"
    response = requests.get(badges)
    badge_data = response.json()
    print(badge_data)
    print("parsing data: ")
    for entry in badge_data['data']:
        name = entry.get("name")
        icon_id = entry.get('iconImageId')
        print(name, icon_id)
    return badge_data
    # print(badge_data['data']['name'])

def get_game_data(universe_id):
    game = f"https://games.roblox.com/v1/games?universeIds={universe_id}"
    # game = f"https://games.roblox.com/v1/games/{universe_id}"
    response = requests.get(game)
    game_data = response.json()
    return game_data

if __name__ == '__main__':
    app.run()
