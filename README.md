<br />
<div align="center">
  <a href="https://github.com/CBadam/mqtt-iot-lab">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">MQTT Virtual IoT Lab</h3>
  <p align="center">
    A local MQTT-based IoT simulation environment built in Python.
    <br />
    Simulating virtual devices, message flow, and distributed system behavior.
    <br />
    <br />
    <a href="https://github.com/CBadam/mqtt-iot-lab">View Repository</a>
    ·
    <a href="https://github.com/CBadam/mqtt-iot-lab/issues/new?labels=bug">Report Bug</a>
    ·
    <a href="https://github.com/CBadam/mqtt-iot-lab/issues/new?labels=Feature">Request Feature</a>
  </p>
</div>


## About The Project
This project simulates a fleet of virtual IoT devices communicating
through a local MQTT broker (Mosquitto).

It demonstrates:

-   Publish / Subscribe architecture
-   Distributed system behavior
-   Device state modeling (battery, temperature)
-   Reliability concepts (QoS, retained messages, Last Will)



## Architecture

Virtual Devices ---\> MQTT Broker (Mosquitto) ---\> Subscribers /
Dashboard

Each virtual device: - Has a unique ID - Publishes temperature and
battery level - Maintains internal state - Can be extended to simulate
failures



## Built With

* [![Python][Python.org]][Python-url]
* [![paho-mqtt][paho-mqtt]][paho-mqtt-url]
* [![Mosquitto][Mosquitto.org]][Mosquitto-url]



## Getting Started

### Prerequisites

* Python 3.12
* paho-mqtt
* Mosquitto MQTT Broker

### Installation

1. Download Mosquitto at https://mosquitto.org/download/.

2. Install Mosquitto with the default configuration.

    When choosing components, make sure to check Service.

3. Add the installation directory (default: C:\Program Files\Mosquitto) to the system environment variables.

4. Go to windows services and find "Mosquitto Broker" and check if startup type is automatic.

5. Clone the repo
    ```sh
    git clone https://github.com/YOUR_USERNAME/mqtt-iot-lab.git
    ```
6. Access the repo
    ```sh
    cd mqtt-iot-lab
    ```
7. Create and activate a virtual environment
    ```sh
    python -m venv venv
    venv\Scripts\activate  
    ```
8. Install requirements
    ```sh
    pip install -r requirements.txt
    ```






[Python.org]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff
[Python-url]: https://www.python.org/
[paho-mqtt-url]: https://pypi.org/project/paho-mqtt/
[paho-mqtt]: https://img.shields.io/badge/paho--mqtt-31210B?style=flat&logo=mqtt&logoColor=white
[Mosquitto-url]: https://mosquitto.org/
[Mosquitto.org]: https://img.shields.io/badge/Mosquitto-3C217E?style=for-the-badge&logo=eclipsemosquitto&logoColor=white
