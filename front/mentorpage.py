from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector

class mentpage:
    def __init__(self,root,w):
        self.root=root
        self.root.title("Mentor Details")
        self.root.geometry("1550x800+0+0")
        self.email=w

        tabelfm=LabelFrame(self.root,bd=2,relief=RIDGE,text="Student Details",font=("arial",16,"bold"))
        tabelfm.place(x=2,y=2,width=1260,height=900)

        detablem=Frame(tabelfm,bd=2,relief=RIDGE)
        detablem.place(x=0,y=100,width=1200,height=350)    

        scroll_xm=ttk.Scrollbar(detablem,orient=HORIZONTAL)
        scroll_ym=ttk.Scrollbar(detablem,orient=VERTICAL)

        self.detailsm=ttk.Treeview(detablem,column=("ID","First Name","Middle Name","Last Name","DOB","Gender","email ID","phone no","Address","Department ID","Unit number","Hostelite","Room number","sgpa1","sgpa2","sgpa3","sgpa4","sgpa5","sgpa6","sgpa7","sgpa8","cgpa","Scholarship"),xscrollcommand=scroll_xm.set,yscrollcommand=scroll_ym.set)    
        
        scroll_xm.pack(side=BOTTOM,fill=X)
        scroll_ym.pack(side=RIGHT,fill=Y)

        scroll_xm.config(command=self.detailsm.xview)
        scroll_ym.config(command=self.detailsm.yview)

        # tabelf=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and search system",font=("arial",12,"bold"))
        # tabelf.place(x=660,y=2,width=660,height=900)

        labelsearch=Label(tabelfm,font=("arial",12,"bold"),text="Search by:",bg="black",fg="white")
        labelsearch.grid(row=0,column=0,sticky=W)


        self.search_var=StringVar()
        self.teext_search=StringVar()
        combo_search=ttk.Combobox(tabelfm,textvariable=self.search_var,font=("times new roman",12,"bold"),width=18,state="readonly")
        combo_search["value"]=("ID","Phone")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=5)
        
        txt_se=ttk.Entry(tabelfm,font=("arial",12,"bold"),textvariable=self.teext_search,width=24)
        txt_se.grid(row=0,column=2,padx=10)

        btnsearch=Button(tabelfm,font=("arial",12,"bold"),command=self.search,text="Search",bg="black",fg="white",width=5)
        btnsearch.grid(row=0,column=3,sticky=W,padx=5)

        btnshowall=Button(tabelfm,font=("arial",12,"bold"),command=self.fetch_datam,text="Show all",bg="black",fg="white",width=7)
        btnshowall.grid(row=0,column=4,sticky=W)

        # self.detailsm.heading("10th marks",text="10th marks")
        # self.detailsm.heading("12th marks",text="12th marks")
        # self.detailsm.heading("Qualifying exam rank",text="Qualifying exam rank")
        # self.detailsm.heading("Qualifying exam",text="Qualifying exam")
        # self.detailsm.heading("fee",text="Fee")
        # self.detailsm.heading("joining year",text="joining year")

        self.detailsm.heading("SRN",text="SRN")
        self.detailsm.heading("First Name",text="First Name")
        self.detailsm.heading("Middle Name",text="Middle Name")
        self.detailsm.heading("Last Name",text="Last Name")
        self.detailsm.heading("DOB",text="DOB")
        self.detailsm.heading("Gender",text="Gender")
        self.detailsm.heading("email ID",text="email ID")
        self.detailsm.heading("phone no",text="Phone no")
        self.detailsm.heading("Address",text="Address")
        self.detailsm.heading("Department ID",text="Dept ID")
        self.detailsm.heading("Hostelite",text="Hostelite")
        self.detailsm.heading("Unit number",text="Unit no")
        self.detailsm.heading("Room number",text="Room no")
        self.detailsm.heading("sgpa1",text="SGPA1")
        self.detailsm.heading("sgpa2",text="SGPA2")
        self.detailsm.heading("sgpa3",text="SGPA3")
        self.detailsm.heading("sgpa4",text="SGPA4")
        self.detailsm.heading("sgpa5",text="SGPA5")
        self.detailsm.heading("sgpa6",text="SGPA6")
        self.detailsm.heading("sgpa7",text="SGPA7")
        self.detailsm.heading("sgpa8",text="SGPA8")
        self.detailsm.heading("cgpa",text="cgpa")
        self.detailsm.heading("Scholarship",text="Scholarship")

        
        self.detailsm["show"]="headings"
        self.detailsm.pack(fill=BOTH,expand=1)
        # #self.details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_datam()


    def fetch_datam(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        #my_cur.callproc('UpdateScholarshipForAllRows')
        w=self.email
        query=("select id,fname,student.mname,lname,dob,gender,email,student.phone,address,did,hos,unit_no,room_no,sgpa1,sgpa2,sgpa3,sgpa4,sgpa5,sgpa6,sgpa7,sgpa8,cgpa,scholarship from student,sgpa,fam,mentor where mentor.memail=%s and id=sid and sid=ssid and mmid=mid")
        my_cur.execute(query,(w,))
        rows=my_cur.fetchall()
        print("in mentor page")
        print(rows)
        if len(rows)!=0:
            self.detailsm.delete(*self.detailsm.get_children())
            for i in rows:
                self.detailsm.insert("",END,values=i)
            conn.commit()
        conn.close()


    def search(self):
        print("here")
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        my_cur.execute("SELECT mid from mentor where memail=%s",(self.email,))
        row1=my_cur.fetchone()
        print(self.teext_search.get())
        my_cur.execute("SELECT id,fname,mname,lname,dob,gender,email,phone,address,did,hos,unit_no,room_no,sgpa1,sgpa2,sgpa3,sgpa4,sgpa5,sgpa6,sgpa7,sgpa8,cgpa,scholarship FROM student,sgpa,fam WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.teext_search.get()) + "%' and id=sid and sid=ssid and mmid=%s",(row1[0],))
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.detailsm.delete(*self.detailsm.get_children())
            for i in rows:
                self.detailsm.insert("",END,values=i)
            conn.commit()
        conn.close()

        

