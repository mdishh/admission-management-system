from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
class ssg:
    def __init__(self,root):
        self.root=root
        self.root.title("Student marks")
        self.root.geometry("1550x800+0+0")

        lframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="SGPA details",padx=2,font=("times new roman",12,"bold"))
        lframe.place(x=5,y=2,width=500,height=900)


        self.srn=StringVar()
        self.sgpa1=StringVar()
        self.sgpa2=StringVar()
        self.sgpa3=StringVar()
        self.sgpa4=StringVar()
        self.sgpa5=StringVar()
        self.sgpa6=StringVar()
        self.sgpa7=StringVar()
        self.sgpa8=StringVar()

        srn_label=Label(lframe,text="ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        srn_label.grid(row=0,column=0,sticky=W)
        self.entry_srn=ttk.Entry(lframe,textvariable=self.srn,width=20,font=("times new roman",12,"bold"))
        self.entry_srn.grid(row=0,column=1)

        sgpa1_label=Label(lframe,text="SGPA1",font=("times new roman",12,"bold"),padx=2,pady=6)
        sgpa1_label.grid(row=1,column=0,sticky=W)
        self.entry_sgpa1=ttk.Combobox(lframe,textvariable=self.sgpa1,width=20,font=("times new roman",12,"bold"))
        self.entry_sgpa1["value"]=("None")
        self.entry_sgpa1.current(0)
        self.entry_sgpa1.grid(row=1,column=1)

        sgpa2_label=Label(lframe,text="SGPA2",font=("times new roman",12,"bold"),padx=2,pady=6)
        sgpa2_label.grid(row=2,column=0,sticky=W)
        self.entry_sgpa2=ttk.Combobox(lframe,textvariable=self.sgpa2,width=20,font=("times new roman",12,"bold"))
        self.entry_sgpa2["value"]=("None")
        self.entry_sgpa2.current(0)
        self.entry_sgpa2.grid(row=2,column=1)

        sgpa3_label=Label(lframe,text="SGPA3",font=("times new roman",12,"bold"),padx=2,pady=6)
        sgpa3_label.grid(row=3,column=0,sticky=W)
        self.entry_sgpa3=ttk.Combobox(lframe,textvariable=self.sgpa3,width=20,font=("times new roman",12,"bold"))
        self.entry_sgpa3["value"]=("None")
        self.entry_sgpa3.current(0)
        self.entry_sgpa3.grid(row=3,column=1)

        sgpa4_label=Label(lframe,text="SGPA4",font=("times new roman",12,"bold"),padx=2,pady=6)
        sgpa4_label.grid(row=4,column=0,sticky=W)
        self.entry_sgpa4=ttk.Combobox(lframe,textvariable=self.sgpa4,width=20,font=("times new roman",12,"bold"))
        self.entry_sgpa4["value"]=("None")
        self.entry_sgpa4.current(0)
        self.entry_sgpa4.grid(row=4,column=1)

        sgpa5_label=Label(lframe,text="SGPA5",font=("times new roman",12,"bold"),padx=2,pady=6)
        sgpa5_label.grid(row=5,column=0,sticky=W)
        self.entry_sgpa5=ttk.Combobox(lframe,textvariable=self.sgpa5,width=20,font=("times new roman",12,"bold"))
        self.entry_sgpa5["value"]=("None")
        self.entry_sgpa5.current(0)
        self.entry_sgpa5.grid(row=5,column=1)

        sgpa6_label=Label(lframe,text="SGPA6",font=("times new roman",12,"bold"),padx=2,pady=6)
        sgpa6_label.grid(row=6,column=0,sticky=W)
        self.entry_sgpa6=ttk.Combobox(lframe,textvariable=self.sgpa6,width=20,font=("times new roman",12,"bold"))
        self.entry_sgpa6["value"]=("None")
        self.entry_sgpa6.current(0)
        self.entry_sgpa6.grid(row=6,column=1)

        sgpa7_label=Label(lframe,text="SGPA7",font=("times new roman",12,"bold"),padx=2,pady=6)
        sgpa7_label.grid(row=7,column=0,sticky=W)
        self.entry_sgpa7=ttk.Combobox(lframe,textvariable=self.sgpa7,width=20,font=("times new roman",12,"bold"))
        self.entry_sgpa7["value"]=("None")
        self.entry_sgpa7.current(0)
        self.entry_sgpa7.grid(row=7,column=1)

        sgpa8_label=Label(lframe,text="SGPA8",font=("times new roman",12,"bold"),padx=2,pady=6)
        sgpa8_label.grid(row=8,column=0,sticky=W)
        self.entry_sgpa8=ttk.Combobox(lframe,textvariable=self.sgpa8,width=20,font=("times new roman",12,"bold"))
        self.entry_sgpa8["value"]=("None")
        self.entry_sgpa8.current(0)
        self.entry_sgpa8.grid(row=8,column=1)

        add_btn=Button(lframe,text="Add",command=self.add_datas,font=("arial",12,"bold"),bg="black",fg="white",width=10)
        add_btn.grid(row=13,column=3,padx=5,pady=20)

        add_btn=Button(lframe,text="Update",command=self.update_data,font=("arial",12,"bold"),bg="black",fg="white",width=10)
        add_btn.grid(row=15,column=3,padx=5,pady=20)

        tabelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Student Details",font=("arial",16,"bold"))
        tabelframe.place(x=520,y=2,width=800,height=900)

        detablesm=Frame(tabelframe,bd=2,relief=RIDGE)
        detablesm.place(x=0,y=100,width=750,height=350)    

        scroll_xm=ttk.Scrollbar(detablesm,orient=HORIZONTAL)
        scroll_ym=ttk.Scrollbar(detablesm,orient=VERTICAL)

        self.detailsm=ttk.Treeview(detablesm,column=("ID","sgpa1","sgpa2","sgpa3","sgpa4","sgpa5","sgpa6","sgpa7","sgpa8","cgpa","Scholarship"),xscrollcommand=scroll_xm.set,yscrollcommand=scroll_ym.set)    
        
        scroll_xm.pack(side=BOTTOM,fill=X)
        scroll_ym.pack(side=RIGHT,fill=Y)

        scroll_xm.config(command=self.detailsm.xview)
        scroll_ym.config(command=self.detailsm.yview)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(tabelframe,textvariable=self.search_var,font=("times new roman",12,"bold"),width=18,state="readonly")
        combo_search["value"]=("ID")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=5)

        self.txt_search=StringVar()
        txtse=ttk.Entry(tabelframe,textvariable=self.txt_search,font=("arial",12,"bold"),width=24)
        txtse.grid(row=0,column=2,padx=10)

        ################table buttons##############
        btnsearch=Button(tabelframe,font=("arial",12,"bold"),command=self.search,text="Search",bg="black",fg="white",width=5)
        btnsearch.grid(row=0,column=3,sticky=W,padx=5)

        btnshowall=Button(tabelframe,font=("arial",12,"bold"),command=self.fetch_datas,text="Show all",bg="black",fg="white",width=7)
        btnshowall.grid(row=0,column=4,sticky=W,padx=3)

        btnMRD=Button(tabelframe,font=("arial",12,"bold"),command=self.fetch_datamrd,text="MRD",bg="black",fg="white",width=7)
        btnMRD.grid(row=0,column=5,sticky=W,padx=3)

        btnCNR=Button(tabelframe,font=("arial",12,"bold"),command=self.fetch_datacnr,text="CNR",bg="black",fg="white",width=7)
        btnCNR.grid(row=0,column=6,sticky=W,padx=3)

        # number_label=Label(tabelframe,text="Number of entries",font=("times new roman",12,"bold"))
        # number_label.grid(row=5,column=1,sticky=W)
        # self.num=ttk.Entry(tabelframe,width=5,font=("times new roman",12,"bold"),state='disabled')
        # self.num.grid(row=5,column=2)


        self.detailsm.heading("SRN",text="SRN")
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
        self.detailsm.bind("<ButtonRelease-1>",self.get_cursors)
        self.fetch_datas()
    def get_cursors(self,event=""):
        cursor_row=self.detailsm.focus()
        content=self.detailsm.item(cursor_row)
        row=content["values"]
        
        self.srn.set(row[0])
        self.sgpa1.set(row[1]),
        self.sgpa2.set(row[2]),
        self.sgpa3.set(row[3]),
        self.sgpa4.set(row[4]),
        self.sgpa5.set(row[5]),
        self.sgpa6.set(row[6]),
        self.sgpa7.set(row[7]),
        self.sgpa8.set(row[8])

    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        #if self.entry_sgpa1.get()=='NULL':
        #    my_cur.execute("update sgpa set sid =%s",(self.entry_srn.get(),))
        if self.entry_sgpa2.get()=='None':
            my_cur.execute("update sgpa set sgpa1=%s where sid=%s)",(self.entry_sgpa1.get(),
                                        self.entry_srn.get(),                     
                                        ))
        elif self.entry_sgpa3.get()=='None':
            my_cur.execute("update sgpa set sgpa1=%s,sgpa2=%s where sid=%s",(
                                        self.entry_sgpa1.get(),
                                            self.entry_sgpa2.get(), self.entry_srn.get()                                                      
                                        ))
        elif self.entry_sgpa4.get()=='None':
            my_cur.execute("update sgpa set sgpa1=%s,sgpa2=%s,sgpa3=%s where sid=%s",(
                                        self.entry_sgpa1.get(),
                                            self.entry_sgpa2.get(),                              
                                            self.entry_sgpa3.get(),self.entry_srn.get()                                                     
                                        ))
        elif self.entry_sgpa5.get()=='None':
            my_cur.execute("update sgpa set sgpa1=%s,sgpa2=%s,sgpa3=%s,sgpa4=%s where sid=%s",(
                                        self.entry_sgpa1.get(),
                                            self.entry_sgpa2.get(),                              
                                            self.entry_sgpa3.get(),                              
                                            self.entry_sgpa4.get(),self.entry_srn.get()                                                         
                                        ))
        elif self.entry_sgpa6.get()=='None':
            my_cur.execute("update sgpa set sgpa1=%s,sgpa2=%s,sgpa3=%s,sgpa4=%s,sgpa5=%s where sid=%s",(
                                        self.entry_sgpa1.get(),
                                            self.entry_sgpa2.get(),                              
                                            self.entry_sgpa3.get(),                              
                                            self.entry_sgpa4.get(),                              
                                            self.entry_sgpa5.get(),                              
                                            self.entry_srn.get()               
                                        ))
        elif self.entry_sgpa7.get()=='None':
            my_cur.execute("update sgpa set sgpa1=%s,sgpa2=%s,sgpa3=%s,sgpa4=%s,sgpa5=%s,sgpa6=%s where sid=%s",(
                                        self.entry_sgpa1.get(),
                                            self.entry_sgpa2.get(),                              
                                            self.entry_sgpa3.get(),                              
                                            self.entry_sgpa4.get(),                              
                                            self.entry_sgpa5.get(),                              
                                            self.entry_sgpa6.get(),  self.entry_srn.get()                            
                                        ))
        elif self.entry_sgpa8.get()=='None':
            my_cur.execute("update sgpa set sgpa1=%s,sgpa2=%s,sgpa3=%s,sgpa4=%s,sgpa5=%s,sgpa6=%s,sgpa7=%s where sid=%s",(self.entry_sgpa1.get(),
                                            self.entry_sgpa2.get(),                              
                                            self.entry_sgpa3.get(),                              
                                            self.entry_sgpa4.get(),                              
                                            self.entry_sgpa5.get(),                              
                                            self.entry_sgpa6.get(),                              
                                            self.entry_sgpa7.get(),       
                                            self.entry_srn.get()                                         
                                        ))
        else:
            my_cur.execute("update sgpa set sgpa1=%s,sgpa2=%s,sgpa3=%s,sgpa4=%s,sgpa5=%s,sgpa6=%s,sgpa7=%s,sgpa8=%s where sid=%s",(
                                            self.entry_sgpa1.get(),
                                            self.entry_sgpa2.get(),                              
                                            self.entry_sgpa3.get(),                              
                                            self.entry_sgpa4.get(),                              
                                            self.entry_sgpa5.get(),                              
                                            self.entry_sgpa6.get(),                              
                                            self.entry_sgpa7.get(),                              
                                            self.entry_sgpa8.get(),
                                            self.entry_srn.get()                         
                                        ))
        messagebox.showinfo("Success","Data updated successfully")
        conn.commit()
        self.fetch_datas()
    def add_datas(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor(buffered=True)
        #        if self.combo_hosyes.get()=='N':
        x=self.entry_srn.get()
        q1=("select * from student where id=%s")
        q2=("select * from sgpa where sid=%s")
        my_cur.execute(q1,(x,))
        row=my_cur.fetchone()
        print(row)
        if row!=None:
            my_cur.execute(q2,(x,))
            ro1=my_cur.fetchone()
            if ro1==None:
                if self.entry_sgpa1.get()=='None':
                    my_cur.execute("insert into sgpa(sid) values(%s)",(self.entry_srn.get(),))
                elif self.entry_sgpa2.get()=='':
                    my_cur.execute("insert into sgpa(sid,sgpa1) values(%s,%s)",(self.entry_srn.get(),
                                        self.entry_sgpa1.get(),                     
                                        ))
                elif self.entry_sgpa3.get()=='None':
                    my_cur.execute("insert into sgpa(sid,sgpa1,sgpa2) values(%s,%s,%s)",(self.entry_srn.get(),
                                        self.entry_sgpa1.get(),
                                            self.entry_sgpa2.get(),                                                       
                                        ))
                elif self.entry_sgpa4.get()=='None':
                    my_cur.execute("insert into sgpa(sid,sgpa1,sgpa2,sgpa3) values(%s,%s,%s,%s)",(self.entry_srn.get(),
                                        self.entry_sgpa1.get(),
                                            self.entry_sgpa2.get(),                              
                                            self.entry_sgpa3.get(),                                                           
                                        ))
                elif self.entry_sgpa5.get()=='None':
                    my_cur.execute("insert into sgpa(sid,sgpa1,sgpa2,sgpa3,sgpa4) values(%s,%s,%s,%s,%s)",(self.entry_srn.get(),
                                        self.entry_sgpa1.get(),
                                            self.entry_sgpa2.get(),                              
                                            self.entry_sgpa3.get(),                              
                                            self.entry_sgpa4.get(),                                                         
                                        ))
                elif self.entry_sgpa6.get()=='None':
                    my_cur.execute("insert into sgpa(sid,sgpa1,sgpa2,sgpa3,sgpa4,sgpa5) values(%s,%s,%s,%s,%s,%s)",(self.entry_srn.get(),
                                        self.entry_sgpa1.get(),
                                            self.entry_sgpa2.get(),                              
                                            self.entry_sgpa3.get(),                              
                                            self.entry_sgpa4.get(),                              
                                            self.entry_sgpa5.get(),                              
                                                                        
                                        ))
                elif self.entry_sgpa7.get()=='None':
                    my_cur.execute("insert into sgpa(sid,sgpa1,sgpa2,sgpa3,sgpa4,sgpa5,sgpa6) values(%s,%s,%s,%s,%s,%s,%s)",(self.entry_srn.get(),
                                        self.entry_sgpa1.get(),
                                            self.entry_sgpa2.get(),                              
                                            self.entry_sgpa3.get(),                              
                                            self.entry_sgpa4.get(),                              
                                            self.entry_sgpa5.get(),                              
                                            self.entry_sgpa6.get(),                              
                                        ))
                elif self.entry_sgpa8.get()=='None':
                    my_cur.execute("insert into sgpa(sid,sgpa1,sgpa2,sgpa3,sgpa4,sgpa5,sgpa6,sgpa7) values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.entry_srn.get(),
                                        self.entry_sgpa1.get(),
                                            self.entry_sgpa2.get(),                              
                                            self.entry_sgpa3.get(),                              
                                            self.entry_sgpa4.get(),                              
                                            self.entry_sgpa5.get(),                              
                                            self.entry_sgpa6.get(),                              
                                            self.entry_sgpa7.get(),                                                       
                                        ))
                else:
                    my_cur.execute("insert into sgpa(sid,sgpa1,sgpa2,sgpa3,sgpa4,sgpa5,sgpa6,sgpa7,sgpa8) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.entry_srn.get(),
                                        self.entry_sgpa1.get(),
                                            self.entry_sgpa2.get(),                              
                                            self.entry_sgpa3.get(),                              
                                            self.entry_sgpa4.get(),                              
                                            self.entry_sgpa5.get(),                              
                                            self.entry_sgpa6.get(),                              
                                            self.entry_sgpa7.get(),                              
                                            self.entry_sgpa8.get(),                              
                                        ))
                messagebox.showinfo('Success','Data has been added successfully!!',parent=self.root)
            else:
                messagebox.showerror("Error","Data already exists")

            
            conn.commit()
            conn.close()
            print("here")
           
            self.fetch_datas()
        else:
            messagebox.showerror('Error!','Student does not exist',parent=self.root)
        

    def fetch_datas(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        my_cur.execute("select * from sgpa")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.detailsm.delete(*self.detailsm.get_children())
            for i in rows:
                self.detailsm.insert("",END,values=i)
            conn.commit()
        conn.close()
        

    def fetch_datamrd(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()
        my_cur.execute("select * from sgpa where scholarship='MRD'")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.detailsm.delete(*self.detailsm.get_children())
            for i in rows:
                self.detailsm.insert("",END,values=i)
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
        my_cur.execute("select * from sgpa where scholarship='CNR'")
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.detailsm.delete(*self.detailsm.get_children())
            for i in rows:
                self.detailsm.insert("",END,values=i)
            conn.commit()
        my_cur.execute("select count(*) from sgpa group by scholarship having scholarship='CNR'")
        row=my_cur.fetchone()
        if row!=None:
            messagebox.showinfo("Details","Number of students awarded with CNR Scholarship is "+str(row[0]),parent=self.root)
        else:
            messagebox.showinfo("Details","Number of students awarded with CNR Scholarship is 0",parent=self.root)
        conn.close()

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="***",database="***")
        my_cur=conn.cursor()

        my_cur.execute("select * from sgpa where sid LIKE '%"+str(self.txt_search.get())+"%'")

        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.detailsm.delete(*self.detailsm.get_children())
            for i in rows:
                self.detailsm.insert("",END,values=i)
            conn.commit()
        conn.close()
        
if __name__=='__main__':
    root=Tk()
    obj1=ssg(root)
    root.mainloop()
