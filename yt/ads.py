import requests

# API call to display ad
response = requests.get('https://reqres.in/api/users?page=2')

# Display ad HTML
print(response.text)