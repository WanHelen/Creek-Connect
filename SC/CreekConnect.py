import sys
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkextrafont import Font
import re
#import sqlite3
from pymongo import MongoClient
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, \
                            QTabWidget, QPushButton, QMenu, QAction, QTextEdit,\
                            QLabel, QLineEdit, QFileDialog, QSizePolicy, QMessageBox, \
                            QDialog, QDialogButtonBox, QTextBrowser

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont, QPixmap

from data import  College, Government, Service, Other
import hashlib

import json

#import partner_manager as partner_manager
#import add_partner as add_partner
#import helpButton as helpButton 
#import account_settings as account_settings
#import newAccount as newAccount
#import contact as contact

# retrieving mongodb connection string from json file
#with open("./assets/variables.json", 'r') as file:
#    data = json.load(file)
#    conn_str = data['conn_str']

# connect to mongodb
conn_str = 'test@gmail.com'
client = MongoClient(conn_str)
db = client['partnerlink']  # database name
users_col = db['users']  # users table


class SignInWindow(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("light")
        super().__init__()
        #self.custom_font = Font(file="./assets/Roboto-Medium.ttf", family="Roboto Medium")
        self.title("Creek Connect")
        self.geometry("900x500")  # window size
        self.setup_login_screen()

    def clear_window(self):
        # Destroy all widgets from the window
        for widget in self.winfo_children():
            widget.destroy()

    def setup_login_screen(self):
        self.clear_window()

        # Adjusting frames for layout
        left_frame = ctk.CTkFrame(self, width=400, height=500, bg_color='white', fg_color="white")
        left_frame.pack(side="left", fill="y", expand=False)
        right_frame = ctk.CTkFrame(self, width=400, height=500)
        right_frame.pack(side="right", fill="y", expand=True)

        login_label = ctk.CTkLabel(right_frame, text="          Welcome!          ", font=("Roboto Medium", 50), bg_color='white', fg_color="#dbdbdb")
        login_label.pack(pady=20)
        
        # Load and display logo in the left frame
        self.logo_image = Image.open("./Login_photo.png")
        self.logo_image = self.logo_image.resize((450, 350), Image.Resampling.LANCZOS)
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = ctk.CTkLabel(left_frame, image=self.logo_image, bg_color='white', fg_color="white", text="")
        self.logo_label.pack(pady=75)

        # Increase size of entries and align them in the right frame
        # Set a fixed width for text entries
        entry_width = 300  
        entry_height = 60
        entry_font = ("Roboto Medium", 20)

        self.email_entry = ctk.CTkEntry(right_frame, placeholder_text="Login with Email", width=entry_width, height=entry_height, font=entry_font)
        self.email_entry.pack(pady=10)

        self.email_status_label = ctk.CTkLabel(right_frame, text="", font=entry_font,bg_color='#dbdbdb', fg_color="#dbdbdb")
        self.email_status_label.pack(pady=5)

        #self.email_entry.bind("<KeyRelease>", self.validate_email)


        self.password_entry = ctk.CTkEntry(right_frame, placeholder_text="Password", show="*", width=entry_width, height=entry_height, font=entry_font)
        self.password_entry.pack(pady=10)
        
        self.password_status_label = ctk.CTkLabel(right_frame, text="", bg_color='#dbdbdb', fg_color="#dbdbdb", font=entry_font)
        self.password_status_label.pack(pady=5)

        #self.password_entry.bind("<KeyRelease>", self.validate_password)

        # Sign In Button in the right frame
        self.sign_in_button = ctk.CTkButton(right_frame, text="login", text_color="#dbdbdb",command=self.sign_in, width=250, height=50, font=entry_font, fg_color="#000000", hover_color="#444444")
        self.sign_in_button.pack(pady=10)

        self.login_error_label = ctk.CTkLabel(right_frame, text="", bg_color='white', fg_color="#dbdbdb", font=entry_font)
        self.login_error_label.pack(pady=2)

    def sign_in(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        #print('email is', email)
        #print('password is ', password)
        #print('password_hash is', password_hash)
        
#        if self.email_status_label.cget("text") == "Email Entered" and password:
        if email == "creekconnectfbla@gmail.com" and password:
        
            #user = users_col.find_one({"email": email})
            
            #if user and user['passwordHash'] == password_hash:

            if password == '123456':
                print("Login successful")
                #self.user_id = user['_id']
                # Store the user's name
                #self.user_name = user.get('name', 'User')  # Default to 'User' if name is not available
                self.destroy()
                window.show()
                #self.create_new_layout()  # Create a new layout after successful login
            else:
                self.login_error_label.configure(text="credentials did not match\nour systems", text_color="red", fg_color="#dbdbdb", bg_color="#dbdbdb", font=("Roboto Medium", 20))
        else:
            self.login_error_label.configure(text="invalid credentials", text_color="red", fg_color="#dbdbdb", bg_color="#dbdbdb")




class MyGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('FBLA CreekConnect')

        self.setGeometry(200,200, 1000,500)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(200, 200, 1000, 600)  # Set margins for the main layout


#        text_name_label = QLabel('\n CreekConnect',self)
#        text_name_label.setFont(QFont('Arial', 15))
#        text_name_label.setStyleSheet("color: black;")  # Set text color to white
#        top_layout.addWidget(text_name_label)
        
        picture_label = QLabel('\n Picture text', self)
        pixmap = QPixmap('Login_photo.png')  # Change the path to your image file

        scaled_width = int(pixmap.width() * 0.8)
        scaled_height = int(pixmap.height() * 0.8)

        # Scale the picture by 80%
        scaled_pixmap = pixmap.scaled(scaled_width, scaled_height)

        picture_label.setPixmap(scaled_pixmap)
#        picture_label.setAlignment(Qt.AlignCenter)


        #top_layout.addWidget(picture_label)
        #main_layout.addLayout(top_layout)
        #main_layout.addWidget(picture_label)

        main_layout = QHBoxLayout()

        # Left frame
        left_frame = QWidget(self)
        left_frame.setFixedWidth(500)

        left_layout = QVBoxLayout(left_frame)

        top_layout = QHBoxLayout()
        top_layout.addWidget(picture_label)


        # Partner Layout
        partner_layout = QVBoxLayout()
        #partner_layout = QHBoxLayout(left_frame)

        current_partner_label = QLabel('Current Partners')
        current_partner_label.setFont(QFont('Times New Roman', 15))
        current_partner_label.setStyleSheet("color: black;")  # Set text color to white
        #current_partner_label.setMaximumSize(300,30)
        current_partner_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        partner_layout.addWidget(current_partner_label)

        # Create the first pushbutton with dropdown menu
        self.button1 = QPushButton('College', left_frame)
        self.button1.setFont(QFont('Arial Rounded MT Bold',14))
        self.button1.setStyleSheet("background-color: silver; color: black;")
        self.button1.setMenu(self.create_menu(College))
        self.button1.setMinimumSize(150, 40)  # Set the minimum width and height
        self.button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        partner_layout.addWidget(self.button1)


        # Create the second pushbutton with dropdown menu
        button2 = QPushButton('Government', left_frame)
        button2.setFont(QFont('Arial Rounded MT Bold',14))
        button2.setStyleSheet("background-color: silver; color: black;")
        button2.setMenu(self.create_menu(Government))
        button2.setMinimumSize(150, 40)  # Set a fixed width and height
        button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        partner_layout.addWidget(button2)


        # Create the third pushbutton with dropdown menu
        button3 = QPushButton('Service', left_frame)
        button3.setFont(QFont('Arial Rounded MT Bold',14))
        button3.setStyleSheet("background-color: silver; color: black;")
        button3.setMenu(self.create_menu(Service))
        button3.setMinimumSize(200, 40)  # Set a fixed width and height
        button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        partner_layout.addWidget(button3)


        # Create pushbutton with dropdown menu
        button4 = QPushButton('Other', left_frame)
        button4.setFont(QFont('Arial Rounded MT Bold',14))
        button4.setStyleSheet("background-color: silver; color: black;")
        button4.setMenu(self.create_menu(Other))
        button4.setMinimumSize(200, 40)  # Set a fixed width and height
        button4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        partner_layout.addWidget(button4)

        top_layout.addLayout(partner_layout)

        left_layout.addLayout(top_layout)
    
        # Create pushbutton with dropdown menu
        #button5 = QPushButton('NewAdd', left_frame)
        #button5.setFont(QFont('Arial',10))
        #button5.setMenu(self.create_menu(NewAdd))
        #left_layout.addWidget(button5)


#        # Search input field
#        self.search_input = QLineEdit(self)
#        self.search_input.setPlaceholderText('Search by Name')
#        left_layout.addWidget(self.search_input)

#        # Search button
#        search_button = QPushButton('Search', left_frame)
#        search_button.clicked.connect(self.handle_search)
#        left_layout.addWidget(search_button)

######



        # Add new items in directory
        Add_button = QPushButton('Add New Partner', left_frame)
        Add_button.setFont(QFont('Arial Rounded MT Bold',14))
        Add_button.setStyleSheet("background-color: silver; color: black;")
        Add_button.setMenu(self.create_addmenu())
        Add_button.setFixedSize(200, 30)
        Add_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        left_layout.addWidget(Add_button)

        # Search input field and button side by side
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit(self)
        self.search_input.setFont(QFont('Arial Rounded MT Bold', 12))
        self.search_input.setStyleSheet("background-color: white; color: navy;")  # Set input field color to white
        self.search_input.setPlaceholderText('Search by Name')
        search_layout.addWidget(self.search_input)
        search_button = QPushButton('Search', left_frame)
        search_button.setFont(QFont('Arial Rounded MT Bold', 12))
        search_button.setStyleSheet("background-color: darkBlue; color: white;")
        search_button.clicked.connect(self.handle_search)
        search_layout.addWidget(search_button)
        left_layout.addLayout(search_layout)


        # Connect Enter key press event to search function
        self.search_input.returnPressed.connect(self.handle_search)

        # Save button
        save_button = QPushButton('Save Information', left_frame)
        save_button.setFont(QFont('Arial Rounded MT Bold', 12))
        save_button.setStyleSheet("background-color: darkBlue; color: white;")
        save_button.setFixedSize(150, 40)
        save_button.clicked.connect(self.save_content)

        bottom_layout = QHBoxLayout()

        bottom_layout.addWidget(save_button)

        # Reset button
        reset_button = QPushButton('Reset', self)
        reset_button.setFont(QFont('Arial Rounded MT Bold', 12))
        reset_button.setStyleSheet("background-color: darkBlue; color: white;")
        reset_button.clicked.connect(self.reset_tabs)
        reset_button.setFixedSize(100, 40)  # Set the size here
        bottom_layout.addWidget(reset_button)

        logout_button = QPushButton('Logout', self)
        logout_button.setFont(QFont('Arial Rounded MT Bold', 12))
        logout_button.setStyleSheet("background-color: darkBlue; color: white;")
        logout_button.clicked.connect(self.logout)
        logout_button.setFixedSize(100, 40)
        bottom_layout.addWidget(logout_button)

        help_button = QPushButton('Help', self)
        help_button.setFont(QFont('Arial Rounded MT Bold', 12))
        help_button.setStyleSheet("background-color: darkBlue; color: white;")
        help_button.setFixedSize(100, 40)
        help_button.clicked.connect(self.help)

        bottom_layout.addWidget(help_button)

        left_layout.addLayout(bottom_layout)

        # Right frame
        self.right_frame = QWidget(self)
        right_layout = QVBoxLayout(self.right_frame)

        # Create a TabWidget in the right frame
        self.tab_widget = QTabWidget(self.right_frame)
        self.tab_widget.setFont(QFont('Arial', 10))
        right_layout.addWidget(self.tab_widget)


        # Add the frames to the main layout
        main_layout.addWidget(left_frame)
        main_layout.addWidget(self.right_frame)

        # Set the main layout for the main window
        self.setLayout(main_layout)

    def help(self):
        # Fetch help content from file
        try:
            with open('Creek_Connect_Help_Guide.txt', 'r') as file:
                help_content = file.read()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while loading the help content: {str(e)}")
            return

        # Create a HelpWindow instance and show it as a modal window
        help_window = HelpWindow(help_content)
        help_window.exec_()
 


    def create_addmenu(self):
        # Create a menu with items from the given list
        menu = QMenu(self)
        font = QFont()
        font.setPointSize(12)
        action1 = menu.addAction('College')
        action1.setFont(font)
        action1.triggered.connect(self.addnew_partner)

        action2 = menu.addAction('Government')
        action2.setFont(font)
        action2.triggered.connect(self.addnew_partner)

        action3 = menu.addAction('Service')
        action3.setFont(font)
        action3.triggered.connect(self.addnew_partner)

        action4 = menu.addAction('Other')
        action4.setFont(font)
        action4.triggered.connect(self.addnew_partner)

        return menu


    def addnew_partner(self):

        action = self.sender()
        selected_category = action.text()

#        self.clear_values_in_tabs(selected_category)
        #self.clear_values_in_tabs()
        self.create_empty(selected_category)

    def create_empty(self, selected_category):
        # Create a menu with items from the given list
        self.reset_tabs()
        self.display_tabs_name(selected_category)


    def create_menu(self, items):
        # Create a menu with items from the given list
        from data import  College, Government, Service, Other
        menu = QMenu(self)
        for item in items:
            action = menu.addAction(item['Name'])
            action.triggered.connect(lambda checked, item=item: self.handle_menu_item_click(item))

        return menu


    def handle_menu_item_click(self, item):
        self.reset_tabs()  # Reset tabs before adding new ones
        self.display_values_in_tabs(item)

    def reset_tabs(self):
        # Reset the tabs by clearing existing ones
        self.tab_widget.clear()
        from data import  College, Government, Service, Other

       

    def logout(self):
        # logout
        reply = QMessageBox.question(self,'Logout', 'Are you sure you want to logout?', \
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                                     
        if reply == QMessageBox.Yes:
          QApplication.quit()


    def display_tabs_name(self, selected_category):
        # Display values in tabs based on the clicked item
        
        tab_names = list(College[0].keys())[1:]  # Exclude 'Name' key

        value_label = QLabel(" ")

        tab_tmp = QWidget()
        tab_layout = QVBoxLayout(tab_tmp)
        tab_layout.addWidget(value_label)
        self.tab_widget.addTab(tab_tmp,"News")
        input_box1 = QLineEdit(tab_tmp)
        submit_button = QPushButton("Submit")
        submit_button.setFont(QFont("Arial", 15))

        tab_Newname = QWidget()
        tab_layout = QVBoxLayout(tab_Newname)
        tab_layout.addWidget(value_label)
        self.tab_widget.addTab(tab_Newname,"Name")
        self.input_name = QLineEdit(tab_Newname)
        submit_button1 = QPushButton("Submit")
        submit_button1.setFont(QFont("Arial", 15))
        tab_layout.addWidget(submit_button1)
        submit_button1.clicked.connect(self.saveToFile)

        tab_information = QWidget()
        tab_layout = QVBoxLayout(tab_information)
        tab_layout.addWidget(value_label)
        self.tab_widget.addTab(tab_information,"Information")
        self.input_information = QLineEdit(tab_information)
        

        submit_button2 = QPushButton("Submit")
        submit_button2.setFont(QFont("Arial", 15))
        tab_layout.addWidget(submit_button2)
        submit_button1.clicked.connect(self.saveToFile)

        tab_address = QWidget()
        tab_layout = QVBoxLayout(tab_address)
        tab_layout.addWidget(value_label)
        self.tab_widget.addTab(tab_address,"Address")
        self.input_address = QLineEdit(tab_address)
        submit_button3 = QPushButton("Submit")
        submit_button3.setFont(QFont("Arial", 15))
        tab_layout.addWidget(submit_button3)
        submit_button2.clicked.connect(self.saveToFile)

        tab_contact = QWidget()
        tab_layout = QVBoxLayout(tab_contact)
        tab_layout.addWidget(value_label)
        self.tab_widget.addTab(tab_contact,"Contact")
        self.input_contact = QLineEdit(tab_contact)
        submit_button4 = QPushButton("Submit")
        submit_button4.setFont(QFont("Arial", 15))
        tab_layout.addWidget(submit_button4)
        submit_button4.clicked.connect(self.saveToFile)


        # for tab_name in tab_names:
        #     tab = QWidget()
        #     tab_layout = QVBoxLayout(tab)
        #     value_label = QLabel(" ")
        #     tab_layout.addWidget(value_label)
        #     self.tab_widget.addTab(tab, tab_name)
        #     self.input_box = QLineEdit(tab)

    def saveToFile(self):
        #from data import  College, Government, Service, Other
        #print ('College:', College)

        #self.button1.setMenu(self.create_menu(College))

        name_content = self.input_name.text()
        info_content = self.input_information.text()
        address_content = self.input_address.text()
        contact_content = self.input_contact.text()

#        action_new_menu = self.dropdown_menu.addAction(name_content)
#        action_new_menu.triggered.connect(self.handleNewMenuAction)

#        # Set the updated menu to the dropdown button
#        self.dropdown_button.setMenu(self.dropdown_menu)


        new_dict = {
            'Name': name_content,
            'Information': info_content,
            'Address': address_content,
            'Contact': contact_content
        }

        print('new_dict', new_dict)
        # Open data111.py and update the 'College' list if it exists
        try:
            with open('data.py', 'r') as file:
                lines = file.readlines()

            college_index = -1
            for i, line in enumerate(lines):
                if 'College' in line:
                    college_index = i
                    break
            
            if college_index != -1:
                # Find the end of the 'College' list
                end_index = college_index
                while ']' not in lines[end_index]:
                    end_index += 1

                # Insert the new dictionary as an element inside the 'College' list
                lines.insert(end_index - 1, f'    {new_dict},\n')

                with open('data.py', 'w') as file:
                    file.writelines(lines)

                print("Dictionary inserted into 'College' list in data.py.")
            else:
                print("Error: 'College' list not found in data.py.")

        except FileNotFoundError:
            print("Error: File 'data.py' not found.")

#        # Write the contents to a file named 'ddd.py'
#        with open('ddd.py', 'w') as file:
#            file.write(f'# Contents of tab1:\n{content_tab1}\n\n# Contents of tab2:\n{content_tab2}\n\n# Contents of tab3:\n{content_tab3}\n')


    def display_values_in_tabs(self, item):
        # Display values in tabs based on the clicked item
        tab_names = list(item.keys())[1:]  # Exclude 'Name' key
        
        for tab_name in tab_names:
            tab = QWidget()
            tab_layout = QVBoxLayout(tab)

            self.value_label = QLabel(item[tab_name])
            self.value_label.setStyleSheet("padding-top: 10px;")  # Set top margin to 10 pixels
            self.value_label.setFont(QFont('Arial', 12))
            #self.value_label.setStyleSheet("color: blue;")  # Set text color to blue
            self.value_label.setWordWrap(True)

            tab_layout.addWidget(self.value_label)
            self.tab_widget.addTab(tab, tab_name)
            
            if tab_name == 'Contact':
               email_layout = QHBoxLayout()
               email_subject = QLabel("Subject:")
               email_subject_input = QLineEdit()
               email_layout.addWidget(email_subject)
               email_layout.addWidget(email_subject_input)

               message_layout = QHBoxLayout()
               message_label = QLabel("Message:")
               message_input = QTextEdit()
               message_layout.addWidget(message_label)
               message_layout.addWidget(message_input)
 
               send_button = QPushButton("Send Email")
               send_button.clicked.connect(self.sendEmail)

               tab_layout.addLayout(email_layout)     
               tab_layout.addLayout(message_layout)
               tab_layout.addWidget(send_button)


    def sendEmail(self):
        # Placeholder functionality for sending email (not implemented in this example)
        QMessageBox.information(self, "Send Email", "Invalid email address")




    def handle_search(self):
        # Search for the entered content in 'Name' key and display values if a match is found
        search_content = self.search_input.text().lower()
        item_found = False

        for category in [College, Government, Service, Other]:
            for item in category:
                if search_content in item['Name'].lower():
                    self.reset_tabs()
                    self.display_values_in_tabs(item)
                    item_found = True
                    break
        if not item_found:
            self.display_not_found_message() 

    def display_not_found_message(self):
        # Display a message in the tabs if the search item is not found
        #not_found_tab = QWidget()
        #not_found_layout = QVBoxLayout(not_found_tab)
        #not_found_label = QLabel('Item not found')
        #not_found_layout.addWidget(not_found_label)
        #self.tab_widget.addTab(not_found_tab, 'Not Found')
        self.reset_tabs()
        #self.display_values_in_tabs('Item not found')


    def save_content(self):
        # Save the content of all tabs to a file
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;All Files (*)')
        if file_path:
            with open(file_path, 'w') as file:
                for i in range(self.tab_widget.count()):
                    current_tab_widget = self.tab_widget.widget(i)
                    current_label = current_tab_widget.findChild(QLabel)
                    if current_label:
                        file.write(f"{self.tab_widget.tabText(i)}:\n")
                        file.write(f"{current_label.text()}\n\n")




class HelpWindow(QDialog):
    def __init__(self, content):
        super().__init__()

        self.setWindowTitle("Help Guide")
        self.setGeometry(100, 100, 400, 300)

        self.initUI(content)

    def initUI(self, content):
        # Create the main vertical layout
        main_layout = QVBoxLayout(self)

        # Create a QTextBrowser to display help content
        self.help_browser = QTextBrowser(self)
        self.help_browser.setPlainText(content)
        main_layout.addWidget(self.help_browser)

        # Create a QDialogButtonBox with OK button
        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(self.close)  # Connect 'accepted' signal to 'close' slot
        main_layout.addWidget(button_box)

        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("QWidget { background-color: lightblue; }")  # Set background color to lightblue for all widgets
    window = MyGUI()
    screen=SignInWindow()
    screen.mainloop()
    #window.show()
    sys.exit(app.exec_())
    






