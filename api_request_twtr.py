import requests
import os
import json



# curl --request GET --location 'tweet.fields=context_annotations&max_results=100&query=camping(nature%20OR%20%22outdoor%20actvities%22)' \
# --header 'Authorization: Bearer $BEARER_TOKEN'

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields

# from%3Agiovannagalvani%20-is%3Aretweet&start_time=2022-06-01T00:00:00.000Z&end_time=2022-07-01T00:00:00.000Z&max_results=100
# &tweet.fields=author_id,in_reply_to_user_id,public_metrics,text&
# expansions=entities.mentions.username,geo.place_id&user.fields=id,location,name,profile_image_url,public_metrics" 

# tweet.fields=context_annotations&max_results=100&query=camping(nature%20OR%20%22outdoor%20actvities%22)

#query_params = {'query': '(from:MSF_brasil -is:retweet) OR #twitterdev','tweet.fields': 'author_id'}
# query_params = {'query': '(from:giovannagalvani -is:retweet)','tweet.fields': 'public_metrics'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r
