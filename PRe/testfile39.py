##################################
## This is Automation Project  ##
##################################

import netmiko
import logging
import os
from getpass import getpass
from netmiko import ConnectHandler

import fastapi
from fastapi import FastAPI

app=FastAPI()

logger=logging.getLogger()
logger.setLevel(logging.INFO)
file_handler=logging.FileHandler("logs2.txt")
formatter=logging.Formatter("%(asctime)s %(levelname)s %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# @app.get("/")
# def greet():
#     return "HELLO WORLD this is my Automation Project "

@app.post("/command")
class Router:
    def __init__(self,address):
        self.address=address
        pass
    
    
    def connection(self):
        sw1={
            "device_type":"cisco_ios",
            "ip":self.address,
            "username":"admin",
            "password":"Pass@123"
        }
        
        self.connection=ConnectHandler(**sw1)
        
    def prompt(self):
        prompt=self.connection.find_prompt()
        print (prompt)
    
        
    def command(self,command):
        
        output=self.connection.send_command(command)
        print(output)


with open("device.txt","r") as file:
    for device in file:
        router = Router(device.strip())
        router.connection()
        router.prompt()
        output=router.command(input("Enter the command : "))
        print(output)
            