import pyttsx3      #To convert text to speech
import PyPDF2       #To extract text from pdf file
from tkinter.filedialog import *  #for input pdf file

book = askopenfilename()    #opening the file
pdfreader = PyPDF2.PdfFileReader(book)  #create a file object
pages = pdfreader.numPages  #get number of pages in the file

for num in range(0, pages):     #runs through all the pages
    page = pdfreader.getPage(num)   #select a page by number
    text = page.extractText()       #get the text from the file
    engine = pyttsx3.init() #initialise the pyttsx3
    engine.say(text)    #convert text to speech
    engine.runAndWait()     #run