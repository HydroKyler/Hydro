from reportlab.pdfgen import canvas
from reportlab.lob.pagesizes import letter
from reportlab.platypus import Image, Paragraph
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
##For making ordered dictionaries
import collections
##For Image manipulation
from PIL import ImageFont
##For timestamp creation
import time
##For reading csv files
import csv
##For checking file existance withing system

#########################################################################################################

def PDFgen():
    c = canvas.Canvas('{}'.format(), pagesize = letter)##Set format to be a file name with Path


##Meta information
    c.setAuthor()
    c.setTitle()
    c.setCreator()
    c.setSubject()
    c.setKeywords()
    

##Global Variables for font, font size, fill color, and stroke color

    def Font(ftype,fsize):
        font = c.setFont(ftype,fsize)
