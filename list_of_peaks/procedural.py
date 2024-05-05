import csv
import operator
from pathlib import Path

#define data filename
csv_filename = "list_of_peaks.csv"

#define file splice point
splicer = "<!---splicer-->"

#define total number of peaks 
def count_total_peaks():
    with open(csv_filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        total = sum(1 for row in data)
    return total
total = count_total_peaks()

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
    return "\n\t</table>\n</div>\n<div>\n\t<iframe class=\"page_footer\" frameBorder=\"0\" src=\"../../formatting_files/footer.html\" seamless></iframe>\n</div>\n</body>"

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
            elif(row[8] == list or row[8] == (list + "a")):
                if((row[8][len(row[8]) - 1]) == "a"):
                    line = output_row(row, counter, reverse, True, 0)
                    counter -= 1
                else:
                    line = output_row(row, counter, reverse, False, listNumber)
                htmlData += line
                counter += 1
        
    return htmlData


def list_of_peaks(base_filename, directory, list, listNumber):

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

list_of_peaks("basic_list.html", "all", "", total)
list_of_peaks("list_of_northeast_131.html", "NE131", "NE131", 90 + 1)
list_of_peaks("list_of_southeast_202.html", "SE202", "SE202", 202 + 1)
list_of_peaks("list_of_northeast_115.html", "NE115", "NE115", 115 + 1)