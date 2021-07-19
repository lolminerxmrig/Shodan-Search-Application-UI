import shodan
import sys, re
import pycountry
import csv
import os.path

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont
from PyQt5.QtCore import Qt
from Table import *
from Search import *
from Tips import *



SHODAN_API_KEY = 'YOUR API KEY'
HEIGHT = 800
WIDTH = 1000

api = shodan.Shodan(SHODAN_API_KEY)

class Application(QWidget):

        def __init__(self, parent=None):
                super(Application, self).__init__(parent)
                self.initUI()
                self.search_query = ''
                self.page_number = 1
                self.total_pages = 0
                self.search_results = []
                self.file_name_counter = 0

        def initUI(self):
                self.setWindowTitle('Shodan Search Application UI')
                self.resize(WIDTH, HEIGHT)
                
                self.palette = QPalette()
                self.palette.setColor(QPalette.Window, QColor(119, 193, 255))
                self.setPalette(self.palette)
                
                self.add_widgets()
                self.show()

        def add_widgets(self):
        
                layout = QVBoxLayout()

                self.SearchWidget = Search(self)
                self.TableWidget = Table(self)

                layout.addWidget(self.SearchWidget)
                layout.addWidget(self.TableWidget)

                self.setLayout(layout)

        def open_tips_widget(self):
                self.TipsWidget = Tips(self)


        def check_text_fields(self):
                search_string = ""
                
                if not self.SearchWidget.textbox_gen_search.text() == "":
                        search_string += self.SearchWidget.textbox_gen_search.text()
                #len(self.SearchWidget.textbox_country.text())< 4 and 
                if len(self.SearchWidget.textbox_country.text()) > 2:
                        search_string += " country:"+ self.get_country(self.SearchWidget.textbox_country.text())
                elif len(self.SearchWidget.textbox_country.text()) == 2:
                        search_string += " country:"+ self.SearchWidget.textbox_country.text()
        
                       
                if re.match(r'[a-zA-ZåäöÅÄÖ ]+$', self.SearchWidget.textbox_city.text()):
                        search_string += " city:"+self.SearchWidget.textbox_city.text()
                else:
                        self.SearchWidget.textbox_city.setText('')

                if not self.SearchWidget.textbox_org.text() == "":
                        search_string += " org:"+self.SearchWidget.textbox_org.text()

                if re.match(r'[0-9.]+$', self.SearchWidget.textbox_ip.text()):
                        search_string += " ip_str:"+self.SearchWidget.textbox_ip.text()
                else:
                        self.SearchWidget.textbox_ip.setText('')

                if re.match(r'[0-9,]+$', self.SearchWidget.textbox_port.text()):
                        search_string += " port:"+self.SearchWidget.textbox_port.text()
                else:
                        self.SearchWidget.textbox_port.setText('')


                self.search_query = search_string
                self.page_number = 1
                self.shodan_search_request(search_string, self.page_number)

        def shodan_search_request(self, search, pagenr):
                
                self.clean_table()
                try:
                        
                        results = api.search(search, page=pagenr)
                        self.search_results = results['matches']
                        self.total_pages = results['total']
                        self.TableWidget.update_table(results)
                        self.SearchWidget.label_pagenr.setText('Page {}/{}'.format(pagenr, self.total_pagenrs(self.total_pages)))
                        self.SearchWidget.label_totalresults.setText('Results: {}'.format(self.total_pages))
                        
                except shodan.APIError as e:
                        self.SearchWidget.label_totalresults.setText('ERROR: {}'.format(e))
                        self.search_results = []

                                  
        def previous_page(self):
                if self.page_number > 1:
                        self.page_number -= 1
                        self.shodan_search_request(self.search_query, self.page_number)
                

        def next_page(self):
                
                if self.page_number <= self.total_pagenrs(self.total_pages):
                        self.page_number += 1
                        self.shodan_search_request(self.search_query, self.page_number)
                        
        def total_pagenrs(self, totalres):
                if totalres % 100 == 0 or totalres % 100 > 50:
                        return round(totalres/100)   
                else:
                        return round(totalres / 100) + 1
              
        def clean_table(self):
                for i in range(100):
                    self.TableWidget.tableWidget.setItem(i,0,QTableWidgetItem(''))
                    self.TableWidget.tableWidget.setItem(i,1,QTableWidgetItem(''))
                    self.TableWidget.tableWidget.setItem(i,2,QTableWidgetItem(''))
                    self.TableWidget.tableWidget.setItem(i,3,QTableWidgetItem(''))
                    self.TableWidget.tableWidget.setItem(i,4,QTableWidgetItem(''))
                    self.TableWidget.tableWidget.setItem(i,5,QTableWidgetItem(''))
                    self.TableWidget.tableWidget.setItem(i,6,QTableWidgetItem(''))
                    self.TableWidget.tableWidget.setItem(i,7,QTableWidgetItem(''))
                    self.TableWidget.tableWidget.setItem(i,8,QTableWidgetItem(''))

        def selected_table_row(self, row):
                self.TableWidget.textArea.clear()
                
                if not len(self.search_results) == 0:
                        for each in self.search_results[row]:

                                self.TableWidget.textArea.insertPlainText(each + ": " + str(self.search_results[row][each]) +"\n")

        def get_country(self, country):
                try:
                        temp = str(pycountry.countries.search_fuzzy(country)).split(', ')[0]
                        temp = temp.split("'")[1]
                        return temp
                except:
                        return country
                
        def check_file_exists(self, filename):
                if os.path.isfile(filename):
                        self.file_name_counter += 1                        
                        return self.check_file_exists(filename[:-4] + " " + str(self.file_name_counter) + '.csv')
                else:
                        return filename

        def call_messagebox(self, title, text, icon):
                msg = QMessageBox()
                msg.setIcon(icon)
                msg.setText(text)
                msg.setWindowTitle(title)
                msg.exec_()
                

        def export_to_csv(self):
                header_list = header_list = ['IP', 'Product', 'Version', 'Port', 'Org', 'Hostnames', 'Country', 'City', 'Timestamp']

                temp_list_large = []
                if self.search_results:
                        for each in self.search_results:
                                temp_list_minor = []
                                if 'ip_str' in each:
                                        temp_list_minor.append(each['ip_str'])
                                else:
                                        temp_list_minor.append('NULL')
                                if 'product' in each:
                                        temp_list_minor.append(each['product'])
                                else:
                                        temp_list_minor.append('NULL')

                                if 'version' in each:
                                        temp_list_minor.append(each['version'])
                                else:
                                        temp_list_minor.append('NULL')
         
                                if 'port' in each:
                                        temp_list_minor.append(str(each['port']))
                                else:
                                        temp_list_minor.append('NULL')
                                if 'org' in each:
                                        temp_list_minor.append(each['org'])
                                else:
                                        temp_list_minor.append('NULL')
                                if 'hostnames' in each:
                                        temp_list_minor.append(each['hostnames'])
                                else:
                                        temp_list_minor.append('NULL')
                                if 'location' in each:
                                        if 'country_name' in each['location']:
                                                temp_list_minor.append(each['location']['country_name'])
                                        else:
                                                temp_list_minor.append('NULL')
                                        if 'city' in each['location']:
                                                temp_list_minor.append(each['location']['city'])
                                        else:
                                                temp_list_minor.append('NULL')
                                else:
                                        temp_list_minor.append('NULL')
                                        temp_list_minor.append('NULL')
                                if 'timestamp' in each:
                                        temp_list_minor.append(each['timestamp'])
                                else:
                                        temp_list_minor.append('NULL')

                                temp_list_large.append(temp_list_minor)

                        filename = 'Exported Shodan Search.csv'
                        filename = self.check_file_exists(filename)
                        try:
                                with open(filename, 'w', encoding='UTF8', newline='') as f:
                                    writer = csv.writer(f)
                                    writer.writerow(header_list)
                                    writer.writerows(temp_list_large)

                                self.call_messagebox('CSV Export', "'{}' was successfully exported.".format(filename), QMessageBox.Information) 
                                
                                
                        except:
                                self.call_messagebox('Error - CSV Export', "An error occurred exporting to CSV.", QMessageBox.Critical) 
                else:
                        self.call_messagebox('CSV Export', "There are no results to export.", QMessageBox.Information) 
                                
                            
           

def main():
    app = QApplication(sys.argv)
    mw = Application()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

