import sys
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from utils.DataFile import *
from utils.FamilyTree import *
import pandas as pd


def handle_search(event):
	#everything for search will happen in this method
	df = loadIn()
	

def handle_submit(event):
	#everything for add is handled here
	df = loadIn()
	df = addNewMember(df, entry.get(), entry1.get(), entry2.get(), entry4.get(), entry5.get(), entry6.get(), True, (var1.get ==1), (var2.get ==1), entry7.get(), '')
	loadOut(df)
	#smallwin = tk.Tk()
	#smallwin.title("Message")
	#smallwin.geometry('250x250')
	#message = tk.Label(smallwin, text = "Add Successful", fg="white",	bg="green", 	width=250,	height=250)


if __name__== '__main__':
	window = tk.Tk()#'''this creates the MAIN window'''
	window.title("CS[U] Mentoring") #'''this sets the title for the gui'''

	window.geometry('500x500') #windo size


	TAB_CONTROL = ttk.Notebook(window) #tab control is in the window

	HOME = ttk.Frame(TAB_CONTROL)
	TAB_CONTROL.add(HOME, text='Home') #this is the home tab, baiscally your landing page for the application

	SEARCH = ttk.Frame(TAB_CONTROL)
	TAB_CONTROL.add(SEARCH, text='Search') #this is the search Tab, this is the most complicated section of this code

	ADD = ttk.Frame(TAB_CONTROL)
	TAB_CONTROL.add(ADD, text='Add') #this is your add tab, where you will add new entries to the table

	TAB_CONTROL.pack(expand=1, fill="both") #packing

	#foramating HOME tab
	homeFont = tkFont.Font(size=30)
	homeLabel = tk.Label(
	HOME, 
	text = "Welcome to the CS[U]\n Mentoring Program \nDatabase",
	font = homeFont,
	fg="white",
	bg="green", 
	width=500, 
	height=500
	)
	homeLabel.pack() #this is the end of everthing for the HOME tab

	#Formatting for the SEARCH tab
	intro = tk.Label(SEARCH,
	text = 'Enter the feild you wish to search by',
	font = tkFont.Font(size=15), 
	).grid(row = 0, column = 0)

	first= tk.Label(SEARCH, 
	text='First Name:',
	).grid(row = 1, column = 0)

	entryS= tk.Entry(SEARCH, 
	width=12, borderwidth = 5
	).grid(row = 1, column = 1)

	last= tk.Label(SEARCH, 
	text='Last Name:',
	).grid(row = 2, column = 0)

	entry1S = tk.Entry(SEARCH, width=12, borderwidth = 5).grid(row = 2, column = 1)

	email= tk.Label(SEARCH, 
	text='Email:',
	).grid(row = 3, column = 0)

	entry2S = tk.Entry(SEARCH, width=12, borderwidth = 5).grid(row = 3, column = 1)

	gradDate= tk.Label(SEARCH, 
	text='Graduation Date (ex: F21):',
	).grid(row = 4, column = 0)

	entry4S = tk.Entry(SEARCH, width=12, borderwidth = 5).grid(row = 4, column = 1)

	var3 = tk.StringVar()
	C3S = tk.Checkbutton(SEARCH, text = "Include people who have graduated in your search.", variable = var3, onvalue = "On", offvalue = "OFF")
	C3S.deselect();
	C3S.grid(row = 5)

	Mentor= tk.Label(SEARCH, 
	text='Name of Mentor:',
	).grid(row = 6, column = 0)

	entry5S = tk.Entry(SEARCH, width=12, borderwidth = 5).grid(row = 6, column = 1)

	Mentee= tk.Label(SEARCH, 
	text='Name of Mentee:',
	).grid(row = 7, column = 0)


	entry6S = tk.Entry(SEARCH, width=12, borderwidth = 5).grid(row = 7, column = 1)

	var1 = tk.StringVar()
	C1S = tk.Checkbutton(SEARCH, text = "Seeking Mentor?", variable = var1, onvalue = "On", offvalue = "OFF")
	C1S.deselect();
	C1S.grid(row = 8)

	var2 = tk.StringVar()
	C2S = tk.Checkbutton(SEARCH, text = "Seeking Mentee?", variable = var2, onvalue = "On", offvalue = "OFF")
	C2S.deselect();
	C2S.grid(row = 9)

	MentorLead= tk.Label(SEARCH, 
	text='Name of Mentor Lead:',
	).grid(row = 10, column = 0)


	entry7S = tk.Entry(SEARCH, width=12, borderwidth = 5).grid(row = 10, column = 1)

	var4 = tk.StringVar()
	C4 = tk.Checkbutton(SEARCH, text = "Return Tree", variable = var4, onvalue = "On", offvalue = "OFF")
	C4.deselect();
	C4.grid(row = 11)

	search = tk.Button(SEARCH, text = "Search",fg = "green")

	search.bind("<Button-1>", handle_search)
	search.grid(row = 12, column = 0)

	#End of SEARCH tab formating FIXME

	#Formating for the ADD tab
	window.configure(background = "#ccffcc")
	intro = tk.Label(ADD,
	text = 'Please enter the students information',
	font = tkFont.Font(size=15), 
	)#.grid(row = 0, column = 0)
	intro.pack()

	first= tk.Label(ADD, 
	text='*Enter First Name:',
	)#.grid(row = 1, column = 0)
	first.pack()

	entry= tk.Entry(ADD, 
	width=12, borderwidth = 5
	)
	entry.pack()#grid(row = 1, column = 1)
	#rtn0 =entry.get()

	last= tk.Label(ADD, 
	text='*Enter Last Name:',
	)
	last.pack()#grid(row = 2, column = 0)

	entry1 = tk.Entry(ADD, width=12, borderwidth = 5)
	entry1.pack()#grid(row = 2, column = 1)
	#rtn1 = entry1.get()

	email= tk.Label(ADD, 
	text='*Enter email:',
	)
	email.pack()#grid(row = 3, column = 0)

	entry2 = tk.Entry(ADD, width=12, borderwidth = 5)
	entry2.pack()#grid(row = 3, column = 1)
	#rtn2 = entry2.get()

	gradDate= tk.Label(ADD, 
	text='Enter Graduation Date (ex: F21):',
	)
	gradDate.pack()#grid(row = 4, column = 0)

	entry4 = tk.Entry(ADD, width=12, borderwidth = 5)
	entry4.pack()#grid(row = 4, column = 1)
	#rtn4 = entry4.get()

	Mentor= tk.Label(ADD, 
	text='Enter Name of Mentor:',
	)
	Mentor.pack()#grid(row = 5, column = 0)

	entry5 = tk.Entry(ADD, width=12, borderwidth = 5)
	entry5.pack()#grid(row = 5, column = 1)
	#rtn5 = entry5.get()

	Mentee= tk.Label(ADD, 
	text='Enter Name of Mentee:',
	)
	Mentee.pack()#grid(row = 6, column = 0)


	entry6 = tk.Entry(ADD, width=12, borderwidth = 5)
	entry6.pack()#grid(row = 6, column = 1)
	#rtn6 = entry6.get()

	var1 = tk.IntVar()
	C1 = tk.Checkbutton(ADD, text = "Seeking Mentor?", variable = var1, onvalue = 1, offvalue = 0)
	C1.deselect();
	C1.pack()#grid(row = 7)

	var2 = tk.IntVar()
	C2 = tk.Checkbutton(ADD, text = "Seeking Mentee?", variable = var2, onvalue = 1, offvalue = 0)
	C2.deselect();
	C2.pack()#grid(row = 8)

	MentorLead= tk.Label(ADD, 
	text='Enter Name of Mentor Lead:',
	)
	MentorLead.pack()#grid(row = 9, column = 0)


	entry7 = tk.Entry(ADD, width=12, borderwidth = 5)
	entry7.pack()#grid(row = 9, column = 1)
	#rtn7 = entry7.get()

	submit = tk.Button(ADD, text = "Submit",fg = "green")

	submit.bind("<Button-1>", handle_submit)
	submit.pack()#grid(row = 10, column = 0)

	warn = tk.Label(ADD, text ='All fields with * must be filled out', fg = 'red')
	warn.pack()#grid(row = 20, column = 0)



	window.mainloop() #endless loop




