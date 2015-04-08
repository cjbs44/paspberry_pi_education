import sys
from PySide.QtGui import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()

        self.setWindowTitle('Window Events')

        self.label = QLabel('Read Me', self)

        button = QPushButton('Push Me', self)
        button.clicked.connect(self.buttonClicked)

        layout = QVBoxLayout(self)
        layout.addWidget(button)
        layout.addWidget(self.label)

        self.setMouseTracking(True)

    def buttonClicked(self):
        """ Update the text when the button is clicked """
        self.label.setText("Clicked")

    def mouseMoveEvent(self, event):
        """
        Update the text when the (tracked) mouse moves our MyWindow
        """
        self.label.setText(str(event.x()) + "," + str(event.y()))

application = QApplication(sys.argv)
widget = MyWindow()
widget.show()
application.exec_()
