import csv
import operator
sorts = ["name", "elevation", "prominence", "isolation", "date", "location"]

links = [sorts.copy(), sorts.copy(), sorts.copy(), sorts.copy(), sorts.copy(), sorts.copy()]
for x in range(0, 6):
    for y in range(0,6):
        if(x == y and not "." in links[x][y]):
            links[x][y] = "southeast_202_" + links[x][y] + "_descending.html"
        elif(not "." in links[x][y]):
            links[x][y] = "southeast_202_" + links[x][y] + ".html"

sortCounters = [0, 2, 3, 4, 5, 7]
sortOrders = [False, True, True, True, True, False]
sortTypes = [False, True, True, True, False, False]
sortCounter = 0

for type in sorts:
    header = "<!DOCTYPE html>\n<html>\n<head>\n\t<link rel=\"stylesheet\" href=\"stylesheet.css\">\n\t<title>Peaks I've climbed!!!</title>\n</head>\n<body>\n<div>\n\t<iframe class=\"page_header\" frameBorder=\"0\" src=\"../../formatting_files/header.html\" seamless></iframe>\n</div>\n<div class=\"page_body\">\n\t<h1>The New Southeast 202</h1>\n\t<p>\n\t\tWhen I started this peakbagging project in March of 2023, I had the intention of climbing all 202 of the 5000fters in the Southeastern United States, seeing it as a natural successor to my project the previous year of climbing all 115 of the 4000fters in the Northeast. However, this iteration of the 202 proved to be untenable, and was replaced with this version: the New Southeast 202. The rough outline of this list is the tallest and most prominent peaks of the American Southeast, including all of the 6000fters and 2000ft prominence peaks, along with a significant fraction of the 5000fters and 1000ft prominence peaks, plus some other miscellaneous peaks thrown in there for good measure. Included in this list are the high points of seven different states: Alabama, Georgia, Tennessee, North Carolina, Virginia, West Virginia, and Kentucky\n\t</p>\n\t<p>\n\t\t Below are all the peaks on this list, with each peak linked to its page on peakbagger, and with the elevation, prominence, isolation, and location pulled from that website (along with 22 additional peaks that didn't meet prominence/elevation cuttoffs to make it on the main list). Also, each peak has the date I climbed it, which may eventually turn into a \"link to the trip report page\" type deal, but as of March 11th, 2024, I'm too lazy to do all that work (for the time being, you can click the \"trip reports\" link in the header and find the ascent by date). Finally, note that I try and use an indigenous name for a mountain whenever I have that data available, so oftentimes the linked peak will show up under a different, colonial name. If you know any other indigenous names for any of these mountains, let me know and I will happy correct their names!!!\n\t</p>\n\t<p>\n\t\tYou can feel free click on each of the table headers and get a list sorted by that parameter (isolation, date, etc.) - the default is prominence, but the list also looks really cool from other perspectives!!!\n\t</p>\n"

    footer = "\n\t</table>\n</div>\n<div>\n\t<iframe class=\"page_footer\" frameBorder=\"0\" src=\"../../formatting_files/footer.html\" seamless></iframe>\n</div>\n</body>"

    htmlData = header + "</div>\n<div style=\"width: 100%; display: table;\">\n\t<table style=\"width:100%\">\n\t\t<tr>\n\t\t\t<th class=\"number\"><a href=\"" + links[sortCounter][2] + "\" class=\"number\">Number &#8645</a></th>\n\t\t\t<th><a href=\"" + links[sortCounter][0] + "\" class=\"name\">Name &#8645</a></th>\n\t\t\t<th><a href=\"" + links[sortCounter][1] + "\" class=\"elevation\">Elevation (ft) &#8645</a></th>\n\t\t\t<th><a href=\"" + links[sortCounter][2] + "\" class=\"prominence\">Prominence (ft) &#8645</a></th>\n\t\t\t<th><a href=\"" + links[sortCounter][3] + "\" class=\"isolation\">Isolation (km) &#8645</a></th>\n\t\t\t<th><a href=\"" + links[sortCounter][4] + "\" class=\"date\">Date Climbed &#8645</a></th>\n\t\t\t<th><a href=\"" + links[sortCounter][5] + "\" class=\"location\">State &#8645</a></th>\n\t\t"
    
    with open("southeast_202.csv", newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(data)
        if(sortTypes[sortCounter]):
            sortedData = sorted(data, key=lambda x: float(x[sortCounters[sortCounter]]), reverse=sortOrders[sortCounter])
        else:
            sortedData = sorted(data, key=operator.itemgetter(sortCounters[sortCounter]), reverse=sortOrders[sortCounter])
        counter = 1
        for row in sortedData:
            line = "<tr>\n\t\t\t"
            if(row[8] == "main"):
                line += "<th class = \"number\">" + str(counter) + "</th>\n\t\t\t"
            else:
                line += "<th class = \"number\">" + "&#183" + "</th>\n\t\t\t"
                counter -= 1
            line += "<th class = \"name\"><a href=\"" + row[1] + "\">" + row[0] + "</a></th>\n\t\t\t"
            line += "<th class = \"elevation\">" + str(row[2]) + "</th>\n\t\t\t"
            line += "<th class = \"prominence\">" + str(row[3]) + "</th>\n\t\t\t"
            line += "<th class = \"isolation\">" + str(row[4]) + "</th>\n\t\t\t"
            line += "<th class = \"date\">" + row[5] + "</th>\n\t\t\t"
            #line += "<th class = \"date\"><a href=\"" + row[6] + "\">" + row[5] + "</a></th>\n\t\t\t"
            line += "<th class = \"location\">" + row[7] + "</th>\n\t\t\t"
            line += "</tr>\n\t\t"
            htmlData += line
            counter += 1
            
    htmlData += footer

    f = open("southeast_202_" + type + ".html", "w")
    f.write(htmlData)
    f.close()

    htmlData = header + "</div>\n<div style=\"width: 100%; display: table;\">\n\t<table style=\"width:100%\">\n\t\t<tr>\n\t\t\t<th class=\"number\"><a href=\"southeast_202_prominence.html\" class=\"number\">Number &#8645</a></th>\n\t\t\t<th><a href=\"southeast_202_name.html\" class=\"name\">Name &#8645</a></th>\n\t\t\t<th><a href=\"southeast_202_elevation.html\" class=\"elevation\">Elevation (ft) &#8645</a></th>\n\t\t\t<th><a href=\"southeast_202_prominence.html\" class=\"prominence\">Prominence (ft) &#8645</a></th>\n\t\t\t<th><a href=\"southeast_202_isolation.html\" class=\"isolation\">Isolation (km) &#8645</a></th>\n\t\t\t<th><a href=\"southeast_202_date.html\" class=\"date\">Date Climbed &#8645</a></th>\n\t\t\t<th><a href=\"southeast_202_location.html\" class=\"location\">State &#8645</a></th>\n\t\t"
    
    with open("southeast_202.csv", newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(data)
        if(sortTypes[sortCounter]):
            sortedData = sorted(data, key=lambda x: float(x[sortCounters[sortCounter]]), reverse=not sortOrders[sortCounter])
        else:
            sortedData = sorted(data, key=operator.itemgetter(sortCounters[sortCounter]), reverse=not sortOrders[sortCounter])
        counter = 1
        for row in sortedData:
            line = "<tr>\n\t\t\t"
            if(row[8] == "main"):
                line += "<th class = \"number\">" + str(counter) + "</th>\n\t\t\t"
            else:
                line += "<th class = \"number\">" + "&#183" + "</th>\n\t\t\t"
                counter -= 1
            line += "<th class = \"name\"><a href=\"" + row[1] + "\">" + row[0] + "</a></th>\n\t\t\t"
            line += "<th class = \"elevation\">" + str(row[2]) + "</th>\n\t\t\t"
            line += "<th class = \"prominence\">" + str(row[3]) + "</th>\n\t\t\t"
            line += "<th class = \"isolation\">" + str(row[4]) + "</th>\n\t\t\t"
            line += "<th class = \"date\">" + row[5] + "</th>\n\t\t\t"
            #line += "<th class = \"date\"><a href=\"" + row[6] + "\">" + row[5] + "</a></th>\n\t\t\t"
            line += "<th class = \"location\">" + row[7] + "</th>\n\t\t\t"
            line += "</tr>\n\t\t"
            htmlData += line
            counter += 1
            
    htmlData += footer

    f = open("southeast_202_" + type + "_descending.html", "w")
    f.write(htmlData)
    f.close()

    sortCounter += 1