import asyncio
import getpass
import json
import os
import random
import websockets
from mapa import Map
from consts import *

# Next 4 lines are not needed for AI agents, please remove them from your code!

async def agent_loop(server_address="localhost:8000", agent_name="student"):
    async with websockets.connect(f"ws://{server_address}/player") as websocket:

        # Receive information about static game properties
        await websocket.send(json.dumps({"cmd": "join", "name": agent_name}))
        #waits for the next mesage
        msg = await websocket.recv()
        #loads the mesage
        game_properties = json.loads(msg)

        mapa = Map(game_properties["map"])
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(mapa)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(mapa._map)
        for x in mapa._map:
            print(x)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        walls = []
        for lin in range(len(mapa._map)):
            for col in range(len(mapa._map[lin])):
                if mapa._map[lin][col]==Tiles.WALL:
                    walls.append([col,lin])
        print(walls)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

        while True:
            try:
                update = json.loads(
                    await websocket.recv()
                )  # receive game update, this must be called timely or your game will get out of sync with the server

                if "map" in update:
                    # we got a new level
                    game_properties = update
                    mapa = Map(update["map"])
                else:
                    # we got a current map state update
                    state = update
                await websocket.send(
                    
                    #random movements
                    json.dumps({"cmd": "key", "key": random.choice('asdw')})
                )  # send key command to server - you must implement this send in the AI agent
                        
            except websockets.exceptions.ConnectionClosedOK:
                print("Server has cleanly disconnected us")
                return

# DO NOT CHANGE THE LINES BELLOW
# You can change the default values using the command line, example:
# $ NAME='arrumador' python3 client.py
loop = asyncio.get_event_loop()
SERVER = os.environ.get("SERVER", "localhost")
PORT = os.environ.get("PORT", "8000")
NAME = os.environ.get("NAME", getpass.getuser())
loop.run_until_complete(agent_loop(f"{SERVER}:{PORT}", NAME))