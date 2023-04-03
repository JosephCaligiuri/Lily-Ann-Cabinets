import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(Qt.WindowFullscreen)
        
        label = QLabel("Hello, World!", self)
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(0, 0, self.width(), self.height())
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())