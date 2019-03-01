import csv

file = open('Publications.txt','r',encoding='utf8');
allPublications = [];

for line in file:
    temp = line.lstrip();
    if temp.startswith('<li style="list-style-position: outside'):
        posBracket = temp.find(">");
        posQuotation1 = temp.find("\"",posBracket);
        posQuotation2 = temp.find("\"",posQuotation1+1)
        posJournalInfo = temp.find("<a",posQuotation2+1);
        posEND = temp.find("/a>",posJournalInfo);
                                
        header = temp[0:posBracket+1];
        
        authors = temp[posBracket+1:posQuotation1];
        authors = authors.strip(',')
        
        title = temp[posQuotation1+1:posQuotation2];
        
        journalInfo = temp[posQuotation2+1:posJournalInfo];
        journalInfo = journalInfo.strip(',')
        journalInfo = journalInfo.strip()
        '''Obtain Journal Years so that we can better classify them'''
        posWild1 = journalInfo.rfind('(')
        posWild2 = journalInfo.rfind(')')
        year = journalInfo[posWild1+1:posWild2];
        
        pdf = temp[posJournalInfo:posEND+3]
        
        entry = [header,authors,title,journalInfo,pdf,year]        
        print(entry)
        
        allPublications.append(entry);
        
file.close();

print(allPublications)

writeCSV = open('PubOrganization.csv','w',encoding='utf8',newline='');
writer = csv.writer(writeCSV);
numLines = len(allPublications);
for i in range(numLines):
    writer.writerow(allPublications[i]);


writeCSV.close();
