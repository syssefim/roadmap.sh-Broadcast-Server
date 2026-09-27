# <img src="roadmap.png" width="35" align="top" /> Broadcast Server

Broadcast Server project from [roadmap.sh](https://roadmap.sh/projects/broadcast-server) Backend Developer Roadmap. 

## 📝 About the Project

A simple broadcast server that allows clients to connect to it and send messages that get broadcasted to all connected clients. Built in Python with `websockets` for WebSocket connections and `prompt_toolkit` for client-side terminal input, alongside the standard library.

## 📌 Installation

1. First, clone the repository and cd into the project:
```
git clone https://github.com/syssefim/roadmap.sh-Broadcast-Server
cd roadmap.sh-Broadcast-Server
```
2. Next, install dependencies and configurations with:
```
pip install -e .
```

## ▶️ Running the Project

First, create and activate a virtual environment:
```
python3 -m venv .venv
source .venv/bin/activate
```
Then, to start the server run:
```
broadcast-server start
```
Finally, to connect a client to the server run:
```
broadcast-server connect
```












---

<div align="center">
  <p>
    Serafim Sharkov • 2026
  </p>
  <p>
    <a href="https://github.com/syssefim">GitHub</a> • 
    <a href="https://www.linkedin.com/in/serafim-sharkov/">LinkedIn</a>
  </p>
</div>
