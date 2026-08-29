# import argparse


# # argparse

# parser = argparse.ArgumentParser(description="broadcast-server")


# parser.add_argument("start", help="Starts the server")

# parser.add_argument("connect", help="Connects the client to the server")

# args = parser.parse_args()


# # if args.start:
# #     print("starting server...")
# # elif args.connect:
# #     print("connecting client to server...")


# print(f"hi {args.start}")




import asyncio
import websockets

async def my_function(websocket):
    # This loop keeps the connection open to receive multiple messages
    async for message in websocket:
        print(f"Server received: {message}")
        
        # Send a response back to the client
        reply = f"Echo: {message}"
        await websocket.send(reply)
        print(f"Server sent: {reply}")

async def main():
    # Start the server on localhost, port 8765
    async with websockets.serve(my_function, "localhost", 8765):
        print("Server started at ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())