# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kalkulator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser


class Ui_MainWindow(object):
    liczba = list()
    num1 = float(0)
    num2 = float(0)
    oper = str("")
    isnum1set = bool(True)

    def addnum(self, num):
        self.liczba.append(str(num))
        self.display.setText("".join(self.liczba))

    def clearnum(self):
        self.liczba = []
        self.num1 = 0
        self.num2 = 0
        self.isnum1set = False
        self.display.setText("")

    def nhentai(self):
        hentaiid = "".join(self.liczba)
        if hentaiid != "":
            webbrowser.open(f"http://nhentai.net/g/{hentaiid}/")
        else:
            webbrowser.open("http://nhentai.net/")

    def operator(self, op):
        if "".join(self.liczba) != "":
            self.num1 = float("".join(self.liczba))
            self.isnum1set = True
            self.liczba = []
        self.oper = op

    def calculate(self):
        if not self.isnum1set and "".join(self.liczba) == "58008":
            self.random.show()
        else:
            if "".join(self.liczba) != "":
                # bierze druga cyfra zamiast dispaly
                self.num2 = float("".join(self.liczba))
                if self.oper == "+":
                    self.num1 = self.num1 + self.num2
                    self.display.setText(str(self.num1))
                elif self.oper == "-":
                    self.num1 = self.num1 - self.num2
                    self.display.setText(str(self.num1))

    def setupUi(self, MainWindow):
        # ------------------window settings------------------
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(272, 508)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("../../_shit/sus.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        MainWindow.setWindowIcon(icon)
        self.kalkulator = QtWidgets.QWidget(MainWindow)
        self.kalkulator.setObjectName("kalkulator")
        self.dodaj = QtWidgets.QPushButton(self.kalkulator)
        self.dodaj.setGeometry(QtCore.QRect(200, 380, 51, 51))
        self.dodaj.setObjectName("dodaj")
        self.odjac = QtWidgets.QPushButton(self.kalkulator)
        self.odjac.setGeometry(QtCore.QRect(200, 320, 51, 51))
        self.odjac.setObjectName("odjac")
        self.razy = QtWidgets.QPushButton(self.kalkulator)
        self.razy.setGeometry(QtCore.QRect(200, 260, 51, 51))
        self.razy.setObjectName("razy")
        self.podziel = QtWidgets.QPushButton(self.kalkulator)
        self.podziel.setGeometry(QtCore.QRect(200, 200, 51, 51))
        self.podziel.setObjectName("podziel")
        self.display = QtWidgets.QTextBrowser(self.kalkulator)
        self.display.setGeometry(QtCore.QRect(20, 20, 231, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.display.setFont(font)
        self.display.setAcceptDrops(False)
        self.display.setObjectName("display")
        self.rownasie = QtWidgets.QPushButton(self.kalkulator)
        self.rownasie.setGeometry(QtCore.QRect(200, 440, 51, 51))
        self.rownasie.setObjectName("rownasie")
        self.trzy = QtWidgets.QPushButton(self.kalkulator)
        self.trzy.setGeometry(QtCore.QRect(140, 380, 51, 51))
        self.trzy.setObjectName("trzy")
        self.dwa = QtWidgets.QPushButton(self.kalkulator)
        self.dwa.setGeometry(QtCore.QRect(80, 380, 51, 51))
        self.dwa.setObjectName("dwa")
        self.jeden = QtWidgets.QPushButton(self.kalkulator)
        self.jeden.setGeometry(QtCore.QRect(20, 380, 51, 51))
        self.jeden.setObjectName("jeden")
        self.szesc = QtWidgets.QPushButton(self.kalkulator)
        self.szesc.setGeometry(QtCore.QRect(140, 320, 51, 51))
        self.szesc.setObjectName("szesc")
        self.piec = QtWidgets.QPushButton(self.kalkulator)
        self.piec.setGeometry(QtCore.QRect(80, 320, 51, 51))
        self.piec.setObjectName("piec")
        self.cztery = QtWidgets.QPushButton(self.kalkulator)
        self.cztery.setGeometry(QtCore.QRect(20, 320, 51, 51))
        self.cztery.setObjectName("cztery")
        self.dziewiec = QtWidgets.QPushButton(self.kalkulator)
        self.dziewiec.setGeometry(QtCore.QRect(140, 260, 51, 51))
        self.dziewiec.setObjectName("dziewiec")
        self.osiem = QtWidgets.QPushButton(self.kalkulator)
        self.osiem.setGeometry(QtCore.QRect(80, 260, 51, 51))
        self.osiem.setObjectName("osiem")
        self.siedem = QtWidgets.QPushButton(self.kalkulator)
        self.siedem.setGeometry(QtCore.QRect(20, 260, 51, 51))
        self.siedem.setObjectName("siedem")
        self.zero = QtWidgets.QPushButton(self.kalkulator)
        self.zero.setGeometry(QtCore.QRect(80, 440, 51, 51))
        self.zero.setObjectName("zero")
        self.przecinek = QtWidgets.QPushButton(self.kalkulator)
        self.przecinek.setGeometry(QtCore.QRect(140, 440, 51, 51))
        self.przecinek.setObjectName("przecinek")
        self.silnia = QtWidgets.QToolButton(self.kalkulator)
        self.silnia.setGeometry(QtCore.QRect(140, 200, 51, 51))
        self.silnia.setObjectName("silnia")
        self.pierwiastek = QtWidgets.QPushButton(self.kalkulator)
        self.pierwiastek.setGeometry(QtCore.QRect(80, 200, 51, 51))
        self.pierwiastek.setObjectName("pierwiastek")
        self.potega = QtWidgets.QPushButton(self.kalkulator)
        self.potega.setGeometry(QtCore.QRect(20, 200, 51, 51))
        self.potega.setObjectName("potega")
        self.pierwiastek_2 = QtWidgets.QPushButton(self.kalkulator)
        self.pierwiastek_2.setGeometry(QtCore.QRect(20, 440, 51, 51))
        self.pierwiastek_2.setObjectName("pierwiastek_2")
        self.clear = QtWidgets.QPushButton(self.kalkulator)
        self.clear.setGeometry(QtCore.QRect(140, 140, 111, 51))
        self.clear.setObjectName("clear")
        self.random = QtWidgets.QPushButton(self.kalkulator)
        self.random.setGeometry(QtCore.QRect(20, 140, 111, 51))
        self.random.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("../../_shit/weirdn.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On
        )
        self.random.setIcon(icon1)
        self.random.setIconSize(QtCore.QSize(111, 51))
        self.random.setObjectName("random")
        self.random.hide()
        MainWindow.setCentralWidget(self.kalkulator)

        # ------------------buttons------------------
        self.zero.clicked.connect(lambda: self.addnum(0))
        self.jeden.clicked.connect(lambda: self.addnum(1))
        self.dwa.clicked.connect(lambda: self.addnum(2))
        self.trzy.clicked.connect(lambda: self.addnum(3))
        self.cztery.clicked.connect(lambda: self.addnum(4))
        self.piec.clicked.connect(lambda: self.addnum(5))
        self.szesc.clicked.connect(lambda: self.addnum(6))
        self.siedem.clicked.connect(lambda: self.addnum(7))
        self.osiem.clicked.connect(lambda: self.addnum(8))
        self.dziewiec.clicked.connect(lambda: self.addnum(9))
        self.clear.clicked.connect(self.clearnum)
        self.random.clicked.connect(self.nhentai)
        self.dodaj.clicked.connect(lambda: self.operator("+"))
        self.odjac.clicked.connect(lambda: self.operator("-"))
        self.razy.clicked.connect(lambda: self.operator("*"))
        self.podziel.clicked.connect(lambda: self.operator("/"))
        self.rownasie.clicked.connect(self.calculate)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kalkulator"))
        self.dodaj.setText(_translate("MainWindow", "+"))
        self.odjac.setText(_translate("MainWindow", "-"))
        self.razy.setText(_translate("MainWindow", "*"))
        self.podziel.setText(_translate("MainWindow", "/"))
        self.display.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.rownasie.setText(_translate("MainWindow", "="))
        self.trzy.setText(_translate("MainWindow", "3"))
        self.dwa.setText(_translate("MainWindow", "2"))
        self.jeden.setText(_translate("MainWindow", "1"))
        self.szesc.setText(_translate("MainWindow", "6"))
        self.piec.setText(_translate("MainWindow", "5"))
        self.cztery.setText(_translate("MainWindow", "4"))
        self.dziewiec.setText(_translate("MainWindow", "9"))
        self.osiem.setText(_translate("MainWindow", "8"))
        self.siedem.setText(_translate("MainWindow", "7"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.przecinek.setText(_translate("MainWindow", ","))
        self.silnia.setText(_translate("MainWindow", "n!"))
        self.pierwiastek.setText(_translate("MainWindow", "√"))
        self.potega.setText(_translate("MainWindow", "x^2"))
        self.pierwiastek_2.setText(_translate("MainWindow", "+/-"))
        self.clear.setText(_translate("MainWindow", "CLEAR"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
