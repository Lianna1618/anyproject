import requests


userId = input("Enter user id: \t")


def login_Sim(userId):
    payload = {"username": f"Player_{userId}", "password": "111111"}

    if not userId:
        raise ValueError

    try:
        response = requests.post(
            "https://predictor-development.mortal.city/api/platformsimulator/login",
            headers=payload,
        )

        # print(f"Status Code: {response.status_code}")
        # print(f"Response Text: {response.text}")

        if response.status_code == 200:
            return response.text

        raise ValueError
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


def login_as_player(token: str):
    response = requests.post(
        f"https://predictor-development.mortal.city/api/auth/LoginAsPlayer?platformToken={token}&platformId=749e73c0-ba25-4f69-9f81-ec21d9942e52",
    )
    return response.text


platform_token = login_Sim(userId)

if platform_token:
    access_token = login_as_player(platform_token)
    print(access_token, "token")


def get_random_matches():
    response = requests.get(
        "https://predictor-development.mortal.city/api/matches/random",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    return response.json()
