from PySide6 import QtWidgets, QtCore

class Page2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the page layout
        layout = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel("Page 2")
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label)
        button = QtWidgets.QPushButton("Go to Page 1", self)
        layout.addWidget(button)

        # Connect the button to the page change
        button.clicked.connect(parent.show_page1)
