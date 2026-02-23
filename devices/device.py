import threading
import time
import random
import paho.mqtt.client as mqtt

class VirtualDevice:
    def __init__(self, device_id, broker="localhost", port=1883):
        self.device_id = device_id
        self.battery = 100.0
        self.temperature = round(random.uniform(20, 25), 2)
        self._timer = None  # Store the timer here

        self.client = mqtt.Client(client_id=device_id)
        self.client.connect(broker, port)
        self.client.loop_start() 
        
        # Start the automated publishing
        self.publish_loop()

    def update_temperature(self):
        self.temperature += random.uniform(-0.5, 0.5)

    def update_battery(self):
        self.battery -= 0.1

    def publish(self):
        self.update_temperature()
        self.update_battery()

        self.client.publish(f"home/{self.device_id}/temperature", round(self.temperature, 2))
        self.client.publish(f"home/{self.device_id}/battery", round(self.battery, 2))

    def publish_loop(self):
        if self.battery > 0:
            self.publish()
            # Save the timer object so we can cancel it later
            self._timer = threading.Timer(3.0, self.publish_loop)
            self._timer.start()
    
    def stop(self):
        """Gracefully shut down the device."""
        if self._timer:
            self._timer.cancel() # Stop the next scheduled publish
        self.client.loop_stop()  # Stop the background MQTT thread
        self.client.disconnect() # Tell the broker we are leaving
        print(f"[{self.device_id}] Cleanly disconnected.")