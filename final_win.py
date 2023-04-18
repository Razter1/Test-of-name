From PyQt5.QtCore import Qt
From PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRedioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
ciass finalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.inituI()
        self.set_appear()
        self.show()
    def inituI(self):
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
