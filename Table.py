import shodan
import sys, re
import pycountry

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont
from PyQt5.QtCore import Qt
from Application import *
from Search import *

class Table(QWidget):

        def __init__(self, parent):
                super().__init__()

                self.initUI()

        def initUI(self):
                
                layout=QHBoxLayout()


                self.tableWidget=QTableWidget()
                self.tableWidget.setColumnCount(9)
                #REPLACE 40k with len or total
                self.tableWidget.setRowCount(100)
                

                self.tableWidget.setHorizontalHeaderItem(0,QTableWidgetItem("IP"))
                self.tableWidget.setHorizontalHeaderItem(1,QTableWidgetItem("Product"))
                self.tableWidget.setHorizontalHeaderItem(2,QTableWidgetItem("Version"))
                self.tableWidget.setHorizontalHeaderItem(3,QTableWidgetItem("Port"))
                self.tableWidget.setHorizontalHeaderItem(4,QTableWidgetItem("Organisation"))
                self.tableWidget.setHorizontalHeaderItem(5,QTableWidgetItem("Hostnames"))
                self.tableWidget.setHorizontalHeaderItem(6,QTableWidgetItem("Country"))
                self.tableWidget.setHorizontalHeaderItem(7,QTableWidgetItem("City"))
                self.tableWidget.setHorizontalHeaderItem(8,QTableWidgetItem("Timestamp"))
                self.tableWidget.selectionModel().selectionChanged.connect(self.row_selection)
                self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

                self.textArea = QPlainTextEdit(self)
                self.textArea.setReadOnly(True)
                layout.addWidget(self.tableWidget, stretch=1)
                layout.addWidget(self.textArea)
                self.tableWidget.setSortingEnabled(True)
                self.setLayout(layout)
                self.show()

        def row_selection(self, selected):
                for ix in selected.indexes():
                        self.parent().selected_table_row(ix.row())       
                        break

 
        def update_table(self, results):
               
                for index, result in enumerate(results['matches']):
                    hostnames = ""
                    if 'ip_str' in result:
                        self.tableWidget.setItem(index,0,QTableWidgetItem(result['ip_str']))
                    else:
                        self.tableWidget.setItem(index,0,QTableWidgetItem('NULL'))

                    if 'product' in result:
                        self.tableWidget.setItem(index,1,QTableWidgetItem(result['product']))
                    else:
                        self.tableWidget.setItem(index,1,QTableWidgetItem('NULL'))

                    if 'version' in result:
                        self.tableWidget.setItem(index,2,QTableWidgetItem(result['version']))
                    else:
                        self.tableWidget.setItem(index,2,QTableWidgetItem('NULL'))
    
                    if 'port' in result:
                        self.tableWidget.setItem(index,3,QTableWidgetItem(str(result['port'])))
                    else:
                        self.tableWidget.setItem(index,3,QTableWidgetItem('NULL'))

                    if 'org' in result:                
                        self.tableWidget.setItem(index,4,QTableWidgetItem(result['org']))
                    else:
                        self.tableWidget.setItem(index,4,QTableWidgetItem('NULL'))

                    if 'hostnames' in result:
                        if result['hostnames']:
                            for each in result['hostnames']:
                                if len(result['hostnames'])>1:
                                    hostnames += each + ", "
                                    hostnames = hostnames[:-2]
                                else:
                                    hostnames = each
                        else:
                            hostnames = 'NULL'
                    else:
                        hostnames = 'NULL'

                    self.tableWidget.setItem(index,5,QTableWidgetItem(hostnames))

                    if 'location' in result:
                        if 'country_name' in result['location']:
                            self.tableWidget.setItem(index,6,QTableWidgetItem(result['location']['country_name']))
                        else:
                            self.tableWidget.setItem(index,6,QTableWidgetItem('NULL'))
                        if 'city' in result['location']:
                            self.tableWidget.setItem(index,7,QTableWidgetItem(result['location']['city']))
                        else:
                            self.tableWidget.setItem(index,7,QTableWidgetItem('NULL'))

                    self.tableWidget.setItem(index,8,QTableWidgetItem(result['timestamp']))
                    
                      
                        
