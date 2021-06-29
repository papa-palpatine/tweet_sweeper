import json
import requests

def auth():
    with open('secrets.json') as j:
        secret = json.load(j)
        bearer = secret['BEARER_TOKEN']
    return bearer

def create_url():
    tweet_fields = "tweet.fields=lang, author_id"
    ids = "ids=1278747501642657792,1255542774432063488"
    url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
    return url

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers):
    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                reponse.status_code, response.text
            )
        )
    return response.json()

def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()
