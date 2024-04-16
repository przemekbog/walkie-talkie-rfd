

import numpy as np
import serial

ser = serial.Serial("/dev/tty.usbserial-A10KQUWB", 115200)

ser.write(np.array([1.0, 1.5, 2.0], dtype='float32'))
