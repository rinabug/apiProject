import json

with open('data/music.json') as music_json:
  music_data = json.load(music_json)

#print(type(music_data))
#print(music_data['name'])
#print(music_data['begin_area']['name'])
print(json.dumps(music_data, indent=3))