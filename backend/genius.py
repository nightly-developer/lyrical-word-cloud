from http.client import responses

import requests

def gt_webpage(access_token,search_term):
    q = search_term["track"]["name"] + ' ' + search_term["track"]["artists"][0]["name"]
    url = "https://api.genius.com/search"
    param = {
        "q": q
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
            context['annotation_count'] = result["annotation_count"]
            context['artist_names'] = result["artist_names"]
            # context['name'] = result["name"]
            context['full_title'] = result["full_title"]
            context['title'] = result["title"]
            context['id'] = result["id"]
            context['lyrics_state'] = result["lyrics_state"]
            context['lyrics_path'] = result["path"]
            context['primary_artist_name'] = result["primary_artist"]['name']
            # context['primary_artist_names'] = result["primary_artist_names"]
            context['release_date_components'] = result["release_date_components"]

            print(context['primary_artist_name'],search_term["track"]["artists"][0]["name"])
            break





    else:
        print(response.status_code)

if '__main__' == __name__:
    access_token = ""
    search_terms = [
        {
            "track": {
                "artists": [
                    {
                        "name": "Lil Nas X"
                    }
                ],
                "name": "SUN GOES DOWN"
            }
        },
        {
            "track": {
                "artists": [
                    {
                        "name": "Ruth B."
                    },
                    {
                        "name": "sped up + slowed"
                    },
                    {
                        "name": "slater"
                    }
                ],
                "name": "Dandelions - slowed + reverb"
            }
        },
        {
            "track": {
                "artists": [
                    {
                        "name": "Lord Huron"
                    }
                ],
                "name": "The Night We Met"
            }
        },
        {
            "track": {
                "artists": [
                    {
                        "name": "One Direction"
                    }
                ],
                "name": "Night Changes"
            }
        },
        {
            "track": {
                "artists": [
                    {
                        "name": "Juice WRLD"
                    },
                    {
                        "name": "Seezyn"
                    }
                ],
                "name": "Hide"
            }
        }
    ]
    for search_term in search_terms:
        gt_webpage(access_token,search_term)
