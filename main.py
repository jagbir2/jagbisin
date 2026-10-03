import netmiko
import logging
import os

print("Current working directory is" ,os.getcwd())
#import paramiko

logger=logging.getLogger()
logger.setLevel(logging.INFO)
file_handler=logging.FileHandler("logs.txt")
logformat=logging.Formatter("%(asctime)s %(levelname)s %(message)s ")
file_handler.setFormatter(logformat)
logger.addHandler(file_handler)


from netmiko import ConnectHandler
# This is the new git comment
with open("device.txt" ,"r") as Test:
    for device in Test:
        


        sw1 = {
            "device_type": "cisco_ios",
            "ip": device,
            "username":"admin",
            "password":"Pass@123"
        }

        connection = ConnectHandler(**sw1)

                    
        prompt=connection.find_prompt()
        print(prompt)

        command = connection.send_command("sh ip int brief")

        print(command)