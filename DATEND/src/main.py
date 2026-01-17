import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QWidget, QSizePolicy
from PySide6 import QtGui
from stage_files import stageWindow
from configuresettings import ConfigureSettings
import os
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("D A T E N D")
        self.setGeometry(100, 100, 500, 380)
        self.setStyleSheet("background-color: #333333;")
        current_directory = os.path.dirname(os.path.abspath(__file__))
        font_folder_path = os.path.join(current_directory, "font")
        font_path_eot = os.path.join(font_folder_path, "IncompleetaRegular.eot")
        font_path_woff = os.path.join(font_folder_path, "IncompleetaRegular.woff")
        font_path_woff2 = os.path.join(font_folder_path, "IncompleetaRegular.woff2")
        font_id_eot = QFontDatabase.addApplicationFont(font_path_eot)
        print("Font ID EOT:", font_id_eot)
        font_id_woff = QFontDatabase.addApplicationFont(font_path_woff)
        print("Font ID WOFF:", font_id_woff)
        font_id_woff2 = QFontDatabase.addApplicationFont(font_path_woff2)
        print("Font ID WOFF2:", font_id_woff2)
        loaded_font_families = QFontDatabase.applicationFontFamilies(font_id_woff)
        font_family = loaded_font_families[0]
        title_font = QFont(font_family)
        font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id_woff)
        font = QtGui.QFont(font_family)
        
        title_label = QLabel(self)
        title_label.setText("D A T E N D")
        title_font = QFont(font)
        title_font.setPointSize(50)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: white;")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setGeometry(50, 50, 400, 100)

        button_width = 250
        button_height = 100

        button_layout = QHBoxLayout()

        spacer_item = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(spacer_item)

        stage_files_button = QPushButton(self)
        stage_files_button.setText("Begin Import")
        stage_files_font = QFont(font)
        stage_files_font.setPointSize(20)
        stage_files_button.setFont(stage_files_font)
        stage_files_button.setStyleSheet("background-color: #555555; color: white;")
        stage_files_button.clicked.connect(self.go_to_stage_files)
        stage_files_button.setMaximumSize(button_width, button_height)
        button_layout.addWidget(stage_files_button)

        spacer_item = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(spacer_item)

        configure_settings_button = QPushButton(self)
        configure_settings_button.setText("Configure Settings")
        configure_settings_font = QFont(font)
        configure_settings_font.setPointSize(20)
        configure_settings_button.setFont(configure_settings_font)
        configure_settings_button.setStyleSheet("background-color: #555555; color: white;")
        configure_settings_button.clicked.connect(self.go_to_configure_settings)
        configure_settings_button.setMaximumSize(button_width, button_height)
        button_layout.addWidget(configure_settings_button)

        button_container = QWidget(self)
        button_container.setLayout(button_layout)
        button_container.setGeometry(50, 200, 400, button_height)
    
    def go_to_stage_files(self):
        self.stage_window = stageWindow()
        self.stage_window.show()

    def go_to_configure_settings(self):
        print("Navigating to Configure Settings page.")
        self.configure_window = ConfigureSettings()
        self.configure_window.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

#updates application icon of this file's current location
sys.path.append('insert desktop file path')
from DATEND import update_file_path

#change this prior
previous_path = ''

while True:
    current_path = os.path.abspath(__file__)
    if previous_path != current_path:
        previous_path = current_path
        update_file_path(current_path)
    #waits a day to check again
    time.sleep(20)
