import requests
import secrets
response = requests.get(
    "https://api.todoist.com/rest/v1/projects", 
    headers={
        "Authorization": "Bearer "+secrets.todoist_auth_token
    }).json()
print(response)