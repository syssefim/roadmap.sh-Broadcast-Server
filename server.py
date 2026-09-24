import asyncio
import websockets
import rand_username



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
  

        #try finally block that handles connected clients and handles client disconnection
        try:
            async for message in websocket:
                print("Received:", message)

                for client, username in connected_clients.items():
                    if client == websocket:
                        await client.send("✅")
                    else:
                        await client.send(f"{username}: {message}")

        finally:
            disconnected_username = connected_clients[websocket]
            del connected_clients[websocket]
            print(f"{disconnected_username} disconnected...")


    # Start the server on localhost
    async with websockets.serve(my_function, "localhost", 6767):
        print(f"Server started at ws://localhost:{6767}")
        await asyncio.Future()  # Run forever
