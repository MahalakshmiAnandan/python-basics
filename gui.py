from tkinter import*
a=Tk()
def check():
    h=Tk()
    if val1.get()=="123":
        h.config(bg="violet")
    else:
        h.config(bg="red")
    

val1=StringVar()
a.title("hello")
a.geometry("300x300")
b=Label(a,text="user name",font="sylfaen")
b.grid(row=0,column=0)
c=Label(a,text="password",font="sylfaen")
c.grid(row=1,column=0)
e=Entry(a)
e.grid(row=0,column=1)
f=Entry(a,show='*',textvariable=val1)
f.grid(row=1,column=1)
g=Button(a,text="Login",fg="red",command=check)
g.grid(row=2,column=1)


a.mainloop()
