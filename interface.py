import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

window = tk.Tk()#'''this creates the MAIN window'''
window.title("CS[U] Mentoring") #'''this sets the title for the gui'''

window.geometry('500x500') #windo size

#'''window.rowconfigure(0, minsize=800, weight=1)
#window.columnconfigure(0, minsize=800, weight=1)'''

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

#Formatting for the SEARCH tab FIXME
intro = tk.Label(SEARCH,
text = 'Enter the feild you wish to search by',
font = tkFont.Font(size=15), 
).grid(row = 0, column = 0)

first= tk.Label(SEARCH, 
text='First Name:',
).grid(row = 1, column = 0)

entry= tk.Entry(SEARCH, 
width=12, borderwidth = 5
).grid(row = 1, column = 1)

last= tk.Label(SEARCH, 
text='Last Name:',
).grid(row = 2, column = 0)

entry1 = tk.Entry(SEARCH, width=12, borderwidth = 5).grid(row = 2, column = 1)

email= tk.Label(SEARCH, 
text='Email:',
).grid(row = 3, column = 0)

entry2 = tk.Entry(SEARCH, width=12, borderwidth = 5).grid(row = 3, column = 1)

gradDate= tk.Label(SEARCH, 
text='Graduation Date (ex: F21):',
).grid(row = 4, column = 0)

entry4 = tk.Entry(SEARCH, width=12, borderwidth = 5).grid(row = 4, column = 1)

var3 = tk.StringVar()
C3 = tk.Checkbutton(SEARCH, text = "Include people who have graduated in your search.", variable = var3, onvalue = "On", offvalue = "OFF")
C3.deselect();
C3.grid(row = 5)

Mentor= tk.Label(SEARCH, 
text='Name of Mentor:',
).grid(row = 6, column = 0)

entry5 = tk.Entry(SEARCH, width=12, borderwidth = 5).grid(row = 6, column = 1)

Mentee= tk.Label(SEARCH, 
text='Name of Mentee:',
).grid(row = 7, column = 0)


entry6 = tk.Entry(SEARCH, width=12, borderwidth = 5).grid(row = 7, column = 1)

var1 = tk.StringVar()
C1 = tk.Checkbutton(SEARCH, text = "Seeking Mentor?", variable = var1, onvalue = "On", offvalue = "OFF")
C1.deselect();
C1.grid(row = 8)

var2 = tk.StringVar()
C2 = tk.Checkbutton(SEARCH, text = "Seeking Mentee?", variable = var2, onvalue = "On", offvalue = "OFF")
C2.deselect();
C2.grid(row = 9)

MentorLead= tk.Label(SEARCH, 
text='Name of Mentor Lead:',
).grid(row = 10, column = 0)


entry7 = tk.Entry(SEARCH, width=12, borderwidth = 5).grid(row = 10, column = 1)

var4 = tk.StringVar()
C4 = tk.Checkbutton(SEARCH, text = "Return Tree", variable = var4, onvalue = "On", offvalue = "OFF")
C4.deselect();
C4.grid(row = 11)


#End of SEARCH tab formating FIXME

#Formating for the ADD tab
window.configure(background = "#ccffcc")
intro = tk.Label(ADD,
text = 'Please enter the students information',
font = tkFont.Font(size=15), 
).grid(row = 0, column = 0)

first= tk.Label(ADD, 
text='*Enter First Name:',
).grid(row = 1, column = 0)

entry= tk.Entry(ADD, 
width=12, borderwidth = 5
).grid(row = 1, column = 1)

last= tk.Label(ADD, 
text='*Enter Last Name:',
).grid(row = 2, column = 0)

entry1 = tk.Entry(ADD, width=12, borderwidth = 5).grid(row = 2, column = 1)

email= tk.Label(ADD, 
text='*Enter email:',
).grid(row = 3, column = 0)

entry2 = tk.Entry(ADD, width=12, borderwidth = 5).grid(row = 3, column = 1)

gradDate= tk.Label(ADD, 
text='Enter Graduation Date (ex: F21):',
).grid(row = 4, column = 0)

entry4 = tk.Entry(ADD, width=12, borderwidth = 5).grid(row = 4, column = 1)

Mentor= tk.Label(ADD, 
text='Enter Name of Mentor:',
).grid(row = 5, column = 0)

entry5 = tk.Entry(ADD, width=12, borderwidth = 5).grid(row = 5, column = 1)

Mentee= tk.Label(ADD, 
text='Enter Name of Mentee:',
).grid(row = 6, column = 0)


entry6 = tk.Entry(ADD, width=12, borderwidth = 5).grid(row = 6, column = 1)

var1 = tk.StringVar()
C1 = tk.Checkbutton(ADD, text = "Seeking Mentor?", variable = var1, onvalue = "On", offvalue = "OFF")
C1.deselect();
C1.grid(row = 7)

var2 = tk.StringVar()
C2 = tk.Checkbutton(ADD, text = "Seeking Mentee?", variable = var2, onvalue = "On", offvalue = "OFF")
C2.deselect();
C2.grid(row = 8)

MentorLead= tk.Label(ADD, 
text='Enter Name of Mentor Lead:',
).grid(row = 9, column = 0)


entry7 = tk.Entry(ADD, width=12, borderwidth = 5).grid(row = 9, column = 1)

warn = tk.Label(ADD, text ='All fields with * must be filled out', fg = 'red').grid(row = 20, column = 0)
window.mainloop() #endless loop




