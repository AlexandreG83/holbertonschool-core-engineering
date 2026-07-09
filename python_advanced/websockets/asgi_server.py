#!/usr/bin/env python3
"""
ASGI WebSocket + HTTP application using Starlette.
Echo server on /ws and simple HTML page on /.
"""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


# --------------------
# HTTP endpoint
# --------------------
async def homepage(request):
    """
    Serve a simple HTML page.
    """
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>WebSocket App</title>
        </head>
        <body>
            <h1>WebSocket App</h1>
            <p>Connect to /ws using WebSocket client</p>
        </body>
    </html>
    """
    return HTMLResponse(html_content)


# --------------------
# WebSocket endpoint
# --------------------
async def websocket_endpoint(websocket):
    """
    Echo WebSocket server.
    """
    await websocket.accept()

    while True:
        message = await websocket.receive_text()
        await websocket.send_text(message)


# --------------------
# App definition
# --------------------
app = Starlette(
    routes=[
        Route("/", homepage),
        WebSocketRoute("/ws", websocket_endpoint),
    ]
)
