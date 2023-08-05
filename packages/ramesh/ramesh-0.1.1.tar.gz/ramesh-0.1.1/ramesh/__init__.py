import csv
import pickle
import os
import turtle
import colorsys
from tkinter import *

def dice():
    import random

    global o,k,d,d1,d3,d2,t
    a=Tk()
    a.geometry("1024x786")
    a.configure(bg="chartreuse")

    def k(x):
        if x=='\u2680':
            return(1)
        elif x=='\u2681':
            return(2)
        elif x=='\u2682':
            return(3)
        elif x=='\u2683':
            return(4)
        elif x=='\u2684':
            return(5)
        elif x=='\u2685':
            return(6)


    def p():
        l=random.choice(o)
        l1=random.choice(o)
        
        l3=k(l)
        l2=k(l1)
        
        j=l3+l2
        d.config(text=l)
        d1.config(text=l1)

        d3.config(text=l2)
        d2.config(text=l3)
        t.config(text=f"your rolled total={j}")
        
    o=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']   




    m=Frame(a,height=100,width=600,bg="yellow")
    m.pack(pady=10)

    d=Label(m,text='',font="lucida 160 bold",fg='blue',bg='lightcoral')
    d.grid(row=0,column=0,padx=5)
    d2=Label(m,text='',font="lucida 16 bold",fg='blue',bg='lightcoral')
    d2.grid(row=1,column=0)

    d1=Label(m,text='',font="lucida 160 bold",fg='red',bg='lightseagreen')
    d1.grid(row=0,column=1)
    d3=Label(m,text='',font="lucida 16 bold",fg='blue',bg='lightcoral')
    d3.grid(row=1,column=1)





    c=Frame(a,height=90,width=600)
    Label(c,text='Dice making',bg='magenta',fg='olivedrab2',font='lucida 19 bold').pack()
    c.pack(side=TOP)


    b=Button(a,text="Roll Dice",command=p,bg='lightslateblue',fg="#FF6031",font="lucida 12 bold")
    b.pack(pady=20)

    t=Label(m,text='',font="lucida 26 bold",fg='blue',bg='lightcoral')
    t.grid(pady=40)

    p()

    a.mainloop()
class ramhasher:
    global m,update1,delete1,ramha,ramhas
    def update1():
        import pickle as d
        with open("xy.dat","ab") as a:
            b=input("enter any text")
            x=input("enter password")
            t={x:b}
            d.dump(t,a)
                   


            
    def ramhas():
        import pickle as d
        with open("xy.dat","rb") as a:
            b=input("enter any no")
            c=False
            while True:
                try:
                    l=d.load(a)
                    if b in l:
                        print(l[b])
                    c=True
                except EOFError:
                    break
    def delete1():
         import os
         h=open("xy.dat","rb")
         h1=open("tem.dat","wb")
         a={}
         found=False
         lo=input("enter roll no to delete:")
         while True:
               try:
                  a=pickle.load(h)
                  if lo in a:
                      found=True
                  else:
                       pickle.dump(a,h1)
               except EOFError:
                   break
         if found==False:
              print("record not found")
         else:
              print("record found and deleted")
         h.close()
         h1.close()
         os.remove("xy.dat")
         os.rename("tem.dat","xy.dat")
         h.close()
    def main():
        print("""
Type 1 for create encrypted document
Type 2 for show encrypted document
Type 3 for delete encrypted document
""")
        while True:
            m=int(input("enter any task"))
            if m==1:
                update1()
            elif m==2:
                ramhas()
            elif m==3:
                delete1()
            else:
                print("wrong enter")
            cj=input("Want more type (y/n)")
            if cj.lower()=="n":
                break
def table():
    from prettytable import PrettyTable
    v=int(input("enter total column No"))
    b=["S.no"]
    for i in range(v):
        b.append(input(f"enter column{i+1} name "))
    myTable = PrettyTable(b)
    m=[]
    n=[]
    n1=[]
    m1=[]
    m2=[]
    i=0
    try:
        while True:
            n.append(input(f"enter any row1 valuec{i+1}"))
            n1.append(input(f"enter any row2 value {i+1}"))
            if len(b)==4:
                m.append(input(f"enter any row3 value {i+1}"))
                myTable.add_row([i+1,n[i],n1[i],m[i]])
            elif len(b)==5:
                m.append(input(f"enter any row3 value {i+1}"))
                m1.append(input(f"enter any row4 value {i+1}"))
                myTable.add_row([i+1,n[i],n1[i],m[i],m1[i]])
            elif len(b)==6:
                m.append(input(f"enter any row3 value {i+1}"))
                m1.append(input(f"enter any row4 value {i+1}"))
                m2.append(input(f"enter any row5 value {i+1}"))
                myTable.add_row([i+1,n[i],n1[i],m[i],m1[i],m2[i]])
            else:
                myTable.add_row([i+1,n[i],n1[i]])
            ch=input("enter if you want more(y/n)")
            if ch=="n" or ch=='N':
                break
            i+=1
    except IndexError:
        pass
    print(myTable)
    a=open("FILE.txt","a")
    a.write("\n"+str(myTable))
    a.close()
    print("your file is ready\n name of yourfile is FILE.txt")

def csvreaderop(Filename):
    from prettytable import from_csv
    with open(Filename,'r') as d:
        s=from_csv(d)
    return s      


def notepad(pdx=30,pdy=2,bgi="lightblue",bgo="lightgreen"):
    "note pad bolte"
    def c():
        q.delete(1.0,END)

    def g():
        import tkinter.messagebox as t
        w=t.showinfo("Help",'click on PLACE ORDER button for placing order')
        print(w)
    def go():
        print("thank for visiting")
    def z():
        import tkinter.messagebox as t
        t.showwarning("warning",'please do not close the whole program close the page only.  \nAlso do not copy our program')    

    def save():
        open ("rrtr","w")

    op=Tk()
    op.geometry("1000x750")
    op.configure(bg=bgo)
    s=Scrollbar(op)
    s.pack(side=RIGHT, fill=Y)
    f4=Frame(width=300,height=80,borderwidth=10,bg='#3D59AB')
    Label(f4, text="Note pad with clear button",bg="orange",fg="red",font="lucida 25 bold",anchor='n').pack()
    f4.pack(side=TOP)
    q=Text(op,width=75,height=23,bg=bgi,yscrollcommand=s.set,font="lucida 17 bold")
    q.pack(padx=pdx,pady=pdy)
    cl=Button(op,text='clear screen',fg='red',font="lucida 20 bold",bg='pink',command=c)
    cl.pack(pady=3)
    m=Menu(op)
    m.add_command(label="Warning",command=z,font="lucida 30 bold")
    m.add_command(label="exit",command=exit)
    m.add_command(label="Help",command=g,font="lucida 30 bold")

    m.add_command(label="Save",command=save,font="lucida 30 bold")
    op.config(menu=m)


    s.config(command=q.yview)
    op.mainloop()
def pattern11():
    import turtle as tu
    tu.Screen().bgcolor("black")
    t=tu.Turtle()

    t.speed(0)
    h=0
    def line(ang,n):
        t.forward(n*0.25)
        t.right(ang)
        t.forward(n*0.25)
    t.goto(0,80)
    for i in range(160):
        t.width(i//100+2)
        c=colorsys.hsv_to_rgb(h,0.8,1)
        t.pencolor(c)
        line(90,i)
        line(50,i)
        t.circle(70,180)
        line(50,i)
        line(90,i)

        h+=0.005
    tu.done()



def pattern12():
    import turtle as tu
    tu.Screen().bgcolor("black")
    t=tu.Turtle()

    tu.width(4)
    t.speed("fastest")
    def square(x):
        for i in range(3):
            t.fd(x)
            t.lt(90)
        t.fd(x)
    for j in range(20):
        for i in range(10):
            t.color(colorsys.hsv_to_rgb(i/10,1-j/20,1))
            t.rt(135)
            square(150-j*4)
            t.rt(135)
            t.circle(50,36)
    tu.hideturtle()
    tu.done()


def pattern8():
    global a,n,h
    t = turtle.Turtle()
    t.screen.bgcolor("black")
    t.begin_fill()
    t.penup()
    t.goto(-200,-100)
    t.pendown()
    t.speed(10)

    a=400
    h=0
    n=100

    def triangle():
        global a,n,h
        for i in range(41):
            c = colorsys.hsv_to_rgb(h,1,0.9)
            h=h+(2/n)
            t.color(c)
            t.forward(a)
            t.left(120)
            a=a-10
    triangle()
    triangle()
    t.end_fill()
    t.clear()
    squary = turtle.Turtle()
    squary.speed(9000)
    #
    for i in range(400):
        c = colorsys.hsv_to_rgb(h,1,0.9)
        h=h+(25/n)
        squary.color(c)
        squary.forward(i)
        squary.left(91)
    triangle()
    t.hideturtle()
    turtle.done()
def pattern7():
    a=turtle.Screen()
    a.bgcolor("black")
    t=turtle.Pen()
    t.speed(11)

    c=[colorsys.hsv_to_rgb(h*0.3,1,0.9)
for h in range(6)]

    for i in range(200):
        t.pencolor(c[i%5])
        t.width(i/100+1)
        t.pu()
        t.forward(i*2)
        t.left(269*3.14+90)
        t.pd()
        t.circle(i,90)
        t.right(3.14*44+69)
        t.forward(10)
        t.circle(i,10)
    turtle.done()

def pattern6():
    t=turtle.Turtle()
    s=turtle.Screen()
    s.bgcolor("black")
    n=10
    h=0
    t.pensize(2)
    a=0
    b=0
    t.speed(100)
    t.goto(0,200)
    t.pendown()
    while(True):
        c=colorsys.hsv_to_rgb(h,1,0.9)
        h+=(1/n)
        t.pencolor(c)
        t.forward(a)
        t.right(b)
        a+=3
        b+=1
        if b==210:
           break
        t.hideturtle()
    turtle.done()
def pattern5():
    import turtle as t
    t.speed(0)
    t.bgcolor("black")

    h=0
    n=100

    for i in range(160):
        c = colorsys.hsv_to_rgb(h,1,0.9)
        h=h+(25/n)
        t.pencolor(c)
        t.right(i)
        t.circle(125,i)
        t.forward(i)
        t.right(90)
    t.done()

def pattern4():
    import turtle as t
    t.width(3)
    t.tracer(10)
    t.bgcolor("black")
    t.speed(10)
    h=0
    n=50
    for i in range(150):
        c = colorsys.hsv_to_rgb(h,1,0.8)
        h+=1/n
        t.pencolor(c)
        t.circle(i,90)
        t.forward(i)
        t.right(270)
        t.circle(i,270)
        t.forward(i)
        t.right(180)
    t.done()  
def pattern10():
    a=turtle.Screen()
    a.bgcolor("black")
    t=turtle.Pen()
    t.speed(12)

    h=0
    n=36
    t.penup()
    t.goto(550,-60)
    t.pendown()


    t.penup()
    t.left(119)
    t.forward(350)
    t.pendown()

    k=250
    while(k!=0):
        c=colorsys.hsv_to_rgb(h,0.6,0.8)
        t.pencolor(c)
        t.fillcolor(c)
        t.left(49)
        t.pu()
        t.forward(k)
        t.pd()
        t.begin_fill()
        t.circle(k,50)
        t.end_fill()
        t.pu()
        t.forward(k)
        t.circle(k,90)
        t.pd()




        k-=2
        h+=5/n
    turtle.done()


def pattern9():
    a=turtle.Screen()
    a.bgcolor("black")
    t=turtle.Pen()
    t.speed(12)

    h=0
    n=36

    for i in range(100):
        c=colorsys.hsv_to_rgb(h,0.7,0.9)
        t.width(i//50+1)
        t.pencolor(c)
        t.left(119)

        t.fillcolor(c)

        t.forward(i)
        t.circle(i,30)
        t.begin_fill()
        for j in range(9):
            t.right(225)
            t.forward(i*0.7)
        t.end_fill()

        t.forward(i*1.5)
        t.circle(i,120)

        h+=1/n
    turtle.done()



def pattern1():
    turtle.Screen().bgcolor("black")
    t=turtle.Pen()
    t.speed(12)
    h=0
    n=36

    for i in range(100):
        c=colorsys.hsv_to_rgb(h,0.6,1)
        t.width(i//100+1)
        t.pencolor(c)
        t.penup()
        t.left(90*i)
        t.circle(i,-45)
        t.forward(i*6)
        t.circle(i,30)
        t.pendown()
        
        while(i!=0):
            t.left(i)
            t.forward(i)
            t.right(90+i)
            t.backward(i*2)
            i -= 1
        h += 5/n
def pattern2():
    turtle.Screen().bgcolor("black")
    t=turtle.Pen()
    c=[colorsys.hsv_to_rgb(h*0.14,1,0.8) for h in range(6)]
    t.speed(0)
    for i in range(150):
        t.width(i//100+1)
        t.pu()
        t.pencolor(c[i%5])
        t.forward(i*2)
        t.pd()
        t.circle(i,-10)
        t.left(59)
        t.pu()
        t.forward(i*2)
        t.pd()
        t.circle(i*2,-120)
    turtle.done()

def pattern3():
    turtle.Screen().bgcolor("black")
    t=turtle.Pen()
    t.speed(11)
    h=0
    for i in range(260):
        c=colorsys.hsv_to_rgb(h,0.8,1)
        t.pencolor(c)
        t.left(60)
        t.circle(-i,30)
        t.circle(-i,-60)
        t.circle(-i,90)
        t.circle(-i,-30)

        h += 0.007

    turtle.done()


def all():
    """ramgui(text="efdwefew",title="wd wd wf defqe",size=30,speed=1000,pdx=30,pdy=60,bgo="white",bgi="#6bfb28",screen="1024x768")"""
    p=("diamond","ramgenrator","csvhelper.main()","BBF","ramgui","i_sort","b_sort"
       ,"s_sort","b_search","position","mergesort","lineasearch",'pattern 1-12',
       'notepad','dice',"cube","csvreaderop","table",'ramhasher.main()','infnitecsv')
    for i in p:
        print(i)
def csvhelper(Filename):
    global o,create,csvreaderop,show,exit,sum2,delete,append,update,search
    def create():
        with open(Filename,'w',newline='')as f:
            s=csv.writer(f)
            s.writerow(["names","roll","marks"])
            a=[]
            while True:
                a1=input("enter name:")
                a2=input("enter rollno:")
                a3=input("enter marks:")
                sp=[a1,a2,a3]
                a.append(sp)
                ch=input("do you want to enter more(y/n)")
                if ch=='n'or ch=='N':
                    break
            s.writerows(a)
    o=("""
Type 1 for create
Type 2 for show
Type 3 for exit
Type 4 for count row
Type 5 for search
Type 6 for delete
Type 7 for append on old file
Type 8 for update old content
""")

    def sum2():
        with open(Filename,'r')as f:
            a=csv.reader(f)
            c=0
            for r in a:
                c+=1
            print(c)
    def show():
        n=csvreaderop(Filename)
        print(n)
    def delete():
        h=open(Filename,"r")
        h1=open("temo.csv","w",newline='')
        a=csv.reader(h)
        s=csv.writer(h1)
        found=False
        lo=input("enter roll no to delete:")
        for i in a:
            if i[1]==lo:
                del i[0],i[1]
                found=True
            else:
                s.writerows([i])
        if(found==False):
            print("Roll no not found")
        else:
            print("Deleted sucessfully")
        h.close()
        h1.close()
        os.remove(Filename)
        os.rename("temo.csv",Filename)
        h.close()
    def append():
        with open(Filename,'a',newline='')as f:
            s=csv.writer(f)
##        s.writerow(["names","roll","marks"])
            a=[]
            while True:
                a1=input("enter name:")
                a2=input("enter rollno:")
                a3=input("enter marks:")
                sp=[a1,a2,a3]
                a.append(sp)
                ch=input("do you want to enter more(y/n)")
                if ch=='n'or ch=='N':
                    break
            s.writerows(a)
    def search():
        h=open(Filename,"r")
        a=csv.reader(h)
        found=False
        lo=input("enter roll no to search:")
        for i in a:
            if i[1]==lo:
                print(i[0],'\t',i[2])
                found=True
        if(found==False):
            print("Roll no not found")
        else:
            print("search sucessfully")
        h.close()

    def update():
        h=open(Filename,'r+')
        a=csv.reader(h)
        l=[]
        r=input("enter roll no:")
        found=False
        for i in a:
            if i[1]==r:
                found=True
                i[1]=r
                i[0]=input('new name')
                i[2]=input("new marks")
            l.append([i[0],i[1],i[2]])
        h.close()
        if found==False:
            print("student not found")
        else:
            h=open('B.csv','w+',newline='')
            s=csv.writer(h)
            s.writerows(l)
            h.seek(0)
            a=csv.reader(h)
            for i in a:
                print(i)
            h.close()
    
    def main():
        print(o)
        while True:
            m=int(input("enter task you want to do"))
            if m==1:
                create()
            elif m==2:
                show()
            elif m==3:
                break
            elif m==5:
                search()
            elif m==4:
                sum2()
            elif m==6:
                delete()
            elif m==7:
                append()
            elif m==8:
                update()
            else:
                break
    main()

def show():
     h=open("t.dat","rb+")
     a={}
     print("names\trollno\tmarks")
     while True:
           try:
              a= pickle.load(h)
              print(a['name'],'\t',a['roll'],'\t',a['marks'])
           except EOFError:
              break
    
def create():
    h=open("t.dat","wb")
    b={}
    while True:
         b['name']=input("enter name")
         b['roll']=input("enter rollno")
         b['marks']=input("enter marks")
         pickle.dump(b,h)
         ch=input("want more to enter (y/n)")
         if ch=='n'or ch=='N':
              break
         b={}
    h.close()
def append():
    h=open("t.dat","ab+")
    b={}
    n=int(input("enter no of data you want to add"))
    for i in range(n):
        b['name']=input("enter name")
        b['roll']=input("enter rollno")
        b['marks']=input("enter marks")
        pickle.dump(b,h)
        b={}
    h.close()
def search():
     h=open("t.dat","rb")
     a={}
     found=False
     lo=input("enter roll no to search:")
     try:
          while True:
               a=pickle.load(h)
               if (a['roll']==lo):
                    print(a['name'],'\t',a['marks']) 
                    found=True
     except EOFError:
          if(found==False):
               print("Roll no not found")
          else:
               print("search sucessfully")
          h.close()

     





def delete():
     h=open("t.dat","rb")
     h1=open("tem.dat","wb")
     a={}
     found=False
     lo=input("enter roll no to delete:")
     while True:
           try:
              a=pickle.load(h)
              if lo==a['roll']:
                       found=True
              else:
                   pickle.dump(a,h1)
           except EOFError:
               break
     if found==False:
          print("record not found")
     else:
          print("record found and deleted")
     h.close()
     h1.close()
     os.remove("t.dat")
     os.rename("tem.dat","t.dat")
     h.close()

def update():
     h=open("t.dat","rb+")
     a={}
     found=False
     lo=input("enter roll no to delete:")
     try:
          while True:
               po=h.tell()
               a=pickle.load(h)
               if (a['roll']==lo):
                    a['name']=input("enter new name ")
                    a['marks']=input("enter new marks ")
                    h.seek(po)
                    pickle.dump(a,h)
                    found=True
     except EOFError:
          if(found==False):
               print("Roll no not found")
          else:
               print("update sucessfully")
          h.close()


d=(
"""operation in binary file given by:-\n
Type 1 for create new
Type 2 for show file
Type 3 for append in old file
Type 4 for delete
Type 5 for update records
Type 6 for search
Type 7 for any other number for exit
Type 8 for calculation
""")

def exiti():
     exit()


def calcu():
     print("you can do calculation\nBy enter your operater and opertion")
     a=eval(input("enetr your operator and operation"))
     print(a)

def BBF():
    print(d)
    while True:
        n=int(input("you want to perfrom operation"))
        if n==1:
             create()
        elif n==2:
             show()
        elif n==3:
             append()
        elif n==4:
             delete()
        elif n==7:
             print("Tab on  yes for exit ")
             exiti()
        elif n==5:
             update()
        elif n==6:
             search()
        elif n==8:
             calcu()
               
        else:
            break


    

def diamond(a,v):
    "arg=number of rows and which word"
    for i in range(0,a):
        for j in range(0,a-1-i):
            print(end=" ")
        for s in range(0,i+1):
            print(v,end=" ")
        print()
    for i in range(a-1,0,-1):
        for j in range(a,i,-1):
            print(end=" ")
        for s in range(0,i):
            print(v,end=" ")
        print()
    
def ramgenrator(p,q):
    from random import randint
    p1=list(p)
    m=[]
    while p1:
        c=randint(0,len(p1)-1)
        o=p1[c]
        if o not in m:
            m.append(o)
            if len(m)==q:
                break
    return m
#selection sort
def s_sort(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a
def i_sort(a):
    v=a[1]
    b=len(a)
    for i in range(b):
        k=a[i]
        j=i-1
        while j>=0 and a[j]>k:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=k
    return a


##binary sort
def infnitecsv(Filename):
    import csv
    with open(Filename,'w',newline='')as f:
        s=csv.writer(f)
        w=[]
        q=int(input("enter total no of columns"))
        for i in range(q):
            w.append(input(f"enter column{i+1}name"))
        s.writerow(w)
        a=[]
        n=0
        if q==2:
            n+=1
            while True:
                a1=input(f"enter row value{n}")
                a2=input(f"enter row value{n}:")
                sp=[a1,a2]
                a.append(sp)
                ch=input("do you want to enter more(y/n)")
                if ch=='n'or ch=='N':
                    break
            s.writerows(a)
        
        elif q==3:
            while True:
                n+=1
                a1=input(f"enter row value{n}")
                a2=input(f"enter row value{n}:")
                a3=input(f"enter row value{n}:")
                sp=[a1,a2,a3]
                a.append(sp)
                ch=input("do you want to enter more(y/n)")
                if ch=='n'or ch=='N':
                    break
            s.writerows(a)
        
        elif q==4:
            while True:
                n+=1
                a1=input(f"enter row value{n}")
                a2=input(f"enter row value{n}:")
                a3=input(f"enter row value{n}:")
                a4=input(f"enter row value{n}")
                sp=[a1,a2,a3,a4]
                a.append(sp)
                ch=input("do you want to enter more(y/n)")
                if ch=='n'or ch=='N':
                    break
            s.writerows(a)
        elif q==5:
            n+=1
            while True:
                a1=input(f"enter row value{n}")
                a2=input(f"enter row value{n}:")
                a3=input(f"enter row value{n}:")
                a4=input(f"enter row value{n}")
                a5=input(f"enter row value{n}:")
                
                sp=[a1,a2,a3,a4,a5]
                a.append(sp)
                ch=input("do you want to enter more(y/n)")
                if ch=='n'or ch=='N':
                    break
            s.writerows(a)
        elif q==6:
            n+=1
            while True:
                a1=input(f"enter row value{n}")
                a2=input(f"enter row value{n}:")
                a3=input(f"enter row value{n}:")
                a4=input(f"enter row value{n}")
                a5=input(f"enter row value{n}:")
                a6=input(f"enter row value{n}:")
                sp=[a1,a2,a3,a4,a5,a6]
                a.append(sp)
                ch=input("do you want to enter more(y/n)")
                if ch=='n'or ch=='N':
                    break
            s.writerows(a)
        else:
            n+=1
            while True:
                a1=input(f"enter row value{n}")
                a2=input(f"enter row value{n}:")
                a3=input(f"enter row value{n}:")
                a4=input(f"enter row value{n}")
                a5=input(f"enter row value{n}:")
                a6=input(f"enter row value{n}:")
                a7=input(f"enter row value{n}:")
                sp=[a1,a2,a3,a4,a5,a6,a7]
                a.append(sp)
                ch=input("do you want to enter more(y/n)")
                if ch=='n'or ch=='N':
                    break
            s.writerows(a)
    print(csvreaderop(Filename))









            

def b_sort(a):
    x=0
    v=False
    while x<len(a) and v==False:
        v=True
        for j in range(len(a)-1-x):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                v=False
        x+=1
    return a


#mergeSort
def mergesort(a,s):
    b=[]
    w=len(a+s)//2+4
    try:
        for i in range(w):
            if a[0]>s[0]:
                b.append(s.pop(0))
            else:
                b.append(a.pop(0))
    except IndexError:
        pass
    b+=a
    b+=s
    return b

def linearsearch(o,p):
    w=0
    b=len(o)
    while w<b:
        m=(w+b)//2
        if o[m]==p:
            return (m+1,True)
        elif o[m]<=p:
            w=m-1
        else:
            b=m+1
            break
    return False

def position(l,b):
    global a
    for i in range(len(l)):
        if l[i]==b:
            print("position",i+1)
            return True
    else:
        return False
def b_search(a,b,c,d):
    if c>=d:
        return False
    m=int((c+d//2))
    if a[m]==b:
        return m
    elif a[m]<b:
        return (b_search(a,b,c+1,d))
    else:
        return (b_search(a,b,c,m-1))
from tkinter import *
import random
def ramgui(text,title,size,speed,pdx,pdy,bgo="white",bgi="#6bfb28",screen="1024x768"):
    """arguments = text,title,bgi,size,speed,pdx,pdy,bgo=white",bgi="#6bfb28",screen="1024x768"""
    global lable,l4,a4
    a4=Tk()
    a4.title("We are thankful of ramesh")
    a4.geometry("1024x768")
    a4.configure(bg=bgi)
##    t2=("""Amul is best, Amul is an Indian state gvernment
##    cooperative under the ownership of Gujarat Cooperative
##    Milk Marketing Federation, Ministry of Cooperation,
##    gvernment of Gujarat based at Anand in Gujarat.
##    Formed in 1946, it is a cooperative brand managed
##    (GCMMF), which today is jointly controlled by 46
##    lakh (4.6 million) milk producers in Gujarat
##    and the apex body of 13 district milk unions,
##    spread across 15,000 villages of Gujarat. Amul
##    Give India's White Revolution, which made
##    country the worlds largest producer of milk
##    and milk products and \nTHANKING YOU FOR WATCHING
##        """)#text,title,padd,y-x,size
    
    l4=Label(a4, bg='#ffffff')
    l4.place(x=pdx, y=pdy)
    def lable():
        color = '#'+("%06x" % random.randint(0, 0xFFFFFF))
        l4.config(text=text, bg=bgo,fg=(color),font=f"lucida {size} bold")
        a4.after(speed, lable)
    lable()
    color = '#'+("%06x" % random.randint(0, 0xFFFFFF))
    f4=Frame(width=300,height=80,borderwidth=12,bg=color)
    Label(f4, text=title,bg="lightgreen",fg="red",
          font="lucida 34 bold",anchor='n').pack()
    f4.pack(side=TOP)
    def o():
        import time
        time.sleep(6)
    Button(a4,text="stop",fg="red",bg="white",font="lucida 13 bold",
            command=o).pack(side=BOTTOM)
    a4.mainloop()




















        
