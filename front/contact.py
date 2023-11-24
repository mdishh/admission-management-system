from tkinter import*
from PIL import Image,ImageTk

class ccontact:
    def __init__(self,root):
        self.root=root
        self.root.title("Contact")
        self.root.geometry("1135x550+230+220")

        frame = Frame(self.root, padx=10, pady=10)
        frame.pack()

        img1=Image.open("images\z.png")
        img1=img1.resize((1000,500),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lab=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lab.place(x=0,y=0,width=1135,height=200)

        text1 = "\n\n\n\n\n\n\n\n\n\n\n\n***: 00/00\n\n***:11\n\n***:88,***\n\n\n\n***: 99, 55\n\n**: 77, ***\n\n***: 33, 44, ***\n\n***: ++ / +++, ---"
        text_label1 = Label(frame, text=text1, justify='left', font=(30),wraplength=1000,pady=200)
        text_label1.pack()


if __name__=='__main__':
    root=Tk()
    obj2=ccontact(root)
    root.mainloop()
