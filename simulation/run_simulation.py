import time
from devices.device import VirtualDevice

if __name__ == "__main__":
    # No manual threading.Thread calls here!
    devices = [VirtualDevice(f"device_{i}") for i in range(5)]

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down devices...")
        for dev in devices:
            dev.stop()
        print("All clear. Goodbye!")