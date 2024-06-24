import requests

url = 'http://text-processing.com/api/sentiment/'

user = input('Enter text: ')

myobj = {'text': user}
response = requests.post(url, data=myobj)

print(response.status_code)
print(response.json())