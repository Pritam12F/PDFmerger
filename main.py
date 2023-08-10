import PyPDF2,os

pdfiles = []

for filename in os.listdir():
    if filename.endswith('.pdf'):
        if filename != 'merged.pdf':
            pdfiles.append(filename)

pdfiles.sort(key=str.lower)
merger = PyPDF2.PdfMerger()

for filename in pdfiles:
        merger.append(filename)

merger.write('merged.pdf')
merger.close()
