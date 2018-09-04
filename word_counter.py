import os
import sys
import re
import time
import PyPDF2

def extractData(pdf_file, page):

    pdfReader = pdf_file
    pageObj = pdfReader.getPage(page)
    data = pageObj.extractText()
    return data

def getWordCount(data):

    data=data.split()
    return len(data)


def count_words(pdfFile, numPages):
    if isinstance(numPages, list):
        totalWords = 0
        for i in numPages:
            text = extractData(pdfFile, i)
            totalWords += getWordCount(text)
        time.sleep(1)
        return totalWords
    else:
        totalWords = 0
        for i in range(numPages):
            text = extractData(pdfFile, i)
            totalWords += getWordCount(text)
        time.sleep(1)
        return totalWords
