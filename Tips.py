import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont
from PyQt5.QtCore import Qt
from Table import *
from Search import *
from Application import *


HEIGHT = 250
WIDTH = 600

class Tips(QWidget):

        def __init__(self, parent):
                super().__init__()
                self.infotext = "This application acts as a substitute to Shodan's web engine. It's meant to facilitate searches with the filter fields and provide with a tabular overview of the results "
                self.infotext2 = "Each search is one query, and Shodan uses credits where each search containing a filter, or specified page of a search, 'costs' one credit. Thus, searches conducted by only entering words in the 'Keyword' filter does not cost any credits. "
                self.infotext3 = "Though the queries are sent to Shodans API, using a VPN is always recommended. More information about Shodans queries and credits can be found via the link below. "
                self.infotext4 = "The filter fields in the application translate to Shodan's established filter names such as 'Organisation' == 'org'. These that are used in the search query to Shodans API "
                self.infotext5 = "These shodan filters can also be used in the 'Keyword' field. For instance, in that field you may add 'Apache' but to that you can also add 'port:80', 'city:stockholm' etc. "
                self.infotext6 = "There are other filters that may be used by higher premium plans from Shodan. The complete list of filters can be found via the link below. "
                
                self.initUI(parent)

        
        def initUI(self, parent):                
                layout = QGridLayout()

                self.setWindowTitle('Shodan Tips')
                self.resize(WIDTH, HEIGHT)
                
                self.palette = QPalette()
                self.palette.setColor(QPalette.Window, QColor(119, 193, 255))
                self.setPalette(self.palette)
                
                self.info_textarea = QPlainTextEdit(self)
                self.info_textarea.setReadOnly(True)

                self.info_textarea2 = QPlainTextEdit(self)
                self.info_textarea2.setReadOnly(True)

                self.info_textarea.insertPlainText(self.infotext)
                self.info_textarea.insertPlainText(self.infotext2)
                self.info_textarea.insertPlainText(self.infotext3)

                self.info_textarea2.insertPlainText(self.infotext4)
                self.info_textarea2.insertPlainText(self.infotext5)
                self.info_textarea2.insertPlainText(self.infotext6)

                self.label_usage = QLabel('USAGE' ,self)
                self.label_usage.setFont(QFont('Consolas', 13))
                
                self.label_filters = QLabel('FILTERS' ,self)
                self.label_filters.setFont(QFont('Consolas', 13))


                urlLinkInfo="<a href=\"https://help.shodan.io/the-basics/credit-types-explained\">QUERIES INFO</a>" 

                self.label_queryinfo = QLabel(urlLinkInfo,self)
                self.label_queryinfo.setFont(QFont('Consolas', 10))
                self.label_queryinfo.setAlignment(Qt.AlignCenter)
                self.label_queryinfo.setOpenExternalLinks(True)

                urlLinkFilters="<a href=\"https://beta.shodan.io/search/filters\">LIST OF FILTERS</a>" 
                self.label_list_filters = QLabel(urlLinkFilters,self)
                self.label_list_filters.setFont(QFont('Consolas', 10))
                self.label_list_filters.setAlignment(Qt.AlignCenter)
                self.label_list_filters.setOpenExternalLinks(True)

                layout.addWidget(self.label_usage,0,0)
                layout.addWidget(self.info_textarea,1,0)
                layout.addWidget(self.label_filters,0,1)
                layout.addWidget(self.info_textarea2, 1,1)
                
                layout.addWidget(self.label_queryinfo,2,0)
                layout.addWidget(self.label_list_filters, 2,1)
                
                self.setLayout(layout)


                
                self.show()
