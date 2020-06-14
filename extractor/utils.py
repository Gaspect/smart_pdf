from PyPDF4.pdf import PageObject
from PyPDF4 import PdfFileReader
from typing import IO
from re import match, fullmatch

#TODO: better isodate format convertion
def to_date(data):
    temp = data[2:10]
    year = temp[0:4]
    month = temp[4:6]
    day = temp[6:]
    return f'{day}/{month}/{year}'

def clean_string(data):
    if len(data)>=1 and data[0] == '/':
            data = data[1:]
    if len(data)>=2 and data[0:2] == 'D:':
        data = to_date(data)
    return data

def clean_info(info):
    cleaned = {}
    for key, val in info.items():
        target = cleaned
        clean_key = clean_string(key).lower()
        if '.' in clean_key:
            spliter = clean_key.split('.')
            for x in spliter[:-1]:
                target[x] = {}
                target = target[x]
            clean_key = spliter[len(spliter)-1]
        clean_val = clean_string(val)
        target[clean_key] = clean_val
    return cleaned


