import requests
from login import log_admin
from faker import Faker
import base64

fake = Faker()


def location(headers):
    payload = {
        "name": fake.name(),
    }

    try:
        image_url = fake.image_url()
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            image_data = base64.b64encode(image_response.content).decode("utf-8")
            payload["imageData"] = image_data
        else:
            print("Failed to fetch image from URL")
            return None

        response = requests.post(
            "https://backend-development.node.fun/locations",
            headers=headers,
            json=payload,
        )

        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        if 200 <= response.status_code <= 299:
            print("Location created successfully")
            response_data = response.json()
            print("Created Location Data:", response_data)

            return response_data.get("name")
        else:
            print("Location not created")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


access_token, refresh_token = log_admin()

if access_token:
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    name = location(headers)
    if name:
        print(f"Created Location Name: {name}")
else:
    print("Failed to log in as admin")


2.--------------------------------------------------------------

import requests
from SA.login import log_admin 
from faker import Faker

fake = Faker()


def location(headers):
    payload = {
        "name": fake.name(),
        "imageUrl": fake.image_url(), 
        "clubs": [],
    }

    try:
        response = requests.post(
            "https://backend-development.node.fun/locations",
            headers=headers,
            json=payload,
        )

        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        if 200 <= response.status_code <= 299:
            print("Location created successfully")
            response_data = response.json()
            print("Created Location Data:", response_data)

            return response_data.get("name")
        else:
            print("Location not created")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


access_token, refresh_token = log_admin()

if access_token:
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    name = location(headers)
    if name:
        print(f"Created Location Name: {name}")
else:
    print("Failed to log in as admin")
