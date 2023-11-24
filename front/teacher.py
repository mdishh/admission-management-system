from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector

class cteacher:
    def __init__(self,root):
        self.root=root
        self.root.title("Teacher details")
        self.root.geometry("1550x800+0+0")

        lframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Teacher details",padx=2,font=("times new roman",12,"bold"))
        lframe.place(x=5,y=2,width=650,height=900)



        #variables
        self.tid=StringVar()
        self.tname=StringVar()
        self.temail=StringVar()
        self.tdept=StringVar()
        self.tphone=StringVar()

        teach_id_label=Label(lframe,text="Teacher ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        teach_id_label.grid(row=0,column=0,sticky=W)
        self.entry_teach=ttk.Entry(lframe,textvariable=self.tid,width=20,font=("times new roman",12,"bold"))
        self.entry_teach.grid(row=0,column=1)
        
        #fname
        name_label=Label(lframe,text="Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        name_label.grid(row=1,column=0,sticky=W)
        self.entry_name=ttk.Entry(lframe,textvariable=self.tname,width=20,font=("times new roman",12,"bold"))
        self.entry_name.grid(row=1,column=1)
        #email
        tem_label=Label(lframe,text="email ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        tem_label.grid(row=2,column=0,sticky=W)
        self.entry_tem=ttk.Entry(lframe,textvariable=self.temail,width=20,font=("times new roman",12,"bold"))
        self.entry_tem.grid(row=2,column=1)
        #dept
        dep_label=Label(lframe,text="Department ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        dep_label.grid(row=3,column=0,sticky=W)
        self.combo_did=ttk.Combobox(lframe,textvariable=self.tdept,font=("times new roman",12,"bold"),width=18,state="readonly")
        self.combo_did["value"]=("CSE","AI&ML","ME","ECE")
        self.combo_did.current(1)
        self.combo_did.grid(row=3,column=1)
        #phone
        pho_label=Label(lframe,text="Mobile",font=("times new roman",12,"bold"),padx=2,pady=6)
        pho_label.grid(row=4,column=0,sticky=W)
        self.entry_pho=ttk.Entry(lframe,textvariable=self.tphone,width=20,font=("times new roman",12,"bold"))
        self.entry_pho.grid(row=4,column=1)

        self.teach=self.entry_teach.get()
        self.name=self.entry_name.get()
        self.tem=self.entry_tem.get()
        self.dep=self.combo_did.get()
        self.pho=self.entry_pho.get()

        btn_frame=Frame(lframe,bd=2,relief=RIDGE)
        btn_frame.place(x=350,y=300,width=250,height=350)
        add_btn=Button(btn_frame,text="Add",command=self.add_tdata,font=("arial",12,"bold"),bg="black",fg="white",width=10)
        add_btn.grid(row=3,column=0,padx=5,pady=20)

        upd_btn=Button(btn_frame,text="Update",command=self.updatet,font=("arial",12,"bold"),bg="black",fg="white",width=10)
        upd_btn.grid(row=4,column=0,padx=5,pady=20)

        del_btn=Button(btn_frame,text="Delete",command=self.tdelete,font=("arial",12,"bold"),bg="black",fg="white",width=10)
        del_btn.grid(row=5,column=0,padx=5,pady=20)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset2,font=("arial",12,"bold"),bg="black",fg="white",width=10)
        reset_btn.grid(row=6,column=0,padx=5,pady=20)

        ##search system

        tabelfr=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and search system",font=("arial",12,"bold"))
        tabelfr.place(x=660,y=2,width=660,height=900)

        labelsearch=Label(tabelfr,font=("arial",12,"bold"),text="Search by:",bg="black",fg="white")
        labelsearch.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(tabelfr,font=("times new roman",12,"bold"),textvariable=self.search_var,width=18,state="readonly")
        combo_search["value"]=("Mobile","Teacher ID")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=5)

        self.text_search=StringVar()
        txtse=ttk.Entry(tabelfr,textvariable=self.text_search,font=("arial",12,"bold"),width=24)
        txtse.grid(row=0,column=2,padx=10)

        btnsearch=Button(tabelfr,font=("arial",12,"bold"),text="Search",bg="black",fg="white",width=5,command=self.search)
        btnsearch.grid(row=0,column=3,sticky=W,padx=5)

        
        btnshowall=Button(tabelfr,font=("arial",12,"bold"),text="Show all",bg="black",fg="white",width=7,command=self.fetch_datat)
        btnshowall.grid(row=0,column=4,sticky=W)

        #===========show data
        detable=Frame(tabelfr,bd=2,relief=RIDGE)
        detable.place(x=0,y=50,width=650,height=350)    

        scroll_x=ttk.Scrollbar(detable,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detable,orient=VERTICAL)

       

        self.detailst=ttk.Treeview(detable,column=("Teacher ID","Name","email ID","phone number","Department ID"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)    
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.detailst.xview)
        scroll_y.config(command=self.detailst.yview)


        self.detailst.heading("Teacher ID",text="Teacher ID")
        self.detailst.heading("Name",text="Name")
        self.detailst.heading("email ID",text="email ID")
        self.detailst.heading("phone number",text="Phone number")
        self.detailst.heading("Department ID",text="Department ID")

        self.detailst["show"]="headings"
        self.detailst.pack(fill=BOTH,expand=1)
        self.detailst.bind("<ButtonRelease-1>",self.get_cursort)
        self.fetch_datat()


    def add_tdata(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        my_cur.execute("select mid from mentor where mid=%s",(self.entry_teach.get(),))
        row2=my_cur.fetchone()
        if row2!=None:
            messagebox.showerror("Error","Teacher ID already exists",parent=self.root)
        else:
            my_cur.execute("insert into mentor values(%s,%s,%s,%s,%s)",(self.entry_teach.get(),self.entry_name.get(),self.entry_tem.get(),self.entry_pho.get(),self.combo_did.get()))
            conn.commit()
            print("Commited")
            conn.close()
            print("Closed")
            messagebox.showinfo("Success","Data has been added successfully!",parent=self.root)
        self.fetch_datat()
        print("Fetched")
        

    def tdelete(self):
        sdel=messagebox.askyesno("Student","Do you want to delete this entry",parent=self.root)
        if sdel>0:
            print("here")
            conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
            my_cur=conn.cursor()
            q1="select ssid from fam where mmid=%s"
            value=(self.entry_teach.get(),)
            my_cur.execute(q1,value)
            rows=my_cur.fetchall()
            em=self.entry_tem.get()
            q2="delete from register_w where email=%s"
            my_cur.execute(q2,(em,))
            query="delete from mentor where mid=%s"
            my_cur.execute(query,value)
            messagebox.showinfo("Success","Entry deleted successfully",parent=self.root)
            for row in rows:
                print(row[0])
                my_cur.callproc('allocatef',(row[0],))
            print("here")
        else:
            return
        conn.commit()
        self.fetch_datat()
        self.reset2()
        conn.close()

    def fetch_datat(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        my_cur.execute("select * from mentor")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.detailst.delete(*self.detailst.get_children())
            for i in rows:
                self.detailst.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursort(self,event=""):
        cursor_row=self.detailst.focus()
        content=self.detailst.item(cursor_row)
        row=content["values"]
        self.tid.set(row[0]),
        self.tname.set(row[1]),
        self.temail.set(row[2]),
        self.tphone.set(row[3]),
        self.tdept.set(row[4])

    def reset2(self,event=""):
        self.tid.set(""),
        self.tname.set(""),
        self.temail.set(""),
        self.tphone.set(""),
        self.tdept.set("")

    def updatet(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        my_cur.execute("update mentor set mname=%s,memail=%s,phone=%s,mdid=%s where mid=%s",(self.tname.get(),self.temail.get(),self.tphone.get(),self.tdept.get(),self.tid.get()))
        conn.commit()
        self.fetch_datat()
        conn.close()
        messagebox.showinfo("Success","Updated successfully!",parent=self.root)

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        if self.search_var.get()=='Mobile':
            my_cur.execute("select * from mentor where phone LIKE '%"+str(self.text_search.get())+"%'")
        else:
            my_cur.execute("select * from mentor where mid LIKE '%"+str(self.text_search.get())+"%'")
        #my_cur.execute("SELECT * FROM mentor WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.detailst.delete(*self.detailst.get_children())
            for i in rows:
                self.detailst.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__=='__main__':
    root=Tk()
    obj1=cteacher(root)
    root.mainloop()
