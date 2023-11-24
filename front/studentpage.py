from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector

class studpage:
    def __init__(self,root,x):
        self.root=root
        self.root.title("Student details")
        self.root.geometry("1550x800+0+0")

        tabelf=LabelFrame(self.root,bd=2,relief=RIDGE,text="My Details",font=("arial",12,"bold"))
        tabelf.place(x=2,y=2,width=660,height=900)

        detable=Frame(tabelf,bd=2,relief=RIDGE)
        detable.place(x=0,y=50,width=650,height=350)    

        scroll_x=ttk.Scrollbar(detable,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detable,orient=VERTICAL)

        

        self.details=ttk.Treeview(detable,column=("ID","First Name","Middle Name","Last Name","DOB","Gender","email ID","phone no","Address","10th marks","12th marks","Qualifying exam rank","Qualifying exam","fee","joining year","Department ID","Hostelite","Unit number","Room number"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)    
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.details.xview)
        scroll_y.config(command=self.details.yview)

        self.details.heading("ID",text="ID")
        self.details.heading("First Name",text="First Name")
        self.details.heading("Middle Name",text="Middle Name")
        self.details.heading("Last Name",text="Last Name")
        self.details.heading("DOB",text="DOB")
        self.details.heading("Gender",text="Gender")
        self.details.heading("email ID",text="email ID")
        self.details.heading("phone no",text="Phone number")
        self.details.heading("Address",text="Address")
        self.details.heading("10th marks",text="10th marks")
        self.details.heading("12th marks",text="12th marks")
        self.details.heading("Qualifying exam rank",text="Qualifying exam rank")
        self.details.heading("Qualifying exam",text="Qualifying exam")
        self.details.heading("fee",text="Fee")
        self.details.heading("joining year",text="joining year")
        self.details.heading("Department ID",text="Department ID")
        self.details.heading("Hostelite",text="Hostelite")
        self.details.heading("Unit number",text="Unit number")
        self.details.heading("Room number",text="Room number")
        
        self.details["show"]="headings"
        self.details.pack(fill=BOTH,expand=1)
        #self.details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data(x)

        ###########FAM###################
        info=Frame(tabelf,bd=2,relief=RIDGE) 
        info.place(x=2,y=500,width=300,height=100)

        FLabel=Label(info,text="My Faculty Advisor",font=("arial",12,"bold"))
        FLabel.grid(row=0,column=0,sticky=W)

        FaLabel=Label(info,text=self.get_fam(x),font=("arial",12,"bold"))
        FaLabel.grid(row=2,column=0,sticky=W)

        
        ###gpas

        tabelfg=LabelFrame(self.root,bd=2,relief=RIDGE,text="My Achievements",font=("arial",12,"bold"))
        tabelfg.place(x=660,y=2,width=660,height=900)

        detableg=Frame(tabelfg,bd=2,relief=RIDGE)
        detableg.place(x=0,y=50,width=650,height=350)    

        scroll_xg=ttk.Scrollbar(detableg,orient=HORIZONTAL)
        scroll_yg=ttk.Scrollbar(detableg,orient=VERTICAL)

        self.detailsg=ttk.Treeview(detableg,column=("SGPA1","SGPA2","SGPA3","SGPA4","SGPA5","SGPA6","SGPA7","SGPA8","CGPA","Scholarship"),xscrollcommand=scroll_xg.set,yscrollcommand=scroll_yg.set)
        self.detailsg.heading("SGPA1",text="SGPA1")
        self.detailsg.heading("SGPA2",text="SGPA2")
        self.detailsg.heading("SGPA3",text="SGPA3")
        self.detailsg.heading("SGPA4",text="SGPA4")
        self.detailsg.heading("SGPA5",text="SGPA5")
        self.detailsg.heading("SGPA6",text="SGPA6")
        self.detailsg.heading("SGPA7",text="SGPA7")
        self.detailsg.heading("SGPA8",text="SGPA8")
        self.detailsg.heading("CGPA",text="CGPA")
        self.detailsg.heading("Scholarship",text="Scholarship")

        self.detailsg.column("SGPA1", width=20)
        self.detailsg.column("SGPA2", width=20)
        self.detailsg.column("SGPA3", width=20)
        self.detailsg.column("SGPA4", width=20)
        self.detailsg.column("SGPA5", width=20)
        self.detailsg.column("SGPA6", width=20)
        self.detailsg.column("SGPA7", width=20)
        self.detailsg.column("SGPA8", width=20)
        self.detailsg.column("CGPA", width=20)
        self.detailsg.column("Scholarship", width=20)

        self.detailsg["show"]="headings"
        self.detailsg.pack(fill=BOTH,expand=1)
        self.fetch_datag(x)


    def fetch_data(self,x):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        query=("select * from student where email=%s")
        my_cur.execute(query,(x,))
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.details.delete(*self.details.get_children())
            for i in rows:
                self.details.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_fam(self,x):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        query=("select mentor.mname from mentor,fam,student where mid=mmid and ssid=id and email=%s")
        my_cur.execute(query,(x,))
        rows=my_cur.fetchall()
        conn.commit()
        conn.close()
        return rows


    def fetch_datag(self,x):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        query=("select sgpa1,sgpa2,sgpa3,sgpa4,sgpa5,sgpa6,sgpa7,sgpa8,cgpa,scholarship from sgpa,student where sid=id and email=%s")
        print(x)
        my_cur.execute(query,(x,))
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.detailsg.delete(*self.detailsg.get_children())
            for i in rows:
                self.detailsg.insert("",END,values=i)
            conn.commit()
        conn.close()

    

# if __name__=='__main__':
#     root=Tk()
#     obj1=studpage()
#     root.mainloop()
