# Display Image
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
import sys

class App(object):
	def AppWindow(self, window):
		window.setWindowTitle("Pulp Fiction")
		window.setGeometry(0, 0, 1920, 1080)

		frame1 = QLabel(window)

		frame1File = open('frame1.css', 'r')
		frame1Contents = frame1File.read()
		frame1File.close()

		frame1.setStyleSheet(frame1Contents)
		pixmap = QPixmap("https://raw.githubusercontent.com/datmemerboi/PyQt-Image-Display/master/PF.png").scaledToWidth(900)
		frame1.resize(pixmap.width(), pixmap.height())
		frame1.move(230, 100)
		frame1.setPixmap(pixmap)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ThisWindow = QMainWindow()
	App().AppWindow(ThisWindow)
	ThisWindow.show()
	sys.exit(app.exec_())