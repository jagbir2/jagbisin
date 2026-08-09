import netmiko
import paramiko
import logging
import getpass
from netmiko import ConnectHandler
from getpass import getpass

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("class.txt")
Formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s ")
file_handler.setFormatter(Formatter)
logger.addHandler(file_handler)


class Router:

    def __init__(self, address):
        self.address = address
        self.connection = None

    def connect(self):
        sw1 = {
            "device_type": "cisco_ios",
            "ip": self.address,
            "username": "admin",
            "password": "Pass@123"
        }

        self.connection = ConnectHandler(**sw1)

    def command(self):
        self.command = self.connection.send_command("sh ip int brief")
        return self.command


try:

    with open("device_list.txt", "r") as devices:

        for device in devices:

            router = Router(device.strip())

            router.connect()

            output = router.command()

            with open("output.txt", "a") as file:
                file.write(f"\n\n --------{router.address}------\n")
                file.write(output)

except Exception as e:
    logger.error(f"failed to connect: {e}")

finally:
    print("Completed")