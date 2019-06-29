from tkinter import*
from tkinter import messagebox
a=Tk()
def check():
    amount=val1.get()*200+val2.get()*170+val3.get()*180+val4.get()*150
    gst=(12/100)*amount
    total=amount+gst
    
    i=Label(a,text=amount)
    i.grid(row=5,column=1)
    j=Label(a,text=gst)
    j.grid(row=4,column=1)
    a1=Tk()
    o=Label(a1,text="your bill amount:")
    o.grid(row=0,column=0)
    l=Label(a1,text=total)
    l.grid(row=0,column=1)
    
    
    
    
    
    
val1=IntVar()
val2=IntVar()
val3=IntVar()
val4=IntVar()
amount=IntVar()
gst=IntVar()

a.title("Thalapakatti")
a.geometry("500x500")
b=Label(a,text="biriyani",font="sylfaen")
b.grid(row=0,column=0)
c=Label(a,text="fried rice",font="sylfaen")
c.grid(row=1,column=0)
d=Label(a,text="noodles",font="sylfaen")
d.grid(row=2,column=0)
e=Label(a,text="chicken lolipop",font="sylfaen")
e.grid(row=3,column=0)
g=Label(a,text="amount",font="sylfaen")
g.grid(row=5,column=0)
g=Label(a,text="gst",font="sylfaen")
g.grid(row=4,column=0)


f1=Entry(a,textvariable=val1)
f1.grid(row=0,column=1)
f2=Entry(a,textvariable=val2)
f2.grid(row=1,column=1)
f3=Entry(a,textvariable=val3)
f3.grid(row=2,column=1)
f4=Entry(a,textvariable=val4)
f4.grid(row=3,column=1)
f5=Entry(a,textvariable=amount)
f5.grid(row=5,column=1)
f6=Entry(a,textvariable=gst)
f6.grid(row=4,column=1)



h=Button(a,text="Submit",command=check)
h.grid(row=6,column=1)



a.mainloop()
