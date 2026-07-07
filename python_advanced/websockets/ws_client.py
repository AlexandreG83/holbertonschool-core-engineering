#!/usr/bin/env python3
"""
Simple WebSocket client.
"""

import asyncio
import os
import sys
import websockets


async def connect_and_send(uri: str, message: str) -> str:
    """
    Connect to the WebSocket server, send one message,
    receive the response, and return it.
    """
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        return response


async def main():
    """
    Read URI and message from environment or CLI arguments,
    then connect, send, and output the response.
    """
    uri = os.environ.get("WS_URI", "ws://localhost:8765")
    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        message = os.environ.get("WS_MESSAGE", "demo")

    response = await connect_and_send(uri, message)
    sys.stdout.write(response)


if __name__ == "__main__":
    asyncio.run(main())
