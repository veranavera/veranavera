import csv
import operator
sorts = ["name", "elevation", "prominence", "isolation", "date", "location", "list"]

links = [sorts.copy(), sorts.copy(), sorts.copy(), sorts.copy(), sorts.copy(), sorts.copy(), sorts.copy()]
for x in range(0, 7):
    for y in range(0,7):
        # and len(links[x][y]) < 42 and len(links[x][y]) > 34
        if(x == y and not "." in links[x][y]):
            links[x][y] = "list_of_peaks_" + links[x][y] + "_descending.html"
        elif(not "." in links[x][y]):
            links[x][y] = "list_of_peaks_" + links[x][y] + ".html"

sortCounters = [0, 2, 3, 4, 5, 7, 8]
sortOrders = [False, True, True, True, True, False, True]
sortTypes = [False, True, True, True, False, False, False]
sortCounter = 0

for type in sorts:
    header = "<!DOCTYPE html>\n<html>\n<head>\n\t<link rel=\"stylesheet\" href=\"stylesheet.css\">\n\t<title>Peaks I've climbed!!!</title>\n</head>\n<body>\n<div>\n\t<iframe class=\"page_header\" frameBorder=\"0\" src=\"../formatting_files/header.html\" seamless></iframe>\n</div>\n<div class=\"page_body\">\n\t<h1>List of peaks I've climbed!!!</h1>\n\t<p>\n\t\tBelow is a list of all the peaks I've climbed and brought a trans pride flag to the top of since May 8th, 2022, with each peak linked to its page on peakbagger, and with the elevation, prominence, isolation, and location pulled from that website. Also, each peak has the date I climbed it, which may eventually turn into a \"link to the ascent on peakbagger\" type deal, but as of February 7th, 2024, I'm too lazy to do all that work (you can still just click the main link and find my trip report on peakbagger in the meantime). For all of the Southeast 202 and Northeast 131 peaks, you can find a trip report on this website, and for all of these peaks, you can find photos of me with the flag on the google drive. Finally, note that I try and use an indigenous name for a mountain whenever I have that data available, so oftentimes the linked peak will show up under a different, colonial name. If you know any other indigenous names for any of these mountains, let me know and I will happy correct their names!!!\n\t</p>\n\t<p>\n\t\tYou can feel free click on each of the table headers and get a list sorted by that parameter (isolation, date, etc.) - the default is prominence, but the list also looks really cool from other perspectives!!!\n\t</p>\n"

    htmlData = header + "</div>\n<div style=\"width: 100%; display: table;\">\n\t<table style=\"width:100%\">\n\t\t<tr>\n\t\t\t<th class=\"number\"><a href=\"" + links[sortCounter][2] + "\" class=\"number\">Number &#8645</a></th>\n\t\t\t<th><a href=\"" + links[sortCounter][0] + "\" class=\"name\">Name &#8645</a></th>\n\t\t\t<th><a href=\"" + links[sortCounter][1] + "\" class=\"elevation\">Elevation (ft) &#8645</a></th>\n\t\t\t<th><a href=\"" + links[sortCounter][2] + "\" class=\"prominence\">Prominence (ft) &#8645</a></th>\n\t\t\t<th><a href=\"" + links[sortCounter][3] + "\" class=\"isolation\">Isolation (km) &#8645</a></th>\n\t\t\t<th><a href=\"" + links[sortCounter][4] + "\" class=\"date\">Date Climbed &#8645</a></th>\n\t\t\t<th><a href=\"" + links[sortCounter][5] + "\" class=\"location\">State &#8645</a></th>\n\t\t\t<th><a href=\"" + links[sortCounter][6] + "\"class=\"list\">Peak on List &#8645</a></th>\n\t\t</tr>\n\t\t"
    
    with open("list_of_peaks.csv", newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(data)
        if(sortTypes[sortCounter]):
            sortedData = sorted(data, key=lambda x: float(x[sortCounters[sortCounter]]), reverse=sortOrders[sortCounter])
        else:
            sortedData = sorted(data, key=operator.itemgetter(sortCounters[sortCounter]), reverse=sortOrders[sortCounter])
        counter = 1
        for row in sortedData:
            line = "<tr>\n\t\t\t"
            line += "<th class = \"number\">" + str(counter) + "</th>\n\t\t\t"
            line += "<th class = \"name\"><a href=\"" + row[1] + "\">" + row[0] + "</a></th>\n\t\t\t"
            line += "<th class = \"elevation\">" + str(row[2]) + "</th>\n\t\t\t"
            line += "<th class = \"prominence\">" + str(row[3]) + "</th>\n\t\t\t"
            line += "<th class = \"isolation\">" + str(row[4]) + "</th>\n\t\t\t"
            #line += "<th class = \"date\">" + row[5] + "</th>\n\t\t\t"
            line += "<th class = \"date\"><a href=\"" + row[6] + "\">" + row[5] + "</a></th>\n\t\t\t"
            line += "<th class = \"location\">" + row[7] + "</th>\n\t\t\t"
            line += "<th class = \"list\">" + row[8] + "</th>\n\t\t"
            line += "</tr>\n\t\t"
            htmlData += line
            counter += 1
            
    htmlData += "\n\t</table>\n</div>\n<div>\n\t<iframe class=\"page_footer\" frameBorder=\"0\" src=\"../formatting_files/footer.html\" seamless></iframe>\n</div>\n</body>"

    f = open("list_of_peaks_" + type + ".html", "w")
    f.write(htmlData)
    f.close()

    htmlData = header + "</div>\n<div style=\"width: 100%; display: table;\">\n\t<table style=\"width:100%\">\n\t\t<tr>\n\t\t\t<th class=\"number\"><a href=\"list_of_peaks_prominence.html\" class=\"number\">Number &#8645</a></th>\n\t\t\t<th><a href=\"list_of_peaks_name.html\" class=\"name\">Name &#8645</a></th>\n\t\t\t<th><a href=\"list_of_peaks_elevation.html\" class=\"elevation\">Elevation (ft) &#8645</a></th>\n\t\t\t<th><a href=\"list_of_peaks_prominence.html\" class=\"prominence\">Prominence (ft) &#8645</a></th>\n\t\t\t<th><a href=\"list_of_peaks_isolation.html\" class=\"isolation\">Isolation (km) &#8645</a></th>\n\t\t\t<th><a href=\"list_of_peaks_date.html\" class=\"date\">Date Climbed &#8645</a></th>\n\t\t\t<th><a href=\"list_of_peaks_location.html\" class=\"location\">State &#8645</a></th>\n\t\t\t<th><a href=\"list_of_peaks_list.html\"class=\"list\">Peak on List &#8645</a></th>\n\t\t</tr>\n\t\t"
    
    with open("list_of_peaks.csv", newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(data)
        if(sortTypes[sortCounter]):
            sortedData = sorted(data, key=lambda x: float(x[sortCounters[sortCounter]]), reverse=not sortOrders[sortCounter])
        else:
            sortedData = sorted(data, key=operator.itemgetter(sortCounters[sortCounter]), reverse=not sortOrders[sortCounter])
        counter = 1
        for row in sortedData:
            line = "<tr>\n\t\t\t"
            line += "<th class = \"number\">" + str(counter) + "</th>\n\t\t\t"
            line += "<th class = \"name\"><a href=\"" + row[1] + "\">" + row[0] + "</a></th>\n\t\t\t"
            line += "<th class = \"elevation\">" + str(row[2]) + "</th>\n\t\t\t"
            line += "<th class = \"prominence\">" + str(row[3]) + "</th>\n\t\t\t"
            line += "<th class = \"isolation\">" + str(row[4]) + "</th>\n\t\t\t"
            #line += "<th class = \"date\">" + row[5] + "</th>\n\t\t\t"
            line += "<th class = \"date\"><a href=\"" + row[6] + "\">" + row[5] + "</a></th>\n\t\t\t"
            line += "<th class = \"location\">" + row[7] + "</th>\n\t\t\t"
            line += "<th class = \"list\">" + row[8] + "</th>\n\t\t"
            line += "</tr>\n\t\t"
            htmlData += line
            counter += 1
            
    htmlData += "\n\t</table>\n</div>\n<div>\n\t<iframe class=\"page_footer\" frameBorder=\"0\" src=\"../formatting_files/footer.html\" seamless></iframe>\n</div>\n</body>"

    f = open("list_of_peaks_" + type + "_descending.html", "w")
    f.write(htmlData)
    f.close()

    sortCounter += 1