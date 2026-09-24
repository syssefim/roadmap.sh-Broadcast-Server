import asyncio
import websockets
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout




async def send_messages(websocket, session):
    while True:
        message = await session.prompt_async("You: ")

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

    # 1. Initialize the prompt_toolkit session
    session = PromptSession()
    
    # async with automatically closes the connection when the block ends
    async with websockets.connect(uri) as websocket:

        # 2. Wrap the task execution in patch_stdout() to protect the input line
        with patch_stdout():
            
            # 3. Pass the session to the send_task
            send_task = asyncio.create_task(send_messages(websocket, session))
            receive_task = asyncio.create_task(receive_messages(websocket))

            # Wait for FIRST_COMPLETED. If the socket closes, receive_task finishes first.
            done, pending = await asyncio.wait(
                [send_task, receive_task],
                return_when=asyncio.FIRST_COMPLETED,
            )

            # Cancel whichever task is still running (usually the send_task)
            for task in pending:
                task.cancel()




