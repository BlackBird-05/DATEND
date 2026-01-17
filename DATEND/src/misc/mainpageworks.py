import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QWidget, QSizePolicy
from PySide6 import QtGui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set main window properties
        self.setWindowTitle("DATEND")
        self.setGeometry(100, 100, 500, 380)
        self.setStyleSheet("background-color: #333333;")

        # Set font for all texts to Incompleeta Regular
        font_id = QtGui.QFontDatabase.addApplicationFont("/users/18890/Desktop/font/IncompleetaRegular.eot")
        font_id += QtGui.QFontDatabase.addApplicationFont("/users/18890/Desktop/font/IncompleetaRegular.woff")
        font_id += QtGui.QFontDatabase.addApplicationFont("/users/18890/Desktop/font/IncompleetaRegular.woff2")

        font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QtGui.QFont(font_family)
        

        # Add title label
        title_label = QLabel(self)
        title_label.setText("D A T E N D")
        title_font = QFont(font)
        title_font.setPointSize(50)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: white;")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setGeometry(50, 50, 400, 100)

        # Compute button dimensions based on golden ratio
        button_width = 250
        button_height = 100

        # Create a horizontal layout for the buttons
        button_layout = QHBoxLayout()

        # Add a spacer item to center the buttons horizontally
        spacer_item = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(spacer_item)

        # Add 'Stage Files' button
        stage_files_button = QPushButton(self)
        stage_files_button.setText("Stage Files")
        stage_files_font = QFont(font)
        stage_files_font.setPointSize(20)
        stage_files_button.setFont(stage_files_font)
        stage_files_button.setStyleSheet("background-color: #555555; color: white;")
        stage_files_button.clicked.connect(self.go_to_stage_files)
        stage_files_button.setMaximumSize(button_width, button_height)
        button_layout.addWidget(stage_files_button)

        # Add a spacer item to separate the buttons
        spacer_item = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(spacer_item)

        # Add 'Configure Settings' button
        configure_settings_button = QPushButton(self)
        configure_settings_button.setText("Configure Settings")
        configure_settings_font = QFont(font)
        configure_settings_font.setPointSize(20)
        configure_settings_button.setFont(configure_settings_font)
        configure_settings_button.setStyleSheet("background-color: #555555; color: white;")
        configure_settings_button.clicked.connect(self.go_to_configure_settings)
        configure_settings_button.setMaximumSize(button_width, button_height)
        button_layout.addWidget(configure_settings_button)

        # Add the button layout to a container widget
        button_container = QWidget(self)
        button_container.setLayout(button_layout)
        button_container.setGeometry(50, 200, 400, button_height)

    def go_to_stage_files(self):
        print("Navigating to Stage Files page.")

    def go_to_configure_settings(self):
        print("Navigating to Configure Settings page.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
