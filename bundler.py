import re
import os
import io
import PyPDF2
from collections import OrderedDict
from pagerange_to_pages import ranges_to_numbers
from user_input import *

bundles_produced = 0

def find_and_append(book, page_list):
    global output_folder_dest
    global bundles_produced
    current_directory = os.path.dirname(os.path.realpath(__file__))
    directory_name = 'pdf_books'
    this_bundle = PyPDF2.PdfFileWriter()
    this_book = open(os.path.join(current_directory, directory_name, str(book)), 'rb')
    read_book = PyPDF2.PdfFileReader(this_book, strict=False)
    if book_cover_included == True:
        this_bundle.addPage(read_book.getPage(0))
    for page in page_list:
        this_bundle.addPage(read_book.getPage(page))
    directory_name = output_folder_dest
    outputStream = open(os.path.join(output_folder_dest, re.sub('\.pdf$', '', str(book)) + '_bundle.pdf'), 'wb')
    while True:
        try:
            this_bundle.write(outputStream)
            bundles_produced += 1
        except PyPDF2.utils.PdfReadError:
            print('CANT WRITE PDF')
        break
    outputStream.close()

for book, page_list in books_pages_dict.items():
    true_page_list = ranges_to_numbers(page_list)
    find_and_append(book, true_page_list)

