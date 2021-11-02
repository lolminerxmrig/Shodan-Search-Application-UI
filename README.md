# Shodan-Search-Application-UI
The Shodan Search Application UI is meant to facilitate shodan searches with filter fields and presenting the results in a tabular view. The project was mainly meant to test the PyQt5 Table widget and to try out Shodans python api module. 

##
The Application file is the main file. Even though the API calls are directed towards shodan, using a VPN is always recommended. The application itself does NOT interact with the identified nodes/addresses. Rather, it only presents the data retrieved from Shodan in a tabular format. The results are presented with 100 nodes at a time. To view 100 more, you have to view the following page. However, Shodan uses credits for the queries, and adding a value to a filter, or changing the page will cost 1 query credit. So as a Warning, this UI makes making queries alot easier and faster, which will consume the credits faster than you think. When a row is selected, additional data is presented in the text area to the right of the table. The additional data can be CVE's, response headers etc. (Basically all the other data that is retrieved from the API call that is not showed in the table.). The images below shows the UI before and after a search. 

Image with results:
![alt text](https://github.com/H4NM/Shodan-Search-Application-UI/blob/main/img/ShodanSearchUIWithResults.png)
