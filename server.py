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
        connected_clients[websocket] = rand_username.generate()
        await websocket.send(f"Connected to server as {connected_clients[websocket]}. Type /help for commands.")  

        other_clients = [client for client in connected_clients if client != websocket]
        broadcast(other_clients, f"{connected_clients[websocket]} joined the chat.")


        # Try finally block that handles connected clients and handles client disconnection
        try:
            async for message in websocket:
                print("Received:", message)

                for client, username in connected_clients.items():
                    await client.send(f"<{connected_clients[websocket]}> {message}")

        finally:
            disconnected_username = connected_clients[websocket]
            del connected_clients[websocket]
            broadcast(connected_clients, f"{disconnected_username} disconnected...")
            print(f"{disconnected_username} disconnected. Number of clinets is now {len(connected_clients)}")






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

