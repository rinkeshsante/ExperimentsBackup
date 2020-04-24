# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 566)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(700, 480, 93, 28))
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(570, 480, 93, 28))
        self.b2.setObjectName("b2")
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(320, 140, 91, 41))
        self.l1.setObjectName("l1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 26))
        self.menubar.setObjectName("menubar")
        self.menuhello_there = QtWidgets.QMenu(self.menubar)
        self.menuhello_there.setObjectName("menuhello_there")
        self.menudefault = QtWidgets.QMenu(self.menubar)
        self.menudefault.setObjectName("menudefault")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionsave_as = QtWidgets.QAction(MainWindow)
        self.actionsave_as.setObjectName("actionsave_as")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionset_size = QtWidgets.QAction(MainWindow)
        self.actionset_size.setObjectName("actionset_size")
        self.actionask_q = QtWidgets.QAction(MainWindow)
        self.actionask_q.setObjectName("actionask_q")
        self.menuhello_there.addAction(self.actionsave)
        self.menuhello_there.addAction(self.actionsave_as)
        self.menuhello_there.addSeparator()
        self.menuhello_there.addAction(self.actionexit)
        self.menudefault.addAction(self.actionset_size)
        self.menudefault.addSeparator()
        self.menudefault.addAction(self.actionask_q)
        self.menubar.addAction(self.menuhello_there.menuAction())
        self.menubar.addAction(self.menudefault.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b1.setText(_translate("MainWindow", "sign in"))
        self.b2.setText(_translate("MainWindow", "sign up"))
        self.l1.setText(_translate("MainWindow", "hello there"))
        self.menuhello_there.setTitle(_translate("MainWindow", "file"))
        self.menudefault.setTitle(_translate("MainWindow", "default"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave_as.setText(_translate("MainWindow", "save as"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionset_size.setText(_translate("MainWindow", "set size"))
        self.actionask_q.setText(_translate("MainWindow", "ask q"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
