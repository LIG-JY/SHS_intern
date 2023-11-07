import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
import pandas as pd
import GiExpertControl as giJongmokTRShow

class indiWindow():
    # UI 선언
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IndiExample")
        giJongmokTRShow.SetQtMode(True)
        giJongmokTRShow.RunIndiPython()
        self.rqidD = {}

        # 인디의 TR을 처리할 변수를 생성합니다.
        #self.IndiTR = QAxWidget("GIEXPERTCONTROL64.GiExpertControl64Ctrl.1")
        self.IndiTR = QAxWidget("GIEXPERTCONTROL.GiExpertControlCtrl.1")

        giJongmokTRShow.SetCallBack('ReceiveData', self.giJongmokTRShow_ReceiveData)
        
    def balance_inquery(self): # 버튼 클릭 시 TR요청. 잔고를 조회합니다.
        account_code_text = "27048031572" # 계좌번호 
        pw_text = "0000" # 비밀번호
        TR_Name = "SABA200QB"          
        ret = giJongmokTRShow.SetQueryName(TR_Name)
        # print(ret)
        # print(giJongmokTRShow.GetErrorCode())
        # print(giJongmokTRShow.GetErrorMessage())
        ret = giJongmokTRShow.SetSingleData(0,account_code_text)
        ret = giJongmokTRShow.SetSingleData(1,"01")
        ret = giJongmokTRShow.SetSingleData(2,pw_text)
        rqid = giJongmokTRShow.RequestData()
        print(type(rqid))
        print('Request Data rqid: ' + str(rqid)) # 0은 실패, ID는 성공
        self.rqidD[rqid] = TR_Name
        return rqid
        
    def giJongmokTRShow_ReceiveData(self,giCtrl,rqid):
        print("in receive_Data:",rqid)
        print('recv rqid: {}->{}\n'.format(rqid, self.rqidD[rqid]))
        TR_Name = self.rqidD[rqid]
        tr_data_output = []
        output = []

        print("TR_name : ",TR_Name)
        if TR_Name == "SABA200QB":
            nCnt = giCtrl.GetMultiRowCount()
            print("c")
            for i in range(0, nCnt):
                tr_data_output.append([])
                for j in range(0,5):
                    tr_data_output[i].append(giCtrl.GetMultiData(i, j))
            print(type(tr_data_output))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.exec_()