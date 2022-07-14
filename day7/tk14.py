import tkinter as tk
def btn_click():
    a = 0
    b = 0
    a=int(entry.get())
    b=int(entry2.get())
    p=a/b
    pay=int(p // 100*100)
    if p > pay:
        pay+=100
    pay2=a-pay*(b-1)

    label3['text'] = '一人あたり{}円({}人)、幹事は{}円です'.format(pay,b-1,pay2)


root=tk.Tk()
root.title('割り勘計算')
root.resizable(False,False)
#root.geometry('600x400')
canvas = tk.Canvas(root,width=400,height=800,bg='skyblue')
canvas.pack()

label=tk.Label(root,text='金額',font=('Arial',16),bg='skyblue')
label.place(x=10,y=10)

entry=tk.Entry(width=30)
entry.place(x=10,y=40)

label2=tk.Label(root,text='人数',font=('Arial',16),bg='skyblue')
label2.place(x=10,y=100)

entry2=tk.Entry(width=30)
entry2.place(x=10,y=130)

btn=tk.Button(text='計算する',command=btn_click)
btn.place(x=10,y=190)

label3 = tk.Label(root,text='',font=('Arial',10),bg='skyblue')
label3.place(x=10,y=240)


#entry=tk.Entry(width=20)
#entry.place(x=10,y=10)
#btn=tk.Button(text='文字列の取得',command=btn_click)
#btn.place(x=20,y=100)



root.mainloop()
