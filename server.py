import asyncio
import websockets
from websockets.asyncio.server import serve, broadcast
import rand_username
import sys
import signal




async def start():
    # Declare a connected clients list
    connected_clients = {}


    # Define handler function
    # Note: the handler is a function that defines how the server interacts with a connected client
    async def my_handler_function(websocket):
        # Oboard client
        username = rand_username.generate()
        connected_clients[websocket] = username
        await websocket.send(f"Connected to server as {username}. Type /help for commands.")  

        other_clients = [client for client in connected_clients if client != websocket]
        broadcast(other_clients, f"{username} joined the chat.")
        print(f"{websocket} joined as {username}. Users: ({len(connected_clients)})")


        # Try finally block that handles connected clients and handles client disconnection
        try:
            async for message in websocket:
                print(f"Received and now broadcasting: <{username}> {message}")
                broadcast(connected_clients, f"<{username}> {message}")

        finally:
            del connected_clients[websocket]
            broadcast(connected_clients, f"{username} disconnected...")
            print(f"{username} disconnected. Users: ({len(connected_clients)})")
            print(f"Broadcasting: {username} disconnected...")






    # Shutdown 
    stop_event = asyncio.Event()
    loop = asyncio.get_running_loop()

    if sys.platform != 'win32':
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, stop_event.set)







    # Start the server on localhost
    async with websockets.serve(my_handler_function, "localhost", 6767):
        print("Server started at ws://localhost:6767 (Press Ctrl+C to stop)")
        
        await stop_event.wait()
        print("\nInitiating graceful shutdown...")

