import requests
from datetime import datetime
# USERNAME = "your created usename"
# TOKEN = "your created token"
USERNAME = "whiteknight16"
TOKEN = "dfghexdghdw"


# CREATING USER

pixela_create_user_end_point = "https://pixe.la/v1/users"

user_params = {
    "token": "dfghexdghdw",
    "username": "whiteknight16",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create_user=requests.post(pixela_create_user_end_point,json=user_params)
# print(create_user.text)

# CREATING GRAPH

pixela_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": "dfghexdghdw",
}
graph_params = {
    "id": "graph1",
    "name": "Coding Hours",
    "unit": "hours",
    "type": "int",
    "color": "shibafu"
}

# create_graph=requests.post(pixela_endpoint,json=graph_params,headers=headers)

# POSTING TO THE GRAPH

graphID = "graph1"
post_value_end_point = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graphID}"
post_params = {
    "date": f"{datetime.now().year}{'{:02d}'.format(datetime.now().month)}{'{:02d}'.format(datetime.now().day)}",
    "quantity": "1"
}
post_data = requests.post(post_value_end_point,json=post_params, headers=headers)
print(post_data.text)

