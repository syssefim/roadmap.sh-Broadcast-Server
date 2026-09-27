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
            
        await websocket.send(message)

async def receive_messages(websocket):
    while True:
        message = await websocket.recv()
        print(f"{message}")


async def connect(port):
    # 1. Get address
    uri = f"ws://localhost:{port}"
    
    # 2. Manage traffic coming to and from the address
    try:
        async with websockets.connect(uri) as websocket:
            with patch_stdout():

                send_task = asyncio.create_task(send_messages(websocket))
                receive_task = asyncio.create_task(receive_messages(websocket))

                done, pending = await asyncio.wait(
                    [send_task, receive_task],
                    return_when=asyncio.FIRST_COMPLETED,
                )

                # initiate shutdown
                for task in pending:
                    task.cancel()
                await asyncio.gather(*pending, return_exceptions=True)

                for task in done:
                    task.result()

    except websockets.ConnectionClosedError as e:
        print(f"⚠️  Connection lost abruptly! Error: {e}")
    except websockets.ConnectionClosedOK as e:
        print(f"ℹ️  Connection closed by server: {e}")
    except Exception as e:
        print(f"❌ Failed to connect: {e}")


