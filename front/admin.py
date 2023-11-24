from tkinter import *
from student import cstudent
from teacher import cteacher
from sgpage import ssg

class cadmin:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin")
        self.root.geometry("1550x800+0+0")

        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=100,width=340,height=450)

        loginbtn1=Button(frame,text="Student Personal details",command=self.stu,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black")
        loginbtn1.place(x=75,y=100,width=220,height=35)

        loginbtn3=Button(frame,text="Student grades",command=self.ssgpa,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black")
        loginbtn3.place(x=100,y=200,width=150,height=35)

        loginbtn2=Button(frame,text="Mentor details",command=self.teach,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black")
        loginbtn2.place(x=100,y=300,width=150,height=35)



    def stu(self):
        self.new_wind=Toplevel(self.root)
        self.call1=cstudent(self.new_wind)

    def teach(self):
        self.new_wind=Toplevel(self.root)
        self.call2=cteacher(self.new_wind)

    def ssgpa(self):
        self.newr=Toplevel(self.root)
        self.call3=ssg(self.newr)



        

