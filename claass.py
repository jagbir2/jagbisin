import netmiko
import os
import logging
from netmiko import ConnectHandler

logger=logging.getLogger()
logger.setLevel(logging.INFO)
file_handler=logging.FileHandler("logs.txt")
log_formatter=logging.Formatter("%(asctime)s %(levelname)s %(message)s ")
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)

class Router():
    def __init__(self,address):
        self.address=address
        
        pass

    def connection(self):
        sw1= {
            "device_type":"cisco_ios",
            "ip":self.address,
            "username":"admin",
            "password":"Pass@123"
        }
        self.connection=ConnectHandler(**sw1)
    
    def prompt(self):
       output= self.connection.find_prompt()
       print(output)

    def command(self):
        output = self.connection.send_command("sh ip int brief")
        print(output)
        
try:
    with open("device.txt", "r") as devices:
        for device in devices:
            router = Router(device.strip())
            router.connection()
            router.prompt()
            router.command()
except Exception as e:
    logger.error(f"Failed to connect due to {e}")
finally:
    print("Completed")
        






        
        