from decouple import config

from backend.spotify import get_tracks, get_access_token

if __name__ == "__main__":
    playlist_id = config("PLAYLIST_ID")
    # access_token, token_type, expires_in = get_access_token()
    # print(access_token)
    access_token = "BQAK5KSM4_Nl-Jb67YEazxVNJm5hmv9R_lE_eapaayzKSG5Oq-2-iTny_-_cLhHdPc4oy-v7-iOUNuvWcn2v12p0WTMCBsEhPFoQMKefLRpwQTm8PmI"
    get_tracks(access_token,playlist_id)