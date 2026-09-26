import asyncio
import websockets
import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout




async def send_messages(websocket):
    # prompt_toolkit
    session = PromptSession()

    while True:
        # try block handles Ctrl+C 
        try:
            message = await session.prompt_async()
        except (KeyboardInterrupt, EOFError):
            # Move up and clear the empty prompt line
            sys.__stdout__.write("\033[1A\033[2K\r")
            sys.__stdout__.flush()

            print("Disconnecting...")
            return

        # prompt_toolkit
        sys.__stdout__.write("\033[1A\033[2K\r")
        sys.__stdout__.flush()

        # help commands
        if message.strip().lower() in ['/quit', '/exit']:
            print("Disconnecting...")
            return 
        elif message.strip().lower() in ['/help']:
            print("To quit the chat, type either /quit or /exit")
            continue
            
        await websocket.send(message)

async def receive_messages(websocket):
    async for message in websocket:
        print(f"{message}")


async def connect(port):
    # 1. Get address
    uri = f"ws://localhost:{port}"
    
    # 2. Manage traffic coming to and from the address
    async with websockets.connect(uri) as websocket:
        with patch_stdout():

            send_task = asyncio.create_task(send_messages(websocket))
            receive_task = asyncio.create_task(receive_messages(websocket))

            done, pending = await asyncio.wait(
                [send_task, receive_task],
                return_when=asyncio.FIRST_COMPLETED,
            )

            for task in pending:
                task.cancel()

