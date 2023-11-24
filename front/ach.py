from tkinter import*
from PIL import Image,ImageTk

class cach:
    def __init__(self,root):
        self.root=root
        self.root.title("Achievements")
        self.root.geometry("1135x550+230+220")

        frame = Frame(self.root, padx=10, pady=10)
        frame.pack()

        img1=Image.open("images\abouts.png")
        img1=img1.resize((1000,500),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lab=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lab.place(x=0,y=0,width=1135,height=200)


        text2="*** is ranked *** in the *** and is the only University in *** to rank in the ***.The Rankings evaluate institutions based on parameters such as ***, ***, ***, *** and ***. Founder's Vision:We realize that our students represent the future of our society and we take our responsibility seriously. We ensure that the rock-solid foundation we help them build here – both, in terms of skills and values – will stand them in good stead no matter which career they choose. Faculty:Our faculty is our most precious resource and one of the three pillars on which *** rests (the other two are students and infrastructure). Our faculty members develop and deliver the educational programs that bring excellent students to *** in the first place."
        text_label2 = Label(frame, text=text2, justify='left', font=(30),wraplength=1000,pady=200)
        text_label2.pack()


if __name__=='__main__':
    root=Tk()
    obj2=cach(root)
    root.mainloop()
