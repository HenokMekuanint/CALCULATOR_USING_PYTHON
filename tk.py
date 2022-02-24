from tkinter import *
import math
import tkinter.font as font

window=Tk()
window.geometry("500x500")
window.title("My calculator")
myFont = font.Font(size=10)

e=Entry(window,width=50)
e.pack()


negative=Button(window,text="Negative",command=lambda: e.insert(END,"-"))
negative.config(width=10,height=2)
negative['font'] = myFont
negative.place(x=0,y=470)

zero=Button(window,text="0",command=lambda: e.insert(END,"0"))
zero.config(width=10,height=2)
zero['font']= myFont
zero.place(x=90,y=470)

dot=Button(window,text=".",command=lambda: e.insert(END,"."))
dot.config(width=10,height=2)
dot['font']=myFont
dot.place(x=180,y=470)

def isequalto():
    text=e.get()
    new = text.split()
    lst = []
    for i in new:
        if i == "*":
            def multiplicaion():
                for j in new:
                    if j != "*":
                        lst.append(float(j))
                #print(lst[0] * lst[1])
                global x
                x=lst[0] * lst[1]

            multiplicaion()
        if i == "+":
            def addition():
                for k in new:
                    if k != "+":
                        lst.append(float(k))
                #print(lst[0] + lst[1])
                global x
                x=lst[0] + lst[1]
            addition()
        if i == "-":
            def subtraction():
                for l in new:
                    if l != "-":
                        lst.append(float(l))
                #print(lst[0] - lst[1])
                global x
                x=lst[0] - lst[1]
            subtraction()
        if i == "/":
            def division():
                for m in new:
                    if m != "/":
                        lst.append(float(m))
                #print(lst[0] / lst[1])
                global x
                x=lst[0] / lst[1]
            division()
        if i == "sqrt":
            def squareroot():
                for j in new:
                    if j != 'sqrt':
                        lst.append(float(j))
                #print(math.sqrt(lst[0]))
                global x
                x=math.sqrt(lst[0])
            squareroot()
        if i=="square":
            def square():
                for j in new:
                    if j!="square":
                        lst.append(float(j))
                global x
                x=lst[0]*lst[0]
            square()
    mylabel2=Label(window,text=x)
    mylabel2.pack()


equal=Button(window,text="=",command=isequalto)
equal.config(width=10,height=2)
equal['font']=myFont
equal.place(x=270,y=470)

one=Button(window,text="1",command=lambda: e.insert(END,"1"))
one.config(width=10,height=2)
one['font']=myFont
one.place(x=0,y=426)

two=Button(window,text="2",command=lambda: e.insert(END,"2"))
two.config(width=10,height=2)
two['font']=myFont
two.place(x=90,y=426)

three=Button(window,text="3",command=lambda: e.insert(END,"3"))
three.config(width=10,height=2)
three['font']=myFont
three.place(x=180,y=426)

plus=Button(window,text="+",command=lambda: e.insert(END," + "))
plus.config(width=10,height=2)
plus['font']=myFont
plus.place(x=270,y=426)

four=Button(window,text="4",command=lambda: e.insert(END,"4"))
four.config(width=10,height=2)
four['font']=myFont
four.place(x=0,y=382)

five=Button(window,text="5",command=lambda: e.insert(END,"5"))
five.config(width=10,height=2)
five['font']=myFont
five.place(x=90,y=382)

six=Button(window,text="6",command=lambda: e.insert(END,"6"))
six.config(width=10,height=2)
six['font']=myFont
six.place(x=180,y=382)

minus=Button(window,text="-",command=lambda: e.insert(END," - "))
minus.config(width=10,height=2)
minus['font']=myFont
minus.place(x=270,y=382)

seven=Button(window,text="7",command=lambda: e.insert(END,"7"))
seven.config(width=10,height=2)
seven['font']=myFont
seven.place(x=0,y=338)

eight=Button(window,text="8",command=lambda: e.insert(END,"8"))
eight.config(width=10,height=2)
eight['font']=myFont
eight.place(x=90,y=338)

nine=Button(window,text="9",command=lambda: e.insert(END,"9"))
nine.config(width=10,height=2)
nine['font']=myFont
nine.place(x=180,y=338)

multipication=Button(window,text="x",command=lambda: e.insert(END," * "))
multipication.config(width=10,height=2)
multipication['font']=myFont
multipication.place(x=270,y=338)

square_root=Button(window,text="sqrt",command=lambda: e.insert(END,"sqrt "))
square_root.config(width=10,height=2)
square_root['font']=myFont
square_root.place(x=0,y=294)

def delete():
    e.delete(1)
    e.pack()
    return

cancel=Button(window,text="cancel",command=delete)
cancel.config(width=10,height=2)
cancel['font']=myFont
cancel.place(x=90,y=294)

square=Button(window,text="square",command=lambda : e.insert(END,"square "))
square.config(width=10,height=2)
square['font']=myFont
square.place(x=180,y=294)

division=Button(window,text="/",command=lambda: e.insert(END," / "))
division.config(width=10,height=2)
division['font']=myFont
division.place(x=270,y=294)


window.mainloop()