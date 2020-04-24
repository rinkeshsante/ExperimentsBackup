from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def window():
	app = QApplication(sys.argv)
	win = QMainWindow()
	win.setGeometry(400,200 , 900 ,400)
	win.setWindowTitle("hello there")

	label = QtWidgets.QLabel(win)
	label.setText("Fire")
	label.move(50,50)

	win.show()
	sys.exit(app.exec_())

window()