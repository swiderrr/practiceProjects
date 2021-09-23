import sys, docx, re, os
from docx2pdf import convert

path = str(sys.argv[1])
town = str(sys.argv[2])
doc = docx.Document(path)


def tableReplace():
    table = doc.tables
    tableText = []
    print(table)
    for t in range(len(table)):
        for row in (table[t].rows):
            for cell in row.cells:
                paragraphs = cell.paragraphs
                for paragraph in paragraphs:
                    if town in paragraph.text:
                        for run in paragraph.runs:
                            if town in run.text:
                                text = run.text.replace(town, '')
                                run.text = text

def textReplace():
    idRegex = re.compile(r'(\d{6}_\d{1,2}.\d{4}.)')
    for paragraph in doc.paragraphs:
        if idRegex.search(paragraph.text):
            for run in paragraph.runs:
                if idRegex.search(run.text):
                    match = idRegex.search(run.text).group(0)
                    text = run.text.replace(match, '')
                    run.text = text

tableReplace()
textReplace()
docNewTitle = os.path.basename(sys.argv[1])
pdfNewTitle = docNewTitle.split('.')
pathDoc = 'C:\\Users\\swidr\\' + docNewTitle
pathPdf = 'C:\\Users\\swidr\\' + pdfNewTitle[0] + '.pdf'
doc.save(pathDoc)
convert(pathDoc, pathPdf)
    



     
    
