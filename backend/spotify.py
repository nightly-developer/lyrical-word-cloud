import requests
from decouple import config

API_CLIENT_ID = config("CLIENT_ID")
API_CLIENT_SECRET = config("CLIENT_SECRET")
base_url = "https://accounts.spotify.com"

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



def get_songs(access_token,playlist_id):
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
            search_term = ""
            document = dict()
            track = item["track"]

            # track information
            document['track_id'] = track["id"]
            document['track_name'] = track["name"]
            search_term += track['name'] + ' '
            document['popularity'] = track["popularity"]
            search_term["explicit"] = track["explicit"]

            # for consistency
            track_number = track["track_number"]


            # album information
            album = track['album']
            document['album_id'] = album["id"]
            document['album_name'] = album["name"]
            search_term += album["name"] + ' '
            document['release_date'] = album["release_date"]


            # artist information
            artists = track["artists"]
            for index,artist in enumerate(artists):
                document['artist_id'] = artist["id"]
                document['artist_name'] = artist["name"]

            print(document)
            print(search_term)
    else:
        print(response.status_code)

if __name__ == "__main__":
    # access_token, token_type, expires_in =get_access_token()
    # print(access_token)
    access_token = "BQAcNlyQMKU7tyJidflj3HDSFihP-Khis2lTcgIRorZbWzBTjdt3xrj12OgC-V_HAjcS4j2L5GsXS8qAhrKnYRUOwvL-pYm-gWQvCUL6ZglOuUzc2Mg"
    get_songs(access_token,"4dftIPIYg6pNApHlsCwyJu")
