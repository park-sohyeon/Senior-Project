import sys
import serial1
import main
import dust

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow
from pympler import muppy
all_objects=muppy.get_objects()

from rain import rain_check

form_class = uic.loadUiType("main.window.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fontSize = 10

        # 버튼에 기능을 연결하는 코드
        self.weather_button.clicked.connect(self.set_weather_dust)
        self.weather_button_2.clicked.connect(self.set_weather_rain)
        self.weather_button_3.clicked.connect(self.set_weather_th)
        # self.weather_button_4.clicked.connect(self.set_weather_window)

    # 미세먼지 버튼 클릭 시 출력
    def set_weather_dust(self):
        serial_result = serial1.serial_check()
        print(serial_result)
        self.textEdit.setText("실내 온도           :     " + str(serial_result[0]) + " ºC \n" + "실내 습도           :     " + str(serial_result[1]) + "  % \n" + "실내 미세먼지     :    " + dust.dust_check_in(serial_result[2]))
        self.textEdit_2.setText("지금 실외 미세먼지 수치는?     " + str(serial_result[3]) + " ㎍/㎥\n" + dust.dust_check_out(serial_result[3]))
        self.textEdit_3.setText("지금 실내 미세먼지 수치는?     " + str(serial_result[2]) + " ㎍/㎥\n" + dust.dust_check_in(serial_result[2]))

    # 강수량 버튼 클릭 시 출력
    def set_weather_rain(self):
        serial_result = serial1.serial_check()
        print(serial_result)
        self.textEdit.setText("실내 온도           :     " + str(serial_result[0]) + " ºC \n" + "실내 습도           :     " + str(serial_result[1]) + "  % \n" + "실내 미세먼지     :    " + dust.dust_check_in(serial_result[2]))
        self.set_weather_rain_text()
    def set_weather_rain_text(self):
        result = rain_check()
        self.textEdit_2.setText("지금 실외 강수량 수치는?     \n" + result["강수량"] + " mm")
        self.textEdit_3.setText("지금 실외 강수형태는?     \n" + result["형태"])


    # 온습도 버튼 클릭 시 출력
    def set_weather_th(self):
        serial_result = serial1.serial_check()
        self.textEdit.setText("실내 온도           :     " + str(serial_result[0]) + " ºC \n" + "실내 습도           :     " + str(serial_result[1]) + "  % \n" + "실내 미세먼지     :    " + dust.dust_check_in(serial_result[2]))
        self.set_weather_th_text()
        self.set_weather_th_text2()
    def set_weather_th_text(self):
        result = rain_check()
        self.textEdit_2.setText("지금 실외 온도 수치는?     " + result["기온"] + " ºC\n" + "지금 실외 습도 수치는?     " + result["습도"] + " %")

    def set_weather_th_text2(self):
        serial_result = serial1.serial_check()
        self.textEdit_3.setText("지금 실내 온도 수치는?     " + str(serial_result[0])+ " ºC\n" + "지금 실내 습도 수치는?     " + str(serial_result[1])+ " %")


    # # 창문/팬 버튼 클릭 시 출력
    # def set_weather_window(self):
    #     serial_result = serial1.serial_check()
    #     self.textEdit.setText("실내 온도           :     "+ str(123) + " ºC \n" + "실내 습도           :     " + str(36) + "  % \n" + "실내 미세먼지     :    " + "매우 나쁨 \n")
    #     self.set_weather_window_text()
    #     self.set_weather_window_text2()
    # def set_weather_window_text(self):
    #     self.textEdit_2.setText("지금 창문 개폐 여부는?     \n" + "닫힘")
    #
    # def set_weather_window_text2(self):
    #     self.textEdit_3.setText("지금 팬 작동 여부는?     \n" + "작동")




if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QtWidgets.QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    sys.exit(app.exec_())