#!/usr/bin/env python3
"""
WebSocket server with basic message validation.
"""

import asyncio
import websockets


async def connection_handler(websocket):
    """
    Receive messages, validate them, and respond accordingly.
    """
    async for message in websocket:
        if message.strip():
            await websocket.send(f"OK:{message}")
        else:
            await websocket.send("ERR:EMPTY")


async def main():
    """
    Start the WebSocket server and keep it running.
    """
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())