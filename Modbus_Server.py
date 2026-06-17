from pyModbusTCP.server import ModbusServer
from PLC_Simulator import get_plc_values
from time import sleep

server = ModbusServer("127.0.0.1", 12345, no_block=True)

try:
    print("Start server...")
    server.start()
    print("Server is online")
    while True:
        plc1, plc2 = get_plc_values()

        server.data_bank.set_holding_registers(0, [plc1])
        server.data_bank.set_holding_registers(1, [plc2])

        sleep(1)

except KeyboardInterrupt:
    print("Shutdown server ...")
    server.stop()
    print("Server is offline")
