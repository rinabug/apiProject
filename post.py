import requests

info = {
  'title': 'Special Agent',
  'body': 'Leroy Jethro Gibbs',
  'userId': '1'
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=info)

print(response.status_code)
print(response.json())