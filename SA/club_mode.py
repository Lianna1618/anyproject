import requests
from SA.login import log_admin
from faker import Faker
import uuid

fake = Faker()


def create_club(headers):
    # Generate a UUID v4 for club_id
    club_id = str(uuid.uuid4())

    # Generate the payload with fake data
    payload = {
        "supervisorDto": {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "email": fake.email(),
        },
        "businessName": fake.company(),
    }

    try:
        # Make the POST request to create the club
        response = requests.post(
            "https://backend-development.node.fun/clubs", headers=headers, json=payload
        )

        # Print the status code and response text
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        # Check if the club was created successfully
        if 200 <= response.status_code <= 299:
            print("Club created successfully")
            response_data = response.json()
            print("Created Club Data:", response_data)

            # Extract the club ID from the response data
            club_id = response_data.get("id")
            return response_data.get("businessName"), club_id
        else:
            print(f"Failed to create club with status code {response.status_code}")
            print(f"Reason: {response.reason}")
            try:
                error_message = response.json()
                print(f"Error Message: {error_message}")
            except ValueError:
                print("Error response content is not valid JSON")
        return None, None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


def update_club_status(headers, club_id):
    # Generate the payload with fake data
    payload = {
        "id": club_id,
        "status": "ACTIVE",
        "moderationComment": fake.text(),
    }

    try:
        # Make the PUT request to update the club status
        response = requests.put(
            f"https://backend-development.node.fun/clubs/moderation/{club_id}",
            headers=headers,
            json=payload,
        )

        # Print the status code and response text
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        if 200 <= response.status_code <= 299:
            response_data = response.json()
            club_status = response_data.get("status")

            print(f"Club Status: {club_status}")

            return club_status
        else:
            print(
                f"Failed to update club status with status code {response.status_code}"
            )
            print(f"Reason: {response.reason}")
            try:
                error_message = response.json()
                print(f"Error Message: {error_message}")
            except ValueError:
                print("Error response content is not valid JSON")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
access_token, refresh_token = log_admin()

if access_token:
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    club_name, club_id = create_club(headers)
    if club_name:
        club_status = update_club_status(headers, club_id)
        if club_status:
            print(f"Created Club: Name={club_name}, ID={club_id}, Status={club_status}")
        else:
            print("Failed to update club status")
    else:
        print("Failed to create club")
