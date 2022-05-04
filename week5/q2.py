from tkinter import *
window=Tk()
#Labels
Label(window,text="custid").grid(row=0,column=0)
Label(window,text="Customer name").grid(row=1,column=0)
Label(window,text="branch").grid(row=2,column=0)
Label(window,text="Amount type").grid(row=3,column=0)
Label(window,text="Amount").grid(row=4,column=0)
#Lists
custids=[]
names=[]
branches=[]
Amount_types=[]
amounts=[]
#Entries
id=Entry(window,width=25)
id.grid(row=0,column=1)
name=Entry(window,width=25)
name.grid(row=1,column=1)
branch=Entry(window,width=25)
branch.grid(row=2,column=1)
r = Radiobutton(window,text="Saving",value=0)
r.grid(row=3,column=1)
r1 = Radiobutton(window,text="Non-saving",value=1)
r1.grid(row=3,column=2)
amount=Scale(window,orient=HORIZONTAL)
amount.grid(row=4,column=1)
#Functions
def insert():
 custids.append(id.get())
 names.append(name.get())
 branches.append(branch.get())
 amounts.append(amount.get())
 id.delete(0,END)
 name.delete(0, END)
 branch.delete(0, END)
 amount.value=0
def update():
 for NAME in names:
    print(NAME,end=" ")
 print()
 for REG in custids:
    print(REG,end=" ")
 print()
 for DEPT in branches:
    print(DEPT,end=" ")
 print()
 for AGE in amounts:
    print(AGE,end=" ")
 print()
def delete():
 id.delete(0,END)
 name.delete(0, END)
 branch.delete(0, END)
 amount.delete(0, END)
#Button
Button(window,text="Insert",command=insert).grid(row=5,column=0)
Button(window,text="Delete",command=delete).grid(row=6,column=0)
Button(window,text="Update",command=update).grid(row=5,column=1)
Button(window,text="Select").grid(row=6,column=1)
window.mainloop()