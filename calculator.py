from tkinter import *
a=Tk()
a.config(bg="white")
a.geometry("570x600+100+200")
a.title("CALCULATOR")
eqn=""

def show(value):
    global eqn
    eqn+=value
    label_result.config(text=eqn)
def clear():
    global eqn
    eqn=""
    label_result.config(text=eqn)
def calculate():
    global eqn
    result=""
    if eqn!="":
        try:
            result=eval(eqn)
        except:
            result="error"
            eqn=""
    label_result.config(text=result)
    
label_result=Label(a,width=25,height=2,text="",font=("arial",30))
label_result.pack()
b1=Button(a,text="1",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("1"))
b2=Button(a,text="2",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("2"))
b3=Button(a,text="3",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("3"))
b4=Button(a,text="4",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("4"))
b5=Button(a,text="5",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("5"))
b6=Button(a,text="6",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("6"))
b7=Button(a,text="7",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("7"))
b8=Button(a,text="8",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("8"))
b9=Button(a,text="9",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("9"))
b10=Button(a,text="00",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("00"))
b11=Button(a,text="0",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("0"))
b12=Button(a,text=".",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("."))
b13=Button(a,text="=",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:calculate())
b14=Button(a,text="+",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("+"))
b15=Button(a,text="-",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("-"))
b16=Button(a,text="*",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("*"))
b17=Button(a,text="/",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("/"))
b18=Button(a,text="c",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:clear())
b19=Button(a,text="%",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("%"))
b20=Button(a,text="//",width=5,height=1,font=("calibri",30,"bold"),bg="blue",fg="black",bd=1,command=lambda:show("//"))
b1.place(x=10,y=100)
b2.place(x=150,y=100)
b3.place(x=290,y=100)
b4.place(x=10,y=200)
b5.place(x=150,y=200)
b6.place(x=290,y=200)
b7.place(x=10,y=300)
b8.place(x=150,y=300)
b9.place(x=290,y=300)
b10.place(x=10,y=400)
b11.place(x=150,y=400)
b12.place(x=290,y=400)
b13.place(x=0,y=500)
b14.place(x=430,y=100)
b15.place(x=430,y=200)
b16.place(x=430,y=300)
b17.place(x=430,y=400)
b18.place(x=150,y=500)
b19.place(x=290,y=500)
b20.place(x=430,y=500)


a.mainloop()

