from pyModbusTCP.server import ModbusServer
from PLC_Simulator import get_plc_values
from time import sleep
import socket


# Function to get the local IP address of the machine
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        IP = s.getsockname()[0]
    finally:
        s.close()
    return IP



A = input("Are you using localhost? (y/n): ")

if A == "y":
    IP = "127.0.0.1"
else:
    IP = get_local_ip()


server = ModbusServer(IP, 12345, no_block=True)


try:
    print("Start server...")
    server.start()
    print(f"Server is online on {IP}")
    while True:
        plc1, plc2 = get_plc_values()

        server.data_bank.set_holding_registers(0, [plc1])
        server.data_bank.set_holding_registers(1, [plc2])

        sleep(1)

except KeyboardInterrupt:
    print("Shutdown server ...")
    server.stop()
    print("Server is offline")
