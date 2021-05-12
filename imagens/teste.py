import requests

response = requests.get('https://qz.com/africa/latest/')

print(response.content)