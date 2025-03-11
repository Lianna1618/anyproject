import requests
import json
import os
from dotenv import load_dotenv
from faker import Faker

fake = Faker()

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def get_all_posts():
    response = requests.get(f"{BASE_URL}/posts").json()
    for x in response:
        print(x)


# get_all_posts()


def get_post_by_id(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}").json()
    print(response)

# get_post_by_id(1)


def create_post():
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
        }

    payload = json.dumps({
        "title": fake.sentence(),
        "body": fake.text(),
        "userId": 1
    })

    response = requests.post(
        f"{BASE_URL}/posts", headers=headers, data=payload
        )
    print(response.status_code)
    print(response.text)

# create_post()


def update_post(post_id):
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
        }

    payload = json.dumps({
        "title": fake.word(),
        "body": fake.text(),
        "userId": 1
    })

    response = requests.put(
        f"{BASE_URL}/posts/{post_id}", headers=headers, data=payload
        )
    print(response.status_code)
    print(response.text)

# update_post(1)


def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    print(response.status_code)
    print(response.text)

# delete_post(1)


get_all_posts()
get_post_by_id(1)
create_post()
update_post(1)
delete_post(1)
