from tkinter import *
from tkinter import ttk

def say_hello(txt):
    print("Hello")
    txt['text'] = "hello"

def main_01():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    txt = ttk.Label(frm, text="Hello World!")
    txt.grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

    ttk.Button(frm, text="SayHello", command=lambda:say_hello(txt)).grid(column=0, row=1)

    root.mainloop()
def main():

    ws = Tk()
    ws.title('PythonGuides')
    ws.geometry('400x300')
    ws['bg']='#fb0'

    tv = ttk.Treeview(ws)
    tv['columns']=('Rank', 'Name', 'Badge')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Rank', anchor=CENTER, width=80)
    tv.column('Name', anchor=CENTER, width=80)
    tv.column('Badge', anchor=CENTER, width=80)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Rank', text='Id', anchor=CENTER)
    tv.heading('Name', text='rank', anchor=CENTER)
    tv.heading('Badge', text='Badge', anchor=CENTER)

    tv.insert(parent='', index=0, iid=0, text='', values=('1','Vineet','Alpha'))
    tv.insert(parent='', index=1, iid=1, text='', values=('2','Anil','Bravo'))
    tv.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'))
    tv.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
    tv.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo'))
    tv.pack()

    ws.mainloop()


















































if __name__ == '__main__':
    main()