import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase, QColor, QPainter, QPixmap
from PySide6.QtWidgets import QFileDialog, QMessageBox, QMainWindow, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QWidget, QSizePolicy
from PySide6 import QtGui
from highlighter import highlighter
import os
import tkinter as tk
from tkinter import filedialog

class stageWindow(QMainWindow):
    def __init__(self):
        self.batchFilePath = []
        self.docFilePath = None
        
        super().__init__()
        self.setWindowTitle('D A T E N D')
        self.setGeometry(100, 100, 500, 500)
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
        loaded_font_families_woff = QFontDatabase.applicationFontFamilies(font_id_woff)
        font_family = loaded_font_families_woff[0]
        title_font = QFont(font_family)
        font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id_woff)
        font = QtGui.QFont(font_family)
        title_font = QFont(font_family)
        title_font = QFont(font_family)
        title_font.setPointSize(50)
        title_font.setBold(True)

        # title label
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

        # Horizontal layout for the buttons
        button_layout = QHBoxLayout()
        second_layout = QHBoxLayout()
        third_layout = QHBoxLayout()

        # Add a spacer item to center the buttons horizontally
        spacer_item = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(spacer_item)

        # Import File button
        import_files_button = QPushButton(self)
        import_files_button.setText("Import File")
        import_files_font = QFont(title_font)
        import_files_font.setPointSize(20)
        import_files_button.setFont(import_files_font)
        import_files_button.setStyleSheet("background-color: #555555; color: white;")
        import_files_button.clicked.connect(self.import_files)
        import_files_button.setMaximumSize(button_width, button_height)
        button_layout.addWidget(import_files_button)

        # spacer
        spacer_item = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_layout.addItem(spacer_item)

        # import batch button
        batch_files_button = QPushButton(self)
        batch_files_button.setText("Import Batch")
        batch_files_font = QFont(title_font)
        batch_files_font.setPointSize(20)
        batch_files_button.setFont(batch_files_font)
        batch_files_button.setStyleSheet("background-color: #555555; color: white;")
        batch_files_button.clicked.connect(self.import_batch)
        batch_files_button.setMaximumSize(button_width, button_height)
        button_layout.addWidget(batch_files_button)

        button_container = QWidget(self)
        button_container.setLayout(button_layout)
        button_container.setGeometry(50, 200, 400, button_height)

        begin_scan_button = QPushButton(self)
        begin_scan_button.setText("Begin Scan")
        begin_scan_font = QFont(title_font)
        begin_scan_font.setPointSize(20)
        begin_scan_button.setFont(begin_scan_font)
        begin_scan_button.setStyleSheet("background-color: #555555; color: white;")
        begin_scan_button.clicked.connect(self.begin_scan)
        begin_scan_button.setMaximumSize(button_width, button_height)
        second_layout.addWidget(begin_scan_button) 

        second_container = QWidget(self)
        second_container.setLayout(second_layout)
        second_container.setGeometry(50, 350, 400, button_height)

        self.confirmation_label = QLabel(self)
        self.confirmation_label.setAlignment(Qt.AlignCenter)
        self.confirmation_label.setStyleSheet("font-size: 16px; color: white;")
        third_layout.addWidget(self.confirmation_label)

        third_container = QWidget(self)
        third_container.setLayout(third_layout)
        third_container.setGeometry(50, 440, 400, 50)

    def open_file_dialog(self):
        files = []
        root = tk.Tk()
        root.withdraw()

        file_paths = filedialog.askopenfilenames(
            title="Select .docx Files or Folder",
            filetypes=[("Word Documents", "*.docx")],
            initialdir="/",
            multiple=True 
        )
        root.destroy()

        if file_paths:
            print("Selected Files/Folder:")
            for file_path in file_paths:
                if os.path.basename(file_path).endswith('.docx'):
                    files.append(file_path)

    def import_files(self):
        print("importing documents.")
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Word Document (*.docx)")
        if fileName != None:
            self.batchFilePath = []
            print(f"Selected file: {fileName}")
            self.docFilePath = fileName
            name = os.path.basename(fileName)
            short_name = name[:20]
            self.confirmation_label.setText('Imported: ' + str(short_name) + "...")

    def import_batch(self):
        print("Importing Batch documents.")
        fileNames = []
        options = QFileDialog.Options()
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", options=options)
        filelist = os.listdir(folder_path)
        for file in filelist:
            if file.endswith('.docx'):
                fileNames.append(folder_path + '/' + file)
        if len(fileNames) != 0:
            self.docFilePath = None
            print("Selected file: ", (name for name in fileNames))
            self.batchFilePath = fileNames
            text = 'imported ' + str(len(self.batchFilePath)) + ' documents'
            self.confirmation_label.setText(text)

    def begin_scan(self):
        print("scanning")
        self.confirmation_label.setText("Beginning Scan... Please wait")
        if len(self.batchFilePath) != 0:
            for file in self.batchFilePath:
                highlighter(file)
            self.confirmation_label.setText("All done!")

        elif self.docFilePath != None:
            highlighter(self.docFilePath)
        else:
            #in case no file is found
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setWindowTitle("Error: No File Found")
            msgBox.setText("No File Detected")
            msgBox.setInformativeText("Please select a .docx file or folder.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

