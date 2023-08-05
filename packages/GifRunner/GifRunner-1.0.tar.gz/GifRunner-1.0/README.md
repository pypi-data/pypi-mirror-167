# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://github.com/karamveer05s/GitRunner)

This is a simple example package. You can use

Example :- 

from tkinter import *
from GifRunner import gifrun

root = Tk()
root.geometry("1200x700+0+0")

img = Label()
img.place(x=20,y=10)

img2 = Label()
img2.place(x=325,y=10)

img3 = Label()
img3.place(x=20,y=320)

img4 = Label()
img4.place(x=325,y=320)

img5 = Label()
img5.place(x=825,y=10)

img6 = Label()
img6.place(x=825,y=320)


gifrun(root,img,r"C:\Users\R&D1\Downloads\iron.gif",310,300)
gifrun(root,img2,r"C:\Users\R&D1\Downloads\1f16e03daa782d9106ef36c6c6b11747.gif",310,500)
gifrun(root,img3,r"C:\Users\R&D1\Downloads\spider_man.gif",300,300)
gifrun(root,img4,r"C:\Users\R&D1\Downloads\av.gif",300,500)
gifrun(root,img5,r"C:\Users\R&D1\Downloads\harry.gif",305,520)
gifrun(root,img6,r"C:\Users\R&D1\Downloads\doraemon.gif",305,520)

root.config(bg="black")
root.mainloop()