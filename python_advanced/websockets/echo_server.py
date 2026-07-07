#!/usr/bin/env python3
"""
Simple WebSocket echo server.
"""

import asyncio
import websockets


async def echo(websocket):
    """
    Receive messages from a client and send them back unchanged.
    """
    async for message in websocket:
        await websocket.send(message)


async def main():
    """
    Start the WebSocket server and keep it running.
    """
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
