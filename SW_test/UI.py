import sys
import rain
import serial1
import dust_api
import dust
import rain_forecast

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
import set_address

form_class = uic.loadUiType("main.window.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fontSize = 10

        # 버튼에 기능을 연결하는 코드
        self.weather_button.clicked.connect(self.set_weather_dust)
        self.weather_button_2.clicked.connect(self.set_weather_rain)
        self.weather_button_3.clicked.connect(self.set_weather_th)
        self.weather_button_4.clicked.connect(self.set_weather_CO)
        self.address_button.clicked.connect(self.set_address)

    def set_weather_dust(self):

        serial_result = serial1.serial_check()
        result = dust_api.dust_check()
        dust_in = dust.dust_check_in(float(serial_result[4]))

        self.textEdit.setText(
            "실내 온도           :     " + (serial_result[0]) + " ºC \n" +
            "실내 습도           :     " +
            serial_result[1] + "  % \n" + "실내 미세먼지     :    " + dust_in)
        self.textEdit_2.setText("지금 실외 미세먼지 센서 수치는?     "
                                + (serial_result[5]) + " ㎍/㎥  " + "<" +
                                dust.dust_check_out(float(serial_result[5]))
                                + ">" + "\n선택한 지역의 미세먼지 API 수치는?   \n" +
                                "(" + result["sidoName"] + " " +
                                result["stationName"] + ")   " +
                                "pm10수치 :  " + result["pm10수치"] + " ㎍/㎥" + "  <" +
                                result["10형태"] + ">  " + "pm2.5수치 :  " +
                                result["pm2.5수치"]
                                + " ㎍/㎥ " + "  <" + result["2.5형태"] + ">")
        self.textEdit_3.setText("지금 실내 미세먼지 센서 수치는?     " +
                                (serial_result[4]) + " ㎍/㎥  " + "< " + dust_in + ">")

    # 강수량 버튼 클릭 시 출력
    def set_weather_rain(self):
        serial_result = serial1.serial_check()
        result = rain.rain_check()
        result1 = rain_forecast.rain_check_forecast()
        self.textEdit.setText("실내 온도           :     "
                              + str(serial_result[0]) + " ºC \n" +
                              "실내 습도           :     " + str(serial_result[1])
                              + "  % \n" + "실내 미세먼지     :    " +
                              dust.dust_check_in(serial_result[4]))
        self.textEdit_2.setText("지금 실외 강수량 API 수치는?     "
                                + result["강수량"] + " mm\n" +
                                "지금 실외 강수형태는?     " + result["형태"]
                                + "\n지금 실외 빗물 센서 수치는?     " +
                                str(serial_result[6]))
        self.textEdit_3.setText("단기예보 강수량 API 수치는?     "
                                + result1["1시간 강수량"] + " (mm)  \n" +
                                "단기예보 강수형태는?     " + result1["강수형태"] +
                                " \n" + "단기예보 강수확률은?     " +
                                result1["강수확률"] + "  % ")


    # 온습도 버튼 클릭 시 출력
    def set_weather_th(self):
        serial_result = serial1.serial_check()
        self.textEdit.setText("실내 온도           :     "
                              + str(serial_result[0]) + " ºC \n" +
                              "실내 습도           :     " + str(serial_result[1])
                              + "  % \n" + "실내 미세먼지     :    " +
                              dust.dust_check_in(serial_result[4]))
        self.textEdit_2.setText("지금 실외 온도 센서 수치는?     "
                                + str(serial_result[2]) + " ºC\n"
                                + "지금 실외 습도 센서 수치는?     " +
                                str(serial_result[3]) + " %")
        self.textEdit_3.setText("지금 실내 온도 센서 수치는?     " +
                                str(serial_result[0]) + " ºC\n" +
                                "지금 실내 습도 센서 수치는?     " +
                                str(serial_result[1]) + " %")

    def set_weather_CO(self):
        serial_result = serial1.serial_check()

        self.textEdit.setText("실내 온도           :     " + str(serial_result[0])
                              + " ºC \n" + "실내 습도           :     " +
                              str(serial_result[1]) + "  % \n" + "실내 미세먼지"
                                                                 "     :    " +
                              dust.dust_check_in(serial_result[4]))
        self.textEdit_2.setText("지금 실외 CO 센서 수치는?     " + str(serial_result[7])
                                + " ppm\n")
        self.textEdit_3.setText("")

    def set_address(self):
        self.hide()
        self.second = set_address.address_set()
        self.second.exec()
        self.show()



if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QtWidgets.QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    sys.exit(app.exec_())
