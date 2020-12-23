import PyPDF2

file = open('8. PDF_and_Spreadsheets\\Some_New_Doc.pdf', 'rb')

pdf_file_binary = PyPDF2.PdfFileReader(file)

print(pdf_file_binary.numPages)

page_one = pdf_file_binary.getPage(0)

page_one_text = page_one.extractText()

print(page_one_text)