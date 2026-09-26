#!/usr/bin/env python3
import asyncio
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


    
    start_parser.add_argument("--port", type=int, default=6767, help="Optional flag to specify what port to start server on.")
    connect_parser.add_argument("--port", type=int, default=6767, help="Optional flag to specify what port to start server on.")


    args = parser.parse_args()


    try:
        if args.command == "start":
            asyncio.run(server.start(args.port))
        elif args.command == "connect":
            asyncio.run(client.connect(args.port))
    except KeyboardInterrupt:
        print("\nShutting down...")






if __name__ == "__main__":
    main()