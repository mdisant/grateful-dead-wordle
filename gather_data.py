# This file will be used to find and downdload Grateful Dead music data
# https://stmorse.github.io/journal/spotify-api.html
# https://developer.spotify.com/dashboard/applications/dc7edc20941b4fa8b1c90a96cdc5806d

import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = "dc7edc20941b4fa8b1c90a96cdc5806d"

AUTH_URL = "https://accounts.spotify.com/api/token"

DICKS_PICKS_ID = "5Uw8A2ryDJNyaVOEBmg1eY"


def get_access_token():
    # POST
    auth_response = requests.post(
        AUTH_URL,
        {
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": os.getenv('CLIENT_SECRET'),
        },
    )

    # Convert POST to JSON
    auth_response_data = auth_response.json()

    # Return the access token
    return auth_response_data["access_token"]


def get_playlist_data(access_token, playlist_id):
    headers = {"Authorization": f"Bearer {access_token}"}

    base_url = "https://api.spotify.com/v1/"

    r = requests.get(base_url + "playlists/" + playlist_id, headers=headers)
    json_data = r.json()

    return json_data


def json_to_file(json_data, playlist_id):
    with open(f"./data/{playlist_id}.json", "w") as f:
        json.dump(json_data, f, indent=4)


def main():
    access_token = get_access_token()
    dicks_picks_data = get_playlist_data(access_token, DICKS_PICKS_ID)
    json_to_file(dicks_picks_data, DICKS_PICKS_ID)


main()
