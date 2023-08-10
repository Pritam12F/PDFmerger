# PDFmerger
PDF merge created using python with help of os,PyPDF2 modules
This program uses the os module methods to get the filnames ending with .pdf and arranges the names in order in a list
Then we create an object called merge and assign it to the PdfMerger() method of PyPDF2
Then we iterate through all the file names in our list and append it to the merger object
Then we use merge.write() to create a new file which now has a value of all the PDF concatenated together
Then we use merge.close() to terminate the object
