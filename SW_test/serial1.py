from collections import defaultdict

import serial
import time

# 'COM8' 부분에 환경에 맞는 포트 입력
ser = serial.Serial('COM8', 9600)

def serial_check():
    while True:
        f = str(ser.readline().decode("utf-8").strip())
        data_list = f.split(',')
        # print(f)
        keys = []
        values = []


        print(data_list)
        if len(data_list) == 5:
            for data in data_list:
                values.append(float(data))
            return values
        else:
            continue



if __name__ == '__main__':
    serial_check()
