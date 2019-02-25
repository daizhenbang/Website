import csv

file = open('Publications.txt','r',encoding='utf8');
allPublications = [];

for line in file:
    temp = line.lstrip();
    if temp.startswith('<li style="list-style-position: outside'):
        posBracket = temp.find(">");
        posQuotation1 = temp.find("\"",posBracket);
        posQuotation2 = temp.find("\"",posQuotation1+1)
        posJournalInfo = temp.find("<a href",posQuotation2+1);
                                
        header = temp[0:posBracket+1];
        
        authors = temp[posBracket+1:posQuotation1];
        authors = authors.strip(",")
        
        title = temp[posQuotation1+1:posQuotation2];
        
        journalInfo = temp[posQuotation2+1:posJournalInfo];
        journalInfo = journalInfo.strip(',')
        journalInfo = journalInfo.strip()
        
        pdf = temp[posJournalInfo:]
        
        entry = [header,authors,title,journalInfo,pdf]        
        
        allPublications.append(entry);
        
file.close();

writeCSV = open('PubOrganization.csv','w',encoding='utf8',newline='');
writer = csv.writer(writeCSV);
numLines = len(allPublications);
for i in range(numLines):
    writer.writerow(allPublications[i]);


writeCSV.close();
