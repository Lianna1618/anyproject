import requests


def login():
    payload = {
        "provider": "EMAIL_PASSWORD",
        "providerCode": "NodeFunSuperAdmin",
        "email": "superadmin@nodefun.app",
    }

    try:
        response = requests.post(
            "https://backend-development.node.fun/login", json=payload
        )

        # Print the status code and full response content for debugging purposes
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")  # Use response.text to get raw text

        if 200 <= response.status_code <= 299:
            try:
                response_data = response.json()
                print(f"Response JSON: {response_data}")  # Print the full JSON response

                # Attempt to extract the access token and refresh token
                access_token = response_data.get(
                    "accessToken"
                )  # Updated key to match response
                refresh_token = response_data.get(
                    "refreshToken"
                )  # Extract refresh token

                if access_token:
                    print(f"Access Token: {access_token}")
                    print(f"Refresh Token: {refresh_token}")
                    return access_token, refresh_token
                else:
                    print("Access token not found in response")
            except ValueError:
                print("Response content is not valid JSON")
        else:
            print(f"Login failed with status code {response.status_code}")
            # Print the reason if available
            print(f"Reason: {response.reason}")
            # Print any error message from the response
            try:
                error_message = response.json()
                print(f"Error Message: {error_message}")
            except ValueError:
                print("Error response content is not valid JSON")
        return None, None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


# Call the function to log in and retrieve the access token and refresh token
access_token, refresh_token = log_admin()

if access_token:
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",  # Adjust content type if needed
    }
    # Now you can use `headers` for further requests that require authentication
    print("The SA is logged in.")
else:
    print("Failed to retrieve access token")
