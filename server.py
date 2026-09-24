import asyncio
import websockets
import rand_username
import sys
import signal


# websockets



# Starts websockets server with websockets.serve(handler, host, port)
async def main():
    # Declare a connected clients list
    connected_clients = {}


    # Define handler function
    # Note: the handler is a function that defines how the server interacts with a connected client
    async def my_function(websocket):
        # connected_clients.append((websocket, rand_username.generate()))   
        connected_clients[websocket] = rand_username.generate()
        #print(websocket)
        
        await websocket.send(f"Connected to server as {connected_clients[websocket]}. Type /help for commands.")
  

        #try finally block that handles connected clients and handles client disconnection
        try:
            async for message in websocket:
                print("Received:", message)

                for client, username in connected_clients.items():
                    # if client == websocket:
                    #     continue
                    #     await client.send("✅")
                    # else:
                    #     await client.send(f"<{connected_clients[websocket]}> {message}")
                    await client.send(f"<{connected_clients[websocket]}> {message}")

        finally:
            disconnected_username = connected_clients[websocket]
            del connected_clients[websocket]
            print(f"{disconnected_username} disconnected...")






    stop_event = asyncio.Event()
    loop = asyncio.get_running_loop()

    if sys.platform != 'win32':
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, stop_event.set)

    # Start the server on localhost
    async with websockets.serve(my_function, "localhost", 6767):
        print("Server started at ws://localhost:6767 (Press Ctrl+C to stop)")
        
        # Wait here until a signal sets the event
        await stop_event.wait()
        
        print("\nInitiating graceful shutdown...")

