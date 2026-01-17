from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QFormLayout, QLineEdit, QCheckBox, QPushButton, QTextEdit, QFileDialog
from PySide6 import QtGui
from PySide6.QtCore import Qt, QFile, QTextStream, QCoreApplication, QUrl
from PySide6.QtGui import QDesktopServices, QFont, QFontDatabase
import subprocess
import os
import storage
import sys



class ConfigureSettings(QMainWindow):
    def __init__(self):
        super().__init__()
        def check_if_checked(self):
            
            try:
                    self.search_transition_words = storage.transition_words
                    print(self.search_transition_words)
            except:
                    self.search_transition_words = False
            try:
                    self.search_text = storage.textual
                    print(self.search_text)
            except:
                    self.search_text = False
            try:
                    self.search_rich = storage.rich
                    print(self.search_rich)
            except:
                    self.search_rich = False
            try:
                    self.return_stats = storage.stats
                    print(self.return_stats)
            except:
                    self.return_stats = False
        current_directory = os.path.dirname(os.path.abspath(__file__))
        font_folder_path = os.path.join(current_directory, "font")
        font_path_woff = os.path.join(font_folder_path, "IncompleetaRegular.woff")
        font_id_woff = QFontDatabase.addApplicationFont(font_path_woff)
        print("Font ID WOFF:", font_id_woff)
        font_family = QFontDatabase.applicationFontFamilies(font_id_woff)
        font = QtGui.QFont(font_family)
        self.isChanges = False
        self.change_csv_file_path = None
        self.add_csv_file_path = None
        self.author_name = ''
        self.themes = ''
        self.gq_words = ''
        check_if_checked(self)
        self.global_issue = ''
        
        self.setWindowTitle("D A T E N D")
        self.setStyleSheet("background-color: #333333;")

        title_label = QLabel("D A T E N D")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(font)
        title_label.setStyleSheet("font-size: 36px; color: #F5F5F5;")

        subtitle_label = QLabel("Literary Devices")
        subtitle_label.setFont(font)
        subtitle_label.setStyleSheet("font-size: 20px; color: #F5F5F5;")

        input_new_csv_button = QPushButton("Input new CSV list")
        input_new_csv_button.setFont(font)
        input_new_csv_button.setStyleSheet("color: #F5F5F5;")
        input_new_csv_button.clicked.connect(self.get_new_csv_file_path)

        add_on_csv_button = QPushButton("Add on CSV list")
        add_on_csv_button.setFont(font)
        add_on_csv_button.setStyleSheet('color: #F5F5F5;')
        add_on_csv_button.clicked.connect(self.get_add_csv_file_path)

        view_list = QPushButton('View Current List')
        view_list.setFont(font)
        view_list.setStyleSheet('color: #F5F5F5;')
        view_list.clicked.connect(self.show_csv)

        save_button = QPushButton('Save')
        save_button.setFont(font)
        save_button.setStyleSheet('background-color: #00008b; color: white;')
        save_button.clicked.connect(self.save_all)

        cancel_button = QPushButton('Cancel')
        cancel_button.setFont(font)
        cancel_button.setStyleSheet('background-color: #8b0000; color: white;')
        cancel_button.clicked.connect(self.cancel_all)

        add_keywords_label = QLabel("Global Issue(s)")
        add_keywords_label.setStyleSheet("color: #F5F5F5;")
        add_keywords_label.setFont(font)
        keywords_field = QLineEdit()
        keywords_field.setStyleSheet('color: #F5F5F5')
        keywords_field.textChanged.connect(self.add_global_issue)

        author_name_field = QLineEdit()
        try:
            print(storage.author_names)
            print(len(storage.author_names))
            if len(storage.author_names) != 0:
                
                author_name = ""
                for name in storage.author_names:
                    name = str(name)
                    author_name = author_name + ", "
                author_name = author_name.rstip(',')
                author_name_field.setPlaceholderText(author_name)
                print("author found in storage")
            else:
                print('author storage but nothing')
                author_name_field.setPlaceholderText("Author Name")
        except:
            print('author not found')
            file = open('storage.py', 'a')
            file.write("author_names = [] \n")
            file.close()
            author_name_field.setPlaceholderText("Author Name")
        author_name_field.setStyleSheet('color: #F5F5F5')
        author_name_field.textChanged.connect(self.add_author_name)

        themes_field = QLineEdit()
        try:
            if len(storage.themes) != 0:
                
                themes = ""
                for theme in storage.themes:
                    theme = str(theme)
                    themes = theme + ", "
                themes = themes.rstip(',')
                themes_field.setPlaceholderText(themes)
                print('themes found in storage')
            else:
                print('themes storage but nothing')
                themes_field.setPlaceholderText('Themes')
        except:
            print('themes not found in storage')
            file = open('storage.py', 'a')
            file.write("themes = [] \n")
            themes_field.setPlaceholderText("Themes")
        themes_field.setStyleSheet('color: #F5F5F5')
        themes_field.textChanged.connect(self.add_themes)

        guiding_question_keywords_field = QLineEdit()
        try:
            if len(storage.gq_words) != 0:
                gq_words = ""
                for word in storage.gq_words:
                    word = str(word)
                    gq_words = word + ", "
                gq_words = gq_words.rstip(',')
                guiding_question_keywords_field.setPlaceholderText(gq_words)
                print('gq words found in storage')
            else:
                guiding_question_keywords_field.setPlaceholderText("Guiding Question Keywords")
                print('gq words in storage but nothing')
        except:
            print('gq words not found in storage')
            file = open('storage.py', 'a')
            file.write("gq_words = [] \n")
            guiding_question_keywords_field.setPlaceholderText("Guiding Question Keywords")
        guiding_question_keywords_field.setStyleSheet('color: #F5F5F5')
        guiding_question_keywords_field.textChanged.connect(self.add_gq)

        checkbox1 = QCheckBox("Search Transition Words")
        checkbox1.setChecked(self.search_transition_words)
        checkbox1.setStyleSheet('color: #F5F5F5;')
        checkbox1.setFont(font)
        checkbox1.toggled.connect(self.store_transition_words)
        checkbox2 = QCheckBox("Search Textual References")
        checkbox2.setChecked(self.search_text)
        checkbox2.setStyleSheet('color: #F5F5F5;')
        checkbox2.setFont(font)
        checkbox2.toggled.connect(self.store_text)
        checkbox3 = QCheckBox("Search Rich Ideas")
        checkbox3.setChecked(self.search_rich)
        checkbox3.setStyleSheet('color: #F5F5F5;')
        checkbox3.setFont(font)
        checkbox3.toggled.connect(self.store_rich)
        checkbox4 = QCheckBox("Return Statistics")
        checkbox4.setChecked(self.search_rich)
        checkbox4.setStyleSheet('color: #F5F5F5;')
        checkbox4.setFont(font)
        checkbox4.toggled.connect(self.store_statistics)

        left_layout = QVBoxLayout()
        left_layout.addWidget(title_label)
        left_layout.addWidget(author_name_field)
        left_layout.addWidget(themes_field)
        left_layout.addWidget(guiding_question_keywords_field)

        checkbox_layout = QFormLayout()
        checkbox_layout.addRow(checkbox1)
        checkbox_layout.addRow(checkbox2)
        checkbox_layout.addRow(checkbox3)
        checkbox_layout.addRow(checkbox4)
        left_layout.addLayout(checkbox_layout)

        right_layout = QVBoxLayout()
        right_layout.addWidget(subtitle_label)
        right_layout.addWidget(input_new_csv_button)
        right_layout.addWidget(add_on_csv_button)
        right_layout.addWidget(view_list)
        right_layout.addWidget(add_keywords_label)
        right_layout.addWidget(keywords_field)
        right_layout.addWidget(save_button)
        right_layout.addWidget(cancel_button)

        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)


                
    def get_new_csv_file_path(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select CSV or txt file", "", "CSV files (*.csv);;Text files (*.txt)")
        if file_path and self.add_csv_file_path == None:
            self.change_csv_file_path = file_path
            print("File path:", file_path)

    def get_add_csv_file_path(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select CSV or txt file", "", "CSV files (*.csv);;Text files (*.txt)")
        if file_path and self.change_csv_file_path == None:
            self.add_csv_file_path = file_path
            print("File path:", file_path)
    
    def show_csv(self):
        try:
            subprocess.run(['open', 'litdevices.txt'])
        except:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setWindowTitle("Error: No File Found")
            msgBox.setText("No File Detected")
            msgBox.setInformativeText("File has been deleted, a new file will be created.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
            file = open('litdevices.txt', 'r')
            file.close()
        
        '''
        if self.add_csv_file_path != None:
            file = QFile(self.add_csv_file_path)
            url = QUrl.fromLocalFile(self.add_csv_file_path)
            QDesktopServices.openUrl(url)
            if file.open(QFile.ReadOnly | QFile.Text):
                stream = QTextStream(file)
                
                contents = stream.readAll()
                print(contents)
            else:
                print('failed to open')
        elif self.change_csv_file_path != None:
            file = QFile(self.change_csv_file_path)
            url = QUrl.fromLocalFile(self.change_csv_file_path)
            QDesktopServices.openUrl(url)
            if file.open(QFile.ReadOnly | QFile.Text):
                stream = QTextStream(file)
                contents = stream.readAll()

                print(contents)
            else:
                print('failed to open')
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setWindowTitle("Error: No File Found")
            msgBox.setText("No File Detected")
            msgBox.setInformativeText("Please select a CSV file to import.")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        '''
    def add_author_name(self, text):
        self.author_name = text
        print(self.author_name)
    
    def add_themes(self, text):
        self.themes = text
        print(self.themes)

    def add_gq(self,text):
        self.gq_words = text
        print(self.gq_words)

    def add_global_issue(self, text):
        self.global_issue = text
        print(self.global_issue)

    def store_transition_words(self, state):
        self.search_transition_words = state
        print(self.search_transition_words)
    
    def store_text(self, state):
        self.search_text = state
        print(self.search_text)

    def store_rich(self, state):
        self.search_rich = state
        print(self.search_rich)
    
    def store_statistics(self, state):
        self.return_stats = state
        print(self.return_stats)

    def save_all(self):
        if os.path.isfile('litdevices.txt'):
            pass
        else:
            file = open('litdevices.txt', 'r')
            file.close()
        if os.path.isfile('storage.py'):
            pass
        else:
            file = open('storage.py', 'r')
            file.close()
        with open('storage.py', 'w') as file:
            self.isChanges = True
            if self.add_csv_file_path != None:
                addunchanged = open('litdevices.txt', 'a')
                file.write('isadd = True \n')
                file.write('add_csv_file_path = "' + self.add_csv_file_path + '" \n')
                addon = open(self.add_csv_file_path, 'r')
                for device in addon:
                    device = device.strip('')
                    seperated = device.split(',')
                    for value in seperated:
                        if value.endswith('.'):
                            value = value[:-1]
                        if value.endswith(','):
                            value.strip(',')
                        addunchanged.write('\n' + value)
            elif self.change_csv_file_path != None:
                changeunchanged = open('litdevices.txt', 'w')
                file.write('isadd = False \n')
                file.write('change_csv_file_path = "' + self.change_csv_file_path + '" \n')
                change = open(self.change_csv_file_path, 'r')
                for device in change:
                    device.strip('')
                    seperated = device.split(',')
                    for value in seperated:
                        if value.endswith('.'):
                            value = value[:-1]
                        if value.endswith(','):
                            value.strip(',')
                        changeunchanged.write('\n' + value)

            file.write('author_names = ' + str(self.author_name.split(', ')) + '\n')
            file.write('themes = ' + str(self.themes.split(', ')) + '\n')
            file.write('gq_words = ' + str(self.gq_words.split(', ')) + '\n')
            file.write('transition_words = ' + str(self.search_transition_words) + '\n')
            print(self.search_transition_words)
            file.write('textual = ' + str(self.search_text) + '\n')
            print(self.search_text)
            file.write('rich = ' + str(self.search_rich) + '\n')
            print(self.search_rich)
            file.write('stats = ' + str(self.return_stats) + '\n')
            print(self.return_stats)

            file.write('global_issues = ' + str(self.global_issue.split(', ')) + '\n')
            file.close()
        self.close()
        sys.exit()

    def cancel_all(self):
        self.close()

