import websocket
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the WebSocket URL from the environment
ECHO = os.getenv("ECHO")

if not ECHO:
    raise ValueError("WEB_URL not found in environment variables.")

messages = []


def on_message(ws, message):
    print(f"Received message: {message}")
    messages.append(message)
    if len(messages) == 10:
        print("First 10 messages received:")
        for msg in messages:
            print(msg)
        ws.close()
    ws.send(f"Our message number {messages.__len__}")


def on_error(ws, error):
    print(f"Error: {error}")


def on_close(ws, close_status_code, close_msg):
    print("Connection closed")


def on_open(ws):
    print("Connection opened")
    ws.send("Hello, server!")
    ws.send("Our message")


ws = websocket.WebSocketApp(
    ECHO,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
)

ws.run_forever()



