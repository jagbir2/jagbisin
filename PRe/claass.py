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

    def connect(self):
        sw1= {
            "device_type":"cisco_ios",
            "ip":self.address,
            "username":"admin",
            "password":"Pass@123"
        }
        self.connect=ConnectHandler(**sw1)
    
    def prompt(self):
       output= self.connect.find_prompt()
       print(output)

    def command(self,command):
        # command=input("Enter the command: ")
        output=self.connect.send_command(command)
        
        return output
    
    def disconnect(self):
        self.connect.disconnect()
        pass
        
router = None


with open("device.txt", "r") as devices:
        for device in devices:
            try:
                router = Router(device.strip())
                router.connect()
                router.prompt()
                output= router.command(input("Enter the command: "))
                print(output)

            except Exception as e:
                logger.error(f"Failed to connect due to {e}")
            finally:
                # if router is not None:
                    # router.disconnect()
                print("Completed")
        






        
        