import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")
# print(bearer_token)

search_url = "https://api.twitter.com/2/tweets/search/recent"


# query=giovannagalvani, twiter.fields: autor_id, in_replay_to_user_id, creat_at, expansions: in_replay_to_user_id

query_params = {'query': 'from:giovannagalvani','tweet.fields': 'author_id'}
#, 'expansions': 'in_replay_to_user_id'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    
    formatJson = json.dumps(json_response, indent=4, sort_keys=True)
    print(formatJson)
    
    with open("resp_tw_gg.json", "w") as outfile:
        json.dump(json_response, outfile, indent=4)


if __name__ == "__main__":
    main()