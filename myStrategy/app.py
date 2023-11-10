import sys
from PyQt5.QtWidgets import QApplication
from service.order_service import indiWindow
      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    IndiWindow = indiWindow()    
    IndiWindow.show()
    app.exec_()