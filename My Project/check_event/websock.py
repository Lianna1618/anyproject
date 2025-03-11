import websocket
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the WebSocket URL from the environment
WEB_URL = os.getenv("WEB_URL")


if not WEB_URL:
    raise ValueError("WEB_URL not found in environment variables.")


def on_message(ws, message):
    print(f"Received message: {message}")


def on_error(ws, error):
    print(f"Error: {error}")


def on_close(ws, close_status_code, close_msg):
    print("Connection closed")


def on_open(ws):
    print("Connection opened")
    ws.send("Hello, server!")


ws = websocket.WebSocketApp(
    WEB_URL,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
)

ws.run_forever()

# # Check protocol status 101 and upgrade connection
# def shake_hand(key):
#     response = (
#         "HTTP/1.1 101 Switching Protocols\r\n"
#         "Upgrade: websocket\r\n"
#         "Connection: Upgrade\r\n"
#         f"Sec-WebSocket-Accept: {response_key(7811941c69e658)}\r\n"
#         "\r\n"
#     )
#     return response


# async def check_connection():
#     uri = "wss://echo.websocket.events"
#     async with websocket.connect(uri) as websocket:
#         response_headers = websocket.response_headers
#         print("Response Headers:")
#         for header, value in response_headers.items():
#             print(f"{header}: {value}")

#         # Check specific headers
#         if (
#             response_headers.get("connection", "").lower() == "upgrade"
#             and response_headers.get("upgrade", "").lower() == "websocket"
#         ):
#             print("Connection upgraded successfully to WebSocket.")
#         else:
#             print("Connection upgrade failed.")

#         # Test sending and receiving a message
#         await websocket.send("Hello, WebSocket!")
#         response = await websocket.recv()
#         print(f"Received: {response}")


# # Run the async function
# asyncio.run(check_connection())
