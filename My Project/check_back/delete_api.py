import requests


def get_post_by_id(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/42").json()
    print(response)

get_post_by_id(1)
