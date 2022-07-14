import tkinter as tk
root=tk.Tk()
root.title('My window')
root.geometry('600x400')
label=tk.Label(root,text='Hello world',font=('Arial',50))
label.place(x=100,y=100)

root.mainloop()
