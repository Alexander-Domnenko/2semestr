import tkinter as tk
#def running():
    #global run
    #run=True
win = tk.Tk()
win.geometry(f"900x700+100+200")
win.title('')

Label_1=tk.Label(win,text='Вы проиграли',
                 fg='red',
                 font=('Arial',18),
                 pady=200,
                 )
#btn1=tk.Button(win,text='Продолжить игру',
              # command=running,
               #font=('Arial',16))
#btn2=tk.Button(win,text='Завершить игру',
               #command=running,
               #font=('Arial',16))
            

Label_1.pack()
btn1.pack()
btn2.pack()
win.mainloop()
