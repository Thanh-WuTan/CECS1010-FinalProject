import socket
import _thread
import urllib.request
import cv2
import numpy as np
import time

from controller import calculate_control_signal, send_control, set_control_ip, find_lane_lines


CONTROL_IP = "192.168.4.100"
CONTROL_PORT = 9999
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sk.settimeout(3000)

CAM_URL = "http://192.168.4.1:80"
stream = urllib.request.urlopen(CAM_URL)
bytes = bytes()


# Set control ip continuously to receive sensor params
def set_control_ip():
    time.sleep(2)
    set_control_ip()
_thread.start_new_thread(set_control_ip, ())


send_control(0, 0)