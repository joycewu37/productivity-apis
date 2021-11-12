# import requests
import secrets
# response = requests.get(
#     "https://api.todoist.com/rest/v1/projects", 
#     headers={
#         "Authorization": "Bearer "+secrets.todoist_auth_token
#     }).json()
# print(response)
'''
from todoist.api import TodoistAPI
api = TodoistAPI(secrets.todoist_auth_token)
api.sync()
# print(api.state['projects'])
import datetime
# print(datetime.date.today())
# print(str(datetime.date.today())+"00:00")
response = api.completed.get_all()#since=str(datetime.date.today())+"T04:00")
print(response['items'])
print(len(response['items']))
'''

PROJECT_IDS = dict()
PROJECT_IDS['School'] = 2212804736
PROJECT_IDS['Independent'] = 2242454039

import requests
response = requests.get(
    "https://api.todoist.com/rest/v1/tasks",
    params={
        "project_id": PROJECT_IDS['Independent'] # school
    },
    headers={
        "Authorization": "Bearer "+secrets.todoist_auth_token
    }).json()
# print(len(response))


# print(requests.get(
#     "https://api.todoist.com/rest/v1/projects", 
#     headers={
#         "Authorization": "Bearer "+secrets.todoist_auth_token}
#     ).json())

'''
'''