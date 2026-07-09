#!/usr/bin/env python3
"""
WebSocket server implementing broadcast messaging.
Each message is sent to all connected clients with prefix B:.
"""

import asyncio
import websockets

# Store all active clients
clients = set()


async def connection_handler(websocket):
    """
    Handle a client connection and broadcast messages.
    """
    # Register new client
    clients.add(websocket)

    try:
        async for message in websocket:
            # Broadcast to all connected clients
            dead_clients = set()

            for client in clients:
                try:
                    await client.send(f"B:{message}")
                except websockets.ConnectionClosed:
                    # Mark disconnected clients for removal
                    dead_clients.add(client)

            # Clean up dead connections
            clients.difference_update(dead_clients)

    finally:
        # Ensure cleanup on disconnect
        clients.discard(websocket)


async def main():
    """
    Start the WebSocket broadcast server.
    """
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
