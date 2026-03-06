from fastapi import WebSocket

async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    while True:

        data = await websocket.receive_text()

        response = "Processing..."

        await websocket.send_text(response)