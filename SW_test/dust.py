def dust_check_out(ave1):
    if (ave1 < 16.000):
        return "좋음"
    elif (ave1 >= 16.000 and ave1 < 36.000 ):
        return "보통"
    elif (ave1 >= 36.000 and ave1 < 76.000 ):
        return "나쁨"
    else:
        return "매우 나쁨"

def dust_check_in(ave2):
    if (ave2 < 16.000):
        return "좋음"
    elif (ave2 >= 16.000 and ave2 < 36.000 ):
        return "보통"
    elif (ave2 >= 36.000 and ave2 < 76.000 ):
        return "나쁨"
    else:
        return "매우 나쁨"


