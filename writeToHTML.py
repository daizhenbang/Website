import csv

info = open("PubOrganization.csv",'r',encoding='utf8');
html = open('PubHTML.txt','w',encoding='utf8');
reader = csv.reader(info);
lines = list(reader);
numLines = len(lines);
numEntries = len(lines[0]);
countYear = 0;
yearStarted = 2019;

for i in range(numLines):
    item = lines[i][0]+lines[i][1]+', "'+lines[i][2] + '",' + lines[i][3] + lines[i][4] + '</li>'
    
    
    if yearStarted == int(lines[i][-1]) and countYear == 0:
        html.write('<h1 id="'+str(yearStarted)+'pubs" align="center">'+str(yearStarted)+'</h1>\n');
        html.write('<ol>\n<li style="list-style-type: none;">\n<ol>\n');
        countYear += 1;
    elif yearStarted-1 == int(lines[i][-1]) and countYear == 1:
        html.write('</ol>\n</li>\n</ol>\n\n');
        countYear = 0;
        yearStarted -= 1;
        html.write('<h1 id="'+str(yearStarted)+'pubs" align="center">'+str(yearStarted)+'</h1>\n');
        html.write('<ol>\n<li style="list-style-type: none;">\n<ol>\n');
        countYear += 1;
        
    html.write('\t'+item+'\n');
    
info.close();
html.close();

