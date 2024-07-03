import csv
import operator
from pathlib import Path
from datetime import datetime
import os

#define data filename
csv_filename = "list_of_peaks.csv"

#define file splice point
splicer = "<!---splicer-->"

#define list column values
list_types = {
    "EAST": 7,
    "WEST": 7,
    "NE115": 8,
    "SE202": 8,
    "NE131": 8,
    "ULTRA": 9,
    "P3K": 10,
    "P2K": 11,
    "P1K": 12,
    "STHP": 13,
    "STPP": 14,
    "STIP": 15,
    "STEP": 16,
    "NE67": 17,
    "ADK46": 18,
    "SE40": 19,
    "NYFT": 20,
    "EAP2K": 21,
    "VT35": 22,
    "CT35": 23,
    "BEL12": 24,
    "OSS10": 25,
    "NHFT": 26,
    "NEK20": 27,
    "LG12": 28,
    "SAR6": 29,
    "FUL3": 30,
    "TUP3": 31
}

#define eastern/western regions of North America
    #with true meaning eastern and vice versa
regions = {
    "ME": True, "NH": True, "VT": True, "MA": True, "RI": True, "CT": True, "NY": True, "NJ": True, "PA": True, "DE": True, "MD": True, "VA": True, "VA/WV": True, "NC": True, "NC/TN": True, "SC": True, "GA": True, "FL": True, "AL": True, "MS": True, "LA": True, "AR": True, "TN": True, "KY": True,"KY/VA": True, "WV": True, "OH": True, "MI": True, "IN": True, "IL": True, "MO": True, "WI": True, "IA": True, "MN": True, "ND": True, "SD": True, "NE": True, "KS": True, "OK": True, "NL": True, "PE": True, "NS": True, "NB": True, "QC": True, "ON": True, "MB": True, "SK": True,
    "WA": False, "OR": False, "CA": False, "NV": False, "UT": False, "AZ": False, "NM": False, "TX": False, "CO": False, "WY": False, "MT": False, "ID": False, "AB": False, "BC": False, "YK": False, "AK": False
}

#define total number of peaks 
def count_peaks(list):
    with open(csv_filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(data)
        if(not list):
            total = sum(1 for row in data)
        else:
            total = 0
            for row in data:
                if(list_types[list] > 8 and row[list_types[list]] == "y"):
                    total += 1
                elif(row[8] == list):
                    total += 1
                elif(list == "EAST" and regions[row[7]]):
                    total += 1
                elif(list == "WEST" and not regions[row[7]]):
                    total += 1
    #add one to the total as a way of making the code function better in csv_reader()
    return total + 1
total = count_peaks("")

def base_file_reader(base_filename, directory):
    #reads base .html file for generating list of peak pages and outputs the beginning of that file
    base_text =  Path(directory + "/" + base_filename).read_text()
    return base_text[slice(0, base_text.find(splicer))]

def add_table_header(links, sortCounter):
    tableHeader = "</div>\n<div style=\"width: 100%; display: table;\">\n\t<table style=\"width:100%\">\n\t\t<tr>\n\t\t\t<th class=\"number\"><a href=\""
    tableHeader += links[sortCounter][2] + "\" class=\"number\">Number &#8645</a></th>\n\t\t\t<th><a href=\""
    tableHeader += links[sortCounter][0] + "\" class=\"name\">Name &#8645</a></th>\n\t\t\t<th><a href=\""
    tableHeader += links[sortCounter][1] + "\" class=\"elevation\">Elevation (ft) &#8645</a></th>\n\t\t\t<th><a href=\"" 
    tableHeader += links[sortCounter][2] + "\" class=\"prominence\">Prominence (ft) &#8645</a></th>\n\t\t\t<th><a href=\""
    tableHeader += links[sortCounter][3] + "\" class=\"isolation\">Isolation (km) &#8645</a></th>\n\t\t\t<th><a href=\""
    tableHeader += links[sortCounter][4] + "\" class=\"date\">Date Climbed &#8645</a></th>\n\t\t\t<th><a href=\""
    tableHeader += links[sortCounter][5] + "\" class=\"location\">State &#8645</a></th>\n\t\t\t<th><a href=\""
    tableHeader += links[sortCounter][6] + "\"class=\"list\">Peak on List &#8645</a></th>\n\t\t</tr>\n\t\t"
    return tableHeader

def add_table_header_reverse(directory):
    tableHeader = "</div>\n<div style=\"width: 100%; display: table;\">\n\t<table style=\"width:100%\">\n\t\t<tr>\n\t\t\t<th class=\"number\"><a href=\""
    tableHeader += "list_of_peaks_prominence.html\" class=\"number\">Number &#8645</a></th>\n\t\t\t<th><a href=\""
    tableHeader += "list_of_peaks_name.html\" class=\"name\">Name &#8645</a></th>\n\t\t\t<th><a href=\""
    tableHeader += "list_of_peaks_elevation.html\" class=\"elevation\">Elevation (ft) &#8645</a></th>\n\t\t\t<th><a href=\""
    tableHeader += "list_of_peaks_prominence.html\" class=\"prominence\">Prominence (ft) &#8645</a></th>\n\t\t\t<th><a href=\""
    tableHeader += "list_of_peaks_isolation.html\" class=\"isolation\">Isolation (km) &#8645</a></th>\n\t\t\t<th><a href=\""
    tableHeader += "list_of_peaks_date.html\" class=\"date\">Date Climbed &#8645</a></th>\n\t\t\t<th><a href=\""
    tableHeader += "list_of_peaks_location.html\" class=\"location\">State &#8645</a></th>\n\t\t\t<th><a href=\""
    tableHeader += "list_of_peaks_list.html\"class=\"list\">Peak on List &#8645</a></th>\n\t\t</tr>\n\t\t"
    return tableHeader

def add_footer():
    footer = "\n\t</table>\n</div>\n<div>\n\t<iframe class=\"page_footer\" frameBorder=\"0\" src=\"../../../formatting_files/footer.html\" seamless></iframe>\n</div>\n</body>"
    return footer

def output_row(row, counter, reverse, unranked, total):
    line = "<tr>\n\t\t\t"
    if(unranked):
        line += "<th class = \"number\">" + "&#183" + "</th>\n\t\t\t"
    elif(reverse):
        line += "<th class = \"number\">" + str(total - counter) + "</th>\n\t\t\t"
    else:
        line += "<th class = \"number\">" + str(counter) + "</th>\n\t\t\t"
    line += "<th class = \"name\"><a href=\"" + row[1] + "\">" + row[0] + "</a></th>\n\t\t\t"
    line += "<th class = \"elevation\">" + str(row[2]) + "</th>\n\t\t\t"
    line += "<th class = \"prominence\">" + str(row[3]) + "</th>\n\t\t\t"
    line += "<th class = \"isolation\">" + str(row[4]) + "</th>\n\t\t\t"
    line += "<th class = \"date\"><a href=\"" + row[6] + "\">" + row[5] + "</a></th>\n\t\t\t"
    line += "<th class = \"location\">" + row[7] + "</th>\n\t\t\t"
    line += "<th class = \"list\">" + row[8] + "</th>\n\t\t"
    line += "</tr>\n\t\t"
    return line

def csv_reader(sortTypes, sortCounter, sortCounters, sortOrders, reverse, list, listNumber):
    htmlData = ""

    with open(csv_filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(data)
        if(reverse):
            if(sortTypes[sortCounter]):
                sortedData = sorted(data, key=lambda x: float(x[sortCounters[sortCounter]]), reverse=not sortOrders[sortCounter])
            else:
                sortedData = sorted(data, key=operator.itemgetter(sortCounters[sortCounter]), reverse=not sortOrders[sortCounter])
        else:
            if(sortTypes[sortCounter]):
                sortedData = sorted(data, key=lambda x: float(x[sortCounters[sortCounter]]), reverse=sortOrders[sortCounter])
            else:
                sortedData = sorted(data, key=operator.itemgetter(sortCounters[sortCounter]), reverse=sortOrders[sortCounter])
        counter = 1
        for row in sortedData:
            if(not list):
                line = output_row(row, counter, reverse, False, total)
                htmlData += line
                counter += 1
            elif(list_types[list] > 8 and row[list_types[list]] == "y"):
                line = output_row(row, counter, reverse, False, listNumber)
                htmlData += line
                counter += 1
            elif(row[8] == list or row[8] == (list + "a")):
                if((row[8][len(row[8]) - 1]) == "a"):
                    line = output_row(row, counter, reverse, True, 0)
                    counter -= 1
                else:
                    line = output_row(row, counter, reverse, False, listNumber)
                htmlData += line
                counter += 1
            elif(list == "EAST" and regions[row[7]]):
                line = output_row(row, counter, reverse, False, listNumber)
                htmlData += line
                counter += 1
            elif(list == "WEST" and not regions[row[7]]):
                line = output_row(row, counter, reverse, False, listNumber)
                htmlData += line
                counter += 1
        
    return htmlData

def list_of_peaks(base_filename, directory, list):

    #create number of peaks on the list
    listNumber = count_peaks(list)
    
    #list the parameters that the lists will sort for
    sorts = ["name", "elevation", "prominence", "isolation", "date", "location", "list"]

    #create a list of filenames for each parameter for ascending and descending
    links = [sorts.copy(), sorts.copy(), sorts.copy(), sorts.copy(), sorts.copy(), sorts.copy(), sorts.copy()]
    for x in range(0, 7):
        for y in range(0,7):
            # and len(links[x][y]) < 42 and len(links[x][y]) > 34
            if(x == y and not "." in links[x][y]):
                links[x][y] = "list_of_peaks_" + links[x][y] + "_reverse.html"
            elif(not "." in links[x][y]):
                links[x][y] = "list_of_peaks_" + links[x][y] + ".html"

    #manually input which parameters should be sorted for 
    sortCounters = [0, 2, 3, 4, 5, 7, 8]
    #change date here for different ordering priorities
    sortOrders = [False, True, True, True, False, False, True]
    sortTypes = [False, True, True, True, False, False, False]
    sortCounter = 0

    for type in sorts:
        #make normal page
        htmlData = base_file_reader(base_filename, directory)
        htmlData += add_table_header(links, sortCounter)
        htmlData += csv_reader(sortTypes, sortCounter, sortCounters, sortOrders, False, list, listNumber)
        htmlData += add_footer()

        f = open(directory + "\list_of_peaks_" + type + ".html", "w")
        f.write(htmlData)
        f.close()

        #make reverse page
        htmlData = base_file_reader(base_filename, directory)
        htmlData += add_table_header_reverse(directory)
        htmlData += csv_reader(sortTypes, sortCounter, sortCounters, sortOrders, True, list, listNumber)
        htmlData += add_footer()

        f = open(directory + "\list_of_peaks_" + type + "_reverse.html", "w")
        f.write(htmlData)
        f.close()

        sortCounter += 1

def update_main_page(base_filename):
    #updates main page with date, peaks climbed, and trip reports

    baseText =  Path(base_filename).read_text()

    #update with current date
    date = datetime.today().strftime('%Y-%m-%d')
    index = baseText.find("<!---date-->")
    outputText = baseText[:index - 10] + date + baseText[index:]

    #update total number of peak mentions
    totalIndices = ["<!---firstTotal-->", "<!---secondTotal-->", "<!---thirdTotal-->"]
    for totalIndex in totalIndices:
        index = outputText.find(totalIndex)
        outputText = outputText[:index - 3] + str(total - 1) + outputText[index:]
        
    #update trip report link
    directory = "trip_reports/northeast_131_reports/"
    fileNames = os.listdir("../" + directory)
    tripReportLink = ""
    for file in fileNames:
        if(tripReportLink < file):
            tripReportLink = file
    tripReportLink = directory + tripReportLink
    beginIndex = outputText.find("<!---beginTripReport-->")
    endIndex = outputText.find("<!---endTripReport-->")
    outputText = outputText[:beginIndex + 23] + "<a href=\"" + tripReportLink + "\">" + outputText[endIndex:]

    f = open(base_filename, "w")
    f.write(outputText)
    f.close()

def update_trip_index(base_filename):
    #updates trip report index with new reports

    baseText = Path(base_filename).read_text()

    directories = ["trip_reports/northeast_131_reports/", "trip_reports/southeast_202_reports/",
                   "trip_reports/northeast_115_reports/", "trip_reports/miscellaneous_reports/"]

    #update with current date
    date = datetime.today().strftime('%Y-%m-%d')
    index = baseText.find("<!---date-->")
    outputText = baseText[:index - 10] + date + baseText[index:]

    #update trip report link
    directory = "trip_reports/northeast_131_reports/"
    fileNames = os.listdir("../" + directory)
    tripReportLink = ""
    for file in fileNames:
        if(tripReportLink < file):
            tripReportLink = file


#update main page
update_main_page("../index.html")

#create list of peaks and comment the ones that are "finished"
def make_lists():
    #master list
    list_of_peaks("basic_list.html", "all/all", "")

    #current project
    list_of_peaks("list_of_northeast_131.html", "project_lists/NE131", "NE131")

    #eastern vs western
    list_of_peaks("list_of_eastern.html", "all/eastern_all", "EAST")
    #list_of_peaks("list_of_western.html", "all/western_all", "WEST")

    #all lists of prominence/location classes
    list_of_peaks("list_of_p1ks.html", "all/all_p1k", "P1K")
    list_of_peaks("list_of_p2ks.html", "all/all_p2k", "P2K")
    #list_of_peaks("list_of_p3ks.html", "all/all_p3k", "P3K", 16 + 1)
    #list_of_peaks("list_of_ultras.html", "all/all_ultra", "ULTRA", 3 + 1)

    #state lists
    #list_of_peaks("list_of_state_epic_points.html", "official_lists/STEP", "STEP", 20 + 1)
    #list_of_peaks("list_of_state_high_points.html", "official_lists/STHP", "STHP", 12 + 1)
    #list_of_peaks("list_of_state_prominent_points.html", "official_lists/STPP", "STPP", 13 + 1)
    #list_of_peaks("list_of_state_isolation_points.html", "official_lists/STIP", "STIP", 11 + 1)

    #current active official lists
    list_of_peaks("list_of_eastern_p2ks.html", "official_lists/EAP2K", "EAP2K")
    #list_of_peaks("list_of_ny_fire_towers.html", "official_lists/NYFT", "NYFT", 30 + 1)
    #list_of_peaks("list_of_catskill_35.html", "official_lists/CT35", "CT35", 33 + 1)
    #list_of_peaks("list_of_vermont_35.html", "official_lists/VT35", "VT35", 30 + 1)
    #list_of_peaks("list_of_northeast_kingdom.html", "official_lists/NEK20", "NEK20", 20 + 1)

    list_of_peaks("list_of_nh_fire_towers.html", "official_lists/NHFT", "NHFT")
    #list_of_peaks("list_of_lake_george_12.html", "official_lists/LG12", "LG12", 12 + 1)
    list_of_peaks("list_of_ossipee_10.html", "official_lists/OSS10", "OSS10")

    #previous projects
    #list_of_peaks("list_of_southeast_202.html", "project_lists/SE202", "SE202", 202 + 1)
    #list_of_peaks("list_of_northeast_115.html", "project_lists/NE115", "NE115", 115 + 1)

    #previous official lists
    #list_of_peaks("list_of_new_england_67.html", "official_lists/NE67", "NE67", 67 + 1)
    #list_of_peaks("list_of_adirondack_46.html", "official_lists/ADK46", "ADK46", 46 + 1)
    #list_of_peaks("list_of_southern_sixers.html", "official_lists/SE40", "SE40", 40 + 1)

    #list_of_peaks("list_of_belknap_12.html", "official_lists/BEL12", "BEL12", 12 + 1)
    #list_of_peaks("list_of_tupper_triad.html", "official_lists/TUP3", "TUP3", 3 + 1)
    #list_of_peaks("list_of_fulton_trifecta.html", "official_lists/FUL3", "FUL3", 3 + 1)
make_lists()

list_of_peaks("list_of_western.html", "all/western_all", "WEST")