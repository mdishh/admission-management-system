from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector

class accpage:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Details")
        self.root.geometry("1550x800+0+0")

        tabelfa=LabelFrame(self.root,bd=2,relief=RIDGE,text="Student Details",font=("arial",16,"bold"))
        tabelfa.place(x=2,y=2,width=1260,height=900)

        detablea=Frame(tabelfa,bd=2,relief=RIDGE)
        detablea.place(x=0,y=100,width=1200,height=350)    

        scroll_xa=ttk.Scrollbar(detablea,orient=HORIZONTAL)
        scroll_ya=ttk.Scrollbar(detablea,orient=VERTICAL)

        self.detailsa=ttk.Treeview(detablea,column=("ID","First Name","Middle Name","Last Name","DOB","Gender","email ID","phone no","Qualifying exam","fee","joining year","Department ID","Hostelite","sgpa1","sgpa2","sgpa3","sgpa4","sgpa5","sgpa6","sgpa7","sgpa8","CGPA","Scholarship"),xscrollcommand=scroll_xa.set,yscrollcommand=scroll_ya.set)    
        
        scroll_xa.pack(side=BOTTOM,fill=X)
        scroll_ya.pack(side=RIGHT,fill=Y)

        scroll_xa.config(command=self.detailsa.xview)
        scroll_ya.config(command=self.detailsa.yview)

        # tabelf=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and search system",font=("arial",12,"bold"))
        # tabelf.place(x=660,y=2,width=660,height=900)

        labelsearch=Label(tabelfa,font=("arial",12,"bold"),text="Search by:",bg="black",fg="white")
        labelsearch.grid(row=0,column=0,sticky=W)


        self.search_var=StringVar()
        combo_search=ttk.Combobox(tabelfa,textvariable=self.search_var,font=("times new roman",12,"bold"),width=18,state="readonly")
        combo_search["value"]=("ID","Phone")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=5)

        self.txt_search=StringVar()
        txtse=ttk.Entry(tabelfa,textvariable=self.txt_search,font=("arial",12,"bold"),width=24)
        txtse.grid(row=0,column=2,padx=10)

        btnsearch=Button(tabelfa,font=("arial",12,"bold"),command=self.search,text="Search",bg="black",fg="white",width=5)
        btnsearch.grid(row=0,column=3,sticky=W,padx=5)

        btnshowall=Button(tabelfa,font=("arial",12,"bold"),command=self.fetch_datama,text="Show all",bg="black",fg="white",width=7)
        btnshowall.grid(row=0,column=4,sticky=W)

        btnMRD=Button(tabelfa,font=("arial",12,"bold"),command=self.fetch_datamrd,text="MRD",bg="black",fg="white",width=7)
        btnMRD.grid(row=0,column=5,sticky=W,padx=3)

        btnCNR=Button(tabelfa,font=("arial",12,"bold"),command=self.fetch_datacnr,text="CNR",bg="black",fg="white",width=7)
        btnCNR.grid(row=0,column=6,sticky=W,padx=3)



        self.detailsa.heading("ID",text="ID")
        self.detailsa.heading("First Name",text="First Name")
        self.detailsa.heading("Middle Name",text="Middle Name")
        self.detailsa.heading("Last Name",text="Last Name")
        self.detailsa.heading("DOB",text="DOB")
        self.detailsa.heading("Gender",text="Gender")
        self.detailsa.heading("email ID",text="email ID")
        self.detailsa.heading("phone no",text="Phone no")
        self.detailsa.heading("Qualifying exam",text="Qualifying exam")
        self.detailsa.heading("fee",text="Fee")
        self.detailsa.heading("joining year",text="Joining year")
        self.detailsa.heading("Department ID",text="Dept ID")
        self.detailsa.heading("Hostelite",text="Hostelite")

        self.detailsa.heading("sgpa1",text="SGPA1")
        self.detailsa.heading("sgpa2",text="SGPA2")
        self.detailsa.heading("sgpa3",text="SGPA3")
        self.detailsa.heading("sgpa4",text="SGPA4")
        self.detailsa.heading("sgpa5",text="SGPA5")
        self.detailsa.heading("sgpa6",text="SGPA6")
        self.detailsa.heading("sgpa7",text="SGPA7")
        self.detailsa.heading("sgpa8",text="SGPA8")
        self.detailsa.heading("CGPA",text="CGPA")
        self.detailsa.heading("Scholarship",text="Scholarship")
        
        self.detailsa["show"]="headings"
        self.detailsa.pack(fill=BOTH,expand=1)
        # #self.details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_datama()


    def fetch_datama(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        query=("select id,fname,mname,lname,dob,gender,email,phone,qeexam,fee,join_year,did,hos,sgpa1,sgpa2,sgpa3,sgpa4,sgpa5,sgpa6,sgpa7,sgpa8,cgpa,scholarship from student,sgpa where id=sid")
        my_cur.execute(query)
        rows=my_cur.fetchall()
        # print(rows)
        if len(rows)!=0:
            self.detailsa.delete(*self.detailsa.get_children())
            for i in rows:
                self.detailsa.insert("",END,values=i)
            conn.commit()
        conn.close()

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="project")
        my_cur=conn.cursor()
        my_cur.execute("select id,fname,mname,lname,dob,gender,email,phone,qeexam,fee,join_year,did,hos,sgpa1,sgpa2,sgpa3,sgpa4,sgpa5,sgpa6,sgpa7,sgpa8,cgpa,scholarship FROM student,sgpa WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%' and id=sid")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.detailsa.delete(*self.detailsa.get_children())
            for i in rows:
                self.detailsa.insert("",END,values=i)
            conn.commit()
        conn.close()

    def fetch_datamrd(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="project")
        my_cur=conn.cursor()
        my_cur.execute("select id,fname,mname,lname,dob,gender,email,phone,qeexam,fee,join_year,did,hos,sgpa1,sgpa2,sgpa3,sgpa4,sgpa5,sgpa6,sgpa7,sgpa8,cgpa,scholarship from student,sgpa where id=sid and scholarship='MRD'")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.detailsa.delete(*self.detailsa.get_children())
            for i in rows:
                self.detailsa.insert("",END,values=i)
            conn.commit()
        my_cur.execute("select count(*) from sgpa group by scholarship having scholarship='MRD'")
        row=my_cur.fetchone()
        if row!=None:
            messagebox.showinfo("Details","Number of students awarded with MRD Scholarship is "+str(row[0]),parent=self.root)
        else:
            messagebox.showinfo("Details","Number of students awarded with MRD Scholarship is 0",parent=self.root)
        conn.close()

    def fetch_datacnr(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        my_cur.execute("select id,fname,mname,lname,dob,gender,email,phone,qeexam,fee,join_year,did,hos,sgpa1,sgpa2,sgpa3,sgpa4,sgpa5,sgpa6,sgpa7,sgpa8,cgpa,scholarship from student,sgpa where id=sid and scholarship='CNR'")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.detailsa.delete(*self.detailsa.get_children())
            for i in rows:
                self.detailsa.insert("",END,values=i)
            conn.commit()
        my_cur.execute("select count(*) from sgpa group by scholarship having scholarship='CNR'")
        row=my_cur.fetchone()
        if row!=None:
            messagebox.showinfo("Details","Number of students awarded with CNR Scholarship is "+str(row[0]),parent=self.root)
        else:
            messagebox.showinfo("Details","Number of students awarded with CNR Scholarship is 0",parent=self.root)
        conn.close()

