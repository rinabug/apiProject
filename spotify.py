import requests
import os

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': os.environ.get('b90c2848e5a94f8ca49b7c2d88889826'),
    'client_secret': os.environ.get('61045a71da934edeab3dc417cf721dcb'),
})

auth_response_data = auth_response.json()

access_token = auth_response_data['acces_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}


BASE_URL = 'https://api.spotify.com/v1/'
track_id = input('Enter track id: ')
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

print(r.status_code)
print(r.json())
