from PyQt5.QtWidgets import *
from PyQt5 import uic

from address import find_address

form_set_wifi = uic.loadUiType("address_ui.ui")[0]
whole_address_all = ["서울", "경기", "인천", "강원", "충남","대전", "충북", "부산", "울산",
                     "대구", "경북", "경남", "전남", "광주", "전북", "제주", "세종"]
eng = ["seoul", "gyeonggi","Incheon", "gangwon","chungnam","daejeon","chungbuk",
       "busan","ulsan","daegu","gyeongbuk","gyeongnam","jeonnam",
       "gwangju","jeonbuk","jeju","sejong"]
class address_set(QDialog, QWidget, form_set_wifi):
    def __init__(self):             #버튼 연결
        super(address_set,self).__init__()
        self.initUi2()
        self.comboBox_2.activated[str].connect(self.set_detail)
        self.pushButton.clicked.connect(self.save_address)
        self.show()
    def initUi2(self): # 시도가 콤보박스에 나열됨
        self.setupUi(self)
        for whole_address in whole_address_all:
            self.comboBox_2.addItem(whole_address)

    def set_detail(self):   # 시도에 맞는 측정소가 콤보박스에 나열됨
        self.comboBox.clear()
        selected_address = self.comboBox_2.currentIndex()
        for detail in find_address(eng[selected_address]):
            self.comboBox.addItem(detail.strip())

    def save_address(self):        # address.txt 파일에 저장.
        addr = self.comboBox_2.currentText()
        det_addr = self.comboBox.currentText()
        text_file = open("address.txt", "w", encoding="utf-8")
        text_file.write(addr + "\n")
        text_file.write(det_addr)
        self.close()