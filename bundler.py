import re
import os
import io
import time
import PyPDF2
from collections import OrderedDict
from pagerange_to_pages import ranges_to_numbers
from user_input import *
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
import first_page
import word_counter
from decimal import Decimal

bundles_produced = 0
pdf_names = []
all_pages = 0
all_words = 0
minutes_per_page = 4

def find_and_append(book, page_list):
    global minutes_per_page
    global book_cover_included
    global output_folder_dest
    global bundles_produced
    global pdf_names
    global all_pages
    global all_words
    current_directory = os.path.dirname(os.path.realpath(__file__))
    directory_name = 'pdf_books'
    this_bundle = PyPDF2.PdfFileWriter()
    this_book = open(os.path.join(current_directory, directory_name, str(book)), 'rb')
    read_book = PyPDF2.PdfFileReader(this_book)
    name_without_pdf = str(re.sub('\.pdf$', '', str(book)))

    #writes first page
    numPages = page_list
    how_many_words = word_counter.count_words(read_book, numPages)
    all_words += how_many_words
    all_pages += len(numPages)
    first_page.Title = 'Book: ' + name_without_pdf
    first_page.SubTitle = ' Week '+ str(folder_index) +' Reading Material'
    first_page.Name = str(len(page_list)) + ' Pages (' +str(minutes_per_page*len(page_list))+ ' Minutes)'
    first_page.go(os.path.join('title pages', name_without_pdf +'_title_page.pdf'))
    


    #adds cover and black page with bookmark
    
    title_page_file = open(os.path.join('title pages', name_without_pdf +'_title_page.pdf'), 'rb')
    read_title_page = PyPDF2.PdfFileReader(title_page_file)
    this_bundle.addPage(read_title_page.getPage(0))
    this_bundle.addPage(read_book.getPage(0))
    this_bundle.addBookmark(name_without_pdf, 1, parent=None, color=(0.0,0.0,1.0))
    this_bundle.setPageMode("/UseOutlines")

    for page in numPages:
        this_bundle.addPage(read_book.getPage(page))
    
    directory_name = output_folder_dest
    outputStream = open(os.path.join(output_folder_dest, 'Bundles', re.sub('\.pdf$', '', str(book)) + '_bundle.pdf'), 'wb')
    
    while True:
        try:
            this_bundle.write(outputStream)
            pdf_names.append((os.path.join(output_folder_dest, 'Bundles', re.sub('\.pdf$', '', str(book)) + '_bundle.pdf'), 'rb'))
            bundles_produced += 1
        except PyPDF2.utils.PdfReadError:
            print('CANT WRITE PDF')
        break
    outputStream.close()

def article_transform(article):
    global minutes_per_page
    global output_folder_dest
    global bundles_produced
    global pdf_names
    global all_pages
    global all_words
    current_directory = os.path.dirname(os.path.realpath(__file__))
    directory_name = 'pdf_papers'
    this_bundle = PyPDF2.PdfFileWriter()
    this_book = open(os.path.join(current_directory, directory_name, str(article)), 'rb')
    read_book = PyPDF2.PdfFileReader(this_book)
    name_without_pdf = str(re.sub('\.pdf$', '', str(article)))

    #writes first page
    numPages = read_book.getNumPages()
    how_many_words = word_counter.count_words(read_book, numPages)
    all_words += how_many_words
    all_pages += numPages
    first_page.Title = 'Article: ' + name_without_pdf
    first_page.SubTitle = ' Week '+ str(folder_index) +' Reading Material'
    first_page.Name = str(numPages) + ' Pages (' +str(minutes_per_page*numPages)+ ' Minutes)'
    first_page.go(os.path.join('title pages', name_without_pdf +'_title_page.pdf'))

    #adds cover and black page with bookmark
    
    title_page_file = open(os.path.join('title pages', name_without_pdf +'_title_page.pdf'), 'rb')
    read_title_page = PyPDF2.PdfFileReader(title_page_file)
    this_bundle.addPage(read_title_page.getPage(0))
    #this_bundle.addBookmark(name_without_pdf, 1, parent=None, color=(0.0,0.0,1.0))
    this_bundle.setPageMode("/UseOutlines")

    for page in range(numPages):
        this_bundle.addPage(read_book.getPage(page))
    
    directory_name = output_folder_dest
    outputStream = open(os.path.join(output_folder_dest, 'Bundles', re.sub('\.pdf$', '', str(article)) + '_bundle.pdf'), 'wb')
    
    while True:
        try:
            this_bundle.write(outputStream)
            pdf_names.append((os.path.join(output_folder_dest, 'Bundles', re.sub('\.pdf$', '', str(article)) + '_bundle.pdf'), 'rb'))
            bundles_produced += 1
        except PyPDF2.utils.PdfReadError:
            print('CANT WRITE PDF')
        break
    outputStream.close()

for book, page_list in books_pages_dict.items():
    true_page_list = ranges_to_numbers(page_list)
    find_and_append(book, true_page_list)

for article in art_bun:
    article_transform(article)

letsMerge = PyPDF2.PdfFileMerger()

def super_title_page():
    global all_pages
    global all_words
    first_page.Title = ' Week '+ str(folder_index) +' Reading Material'
    first_page.SubTitle = str(all_pages) + ' Pages (' +str(int(minutes_per_page*all_pages/60))+ ' Hours)'
    first_page.Name = ''
    first_page.go(os.path.join('title pages', 'title_page.pdf'))
    title_page_file = open(os.path.join('title pages', 'title_page.pdf'), 'rb')
    read_title_page = PyPDF2.PdfFileReader(title_page_file)
    letsMerge.append(read_title_page)

super_title_page()

for name in pdf_names:
    letsMerge.append(PyPDF2.PdfFileReader(*name))
letsMerge.write(open(os.path.join(output_folder_dest, 'Bundles', 'Reading Material Week ' +str(folder_index)+ '.pdf'), 'wb'))
