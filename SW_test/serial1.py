import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

def serial_check():
    while True:
        try:
            ser.reset_input_buffer()
            f = str(ser.readline().decode("utf-8").strip())
        except:
            continue
        data_list = f.split(',')
        values = []

        if len(data_list) == 8:
            for data in data_list:
                values.append(float(data))
            return values
        else:
            continue
