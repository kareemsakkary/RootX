from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import pyqtgraph as pg

from mainwindow import Ui_MainWindow

class main(QMainWindow ,Ui_MainWindow):
    def calc(self) : 
        if "" not in [self.Fun.text(),self.Count.text(),self.inc.text(),self.Start.text]:
            function = str(self.Fun.text())
            start= float(self.Start.text())
            increment = float(self.inc.text())
            num = int(self.Count.text())
            x=start
            Xs=[]
            Ys=[]
            self.tableWidget.setColumnCount(num)
            for i in range(0,num):
                s=str("("+str(x)+")")
                newFunction=function.replace("x",s)
                y=eval(newFunction)
                Xitem =QTableWidgetItem(str(x))
                Xitem.setTextAlignment(Qt.AlignCenter)
                Xitem.setFlags(Qt.ItemIsEnabled)

                Yitem =QTableWidgetItem(str(y))
                Yitem.setTextAlignment(Qt.AlignCenter)
                Yitem.setFlags(Qt.ItemIsEnabled)

                Xs.append(x)
                Ys.append(y)
                self.tableWidget.setItem(0,i,Xitem)
                self.tableWidget.setItem(1,i,Yitem)
                x+=increment
            pg.plot(Xs,Ys)
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calc)
    
app= QApplication(sys.argv)
window = main()
window.show()
app.exec_()
