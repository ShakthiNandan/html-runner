from tkinter import *
import webbrowser as w
import os
path=os.path.expanduser("~\Desktop")
try:
    os.mkdir(path+"\WEB")
except OSError:
    print("Error Path exists")
path+="\WEB"
def run():
	w.open(path+"\example.html")
def saver(a):
    data=a.get('1.0','end')
    print(data)
    if(a==html):
        with open(path+"\example.html","w") as wf:
            wf.write(data)
    elif(a==css):
        with open(path+"\example.css","w") as wf:
            wf.write(data)
    elif(a==js):
        with open(path+"\example.js","w") as wf:
            wf.write(data)
			
			
import tkinter
top = tkinter.Tk()
top.configure(bg="grey")
Grid.columnconfigure(top,0,weight=1)
Grid.rowconfigure(top,0,weight=1)
Grid.columnconfigure(top,1,weight=1)
Grid.rowconfigure(top,1,weight=1)
Grid.columnconfigure(top,2,weight=1)
Grid.rowconfigure(top,2,weight=1)
Grid.columnconfigure(top,3,weight=1)
Grid.rowconfigure(top,3,weight=1)
top.title("HTML RUNNER")
ti=Label(top,text="HTML RUNNER",font=("Arial 10"))
Labhtml=Label(top,text="HTML",font=("Arial 8"))
Labcss=Label(top,text="CSS",font=("Arial 8"))
Labjs=Label(top,text="JS",font=("Arial 8"))
html=Text(top,height=20,width=40,wrap='word')
savehtml=Button(top,text="Save",font=("Arial",10),command=lambda: saver(html))
css=Text(top,height=20,width=40,wrap='word')
savecss=Button(top,text="Save",font=("Arial",10),command=lambda: saver(css))
js=Text(top,height=20,width=40,wrap='word')
savejs=Button(top,text="Save",font=("Arial",10),command=lambda: saver(js))
add=Button(top,text="RUN",font=("Arial",10),command=lambda: run())

ti.grid(row=0,column=1)
Labhtml.grid(row=1,column=0)
Labcss.grid(row=1,column=1)
Labjs.grid(row=1,column=2)
html.grid(row=2,column=0)
savehtml.grid(row=3,column=0)
css.grid(row=2,column=1)
savecss.grid(row=3,column=1)
js.grid(row=2,column=2)
savejs.grid(row=3,column=2)
add.grid(row=4,column=1)

top.mainloop()
