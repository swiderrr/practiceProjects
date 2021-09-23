#! python3
import os, requests, bs4, webbrowser, re, time, openpyxl, datetime, os


def drawCount(linkList):
    for link in linkList:
        rowNum = linkList.index(link)
        drawNum = 0
        matchUrl = requests.get(shorterUrl + linkList[rowNum], proxies={"http":"http://myproxy:3129"})
        match = bs4.BeautifulSoup(matchUrl.text, features='lxml')
        scoreList = match.select('i')
        for score in scoreList:
            wynik = str(score)
            if ((wynik == '<i class="icon icon__lo"></i>') or (wynik == '<i class="icon icon__wo"></i>')):
                drawNum = drawNum + 1
            else:
                continue
            ws.cell(row=rowNum, column=1, value=(shorterUrl + linkList[rowNum]))
            ws.cell(row=rowNum, column=2, value=drawNum)
        

#Ustalanie aktualnego czasu, żeby nieanalizować spotkań, które już się odbyły
t = time.localtime()
time = time.strftime("%H%M", t)
date = datetime.datetime.now().strftime("%d-%b")
#Tworzenie pliku excel i arkusza z aktualną datą
wb = openpyxl.load_workbook(r"G:\Wyniki.xlsx")
wb.create_sheet(date)
ws = wb[date]
#Pobranie strony
mainUrl = 'https://www.betexplorer.com/next/basketball/'
shorterUrl = 'https://www.betexplorer.com'
res = requests.get(mainUrl, proxies={"http":"http://myproxy:3129"})
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, features="lxml")

#Filtrowanie spotkań, które dopiero się odbędą
events = soup.select('.table-main__time', features="lxml")
allEventLinks = soup.select('td.table-main__tt > a')
eventLinks = []

#Pętla porównująca czas wydarzenia z aktualnym czasem. Jeżeli spotkanie się jeszcze nie odbyło to do nowej listy dodaje link wydarzenia.
for i in range(len(events)):
    if int((events[i].getText()).replace(":", "")) > int(time):
        eventLinks.append(allEventLinks[i].get('href'))
    else:
        continue

drawCount(eventLinks)
wb.save(r"G:\Wyniki.xlsx")

