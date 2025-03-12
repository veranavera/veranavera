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
    "ME": 10,
    "NH": 10,
    "VT": 10,
    "MA": 10,
    "RI": 10,
    "CT": 10,
    "NY": 10,
    "NJ": 10,
    "PA": 10,
    "DE": 10,
    "MD": 10,
    "VA": 10,
    "WV": 10,
    "KY": 10,
    "NC": 10,
    "TN": 10,
    "GA": 10,
    "AL": 10,
    "OH": 10,
    "IN": 10,
    "IL": 10,
    "MO": 10,
    "KS": 10,
    "TX": 10,
    "NM": 10,
    "AZ": 10,
    "UT": 10,
    "ID": 10,
    "OR": 10,
    "WA": 10,
    "EAST": 10,
    "WEST": 10,
    "NE115": 11,
    "SE202": 11,
    "NE131": 11,
    "LCL": 20,
    "OR78": 11,
    "ULTRA": 12,
    "P3K": 13,
    "P2K": 14,
    "P1K": 15,
    "STHP": 16,
    "STPP": 17,
    "STIP": 18,
    "STEP": 19,
    "NE67": 21,
    "ADK46": 22,
    "SE40": 23,
    "NYFT": 24,
    "EAP2K": 25,
    "VT35": 26,
    "CT35": 27,
    "BEL12": 28,
    "OSS10": 29,
    "NHFT": 30,
    "NEK20": 31,
    "LG12": 32,
    "SAR6": 33,
    "FUL3": 34,
    "TUP3": 35
}

project_lists = {
    "NE115": "../../project_lists/NE115/list_of_peaks_elevation.html",
    "n/a": "",
    "SE202": "../../project_lists/SE202/list_of_peaks_elevation.html",
    "SE202a": "../../project_lists/SE202/list_of_peaks_elevation.html",
    "NE131": "../../project_lists/NE131/list_of_peaks_prominence.html",
    "NE131a": "../../project_lists/NE131/list_of_peaks_prominence.html",
    "LCL": "../../project_lists/LCL/list_of_peaks_date_reverse.html",
    "OR78": "../../project_lists/OR78/list_of_peaks_prominence.html",
    "OR78a": "../../project_lists/OR78/list_of_peaks_prominence.html",
}
#define eastern/western regions of North America
    #with true meaning eastern and vice versa
regions = {
    "ME": True, "NH": True, "VT": True, "MA": True, "RI": True, "CT": True, "NY": True, "NJ": True, "PA": True, "DE": True, "MD": True, "VA": True, "VA/WV": True, "NC": True, "NC/TN": True, "SC": True, "GA": True, "FL": True, "AL": True, "MS": True, "LA": True, "AR": True, "TN": True, "KY": True,"KY/VA": True, "WV": True, "OH": True, "MI": True, "IN": True, "IL": True, "MO": True, "WI": True, "IA": True, "MN": True, "ND": True, "SD": True, "NE": True, "KS": True, "OK": True, "NL": True, "PE": True, "NS": True, "NB": True, "QC": True, "ON": True, "MB": True, "SK": True,
    "WA": False, "OR": False, "CA": False, "NV": False, "UT": False, "AZ": False, "NM": False, "TX": False, "CO": False, "WY": False, "MT": False, "ID": False, "AB": False, "BC": False, "YK": False, "AK": False
}

#define states/small regions 
states = {
    "ME": "maine",
    "NH": "new_hampshire",
    "VT": "vermont",
    "MA": "massachusetts",
    "RI": "rhode_island",
    "CT": "connecticut",
    "NY": "new_york",
    "NJ": "new_jersey",
    "PA": "pennsylvania",
    "DE": "delaware",
    "MD": "maryland",
    "VA": "virginia",
    "WV": "west_virginia",
    "VA/WV": "virginia",
    "KY": "kentucky",
    "KY/VA": "virginia",
    "NC": "north_carolina",
    "TN": "tennessee",
    "NC/TN": "north_carolina",
    "GA": "georgia",
    "AL": "alabama",
    "OH": "ohio",
    "IN": "indiana",
    "IL": "illinois",
    "MO": "missouri",
    "KS": "kansas",
    "TX": "texas",
    "NM": "new_mexico",
    "AZ": "arizona",
    "UT": "utah",
    "ID": "idaho",
    "OR": "oregon",
    "WA": "washington",
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
                if(list_types[list] > 11 and row[list_types[list]] == "y"):
                    total += 1
                elif(row[11] == list):
                    total += 1
                elif(list == row[10] or list in row[10]):
                    total += 1
                elif(list == "EAST" and regions[row[10]]):
                    total += 1
                elif(list == "WEST" and not regions[row[10]]):
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
    line += "<th class = \"prominence\">" + str(row[4]) + "</th>\n\t\t\t"
    line += "<th class = \"isolation\">" + str(row[7]) + "</th>\n\t\t\t"
    line += "<th class = \"date\"><a href=\"" + row[9] + "\">" + row[8] + "</a></th>\n\t\t\t"
    line += "<th class = \"location\"><a class=\"location\"; href=\"../../state_lists/" + states[row[10]] + "_all/list_of_peaks_date_reverse.html\">" + row[10] + "</a></th>\n\t\t\t"
    line += "<th class = \"list\"><a class=\"list\"; href=\"" + project_lists[row[11]] + "\">" + row[11] + "</a></th>\n\t\t"
    line += "</tr>\n\t\t"
    return line

def csv_reader(sortTypes, sortCounter, sortCounters, sortOrders, reverse, list, listNumber):
    htmlData = ""

    with open(csv_filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(data)
        counter = 0
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
            elif(list_types[list] > 11 and row[list_types[list]] == "y"):
                line = output_row(row, counter, reverse, False, listNumber)
                htmlData += line
                counter += 1
            elif(row[11] == list or row[11] == (list + "a")):
                if((row[11][len(row[11]) - 1]) == "a"):
                    line = output_row(row, counter, reverse, True, 0)
                    counter -= 1
                else:
                    line = output_row(row, counter, reverse, False, listNumber)
                htmlData += line
                counter += 1
            elif(list == "EAST" and regions[row[10]]):
                line = output_row(row, counter, reverse, False, listNumber)
                htmlData += line
                counter += 1
            elif(list == "WEST" and not regions[row[10]]):
                line = output_row(row, counter, reverse, False, listNumber)
                htmlData += line
                counter += 1
            elif(list == row[10] or list in row[10]):
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
    sortCounters = [0, 2, 4, 7, 8, 10, 11]
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

    baseText = Path(base_filename).read_text()

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

    directories = ["trip_reports/long_covid_reports/", "trip_reports/northeast_131_reports/", "trip_reports/southeast_202_reports/",
                   "trip_reports/northeast_115_reports/", "trip_reports/miscellaneous_reports/"]
    directory = directories[0]
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

def format_csv_file():
    #vera, when you climb your first 14er/P10k, update this code to run on the comas in the prominence section to you overachiever you :)
    with open(csv_filename, "r+") as file:
        data = file.read()
    comma_number = 31
    lines = data.split("\n")
    new_data = ""
    for line in lines:
        if(line.count(",") > comma_number):
            values = line.split(",")
            print(values)
            value = values[2] + values[3]
            value.strip("\"")
            value = value[1:len(value)-1]
            vals = ""
            for val in values:
                if(val == values[2] or val == values[3]):
                    if(values[2] == val):
                        vals += value + ","
                        print(value)
                else:
                    vals += val + ","
            print(vals)
            new_data += vals + "\n"
        else:
            new_data += line + "\n"
    with open(csv_filename, "r+") as file:
        file.write(new_data)
        file.truncate()
        file.close()

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
    fileNames = os.listdir("../" + directories[3])
    tripReportLink = ""
    for file in fileNames:
        if(tripReportLink < file):
            tripReportLink = file

#update main page
update_main_page("../index.html")

#format csv file
#format_csv_file()

#create list of peaks and comment the ones that are "finished"
def make_lists():
    #master list
    list_of_peaks("basic_list.html", "all/all", "")

    #current project
    list_of_peaks("list_of_oregon_78.html", "project_lists/OR78", "OR78")

    #eastern vs western
    #list_of_peaks("list_of_eastern.html", "all/eastern_all", "EAST")
    #list_of_peaks("list_of_western.html", "all/western_all", "WEST")
    list_of_peaks("list_of_new_york.html", "state_lists/new_york_all", "NY")
    list_of_peaks("list_of_vermont.html", "state_lists/vermont_all", "VT")
    list_of_peaks("list_of_new_hampshire.html", "state_lists/new_hampshire_all", "NH")
    list_of_peaks("list_of_maine.html", "state_lists/maine_all", "ME")

    #all lists of prominence/location classes
    #list_of_peaks("list_of_p1ks.html", "all/all_p1k", "P1K")
    #list_of_peaks("list_of_p2ks.html", "all/all_p2k", "P2K")
    #list_of_peaks("list_of_p3ks.html", "all/all_p3k", "P3K")
    #list_of_peaks("list_of_ultras.html", "all/all_ultra", "ULTRA")
make_lists()

#useful function lines


    #all lists of prominence/location classes
    #list_of_peaks("list_of_p1ks.html", "all/all_p1k", "P1K")
    #list_of_peaks("list_of_p2ks.html", "all/all_p2k", "P2K")
    #list_of_peaks("list_of_p3ks.html", "all/all_p3k", "P3K")
    #list_of_peaks("list_of_ultras.html", "all/all_ultra", "ULTRA")

    #tripple points
    #list_of_peaks("list_of_state_epic_points.html", "official_lists/STEP", "STEP")
    #list_of_peaks("list_of_state_high_points.html", "official_lists/STHP", "STHP")
    #list_of_peaks("list_of_state_prominent_points.html", "official_lists/STPP", "STPP")
    #list_of_peaks("list_of_state_isolation_points.html", "official_lists/STIP", "STIP")

    #state lists
    #list_of_peaks("list_of_new_hampshire.html", "state_lists/new_hampshire_all", "NH")

    #previous projects
    #list_of_peaks("list_of_long_covid_list.html", "project_lists/LCL", "LCL")
    #list_of_peaks("list_of_northeast_131.html", "project_lists/NE131", "NE131")
    #list_of_peaks("list_of_southeast_202.html", "project_lists/SE202", "SE202")
    #list_of_peaks("list_of_northeast_115.html", "project_lists/NE115", "NE115")

    #previous official lists
    #list_of_peaks("list_of_new_england_67.html", "official_lists/NE67", "NE67")
    #list_of_peaks("list_of_adirondack_46.html", "official_lists/ADK46", "ADK46")
    #list_of_peaks("list_of_southern_sixers.html", "official_lists/SE40", "SE40")
    #list_of_peaks("list_of_ny_fire_towers.html", "official_lists/NYFT", "NYFT")

    #list_of_peaks("list_of_belknap_12.html", "official_lists/BEL12", "BEL12")
    #list_of_peaks("list_of_tupper_triad.html", "official_lists/TUP3", "TUP3")
    #list_of_peaks("list_of_fulton_trifecta.html", "official_lists/FUL3", "FUL3")
    
    #current active official lists
    #list_of_peaks("list_of_eastern_p2ks.html", "official_lists/EAP2K", "EAP2K")
    #list_of_peaks("list_of_catskill_35.html", "official_lists/CT35", "CT35")
    #list_of_peaks("list_of_vermont_35.html", "official_lists/VT35", "VT35")
    #list_of_peaks("list_of_northeast_kingdom.html", "official_lists/NEK20", "NEK20")

    #list_of_peaks("list_of_nh_fire_towers.html", "official_lists/NHFT", "NHFT")
    #list_of_peaks("list_of_lake_george_12.html", "official_lists/LG12", "LG12")
    #list_of_peaks("list_of_ossipee_10.html", "official_lists/OSS10", "OSS10")

    #state pages
    
    #list_of_peaks("list_of_virginia.html", "state_lists/virginia_all", "VA")
    #list_of_peaks("list_of_tennessee.html", "state_lists/tennessee_all", "TN")
    #list_of_peaks("list_of_north_carolina.html", "state_lists/north_carolina_all", "NC")
    #list_of_peaks("list_of_west_virginia.html", "state_lists/west_virginia_all", "WV")
    #list_of_peaks("list_of_texas.html", "state_lists/texas_all", "TX")
    #list_of_peaks("list_of_new_jersey.html", "state_lists/new_jersey_all", "NJ")