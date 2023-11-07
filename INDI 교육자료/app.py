import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
import pandas as pd
import GiExpertControl as singleQueryTR
from TestUI import Ui_MainWindow
from telegramBot import TelegramBot

main_ui = Ui_MainWindow()

class indiWindow(QMainWindow):
    # UI 선언
    def __init__(self):
        super().__init__()

        ## 계좌설정
        self.account_code_text = "27048031572"
        self.pw_text = "0000"

        ## 텔레봇 멤버변수
        self.bot = TelegramBot()

        ## debug
        print("계좌번호는 잘 나오나요?")
        print(self.account_code_text)

        self.setWindowTitle("IndiExample")
        singleQueryTR.SetQtMode(True)
        singleQueryTR.RunIndiPython()
        self.rqidD = {}
        main_ui.setupUi(self)

        ## debug
        print("주문하냐??")
        self.order()
        print("주문됬냐??")  

        ## TODO: make UI screen
        main_ui.pushButton.clicked.connect(self.pushButton_clicked)
        # main_ui.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        # main_ui.pushButton_3.clicked.connect(self.pushButton_3_clicked)
        singleQueryTR.SetCallBack('ReceiveData', self.singleQueryTR_ReceiveData)

    def tr_data_output_to_string(tr_data_output):
        result = ""
        for row in tr_data_output:
            result += ", ".join(map(str, row)) + "\n"
        return result    

    ## TODO: change method name
    def pushButton_clicked(self):
        TR_Name = "SABA200QB"             
        ret = singleQueryTR.SetQueryName(TR_Name)          
        # print(singleQueryTR.GetErrorCode())
        # print(singleQueryTR.GetErrorMessage())
        ret = singleQueryTR.SetSingleData(0,self.account_code_text)
        ret = singleQueryTR.SetSingleData(1,"01")
        ret = singleQueryTR.SetSingleData(2,self.pw_text)
        rqid = singleQueryTR.RequestData()
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name    

    def singleQueryTR_ReceiveData(self, giCtrl, rqid):
        print("in receive_Data:", rqid)
        print('recv rqid: {}->{}\n'.format(rqid, self.rqidD[rqid]))
        TR_Name = self.rqidD[rqid]

        if TR_Name == "SABA200QB":
            self.process_SABA200QB(giCtrl)
        elif TR_Name == "SABA101U1":
            self.process_SABA101U1(giCtrl)
            
    def process_SABA200QB(self, giCtrl):
        column_names = [
            "종목코드",
            "종목명",
            "결제일 잔고 수량",
            "매도 미체결수량",
            "매수 미체결수량",
            "현재가",
            "평균단가"
        ]
        tr_data_output = []

        nCnt = giCtrl.GetMultiRowCount()
        for i in range(nCnt):
            item_data = []
            for j in range(7):
                item_data.append(f"{column_names[j]} : {giCtrl.GetMultiData(i, j)}\n")
            
            tr_data_output.append(''.join(item_data))
            separator = "\n" + "-" * 30 + "\n"
            if (i != nCnt - 1):
                tr_data_output.append(separator)

            # Update the table widget
            for j in range(5):
                main_ui.tableWidget.setItem(i, j, QTableWidgetItem(str(giCtrl.GetMultiData(i, j))))
        
        self.bot.sendMessage(''.join(tr_data_output))
        
        self.bot.send_message_with_time("계좌를 조회했습니다.\n")

    def process_SABA101U1(self, giCtrl):
        try:
            DATA = {
                'Order_Num': giCtrl.GetSingleData(0),  # 주문번호
                'Num': giCtrl.GetSingleData(2),  # 메시지 구분
                'Msg1': giCtrl.GetSingleData(3),  # 메시지1
                'Msg2': giCtrl.GetSingleData(4),  # 메시지2
                'Msg3': giCtrl.GetSingleData(5)  # 메시지3
            }
            print("매수 및 매도 주문결과:", DATA)

            # TODO: 텔레그램으로 메시지 전송
            msg = "안녕"  # 메세지 내용 DATA put 가공
            self.bot.sendMessage(msg)
        except Exception as e:
            error_message = "에러 발생"
            print(error_message)

            # TODO: 에러 메시지를 텔레그램으로 전송
            self.bot.sendMessage(error_message)
    
    def order(self): # 주문구현
        print("주문 시도!")
        TR_Name = "SABA101U1" # 매도/매수 XTR        
        ret = singleQueryTR.SetQueryName(TR_Name)          
        # print(singleQueryTR.GetErrorCode())
        # print(singleQueryTR.GetErrorMessage())
        ret = singleQueryTR.SetSingleData(0,self.account_code_text) #계좌번호
        ret = singleQueryTR.SetSingleData(1,"01")  #계좌상품
        ret = singleQueryTR.SetSingleData(2,self.pw_text) #계좌비번
        ret = singleQueryTR.SetSingleData(3,"") 
        ret = singleQueryTR.SetSingleData(4,"") 
        ret = singleQueryTR.SetSingleData(5,"0") #선물대용매도여부
        ret = singleQueryTR.SetSingleData(6,"00") #신용거래구분
        ret = singleQueryTR.SetSingleData(7,"2") #매도/매수 구분 : 매수
        ret = singleQueryTR.SetSingleData(8,"A005930") #종목코드 저장된 클래스 불러오기
        ret = singleQueryTR.SetSingleData(9,"3") #주문 수량 저장된 클래스에서 불러오기
        ret = singleQueryTR.SetSingleData(10,"") #주문 가격 저장된 클래스에서 불러오기 (시간 외 종가면 0)
        ret = singleQueryTR.SetSingleData(11, "1") #정규시간외구분코드
        ret = singleQueryTR.SetSingleData(12,"1") #호가유형코드 (기능 추가 최우선)
        ret = singleQueryTR.SetSingleData(13,"0") #주문조건코드
        ret = singleQueryTR.SetSingleData(14,"0") #신용대출통합주문구분코드
        ret = singleQueryTR.SetSingleData(15,"") #신용대출일자
        ret = singleQueryTR.SetSingleData(16,"") #원주문번호
        ret = singleQueryTR.SetSingleData(17,"") 
        ret = singleQueryTR.SetSingleData(18,"")
        ret = singleQueryTR.SetSingleData(19,"")
        ret = singleQueryTR.SetSingleData(20,"") #프로그램매매여부
        ret = singleQueryTR.SetSingleData(21,"Y") #결과메시지 처리여부
        rqid = singleQueryTR.RequestData()
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name

    def orderTR_ReceiveSysMsg(self, MsgID):
        print("System Message Received = ", MsgID)

    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    IndiWindow = indiWindow()    
    IndiWindow.show()
    app.exec_()