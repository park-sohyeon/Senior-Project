import serial1
import serial

def dust_check_out(ave1):
    if (ave1 <= 15):
        return "좋음"
    elif (ave1 > 15 and ave1 <= 35 ):
        return "보통"
    elif (ave1 >= 36 and ave1 <= 75 ):
        return "나쁨"
    else:
        return "매우 나쁨"

def dust_check_in(ave2):
    if (ave2 <= 15):
        return "좋음"
    elif (ave2 > 15 and ave2 <= 35 ):
        return "보통"
    elif (ave2 >= 36 and ave2 <= 75):
        return "나쁨"
    else:
        return "매우 나쁨"


