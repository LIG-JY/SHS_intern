import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
import pandas as pd
import datetime
import GiExpertControl as singleQueryTR
from ui.myUI import Ui_MainWindow
from domain.telegram_bot import TelegramBot
from domain.order_strategy import OrderStrategy

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

        ## UI 설정 및 TR run settings
        self.setWindowTitle("myApp")
        singleQueryTR.SetQtMode(True)
        singleQueryTR.RunIndiPython()
        self.rqidD = {}
        main_ui.setupUi(self)

        # TODO(RUN하면 텔레로 계좌 조회)
        print("hello app!")
        self.view_account()

        # 60초마다 view_trade_history 함수를 호출하는 타이머 생성
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.view_trade_history)
        self.timer.start(60000)  # 60초(60,000 밀리초)마다 타이머 이벤트 발생

        ## debug
        self.order()

        ## TODO: make UI screen
        main_ui.pushButton.clicked.connect(lambda:self.order())
        singleQueryTR.SetCallBack('ReceiveData', self.singleQueryTR_ReceiveData)

    
    ## (계좌조회) 
    # TODO: ui layer, 조회 layer 분리
    def view_account(self):
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
    
    # 비즈니스 로직 : 평단가 낮추기 전략
    def bulkOrder(self):
        # button 입력 받기:
        stock_code = main_ui.lineEdit.text()
        order_quantity = int(main_ui.lineEdit_2.text())
        count = int(main_ui.lineEdit_3.text())
        price_change = int(main_ui.lineEdit_4.text())
        start_price = int(main_ui.lineEdit_5.text())

        # strategy = OrderStrategy(stock_code, order_quantity, count, price_change, start_price) -> DTO
        print(stock_code)
        print(order_quantity)
        print(count)
        print(price_change)
        print(start_price)

        print(type(stock_code))
        print(type(order_quantity)) #int
        print(type(count)) #int
        print(type(price_change)) #int
        print(type(start_price)) #int

        temp = start_price
        for i in range(count):
            self.order()
            # self.order(stock_code, str(order_quantity), str(temp))  # 지정가 변화 호출
            temp -= int(price_change)
    

    # 주문하기
    def order(self, code="A005930", quantity="1", price=""): 
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
        ret = singleQueryTR.SetSingleData(8,code) #종목코드 저장된 클래스 불러오기
        ret = singleQueryTR.SetSingleData(9,quantity) #주문 수량 저장된 클래스에서 불러오기
        ret = singleQueryTR.SetSingleData(10,price) #주문 가격 저장된 클래스에서 불러오기 (시간 외 종가면 0)
        ret = singleQueryTR.SetSingleData(11, "1") #정규시간외구분코드
        ret = singleQueryTR.SetSingleData(12,"1") #호가유형코드 (기능 추가 최우선)  1. 시장가 2. 지정가 X.최유리
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
    
    ## 체결 내역 조회
    def view_trade_history(self):
        TR_Name = "SABA231Q1"             
        ret = singleQueryTR.SetQueryName(TR_Name)          
        # print(singleQueryTR.GetErrorCode())
        # print(singleQueryTR.GetErrorMessage())
        ret = singleQueryTR.SetSingleData(0,self.get_today_date_string()) #매매일자 #TODO(날짜를 받아오기)
        ret = singleQueryTR.SetSingleData(1,self.account_code_text) #계좌번호
        ret = singleQueryTR.SetSingleData(2,self.pw_text) #비밀번호
        ret = singleQueryTR.SetSingleData(3,"00") #장구분
        ret = singleQueryTR.SetSingleData(4,"0") #체결구분 : 0은 미체결/체결 구분없이 조회
        ret = singleQueryTR.SetSingleData(5,"1") #건별구분
        ret = singleQueryTR.SetSingleData(6,"*") #입력종목코드 : * 전체
        ret = singleQueryTR.SetSingleData(7,"") #계계좌상품코드 : 공백은 전체계좌
        ret = singleQueryTR.SetSingleData(8,"Y") #작업구분
        rqid = singleQueryTR.RequestData()
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid))
        self.rqidD[rqid] = TR_Name    

    ## output 처리
    def singleQueryTR_ReceiveData(self, giCtrl, rqid):
        print("in receive_Data:", rqid)
        print('recv rqid: {}->{}\n'.format(rqid, self.rqidD[rqid]))
        TR_Name = self.rqidD[rqid]

        if TR_Name == "SABA200QB":
            self.process_SABA200QB(giCtrl)
        elif TR_Name == "SABA101U1":
            self.process_SABA101U1(giCtrl)
        elif TR_Name == "SABA231Q1":
            self.process_SABA231Q1(giCtrl)
            
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
            msg = ""  # 메세지 내용 DATA put 가공
            msg += ("주문번호 : " + DATA["Order_Num"] + "\n")
            msg += DATA["Msg1"] + "\n"
            msg += DATA["Msg2"]
            self.bot.sendMessage(msg)
        except Exception as e:
            error_message = "에러 발생"
            print(error_message)

            # TODO: 에러 메시지를 텔레그램으로 전송
            self.bot.sendMessage(error_message)
    
    ## 현물 체결/미체결 조회 output
    def process_SABA231Q1(self, giCtrl):
        try:
            nCnt = giCtrl.GetMultiRowCount()
            tr_data_output = []
            
            for i in range(nCnt):
                item_data = []
                
                ## 0(주문번호) 9(호가 유형 구분) 14(종목명) 24(체결수량) 25(체결단가)
                item_data.append(f"주문번호 : {giCtrl.GetMultiData(i, 0)}\n")
                item_data.append(f"호가 유형 구분 : {giCtrl.GetMultiData(i, 9)}\n")
                item_data.append(f"종목명 : {giCtrl.GetMultiData(i, 14)}\n")
                item_data.append(f"주문수량 : {giCtrl.GetMultiData(i, 15)}\n")
                item_data.append(f"주문단가 : {giCtrl.GetMultiData(i, 16)}\n")
                item_data.append(f"체결수량 : {giCtrl.GetMultiData(i, 24)}\n")
                item_data.append(f"체결단가 : {giCtrl.GetMultiData(i, 25)}\n")
                
                tr_data_output.append(''.join(item_data))
                separator = "\n" + "-" * 30 + "\n"
                if (i != nCnt - 1):
                    tr_data_output.append(separator)

            self.bot.sendMessage(''.join(tr_data_output))
            self.bot.send_message_with_time("체결 결과를 조회했습니다.\n")
        except Exception as e:
            error_message = "에러 발생"
            print(error_message)

            # TODO: 에러 메시지를 텔레그램으로 전송
            self.bot.sendMessage(error_message)
    
    ## UTILITY
    def get_today_date_string(self):
        today = datetime.date.today()
        date_string = today.strftime("%Y%m%d")
        print(date_string) # debug
        return date_string
      


    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    IndiWindow = indiWindow()    
    IndiWindow.show()
    app.exec_()