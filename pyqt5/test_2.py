from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys


class MyWin(QMainWindow):
	# calling parent contructor
	def __init__(self):
		super(MyWin,self).__init__()
		self.setGeometry(400,200 , 900 ,400)
		self.setWindowTitle("hello there")
		self.initUI()

	def initUI(self):
		self.label = QtWidgets.QLabel(self)
		self.label.setText("Fire")
		self.label.move(400,20)

		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("submit")
		self.b1.move(770,350)
		self.b1.clicked.connect(self.clicked)

	def clicked(self):
		self.label.setText("pressed the b1")
		self.update()

	def update(self):
		self.label.adjustSize()

def clicked():
	print('click')

def window():
	app = QApplication(sys.argv)
	win = MyWin()
	
	win.show()
	sys.exit(app.exec_())

window()