from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector

class cstudent:
    def __init__(self,root):
        self.root=root
        self.root.title("Student details")
        self.root.geometry("1550x800+0+0")

        #variables
        self.svar_gender=""
        self.qev=""
        self.hst=""
        self.gvar_gender=""
        self.alum=""


        self.svar_genderv=StringVar()
        self.qevv=StringVar()
        self.hstv=StringVar()
        self.gvar_genderv=StringVar()
        self.alumv=StringVar()
        self.srnv=StringVar()
        self.fnamev=StringVar()
        self.mnamev=StringVar()
        self.lnamev=StringVar()
        self.dobv=StringVar()
        self.emailv=StringVar()
        self.phv=StringVar()
        self.addv=StringVar()
        self.tenv=StringVar()
        self.twev=StringVar()
        self.qrv=StringVar()
        self.feev=StringVar()
        self.jyearv=StringVar()
        self.didv=StringVar()
        self.unitv=StringVar()
        self.roomv=StringVar()

        self.gnamev=StringVar()
        self.gelv=StringVar()
        self.gmailv=StringVar()
        self.gdescv=StringVar()
        self.gphv=StringVar()
        self.gaddv=StringVar()
        self.gagev=StringVar()
        self.gsrnv=StringVar()
        self.alumv=StringVar()
        self.gvar_genderv=StringVar()
        #logo
        img2=Image.open("images\somelogo.png")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lab2=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lab2.place(x=0,y=0,width=230,height=140)


        lframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Student details",padx=2,font=("times new roman",12,"bold"))
        lframe.place(x=5,y=2,width=325,height=900)

        lframe2=LabelFrame(self.root,bd=2,relief=RIDGE,text="Guardian details",padx=2,font=("times new roman",12,"bold"))
        lframe2.place(x=330,y=2,width=325,height=900)

        #labels and entries

        #stud_id
        stud_id_label=Label(lframe,text="Student ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        stud_id_label.grid(row=0,column=0,sticky=W)
        self.entry_ref=ttk.Entry(lframe,width=20,textvariable=self.srnv,font=("times new roman",12,"bold"))
        self.entry_ref.grid(row=0,column=1)
        
        #fname
        fname_label=Label(lframe,text="First name",font=("times new roman",12,"bold"),padx=2,pady=6)
        fname_label.grid(row=1,column=0,sticky=W)
        self.entry_fname=ttk.Entry(lframe,width=20,textvariable=self.fnamev,font=("times new roman",12,"bold"))
        self.entry_fname.grid(row=1,column=1)
        #mname
        mname_label=Label(lframe,text="Middle name",font=("times new roman",12,"bold"),padx=2,pady=6)
        mname_label.grid(row=2,column=0,sticky=W)
        self.entry_mname=ttk.Entry(lframe,width=20,textvariable=self.mnamev,font=("times new roman",12,"bold"))
        self.entry_mname.grid(row=2,column=1)
        #lname
        lname_label=Label(lframe,text="Last Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lname_label.grid(row=3,column=0,sticky=W)
        self.entry_lname=ttk.Entry(lframe,width=20,textvariable=self.lnamev,font=("times new roman",12,"bold"))
        self.entry_lname.grid(row=3,column=1)
        #dob
        dob_label=Label(lframe,text="Date of Birth",font=("times new roman",12,"bold"),padx=2,pady=6)
        dob_label.grid(row=4,column=0,sticky=W)
        self.entry_dob=ttk.Entry(lframe,width=20,textvariable=self.dobv,font=("times new roman",12,"bold"))
        self.entry_dob.grid(row=4,column=1)
        #gender
        gen_label=Label(lframe,text="Gender",font=("times new roman",12,"bold"),padx=2,pady=6)
        gen_label.grid(row=5,column=0,sticky=W)
        self.combo_gender=ttk.Combobox(lframe,textvariable=self.svar_genderv,font=("times new roman",12,"bold"),width=18,state="readonly")
        self.combo_gender["value"]=("M","F","O")
        self.combo_gender.current(0)
        self.combo_gender.grid(row=5,column=1)
        #emailid
        email_id_label=Label(lframe,text="email ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        email_id_label.grid(row=6,column=0,sticky=W)
        self.entry_email=ttk.Entry(lframe,width=20,textvariable=self.emailv,font=("times new roman",12,"bold"))
        self.entry_email.grid(row=6,column=1)
        #phone number
        phone_label=Label(lframe,text="Phone number",font=("times new roman",12,"bold"),padx=2,pady=6)
        phone_label.grid(row=7,column=0,sticky=W)
        self.entry_phone=ttk.Entry(lframe,width=20,textvariable=self.phv,font=("times new roman",12,"bold"))
        self.entry_phone.grid(row=7,column=1)
        #address
        add_label=Label(lframe,text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)
        add_label.grid(row=8,column=0,sticky=W)
        self.entry_add=ttk.Entry(lframe,width=20,textvariable=self.addv,font=("times new roman",12,"bold"))
        self.entry_add.grid(row=8,column=1)
        #10th
        tenth_label=Label(lframe,text="10th marks",font=("times new roman",12,"bold"),padx=2,pady=6)
        tenth_label.grid(row=9,column=0,sticky=W)
        self.entry_tenth=ttk.Entry(lframe,width=20,textvariable=self.tenv,font=("times new roman",12,"bold"))
        self.entry_tenth.grid(row=9,column=1)
        #12th
        twelfth_id_label=Label(lframe,text="12th marks",font=("times new roman",12,"bold"),padx=2,pady=6)
        twelfth_id_label.grid(row=10,column=0,sticky=W)
        self.entry_twelfth=ttk.Entry(lframe,width=20,textvariable=self.twev,font=("times new roman",12,"bold"))
        self.entry_twelfth.grid(row=10,column=1)
        #qe
        qual_ex_label=Label(lframe,text="Qualifying Exam",font=("times new roman",12,"bold"),padx=2,pady=6)
        qual_ex_label.grid(row=11,column=0,sticky=W)
        self.combo_qe=ttk.Combobox(lframe,textvariable=self.qevv,font=("times new roman",12,"bold"),width=18,state="readonly")
        self.combo_qe["value"]=("PESSAT","KCET","JEE")
        self.combo_qe.current(0)
        self.combo_qe.grid(row=11,column=1)
        print(self.twev)
        
        #qe rank
        qual_rank_label=Label(lframe,text="Qualifying Exam Rank",font=("times new roman",12,"bold"),padx=2,pady=6)
        qual_rank_label.grid(row=12,column=0,sticky=W)
        self.entry_qual_rank=ttk.Entry(lframe,width=20,textvariable=self.qrv,font=("times new roman",12,"bold"))
        self.entry_qual_rank.grid(row=12,column=1)
        
        #fee
        fee_label=Label(lframe,text="Fee",font=("times new roman",12,"bold"),padx=2,pady=6)
        fee_label.grid(row=13,column=0,sticky=W)
        self.entry_fee=ttk.Entry(lframe,width=20,textvariable=self.feev,font=("times new roman",12,"bold"))
        self.entry_fee.grid(row=13,column=1)
        #joining year
        jyear_label=Label(lframe,text="joining year",font=("times new roman",12,"bold"),padx=2,pady=6)
        jyear_label.grid(row=14,column=0,sticky=W)
        self.entry_jyear=ttk.Entry(lframe,width=20,textvariable=self.jyearv,font=("times new roman",12,"bold"))
        self.entry_jyear.grid(row=14,column=1)
        #dept_id
        # did_label=Label(lframe,text="Department ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        # did_label.grid(row=15,column=0,sticky=W)
        # self.entry_did=ttk.Entry(lframe,width=20,textvariable=self.didv,font=("times new roman",12,"bold"))
        # self.entry_did.grid(row=15,column=1)
        did_label=Label(lframe,text="Dept ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        did_label.grid(row=15,column=0,sticky=W)
        self.combo_did=ttk.Combobox(lframe,textvariable=self.didv,font=("times new roman",12,"bold"),width=18,state="readonly")
        self.combo_did["value"]=("CSE","AI&ML","ME","ECE")
        self.combo_did.current(1)
        self.combo_did.grid(row=15,column=1)
        #hostel
        hosyes=Label(lframe,text="Hostel",font=("times new roman",12,"bold"),padx=2,pady=6)
        hosyes.grid(row=16,column=0,sticky=W)
        self.combo_hosyes=ttk.Combobox(lframe,textvariable=self.hstv,font=("times new roman",12,"bold"),width=18,state="readonly")
        self.combo_hosyes["value"]=("Y","N")
        self.combo_hosyes.current(1)
        self.combo_hosyes.grid(row=16,column=1)

        unit_label=Label(lframe,text="Unit no",font=("times new roman",12,"bold"),padx=2,pady=6)
        unit_label.grid(row=17,column=0,sticky=W)
        self.entry_unit=ttk.Entry(lframe,width=20,textvariable=self.unitv,font=("times new roman",12,"bold"))
        self.entry_unit.grid(row=17,column=1)

        room_label=Label(lframe,text="Room no",font=("times new roman",12,"bold"),padx=2,pady=6)
        room_label.grid(row=18,column=0,sticky=W)
        self.entry_room=ttk.Entry(lframe,width=20,textvariable=self.roomv,font=("times new roman",12,"bold"))
        self.entry_room.grid(row=18,column=1)

        ###############Guardian
        #guardian name
        gname_label=Label(lframe2,text="Guardian name",font=("times new roman",12,"bold"),padx=2,pady=6)
        gname_label.grid(row=0,column=0,sticky=W)
        self.entry_gname=ttk.Entry(lframe2,textvariable=self.gnamev,width=20,font=("times new roman",12,"bold"))
        self.entry_gname.grid(row=0,column=1)

        #relation
        grel_label=Label(lframe2,text="Relation",font=("times new roman",12,"bold"),padx=2,pady=6)
        grel_label.grid(row=1,column=0,sticky=W)
        self.entry_grel=ttk.Entry(lframe2,textvariable=self.gelv,width=20,font=("times new roman",12,"bold"))
        self.entry_grel.grid(row=1,column=1)

        #email
        gem_label=Label(lframe2,text="email id",font=("times new roman",12,"bold"),padx=2,pady=6)
        gem_label.grid(row=2,column=0,sticky=W)
        self.entry_gem=ttk.Entry(lframe2,width=20,textvariable=self.gmailv,font=("times new roman",12,"bold"))
        self.entry_gem.grid(row=2,column=1)

        #designation
        gdes_label=Label(lframe2,text="Designation",font=("times new roman",12,"bold"),padx=2,pady=6)
        gdes_label.grid(row=3,column=0,sticky=W)
        self.entry_gdes=ttk.Entry(lframe2,textvariable=self.gdescv,width=20,font=("times new roman",12,"bold"))
        self.entry_gdes.grid(row=3,column=1)

        #phone number
        gp_label=Label(lframe2,text="Phone number",font=("times new roman",12,"bold"),padx=2,pady=6)
        gp_label.grid(row=4,column=0,sticky=W)
        self.entry_gp=ttk.Entry(lframe2,textvariable=self.gphv,width=20,font=("times new roman",12,"bold"))
        self.entry_gp.grid(row=4,column=1)

        #address
        gadd_label=Label(lframe2,text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)
        gadd_label.grid(row=5,column=0,sticky=W)
        self.entry_gadd=ttk.Entry(lframe2,textvariable=self.gaddv,width=20,font=("times new roman",12,"bold"))
        self.entry_gadd.grid(row=5,column=1)

        #age
        gage_label=Label(lframe2,text="Age",font=("times new roman",12,"bold"),padx=2,pady=6)
        gage_label.grid(row=6,column=0,sticky=W)
        self.entry_gage=ttk.Entry(lframe2,textvariable=self.gagev,width=20,font=("times new roman",12,"bold"))
        self.entry_gage.grid(row=6,column=1)

    
        #alumnus
        galu_label=Label(lframe2,text="Alumnus of PES",font=("times new roman",12,"bold"),padx=2,pady=6)
        galu_label.grid(row=7,column=0,sticky=W)
        self.combo_galu=ttk.Combobox(lframe2,textvariable=self.alumv,font=("times new roman",12,"bold"),width=18,state="readonly")
        self.combo_galu["value"]=("Y","N")
        self.combo_galu.current(0)
        self.combo_galu.grid(row=7,column=1)

        #gender
        ggen_label=Label(lframe2,text="Gender",font=("times new roman",12,"bold"),padx=2,pady=6)
        ggen_label.grid(row=8,column=0,sticky=W)
        self.combo_ggen=ttk.Combobox(lframe2,textvariable=self.gvar_genderv,font=("times new roman",12,"bold"),width=18,state="readonly")
        self.combo_ggen["value"]=("M","F","O")
        self.combo_ggen.current(0)
        self.combo_ggen.grid(row=8,column=1)

        #vars        
        self.srn=self.entry_ref.get()
        self.fname=self.entry_fname.get()
        self.mname=self.entry_mname.get()
        self.lname=self.entry_lname.get()
        self.dob=self.dobv.get()
        self.email=self.entry_email.get()
        self.ph=self.entry_phone.get()
        self.add=self.entry_add.get()
        self.ten=self.entry_tenth.get()
        self.twe=self.entry_twelfth.get()
        self.qr=self.entry_qual_rank.get()
        self.fee=self.entry_fee.get()
        self.jyear=self.entry_jyear.get()
        self.did=self.combo_did.get()
        self.unit=self.entry_unit.get()
        self.room=self.entry_room.get()

        self.gname=self.entry_gname.get()
        self.gel=self.entry_grel.get()
        self.gmail=self.entry_gem.get()
        self.gdesc=self.entry_gdes.get()
        self.gph=self.entry_gp.get()
        self.gadd=self.entry_gadd.get()
        self.gage=self.entry_gage.get()
        self.gsrn=self.entry_ref.get()

        


        #buttons++++++++
        btn_frame=Frame(lframe2,bd=2,relief=RIDGE)
        btn_frame.place(x=2,y=500,width=250,height=200)
        add_btn=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="white",width=10)
        add_btn.grid(row=3,column=0,padx=5,pady=20)

        upd_btn=Button(btn_frame,text="Update",command=self.update_data,font=("arial",12,"bold"),bg="black",fg="white",width=10)
        upd_btn.grid(row=3,column=2,padx=5,pady=20)

        del_btn=Button(btn_frame,text="Delete",command=self.sdelete,font=("arial",12,"bold"),bg="black",fg="white",width=10)
        del_btn.grid(row=6,column=0,padx=5,pady=20)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset1,font=("arial",12,"bold"),bg="black",fg="white",width=10)
        reset_btn.grid(row=6,column=2,padx=5,pady=20)

        #################search system##########################

        tabelf=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and search system",font=("arial",12,"bold"))
        tabelf.place(x=660,y=2,width=660,height=900)

        labelsearch=Label(tabelf,font=("arial",12,"bold"),text="Search by:",bg="black",fg="white")
        labelsearch.grid(row=0,column=0,sticky=W)


        self.search_var=StringVar()
        combo_search=ttk.Combobox(tabelf,textvariable=self.search_var,font=("times new roman",12,"bold"),width=18,state="readonly")
        combo_search["value"]=("Phone","ID")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=5)

        self.txt_search=StringVar()
        txtse=ttk.Entry(tabelf,textvariable=self.txt_search,font=("arial",12,"bold"),width=24)
        txtse.grid(row=0,column=2,padx=10)

        btnsearch=Button(tabelf,font=("arial",12,"bold"),command=self.search,text="Search",bg="black",fg="white",width=5)
        btnsearch.grid(row=0,column=3,sticky=W,padx=5)

        btnshowall=Button(tabelf,font=("arial",12,"bold"),command=self.fetch_data,text="Show all",bg="black",fg="white",width=7)
        btnshowall.grid(row=0,column=4,sticky=W)

        #===========show data
        detable=Frame(tabelf,bd=2,relief=RIDGE)
        detable.place(x=0,y=50,width=650,height=350)    

        scroll_x=ttk.Scrollbar(detable,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detable,orient=VERTICAL)

       

        self.details=ttk.Treeview(detable,column=("ID","First Name","Middle Name","Last Name","DOB","Gender","email ID","phone no","Address","10th marks","12th marks","Qualifying exam","Qualifying exam rank","fee","joining year","Department ID","Hostelite","Unit number","Room number","Guardian name","Relation","Email Id","Designation","phone number","address","Age","Alumnus of PES","gender"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)    
        
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
        self.details.heading("Qualifying exam",text="Qualifying exam")
        self.details.heading("Qualifying exam rank",text="Qualifying exam rank")
        self.details.heading("fee",text="Fee")
        self.details.heading("joining year",text="joining year")
        self.details.heading("Department ID",text="Department ID")
        self.details.heading("Hostelite",text="Hostelite")
        self.details.heading("Unit number",text="Unit number")
        self.details.heading("Room number",text="Room number")
        
        self.details.heading("Guardian name",text="Guardian name")
        self.details.heading("Relation",text="Relation")
        self.details.heading("Email Id",text="Email Id")
        self.details.heading("Designation",text="Designation")
        self.details.heading("phone number",text="phone number")
        self.details.heading("address",text="address")
        self.details.heading("Age",text="Age")
        self.details.heading("Alumnus of PES",text="Alumnus of PES")
        self.details.heading("gender",text="gender")
        self.details["show"]="headings"
        self.details.pack(fill=BOTH,expand=1)
        self.details.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor(buffered=True)
        my_cur.execute("select id from student where id=%s",(self.entry_ref.get(),))
#         ro10=my_cur.fetchone()
#         if ro10[0]!=None:
#             messagebox.showerror("Error","The given ID already exists!",parent=self.root)
# #        if self.combo_hosyes.get()=='N':
#         else:
        my_cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.entry_ref.get(),
                    self.entry_fname.get(),
                    self.entry_mname.get(),
                    self.entry_lname.get(),
                    self.entry_dob.get(),
                    self.combo_gender.get(),
                    self.entry_email.get(),
                    self.entry_phone.get(),
                    self.entry_add.get(),
                    self.entry_tenth.get(),
                    self.entry_twelfth.get(),
                    self.entry_qual_rank.get(),
                    self.combo_qe.get(),
                    self.entry_fee.get(),
                    self.entry_jyear.get(),
                    self.combo_did.get(),
                    self.combo_hosyes.get(),
                    self.entry_unit.get(),
                    self.entry_room.get()
                ))
        my_cur.execute("insert into guardian values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.entry_gname.get(),
                                                                                            self.entry_grel.get(),
                                                                                            self.entry_gem.get(),
                                                                                            self.entry_gdes.get(),
                                                                                            self.entry_gp.get(),
                                                                                            self.entry_gadd.get(),
                                                                                            self.entry_gage.get(),
                                                                                            self.entry_ref.get(),
                                                                                            self.combo_galu.get(),
                                                                                            self.combo_ggen.get(),
                                                                                            ))
            #q2="(select allocatef(%s))"
        val2=self.entry_ref.get()
        print(val2)
        my_cur.callproc('allocatef', (val2,))
        result = my_cur.fetchone()
        conn.commit()
        print("Commited")
        self.fetch_data()
        print("Fetched")
        conn.close()
        print("Closed")
        messagebox.showinfo("Success","Student has been added successfully!",parent=self.root)
      

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        my_cur.execute("select id,fname,mname,lname,dob,student.gender,email,phone,address,tenth,twelth,qemarks,qeexam,fee,join_year,did,hos,unit_no,room_no,gname,rel,gemail,designation,gphone,gaddr,age,alum,guardian.gender from student,guardian where id=gsrn")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.details.delete(*self.details.get_children())
            for i in rows:
                self.details.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.details.focus()
        content=self.details.item(cursor_row)
        row=content["values"]
        
        self.srnv.set(row[0])
        self.fnamev.set(row[1]),
        self.mnamev.set(row[2]),
        self.lnamev.set(row[3]),
        self.dobv.set(row[4]),
        self.svar_genderv.set(row[5]),
        self.emailv.set(row[6]),
        self.phv.set(row[7]),
        self.addv.set(row[8]),
        self.tenv.set(row[9]),
        self.twev.set(row[10]),
        self.qrv.set(row[11]),
        self.qevv.set(row[12]),
        self.feev.set(row[13]),
        self.jyearv.set(row[14]),
        self.didv.set(row[15]),
        self.hstv.set(row[16]),
        self.unitv.set(row[17]),
        self.roomv.set(row[18]),    

        self.gnamev.set(row[19]),
        self.gelv.set(row[20]),
        self.gmailv.set(row[21]),
        self.gdescv.set(row[22]),
        self.gphv.set(row[23]),
        self.gaddv.set(row[24]),
        self.gagev.set(row[25]),
        self.alumv.set(row[26])
        self.gvar_genderv.set(row[27]),

    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()

        my_cur.execute("update student set fname=%s,mname=%s,lname=%s,dob=%s,gender=%s,email=%s,phone=%s,address=%s,tenth=%s,twelth=%s,qemarks=%s,qeexam=%s,fee=%s,join_year=%s,did=%s,hos=%s,unit_no=%s,room_no=%s where id=%s",(
                self.fnamev.get(),
                self.mnamev.get(),
                self.lnamev.get(),
                self.dobv.get(),
                self.svar_genderv.get(),
                self.emailv.get(),
                self.phv.get(),
                self.addv.get(),
                self.tenv.get(),
                self.twev.get(),
                self.qrv.get(),     
                self.qevv.get(),
                self.feev.get(),
                self.jyearv.get(),
                self.didv.get(),
                self.hstv.get(),
                self.unitv.get(),
                self.roomv.get(),
                self.srnv.get()
                ))    
        my_cur.execute("update guardian set gname=%s,rel=%s,gemail=%s,designation=%s,gphone=%s,gaddr=%s,age=%s,alum=%s,gender=%s where gsrn=%s",(
                                                                                         self.gnamev.get(),
                                                                                         self.gelv.get(),
                                                                                         self.gmailv.get(),
                                                                                         self.gdescv.get(),
                                                                                         self.gphv.get(),
                                                                                         self.gaddv.get(),
                                                                                         self.gagev.get(),
                                                                                         self.alumv.get(),
                                                                                         self.gvar_genderv.get(),
                                                                                         self.srnv.get()
        ))
        
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Updated successfully!",parent=self.root)

    def sdelete(self):
        sdel=messagebox.askyesno("Student","Do you want to delete this entry",parent=self.root)
        if sdel>0:
            print("here")
            conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
            my_cur=conn.cursor()
            query="delete from student where id=%s"
            print("here")
            print(self.srnv.get)
            value=(self.srnv.get(),)
            my_cur.execute(query,value)
            q2="delete from register_w where email=%s"
            my_cur.execute(q2,(self.entry_email.get(),))
            print("here")
            messagebox.showinfo("Success","Entry deleted successfully",parent=self.root)
        else:
            return
        conn.commit()
        self.fetch_data()
        self.reset1()
        conn.close()
    
    def reset1(self):
        print("hereeee")
        self.srnv.set("")
        self.fnamev.set(""),
        self.mnamev.set(""),
        self.lnamev.set(""),
        self.dobv.set(""),
        self.svar_genderv.set(""),
        self.emailv.set(""),
        self.phv.set(""),
        self.addv.set(""),
        self.tenv.set(""),
        self.twev.set(""),
        self.qrv.set(""),
        self.qevv.set(""),
        self.feev.set(""),
        self.jyearv.set(""),
        self.didv.set(""),
        self.hstv.set(""),
        self.unitv.set(""),
        self.roomv.set(""),    
        self.gnamev.set(""),
        self.gelv.set(""),
        self.gagev.set(""),
        self.gphv.set(""),
        self.gmailv.set(""),
        self.gaddv.set(""),
        self.gdescv.set(""),
        self.gvar_genderv.set(""),
        self.alumv.set("")
    
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        # if self.search_var.get()=='Mobile':
        #     my_cur.execute("select * from student where phone=%s",(self.txt_search.get(),))
        # else:
        #     my_cur.execute("select * from student where id=%s",(self.txt_search.get(),))
        my_cur.execute("select id,fname,mname,lname,dob,student.gender,email,phone,address,tenth,twelth,qeexam,qemarks,fee,join_year,did,hos,unit_no,room_no,gname,rel,gemail,designation,gphone,gaddr,age,alum,guardian.gender FROM student,guardian WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%' and id=gsrn")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.details.delete(*self.details.get_children())
            for i in rows:
                self.details.insert("",END,values=i)
            conn.commit()
        conn.close()



if __name__=='__main__':
    root=Tk()
    obj1=cstudent(root)
    root.mainloop()




