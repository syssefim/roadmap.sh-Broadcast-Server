#!/usr/bin/env python3
import asyncio
import websockets
import argparse
import server
import client

# argparse

def main():
    parser = argparse.ArgumentParser(description="Broadcast server.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Create a specific sub-parser for the literal word "start"
    start_parser = subparsers.add_parser("start", help="Starts the broadcast server.")
    connect_parser = subparsers.add_parser("connect", help="Connects to the broadcast server.")



    # # Add the port argument specifically to the "start" command
    # start_parser.add_argument("--port", type=int, default=6767, help="Optional flag to specify what port to start server on.")

    args = parser.parse_args()


    try:
        if args.command == "start":
            asyncio.run(server.start())
        elif args.command == "connect":
            asyncio.run(client.connect())
    except KeyboardInterrupt:
        print("\nShutting down...")






if __name__ == "__main__":
    main()