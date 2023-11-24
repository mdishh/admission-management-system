from tkinter import*
from PIL import Image,ImageTk

class cabout:
    def __init__(self,root):
        self.root=root
        self.root.title("About us")
        self.root.geometry("1135x550+230+220")
        frame = Frame(self.root, padx=10, pady=10)
        frame.pack()

        img1=Image.open(r"images\x.png")
        img1=img1.resize((1000,500),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lab=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lab.place(x=0,y=0,width=1135,height=200)

        text1 = "\n\n\n\n\n*** located in ***, India is one of the country’s leading teaching and research universities. The University is committed to providing “navigation for the real world” that inspires students to find their true north.Our students graduate with the ability to adapt to an intellectually and technologically changing environment. Over the years, we have accomplished this with the participative efforts of the management, staff, students and parents.*** is ranked *** in the *** and is the only University in *** to rank in the ***.\n\n\n\n\n\nThe Rankings evaluate institutions based on parameters such as ***,***,*** and ***."
        text_label1 = Label(frame, text=text1, justify='left', font=(30),wraplength=1000,pady=200)
        text_label1.pack()

        


if __name__=='__main__':
    root=Tk()
    obj2=cabout(root)
    root.mainloop()
