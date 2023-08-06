from ursinanetworking import *
from ursinanetworking.easyursinanetworking import *
import json

config = json.load(open(os.getcwd() + "/config.json"))

server = UrsinaNetworkingServer(config["ip"], config["port"])
easy = EasyUrsinaNetworkingServer(server)

world = json.load(open(os.getcwd() + "/world.json"))["world"]


@server.event
def onClientConnected(Client):
    print(f"{config['name']} > {Client} connected!")
