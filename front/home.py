from tkinter import *
from PIL import Image,ImageTk
from about import cabout
from ach import cach
from contact import ccontact
from admissions import calumni
from login import clogin

class home:
    def __init__(self,root):
        self.root=root
        self.root.title("College admission management system")
        self.root.geometry("1550x800+0+0")

        #long image
        img1=Image.open("images\y.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lab=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lab.place(x=0,y=0,width=1550,height=140)

        #logo
        img2=Image.open("images\somelogo.png")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lab2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lab2.place(x=0,y=0,width=230,height=140)

        #title
        lab_t=Label(self.root,text="COLLEGE ADMISSION MANAGEMENT SYSTEM",font=("times new roman",32),bg="white",fg="black",bd=4,relief=RIDGE)
        lab_t.place(x=0,y=140,width=1550,height=50)

        #main frame(container)
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        ###all the buttons

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        #login
        login=Button(btn_frame,text="Login",width=22,command=self.calllogin,font=("times new roman",14,"bold"),bg="white",fg="black",bd=0,cursor="hand2")
        login.grid(row=0,column=0,pady=1)

        #about us
        about=Button(btn_frame,text="About us",command=self.onabout,width=22,font=("times new roman",14,"bold"),bg="white",fg="black",bd=0,cursor="hand2")
        about.grid(row=1,column=0,pady=1)

        #achievements
        ach=Button(btn_frame,text="Achievements",command=self.onach,width=22,font=("times new roman",14,"bold"),bg="white",fg="black",bd=0,cursor="hand2")
        ach.grid(row=2,column=0,pady=1)
        
        #notable alumni
        nota=Button(btn_frame,text="Admissions",command=self.onalumni,width=22,font=("times new roman",14,"bold"),bg="white",fg="black",bd=0,cursor="hand2")
        nota.grid(row=3,column=0,pady=1)

        #contact us
        con=Button(btn_frame,text="Contact Us",command=self.oncontact,width=22,font=("times new roman",14,"bold"),bg="white",fg="black",bd=0,cursor="hand2")
        con.grid(row=4,column=0,pady=1)
        

        ##main 
        img3=Image.open("images\x.png")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        right=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        right.place(x=225,y=0,width=1310,height=590)

        #bottom images

        
        img5=Image.open("images\zz.png")
        img5=img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        d2=Label(self.root,image=self.photoimg5,bd=4,relief=RIDGE)
        d2.place(x=0,y=420,width=230,height=290)


        ##functions imported from outside
    def onabout(self):
        self.new_wind=Toplevel(self.root)
        self.app=cabout(self.new_wind)
     
    def oncontact(self):
        self.new_window=Toplevel(self.root)
        self.app1=ccontact(self.new_window)

    def onach(self):
        self.new_window1=Toplevel(self.root)
        self.app2=cach(self.new_window1)

    def onalumni(self):
        self.new_window2=Toplevel(self.root)
        self.app2=calumni(self.new_window2)

    def calllogin(self):
        self.neww=Toplevel(self.root)
        self.app3=clogin(self.neww)

    
            




if __name__=='__main__':
    root=Tk()
    obj=home(root)
    root.mainloop()

