


import subprocess
import tkinter
import pickle
import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PySide6.QtGui import QIcon


#folder of the files
folder = os.getcwd()
#check cwd is correct
# #print("cwd is " + folder)
file_path = folder + "/main.py"
def update_file_path(new_path):
    global file_path
    file_path = new_path


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DATEND")
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet("background-color: #333333;")
        self.initUI()

    def initUI(self):
        
        btn = QPushButton("Boot up DATEND", self)
        btn.setGeometry(150, 80, 150, 40)
        btn.setStyleSheet("background-color: #555555; color: white;")
        icon = QIcon(folder + "/icon.png")
        self.setWindowIcon(icon)
        btn.clicked.connect(self.run_my_program)

    def run_my_program(self):
        try:
            subprocess.Popen(["python", file_path])
        except Exception as e:
            options = QFileDialog.ReadOnly
            folder_path = QFileDialog.getExistingDirectory(
                self, "Please select the DATEND Supporting Folder", options=options
            )
            if folder_path:
                folder = folder_path
                subprocess.Popen(["python", file_path])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
