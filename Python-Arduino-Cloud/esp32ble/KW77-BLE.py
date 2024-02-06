import asyncio
from bleak import BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic
import time

ESP32_ADDRESS = "F6:F1:32:70:01:36"
CHARACTERISTIC_UUID2 = "00002A37-0000-1000-8000-00805F9B34FB"

def interpret(data):
    """
    data is a list of integers corresponding to readings from the BLE HR monitor
    """

    byte0 = data[0]
    res = {}
    res["hrv_uint8"] = (byte0 & 1) == 0
    sensor_contact = (byte0 >> 1) & 3
    if sensor_contact == 2:
        res["sensor_contact"] = "No contact detected"
    elif sensor_contact == 3:
        res["sensor_contact"] = "Contact detected"
    else:
        res["sensor_contact"] = "Sensor contact not supported"
    res["ee_status"] = ((byte0 >> 3) & 1) == 1
    res["rr_interval"] = ((byte0 >> 4) & 1) == 1

    if res["hrv_uint8"]:
        res["hr"] = data[1]
        i = 2
    else:
        res["hr"] = (data[2] << 8) | data[1]
        i = 3

    if res["ee_status"]:
        res["ee"] = (data[i + 1] << 8) | data[i]
        i += 2

    if res["rr_interval"]:
        res["rr"] = []
        while i < len(data):
            # Note: Need to divide the value by 1024 to get in seconds
            res["rr"].append((data[i + 1] << 8) | data[i])
            i += 2

    return res
def notification_handler(characteristic: BleakGATTCharacteristic, data: bytearray):
    print(data)
    print(interpret(data))
async def main(address,uuid):
    async with BleakClient(address) as client:
        await client.start_notify(uuid, notification_handler)
        await asyncio.sleep(20.0)
        await client.stop_notify(uuid)

asyncio.run(main(ESP32_ADDRESS,CHARACTERISTIC_UUID2))

