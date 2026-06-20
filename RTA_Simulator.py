from pyModbusTCP.client import ModbusClient
from time import sleep  

A = input("Are you using localhost? (y/n): ")

if A == "y":
    SERVER_IP = "127.0.0.1"
else:
    SERVER_IP = input("Enter the server IP address: ")

client = ModbusClient(host=SERVER_IP, port=12345)
print(f"Connecting to server at {SERVER_IP}")
client.open()


try:
    while True:
        plc1 = client.read_holding_registers(0)
        plc2 = client.read_holding_registers(1)

        print(f"plc1: {plc1[0]} | plc2: {plc2[0]}")
        sleep(1)

except KeyboardInterrupt:
    print("Disconnecting...")
    client.close()