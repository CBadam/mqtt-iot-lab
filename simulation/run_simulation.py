import threading
import time
from devices.devices import VirtualDevice

def run_device(device_id):
    device = VirtualDevice(device_id)

    while device.battery > 0:
        device.publish()
        time.sleep(3)

for i in range(5):
    threading.Thread(target=run_device, args=(f"device_{i}",)).start()