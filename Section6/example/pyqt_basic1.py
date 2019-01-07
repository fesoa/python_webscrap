import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv) #sys.argv: 현재 경로

label = QLabel("PyQT First Test!")
label.show()

print("Before Loop")
app.exec_()
print("After Loop")
