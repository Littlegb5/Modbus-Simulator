from pyModbusTCP.client import ModbusClient
from time import sleep

client = ModbusClient(host="127.0.0.1", port=12345)
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