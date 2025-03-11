import requests
from loggin_admin import admin_auth
from faker import Faker

fake = Faker()


def update_club(headers):
    payload = {
        "id": "114748de-f4c0-4ec9-be25-a779c486d8b3",
        "email": fake.email(),
        "name": fake.name(),
        "businessName": fake.company(),
        "website": fake.url(),
        "description": fake.text(),
        "openAt": fake.time(),
        "closeAt": fake.time(),
        "capacity": fake.random_number(),
        "authorisedRepresentativeFirstname": fake.first_name(),
        "authorisedRepresentativeLastname": fake.last_name(),
        "logo": fake.image_url(),
        "address": {
            "country": fake.country(),
            "address": fake.address(),
            "state": fake.state(),
            "postalCode": fake.postcode(),
            "city": fake.city(),
        },
        "gIdPdf": fake.image_url(),
        "businessLicensePdf": fake.image_url(),
    }

    try:
        response = requests.put(
            "https://backend-development.node.fun/clubs/114748de-f4c0-4ec9-be25-a779c486d8b3",
            headers=headers,
            json=payload,
        )

        print(f"Request Payload: {payload}")
        print(f"Request Headers: {headers}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Text: {response.text}")

        if 200 <= response.status_code <= 299:
            try:
                response_json = response.json()
                status = response_json.get("status")
                print(f"Club status: {status}")
                return status
            except ValueError:
                print("Response is not in JSON format")
                return None
        else:
            if response.status_code == 400:
                print("Bad Request - Often due to missing a required parameter.")
            elif response.status_code == 401:
                print("Unauthorized - Invalid or expired access token.")
            elif response.status_code == 403:
                print("Forbidden - Access to the resource is denied.")
            elif response.status_code == 404:
                print("Not Found - The endpoint URL is incorrect.")
            elif response.status_code == 500:
                print("Internal Server Error - Something went wrong on the server.")
            else:
                print(response.status_code)
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


access_token, refresh_token = admin_auth()

if access_token:
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    update_club(headers)
else:
    print("Failed to log in and obtain access token.")
