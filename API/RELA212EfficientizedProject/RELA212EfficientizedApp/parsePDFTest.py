# import py_pdf_parser
# from py_pdf_parser.loaders import load_file
# from py_pdf_parser.visualise import visualise
# import os
# cwd = os.getcwd()
# print(cwd)
# # Pull in the file
# pdf_file = load_file('./API/RELA212EfficientizedProject/RELA212EfficientizedApp/test.pdf')

# visualise(pdf_file)

# textLines = pdf_file.elements.filter_by_text_equal("*").extract_single_element()

# print(pdf_file)
# print(textLines)

import PyPDF2
reader = PyPDF2.PdfFileReader('./API/RELA212EfficientizedProject/RELA212EfficientizedApp/test.pdf')
pageObject = reader.getPage(1)
firstPageText = pageObject.extractText()
splitStrings = firstPageText.replace("\n", "").split("*")
print(splitStrings)