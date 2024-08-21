import requests
from decouple import config

access_token = config("GENIUS_ACCESS_TOKEN")

def get_webpage_url(search_object):
    url = "https://api.genius.com/search"
    param = {
        "q": search_object['search_term']
    }

    headers = {
        'Authorization': "Bearer " + access_token
    }

    response = requests.get(url, params=param, headers=headers)

    if response.ok:
        response_json = response.json()
        hits = response_json["response"]["hits"]

        context = dict()
        for hit in hits:
            result = hit["result"]
            context['id'] = result["id"]
            context['title'] = result["title"]
            context['full_title'] = result["full_title"]

            primary_artists = result["primary_artists"][0]["name"].replace(' &',',')
            primary_artists = set(primary_artists.split(', '))
            context['primary_artists'] = primary_artists

            if context["primary_artists"].issubset(search_object["set_of_artists"]):
                if result["lyrics_state"]:
                    context['lyrics_path'] = result["path"]
                    return result["id"]


            return "did not find any match"
            # return context["primary_artists"], search_object["set_of_artists"]



            # context['name'] = result["name"]
            # context['primary_artist_names'] = result["primary_artist_names"]
            # context['release_date_components'] = result["release_date_components"]
            # context['annotation_count'] = result["annotation_count"]


            # print(context)
    else:
        print(response.status_code)