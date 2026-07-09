#!/usr/bin/env python3
"""
WebSocket server implementing unicast messaging.
Each client receives only its own messages prefixed with U:.
"""

import asyncio
import websockets


# Set to store active connections
clients = set()


async def handler(websocket):
    """
    Handle a single client connection.
    """
    # Register client
    clients.add(websocket)

    try:
        async for message in websocket:
            # Send response only to sender (unicast)
            await websocket.send(f"U:{message}")

    finally:
        # Unregister client on disconnect
        clients.remove(websocket)


async def main():
    """
    Start the WebSocket server.
    """
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
