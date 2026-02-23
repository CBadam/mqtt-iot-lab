import time
import random
import paho.mqtt.client as mqtt

class VirtualDevice:
    def __init__(self, device_id, broker="localhost", port=1883):
        self.device_id = device_id
        self.battery = 100.0

        self.client = mqtt.Client(client_id=device_id)
        self.client.connect(broker, port)
        self.client.loop_start()

    def read_temperature(self):
        return round(random.uniform(20, 25), 2)

    def update_battery(self):
        self.battery -= 0.1

    def publish(self):
        temp = self.read_temperature()
        self.update_battery()

        self.client.publish(f"home/{self.device_id}/temperature", temp)
        self.client.publish(f"home/{self.device_id}/battery", round(self.battery, 2))

        print(f"[{self.device_id}] Temp: {temp} | Battery: {self.battery:.2f}")