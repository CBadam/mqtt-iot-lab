import time
from devices.device import VirtualDevice

if __name__ == "__main__":
    # No manual threading.Thread calls here!
    devices = [VirtualDevice(f"device_{i}") for i in range(5)]
    time.sleep(10) # Let them work for a bit
    print("--- DISRUPTING DEVICE_0 ---")
    devices[0].simulate_network_failure()
    time.sleep(20) # Let them work for a bit
    print("--- RECOVERING DEVICE_0 ---")
    devices[0].simulate_network_recovery()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down devices...")
        for dev in devices:
            dev.stop()
        print("All clear. Goodbye!")