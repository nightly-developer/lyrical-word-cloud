import requests
from decouple import config
from backend.genius import get_webpage_url

API_CLIENT_ID = config("SPOTIFY_CLIENT_ID")
API_CLIENT_SECRET = config("SPOTIFY_CLIENT_SECRET")
base_url = "https://accounts.spotify.com"


def string_manipulation(s):
    # remove feature artist name from track name
    index = s.find('(')
    return s[:index] if index != -1 else  s.rstrip()


def get_access_token():
    # URL for the POST request
    url = "https://accounts.spotify.com/api/token"

    # Data to be sent in the POST request
    data = {
        "grant_type": "client_credentials",
        "client_id": API_CLIENT_ID,
        "client_secret": API_CLIENT_SECRET
    }

    # Headers to be included in the POST request
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Make the POST request
    response = requests.post(url, data=data,headers=headers)

    # Print the status code and response content
    status_code = response.status_code
    if status_code <= 200:
        return response.json()["access_token"], response.json()["token_type"], response.json()["expires_in"]



def get_tracks(access_token,playlist_id):
    url= f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    params = {
        "market": "ES",
        # "fields": "id,public,tracks(items(track(artists(id,name),id,name)))"
        # "fields": "items(track(id,name,popularity,album(id,name,release_date),artists(id,name)))"
        "fields": "limit,offset,total,items(track(album(id,name,release_date),artists(id,name),explicit,id,name,popularity,track_number))"
    }

    headers = {
        "Authorization": "Bearer " + access_token
    }
    # Make the GET request
    response = requests.get(url, headers=headers, params=params)

    if response.ok:
        response_json: object = response.json()
        total = response_json["total"]

        limit: int = response_json["limit"]
        offset: int = response_json["offset"]
        items = response_json["items"]

        for item in items:
            document = dict()
            search_object = dict()
            search_term = ""
            track = item["track"]
            track_number = track["track_number"] # for consistency

            # track information
            document["track_id"] = track["id"]
            track_name = track["name"]
            document["track_name"] = track_name
            document["popularity"] = track["popularity"]

            # album information
            album = track['album']
            document['album_id'] = album["id"]
            document['album_name'] = album["name"]
            document['release_date'] = album["release_date"]

            artist_list = []
            set_of_artists = set()
            for artist in track["artists"]:
                artist_list.append(artist["name"])
                set_of_artists.add(artist["name"])

            # artist_name = artist_names = ""
            primary_artists = ""
            if len(artist_list) > 1:
                if any(["ft.","feat."]) in artist_list:
                    primary_artists = artist_list[0]
                primary_artists = " ".join(artist_list)
            else:
                primary_artists = artist_list[0]


            # artist information
            document["artists"] = track["artists"]
            # artist_name = track["artists"][0]["name"]

            # search Object
            track_name = string_manipulation(track["name"])
            search_term += track_name + ' '
            search_term += primary_artists
            search_object["track_name"] = track_name
            search_object["artist_name"] = primary_artists
            search_object["set_of_artists"] = set_of_artists
            search_object["track_number"] = track_number
            search_object["search_term"] = search_term
            search_object["explicit"] = track["explicit"]

            # print(document)
            print(get_webpage_url(search_object))
    else:
        print(response.status_code)
