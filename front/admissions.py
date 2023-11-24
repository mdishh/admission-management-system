from tkinter import*
from PIL import Image,ImageTk

class calumni:
    def __init__(self,root):
        self.root=root
        self.root.title("Alumni")
        self.root.geometry("1135x550+230+220")


        frame = Frame(self.root, padx=10, pady=10)
        frame.pack()

        img1=Image.open("images\z.png")
        img1=img1.resize((1000,500),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lab=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lab.place(x=0,y=0,width=1135,height=200)

        text1 = "Today, the programs at *** are sought after by students from around the country. Leading industries choose *** when they need the right talent. One of the key reasons for this is the University’s focus on admitting the best talent in India and abroad. We are proud about the tradition of ***,***,***,***, and select other National level entrance exams are considered. The consideration of an entrance exam is subject to the discretion of ***."
        text_label1 = Label(frame, text=text1, justify='left', font=(30),wraplength=1000,pady=200)
        text_label1.pack()

       
        



if __name__=='__main__':
    root=Tk()
    obj2=calumni(root)
    root.mainloop()
