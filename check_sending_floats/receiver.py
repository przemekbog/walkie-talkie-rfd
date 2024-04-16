

import numpy as np
import serial

ser = serial.Serial("/dev/tty.usbserial-A10KQMP1", 115200)

res = ser.read(3*4)
print(np.frombuffer(res, dtype='float32'))

