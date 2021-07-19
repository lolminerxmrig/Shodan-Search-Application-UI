import shodan
import sys, re
import pycountry

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont
from PyQt5.QtCore import Qt
from Application import *
from Table import *

         
class Search(QWidget):

        def __init__(self, parent):
                super().__init__()
                self.initUI(parent)

        
        def initUI(self, parent):                
                layout = QGridLayout()

                #GENERAL SEARCH BOX
                self.textbox_gen_search = QLineEdit(self)
                self.textbox_gen_search.resize(280,20)
                #self.textbox_gen_search.setPlaceholderText("E.g. Webcam, Apache etc.")               

                #COUNTRY SEARCH BOX
                self.textbox_country = QLineEdit(self)
                self.textbox_country.resize(75,20)
                #self.textbox_country.setPlaceholderText("E.g. UK, FR, DK etc.")               

                #CITY SEARCH BOX
                self.textbox_city = QLineEdit(self)
                self.textbox_city.resize(75, 20)

                #ORG SEARCH BOX
                self.textbox_org = QLineEdit(self)
                self.textbox_org.resize(85, 20)

                #IP SEARCH BOX
                self.textbox_ip = QLineEdit(self)
                self.textbox_ip.resize(75, 20)

                #PORT SEARCH BOX
                self.textbox_port = QLineEdit(self)
                self.textbox_port.resize(75, 20)

                #LABELS
                self.label_keyword = QLabel('Keywords:' ,self)
                self.label_keyword.setFont(QFont('Consolas', 11))
                self.label_keyword.setAlignment(Qt.AlignRight)

                self.label_country = QLabel('Country:' ,self)
                self.label_country.setFont(QFont('Consolas', 11))
                self.label_country.setAlignment(Qt.AlignRight)

                self.label_city = QLabel('City:' ,self)
                self.label_city.setFont(QFont('Consolas', 11))
                self.label_city.setAlignment(Qt.AlignRight)

                self.label_org = QLabel('Organisation:' ,self)
                self.label_org.setFont(QFont('Consolas', 11))
                self.label_org.setAlignment(Qt.AlignRight)

                self.label_ip = QLabel('IP:' ,self)
                self.label_ip.setFont(QFont('Consolas', 11))
                self.label_ip.setAlignment(Qt.AlignRight)
                
                self.label_port = QLabel('Port:' ,self)
                self.label_port.setFont(QFont('Consolas', 11))
                self.label_port.setAlignment(Qt.AlignRight)

                self.label_totalresults = QLabel('')
                self.label_totalresults.resize(42, 30)
                self.label_totalresults.setFont(QFont('Consolas', 13))
                #self.label_totalresults.setStyleSheet('color: green')                


                self.label_pagenr = QLabel('Page ')
                self.label_pagenr.setFont(QFont('Consolas', 12))

                
                #BUTTONS
                self.button_tips = QPushButton('USAGE AND FILTERS', self)
                self.button_tips.setStyleSheet("color: black;"
                                        "background-color: lightgrey;"
                                        "selection-color: grey;"
                                        "selection-background-color: black;")
                self.button_tips.setFont(QFont('Consolas', 10))

                
                self.button_CSV = QPushButton('EXPORT RESULTS TO CSV', self)
                self.button_CSV.setStyleSheet("color: black;"
                        "background-color: lightgrey;"
                        "selection-color: grey;"
                        "selection-background-color: black;")
                
                self.button_CSV.setFont(QFont('Consolas', 10))

                self.button_search = QPushButton('SEARCH', self)
                self.button_search.setFont(QFont('Consolas', 13))

                self.button_search.setStyleSheet("color: black;"
                        "background-color: lightgrey;"
                        "selection-color: grey;"
                        "selection-background-color: black;")

                
                self.button_pageforward = QPushButton('>', self)
                self.button_pageforward.setStyleSheet("background-color: rgba(255, 255, 255, 100);")

                self.button_pageback = QPushButton('<', self)
                self.button_pageback.setStyleSheet("background-color: rgba(255, 255, 255, 100);")

                # connect button to function on_click
                
                self.button_tips.clicked.connect(parent.open_tips_widget)
                self.button_CSV.clicked.connect(parent.export_to_csv)
                self.button_search.clicked.connect(parent.check_text_fields)
                self.button_pageback.clicked.connect(parent.previous_page)
                self.button_pageforward.clicked.connect(parent.next_page)

                layout.addWidget(self.label_keyword, 0,0)
                layout.addWidget(self.textbox_gen_search, 0,1)
                layout.addWidget(self.button_tips, 0,3, 1,3)
                layout.addWidget(self.button_CSV, 1,3, 1,3)

                layout.addWidget(self.label_country,1,0)
                layout.addWidget(self.textbox_country, 1,1)

                layout.addWidget(self.label_city, 2,0)
                layout.addWidget(self.textbox_city,2,1)

                layout.addWidget(self.label_org,3,0)
                layout.addWidget(self.textbox_org,3,1)

                layout.addWidget(self.label_ip,4,0)
                layout.addWidget(self.textbox_ip,4,1)

                layout.addWidget(self.label_port,5,0)
                layout.addWidget(self.textbox_port,5,1)

                layout.addWidget(self.button_search,6,0)
                layout.addWidget(self.label_totalresults,6,1)

                    
                layout.addWidget(self.button_pageback,6,3)
                layout.addWidget(self.label_pagenr,6,4)
                layout.addWidget(self.button_pageforward,6,5)


                self.setLayout(layout)
                self.show()

