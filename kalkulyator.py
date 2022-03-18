
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QPushButton,QRadioButton,QMessageBox,QLineEdit
from PyQt5.QtGui import QFont
import random
import sys
class Tugma(QPushButton):
    def __init__(self,name,ob,x,y):
        super().__init__(name,ob)
        self.setFont(QFont("Times",40))
        self.setGeometry(x,y,100,100)
    def click(self,fun):
        self.clicked.connect(fun)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,500,800)
        self.begin()
    def font(self,ob):
        ob.setFont(QFont("Times",40))
    def begin(self):
        self.ls=[str(i) for i in range(1,16)]
        random.shuffle(self.ls)
        
        self.a1=Tugma("0",self,50,160)
        self.a2=Tugma("*",self,160,160)
        self.a3=Tugma("/",self,270,160)
        self.a4=Tugma("+",self,380,160)
        self.a5=Tugma("1",self,50,270)
        self.a6=Tugma("2",self,160,270)
        self.a7=Tugma("3",self,270,270)
        self.a8=Tugma("-",self,380,270)
        self.a9=Tugma("4",self,50,380)
        self.a10=Tugma("5",self,160,380)
        self.a11=Tugma("6",self,270,380)
        self.a12=Tugma(".",self,380,380)
        self.a13=Tugma("7",self,50,490)
        self.a14=Tugma("8",self,160,490)
        self.a15=Tugma("9",self,270,490)
        self.a16=Tugma("C",self,380,490)
        self.a17=Tugma("=",self,380,600)
        
        self.kiritish = QLineEdit(self)
        self.kiritish.setFont(QFont("Times", 37))
        self.kiritish.move(50, 50)

        self.a1.click(self.A1)
        self.a2.click(self.A2)
        self.a3.click(self.A3)
        self.a4.click(self.A4)
        self.a5.click(self.A5)
        self.a6.click(self.A6)
        self.a7.click(self.A7)
        self.a8.click(self.A8)
        self.a9.click(self.A9)
        self.a10.click(self.A10)
        self.a11.click(self.A11)
        self.a12.click(self.A12)
        self.a13.click(self.A13)
        self.a14.click(self.A14)
        self.a15.click(self.A15)
        self.a16.click(self.A16)
        self.a17.click(self.A17)
    def A1(self):
        self.kiritish.setText(self.kiritish.text()+self.a1.text())
    def A2(self):
        self.kiritish.setText(self.kiritish.text()+self.a2.text())
    def A3(self):
        self.kiritish.setText(self.kiritish.text()+self.a3.text())
    def A4(self):
        self.kiritish.setText(self.kiritish.text()+self.a4.text())
    def A5(self):
        self.kiritish.setText(self.kiritish.text()+self.a5.text())
    def A6(self):
        self.kiritish.setText(self.kiritish.text()+self.a6.text())
    def A7(self):
        self.kiritish.setText(self.kiritish.text()+self.a7.text())
    def A8(self):
        self.kiritish.setText(self.kiritish.text()+self.a8.text())
    def A9(self):
        self.kiritish.setText(self.kiritish.text()+self.a9.text())
    def A10(self):
        self.kiritish.setText(self.kiritish.text()+self.a10.text())
    def A11(self):
        self.kiritish.setText(self.kiritish.text()+self.a11.text())
    def A12(self):
        self.kiritish.setText(self.kiritish.text()+self.a12.text())
    def A13(self):
        self.kiritish.setText(self.kiritish.text()+self.a13.text())
    def A14(self):
        self.kiritish.setText(self.kiritish.text()+self.a14.text())
    def A15(self):
        self.kiritish.setText(self.kiritish.text()+self.a15.text())
    def A17(self):
        try:
            self.f=eval(self.kiritish.text())
            self.f=str(self.f)
            self.kiritish.setText(self.f)
        except:
            self.kiritish.setText("0 ga bolinmaydi")
            self.kiritish.adjustSize()
    def A16(self):
        self.kiritish.setText("")
       








app=QApplication(sys.argv)
oyna=Window()
oyna.show()
sys.exit(app.exec_())

