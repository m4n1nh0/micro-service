import requests

client_id = "04e480ef96274a468c13f6ca4eb137ec"
client_secret = "efa6bd93ffa6410d8eb6b64382c353d1"
URL_TOKEN = 'https://accounts.spotify.com/api/token'
auth = requests.post(URL_TOKEN, {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
})
auth_data = auth.json()
token = auth_data['access_token']
headers = {
    'Authorization': 'Bearer {token}'.format(token=token)
}

URL = 'https://api.spotify.com/v1/'
party = '37i9dQZF1DX8mBRYewE6or'
pop = '37i9dQZF1DWVLcZxJO5zyf'
rock = '37i9dQZF1DWWsq4e0rDzty'
classico = '37i9dQZF1DWXmUP9DYdke2'


def playlist(temp):
    url_ret = " "
    if temp > 30:
        req = requests.get(URL + 'playlists/' + party, headers=headers)
        result = req.json()
        url_ret = result["external_urls"]["spotify"]
    elif 15 < temp < 30:
        req = requests.get(URL + 'playlists/' + pop, headers=headers)
        result = req.json()
        url_ret = result["external_urls"]["spotify"]
    elif 10 < temp < 14:
        req = requests.get(URL + 'playlists/' + rock, headers=headers)
        result = req.json()
        url_ret = result["external_urls"]["spotify"]
    else:
        req = requests.get(URL + 'playlists/' + classico, headers=headers)
        result = req.json()
        url_ret = result["external_urls"]["spotify"]

    return url_ret
