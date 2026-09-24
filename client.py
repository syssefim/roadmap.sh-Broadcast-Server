import asyncio
import websockets
import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout




async def send_messages(websocket):
    session = PromptSession()

    while True:
        message = await session.prompt_async()

        sys.__stdout__.write("\033[1A\033[2K\r")
        sys.__stdout__.flush()

        # Check if the user wants to leave
        if message.strip().lower() in ['/quit', '/exit']:
            print("Disconnecting...")
            return  # Exiting the function marks the task as completed
        elif message.strip().lower() in ['/help']:
            print("To quit the chat, type either /quit or /exit")
            continue
            
        await websocket.send(message)

async def receive_messages(websocket):
    async for message in websocket:
        print(f"{message}")


async def communicate():
    uri = f"ws://localhost:{6767}"
    
    # async with automatically closes the connection when the block ends
    async with websockets.connect(uri) as websocket:
        with patch_stdout():

            # 1. Create independent tasks instead of gathering them directly
            send_task = asyncio.create_task(send_messages(websocket))
            receive_task = asyncio.create_task(receive_messages(websocket))

            # 2. Wait for FIRST_COMPLETED. If the socket closes, receive_task finishes first.
            done, pending = await asyncio.wait(
                [send_task, receive_task],
                return_when=asyncio.FIRST_COMPLETED,
            )

            # 3. Cancel whichever task is still running (usually the send_task)
            for task in pending:
                task.cancel()




