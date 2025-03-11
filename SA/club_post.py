import requests
from SA.login import log_admin
from faker import Faker


fake = Faker()


def create_club(headers):
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
            print(f"Created Club ID: {club_id}")
            return club_id
        else:
            print(f"Failed to create club with status code {response.status_code}")
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
    club_id = create_club(headers)
#     if club_id:
#         print("Created Club ID:", club_id)
#         # Use the club ID in another API call
#         # For demonstration, let's assume another API endpoint for updating club information
#         update_endpoint = f"https://backend-development.node.fun/clubs/{club_id}/update"
#         update_payload = {
#             "name": "Updated Club Name",
#             "description": "Updated Club Description",
#             # Add more fields as needed
#         }
#         response = requests.put(update_endpoint, headers=headers, json=update_payload)
#         print("Update Response:", response.text)
#     else:
#         print("Failed to create club")
# else:
#     print("Failed to retrieve access token")
