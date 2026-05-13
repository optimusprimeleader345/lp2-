from tkinter import *

def check():
    if f.get() == 1 and c.get() == 1:
        ans.config(text="You may have Flu")

    elif f.get() == 1 and h.get() == 1:
        ans.config(text="You may have Fever")

    elif cp.get() == 1:
        ans.config(text="Chest problem detected")

    else:
        ans.config(text="You are healthy")

root = Tk()
root.title("Expert System")
root.geometry("300x300")

f = IntVar()
c = IntVar()
h = IntVar()
cp = IntVar()

Checkbutton(root, text="Fever", variable=f).pack()
Checkbutton(root, text="Cough", variable=c).pack()
Checkbutton(root, text="Headache", variable=h).pack()
Checkbutton(root, text="Chest Pain", variable=cp).pack()

Button(root, text="Check", command=check).pack()

ans = Label(root, text="")
ans.pack()

root.mainloop()