import csv
import urllib
from lxml import html

## All of the courses at LU for a year are held in the following URL structure:
## http://timetable.lakeheadu.ca/2016SS_UG_TBAY/algo.html
## 2016SS means year 2016, spring/summer courses. the last bit is
## the first four letters of the program.

##List of programs

prog = [
    "algo",
    "anth",
    "biol",
    "busi",
    "clas",
    "comp",
    "crim",
    "econ",
    "educ",
    "engi",
    "engl",
    "fren",
    "geog",
    "gero",
    "gsci", #general science
    "hist",
    "indi",
    "intd", #interdiciplinary studies
    "math",
    "nala", #native language
    "nrmt", #natural resource management
    "nurs",
    "outd",
    "phil",
    "poli",
    "psyc",
    "soci",
    "sowk", #social work
    "visu",
    "wome"]
     
for program in prog:
    print program
    
##THIS IS EXAMPLE CODE FOR WRITING TO A CSV FILE

## ',' delimiter is recognized by excel.
## This will make a csv file in your working directory
with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter = ',',
                            quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam']*5+['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

##END EXAMPLE

##THIS IS EXAMPLE CODE FOR PULLING FROM A URL

url = "http://timetable.lakeheadu.ca/2016SS_UG_TBAY/algo.html"
page = html.fromstring(urllib.urlopen(url).read())

print html.tostring(page)

##END EXAMPLE
