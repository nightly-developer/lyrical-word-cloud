from decouple import config

from backend.spotify import get_tracks

if __name__ == "__main__":
    playlist_id = config("PLAYLIST_ID")
    # access_token, token_type, expires_in = get_access_token()
    # print(access_token)
    access_token = ""
    get_tracks(access_token,playlist_id)