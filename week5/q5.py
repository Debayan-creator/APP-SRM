from tkinter import *
window=Tk()
#Labels
Label(window,text="Booking id").grid(row=0,column=0)
Label(window,text="Name").grid(row=1,column=0)
Label(window,text="Movie NaMe").grid(row=2,column=0)
Label(window,text="Class").grid(row=3,column=0)
Label(window,text="Time of the show").grid(row=3,column=3)
Label(window,text="No. of tickets").grid(row=4,column=0)
#Lists
ids=[]
names=[]
movies=[]
times=[]
tickets=[]
#Entries
id=Entry(window,width=25)
id.grid(row=0,column=1)
name=Entry(window,width=25)
name.grid(row=1,column=1)
movie=Entry(window,width=25)
movie.grid(row=2,column=1)
r = Radiobutton(window,text="A",value=0)
r.grid(row=3,column=1)
r1 = Radiobutton(window,text="B",value=1)
r1.grid(row=3,column=2)
Checkbutton(window,text="7:15pm").grid(row=3,column=4)
Checkbutton(window,text="9:00pm").grid(row=3,column=5)
ticket=Scale(window,width=15,orient=HORIZONTAL)
ticket.grid(row=4,column=1)
#Functions
def insert():
 ids.append(id.get())
 names.append(name.get())
 tickets.append(ticket.get())
 movies.append(movie.get())
 id.delete(0,END)
 name.delete(0, END)
 movie.delete(0, END)
def update():
 for NAME in names:
    print(NAME,end=" ")
 print()
 for ID in ids:
    print(ID,end=" ")
 print()
 for MOVIE in movies:
    print(MOVIE,end=" ")
 print()
 for TICKET in tickets:
    print(TICKET,end=" ")
 print()
def delete():
 id.delete(0,END)
 name.delete(0, END)
 movie.delete(0, END)
#Button
Button(window,text="Insert",command=insert).grid(row=5,column=0)
Button(window,text="Delete",command=delete).grid(row=6,column=0)
Button(window,text="Update",command=update).grid(row=5,column=1)
Button(window,text="Select").grid(row=6,column=1)
window.mainloop()
