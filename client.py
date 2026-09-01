import asyncio
import websockets
import argparse

# argparse

parser = argparse.ArgumentParser(description="Broadcast server.")

parser.add_argument("connect", help="Connects to broadcast server.")

args = parser.parse_args()





async def communicate(msg):
    uri = "ws://localhost:8765"
    
    # async with automatically closes the connection when the block ends
    async with websockets.connect(uri) as websocket:
        
        # Send data to the server
        await websocket.send(msg)
        print(f"Client sent: {msg}")
        
        # Wait for the server's reply
        response = await websocket.recv()
        print(f"Client received: {response}")

if __name__ == "__main__":
    message = input("You: ")


    if args.connect:
        asyncio.run(communicate(message))