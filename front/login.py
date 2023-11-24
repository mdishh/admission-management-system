from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from admin import cadmin
from studentpage import studpage
from mentorpage import mentpage
from accounts import accpage



class clogin:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        img2=Image.open("images\y.png")
        img2=img2.resize((1500,900),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(img2)
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=170,width=340,height=450)

        #variables
        self.roll=StringVar()
        

        img1=Image.open("images\somelogo.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbling1=Label(self.root,image=self.photoimage1,bg="white",borderwidth=0)
        lbling1.place(x=615,y=175,width=100,height=100)

        #login_str=Label(frame,text="Login",font=("times new roman",18,"bold"),fg="black",bg="white")
        #login_str.place(x=135,y=100)

        usrn=Label(frame,text="Username",font=("times new roman",12,"bold"),fg="black",bg="white")
        usrn.place(x=70,y=130)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=160,width=270)

        password=Label(frame,text="Password",font=("times new roman",12,"bold"),fg="black",bg="white")
        password.place(x=70,y=210)

        self.passw=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.passw.place(x=40,y=240,width=270)

        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black")
        loginbtn.place(x=110,y=350,width=160,height=35)

        # self.rollw=ttk.Entry(frame,font=("times new roman",15,"bold"))
        # self.rollw.place(x=20,y=300,width=160,height=35)
        rolabel=Label(frame,text="Role",font=("times new roman",12,"bold"),fg="black",bg="white")
        rolabel.place(x=20,y=270,width=160,height=35)
        self.rollw=ttk.Combobox(frame,textvariable=self.roll,font=("times new roman",12,"bold"),width=16,state="readonly")
        self.rollw["value"]=("Student","Teacher","Accounts")
        self.rollw.current(0)
        self.rollw.place(x=40,y=310,width=160,height=30)


        registerbtn=Button(frame,text="Create new account",command=self.gotoregister,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="white")
        registerbtn.place(x=20,y=400,width=200)

       


    def login(self):
        if self.txtuser=="" or self.passw=="":
            messagebox.showerror("Error all fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="***",database="***")
            #print(conn)
            my_cur=conn.cursor()
            #query=("select * from register where email=%s and password=%s")
            query=("select * from register_w where email=%s")
            given_pass=self.passw.get()
            value=(self.txtuser.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            #print("hereee")
            #print(self.rollw)
            if row!=None:
                if row[1]==given_pass:
                    if row[0]=='admin@gmail.com' and row[1]=='admin' and self.rollw.get()=='Accounts':
                        messagebox.showinfo("Success","login successful")
                        self.calladmin()
                    elif row[-1]=='Student' and self.rollw.get()=='Student':
                        messagebox.showinfo("Success","login successful")
                        self.callstudent(row[0])
                    elif row[-1]=='Teacher' and self.rollw.get()=='Teacher':
                        messagebox.showinfo("Success","login successful")
                        self.callmentor(row[0])
                    elif row[-1]=='Accounts' and self.rollw.get()=='Accounts':
                        messagebox.showinfo("Success","login successful")
                        self.callaccounts()
                    else:
                        messagebox.showerror("Error","Invalid credentials")
                else:
                    messagebox.showerror("Error","incorrect password")
                    self.root.destroy()
                conn.commit()
                conn.close()
            if row==None:
                messagebox.showerror("Error","User not found!")
            conn.commit()
            conn.close()
            
    
    def gotoregister(self):
        self.new_window=Toplevel(self.root)
        self.app=cregister(self.new_window)
        #self.root.destroy()

    def calladmin(self):
        self.new_window=Toplevel(self.root)
        self.app1=cadmin(self.new_window)
        #self.root.destroy()

    def callstudent(self,x):
        self.new_wi=Toplevel(self.root)
        self.app2=studpage(self.new_wi,x)
        #self.root.destroy()
        
    def callmentor(self,x):
        self.neww=Toplevel(self.root)
        self.app3=mentpage(self.neww,x)
        #self.root.destroy()

    def callaccounts(self):
        self.neww1=Toplevel(self.root)
        self.app4=accpage(self.neww1)
        #self.root.destroy()



class cregister:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        img2=Image.open("images\y.png")
        img2=img2.resize((1500,900),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(img2)
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=170,width=340,height=500)

        #variable
        self.rollr=StringVar()

        img1=Image.open("images\somelogo.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbling1=Label(self.root,image=self.photoimage1,bg="white",borderwidth=0)
        lbling1.place(x=615,y=175,width=100,height=100)

        #login_str=Label(frame,text="Login",font=("times new roman",18,"bold"),fg="black",bg="white")
        #login_str.place(x=135,y=100)

        usrn=Label(frame,text="email id",font=("times new roman",12,"bold"),fg="black",bg="white")
        usrn.place(x=70,y=130)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=160,width=270)

        password1=Label(frame,text="Password",font=("times new roman",12,"bold"),fg="black",bg="white")
        password1.place(x=70,y=210)

        self.passw=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.passw.place(x=40,y=240,width=270)

        passwordc=Label(frame,text="Confirm Password",font=("times new roman",12,"bold"),fg="black",bg="white")
        passwordc.place(x=70,y=270)

        self.passwc=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.passwc.place(x=40,y=300,width=270)

        rorlabel=Label(frame,text="Role",font=("times new roman",12,"bold"),fg="black",bg="white")
        rorlabel.place(x=20,y=330,width=160,height=35)
        self.rollwr=ttk.Combobox(frame,font=("times new roman",12,"bold"),width=16,state="readonly")
        self.rollwr["value"]=("Student","Teacher","Accounts")
        self.rollwr.current(0)
        self.rollwr.place(x=40,y=360,width=160,height=30)


        regbtn=Button(frame,text="Register",command=self.register,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black")
        regbtn.place(x=110,y=400,width=120,height=35)

        # registerbtn=Button(frame,text="Create new account",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="white")
        # registerbtn.place(x=20,y=400,width=200)

        # forpass=Button(frame,text="Forgot Password",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="white")
        # forpass.place(x=20,y=350,width=160)

    def register(self):
        if self.txtuser.get()=="" or self.passw.get()=="" or self.passwc.get()=="":
            messagebox.showerror("Error all fields are required")
        elif self.passw.get()!=self.passwc.get():
            messagebox.showerror("The new password and confirm password must be same")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="***",database="***")
            my_cur=conn.cursor()
            query=("select * from register_w where email=%s")
            value=(self.txtuser.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists!!!")
            else:
                my_pass=self.passwc.get()
                my_cur.execute("insert into register_w values(%s,%s,%s)",(self.txtuser.get(),
                                                                        my_pass,self.rollwr.get()
                                                                        ))
                
                messagebox.showinfo("Success","Successfully registered!!")
            conn.commit()
            conn.close()
            self.root.destroy()

 
if __name__=='__main__':
    root=Tk()
    app=clogin(root)
    root.mainloop()















