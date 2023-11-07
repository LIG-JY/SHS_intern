# ## TODO: 조회 DEBUG PRINT문      
    # def singleQueryTR_ReceiveData(self,giCtrl,rqid):
    #     print("in receive_Data:",rqid)
    #     print('recv rqid: {}->{}\n'.format(rqid, self.rqidD[rqid]))
    #     TR_Name = self.rqidD[rqid]
    #     tr_data_output = []
    #     output = []

    #     print("TR_name : ",TR_Name)
    #     if TR_Name == "SABA200QB":
    #         nCnt = giCtrl.GetMultiRowCount()
    #         column_names = ["종목코드",
    #                         "종목명",
    #                         "결제일 잔고 수량",
    #                         "매도 미체결수량",
    #                         "매수 미체결수량",
    #                         "현재가",
    #                         "평균단가" ]
    #         temp = []
    #         for i in range(0, nCnt):
    #             temp.append([])
    #             main_ui.tableWidget.setItem(i,0,QTableWidgetItem(str(giCtrl.GetMultiData(i, 0))))
    #             main_ui.tableWidget.setItem(i,1,QTableWidgetItem(str(giCtrl.GetMultiData(i, 1))))
    #             main_ui.tableWidget.setItem(i,2,QTableWidgetItem(str(giCtrl.GetMultiData(i, 2))))
    #             main_ui.tableWidget.setItem(i,3,QTableWidgetItem(str(giCtrl.GetMultiData(i, 5))))
    #             main_ui.tableWidget.setItem(i,4,QTableWidgetItem(str(giCtrl.GetMultiData(i, 6))))
    #             for j in range(0,7):
    #                 temp[i].append(column_names[j] + " : " +  giCtrl.GetMultiData(i, j) + "\n")
    #             tr_data_output.append(''.join([str(item) for item in temp[i]]))
    #             # print("\n")
    #         # COLUMN : 0 종목코드, 1 종목명, 2 결제일 잔고 수량, 3 매도 미체결수량 4. 매수미체결수량 5. 현재가 6. 평균단가.
            
    #         self.bot.sendMessage(''.join([str(item) for item in tr_data_output]))
    #         self.bot.send_message_with_time("계좌를 조회했습니다.\n")
    #         return
    #     if TR_Name == "SABA101U1":
    #         DATA = {}
    #         DATA['Order_Num'] = giCtrl.GetSingleData(0)  # 주문번호
    #         DATA['Num'] = giCtrl.GetSingleData(2)  # 메시지 구분
    #         DATA['Msg1'] = giCtrl.GetSingleData(3)  # 메시지1
    #         DATA['Msg2'] = giCtrl.GetSingleData(4)  # 메시지2
    #         DATA['Msg3'] = giCtrl.GetSingleData(5)  # 메시지3
    #         print("매수 및 매도 주문결과 :", DATA)

    #         ## todo 텔레그램으로 쏘기
    #         msg = "안녕" ## 메세지 내용 DATA put
    #         self.bot.sendMessage(msg)
    #         return