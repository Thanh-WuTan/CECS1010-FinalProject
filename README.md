# MakerBot Mini

## I. Uploading Firmware and Hardware Testing

### 1. Hardware Design
To run the demo examples, you will need the following hardware components:

- ESP32-CAM module.
- MakerBot Mini board to control the motors.
- A round robot chassis or a similar frame equipped with 5V motors.
- Other components: batteries, charger, and connecting wires.

**WIFI connection information for ESP32-CAM**

- SSID: `MBotMini-<ID>`, where ID is the hardware identifier of the ESP32-CAM.
- Password: `makerbotisfun`

You can change this information by editing the code and re-uploading the firmware.

### 2. Uploading Firmware

First, we need to upload the firmware to both the MakerBot board and the ESP32-CAM module.

**Uploading firmware with PlatformIO:** We recommend using PlatformIO installed on Visual Studio Code to upload the firmware. After that, you can upload the firmware by opening the folders using PlatformIO, compiling, and uploading the code to the boards. You can find the PlatformIO setup and usage guide [here](docs/Guide-PlatformIO-Windows.pdf).

You will also need to install the CH340 Driver when using Windows, following the instructions here: <https://www.arduined.eu/ch340-windows-10-driver-download/>.

Open the folder [./firmware](./firmware) in Visual Studio Code and upload the firmware as instructed. The firmware configuration can be found at: [firmware/src/config.h](firmware/src/config.h).

**Note: The firmware source code does not currently support Arduino IDE.**

### 3. Checking Camera Signal from ESP32-CAM

Connect to the WIFI `MBotMini-<ID>` and open a web browser, then go to: [http://192.168.4.1](http://192.168.4.1) to view the images captured by the camera.

**Reading the camera feed from ESP32-CAM using Python:**

To read the camera feed using Python, your computer needs to have Python and the OpenCV package installed. First, install Python with the package manager Pip, then use Pip to install OpenCV: `pip install opencv-python`. We recommend using [Anaconda](https://www.anaconda.com/) / [Miniconda](https://docs.conda.io/en/latest/miniconda.html) to manage your Python environment.

Run the Python script to read the camera feed from ESP32: Connect to the WIFI network of the ESP32-CAM, then run the program located at [client/read_esp32_cam/read_cam.py](client/read_esp32_cam/read_cam.py).

```bash
cd client/read_esp32_cam/
pip install -r requirements.txt
python read_cam.py
```

![](images/keyboard_control_with_cam.png)
