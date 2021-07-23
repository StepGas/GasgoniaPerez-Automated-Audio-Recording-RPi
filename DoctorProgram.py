from tkinter import *

root=Tk()
root.attributes('-fullscreen',True)
root.configure(background='white')

def save():
    fileEdit= open('/home/pi/Desktop/Doctor/Info.txt','w')
    femail=Temail.get()
    fsurname=Tsurname.get()
    fname=Tname.get()
    fileEdit.write(femail+"\n")
    fileEdit.write(fsurname+"\n")
    fileEdit.write(fname)    
    fileEdit.close()

def end():
    root.destroy()
    
Lwelcome= Label(root,text="Please insert required information")
Lemail= Label(root,text="Doctor's e-mail")
Lsurname= Label(root,text="Patient's Family Name")
Lname= Label(root,text="Patient's First Name")

Temail=Entry(root,width=50)
Tsurname=Entry(root,width=50)
Tname=Entry(root,width=50)

Bsave = Button(root, text="Save", padx=15, pady=7, command=save)
Bend = Button(root, text="Close Program", padx=15, pady=7, command=end)

Lwelcome.pack()
Lemail.pack()
Temail.pack()
Lsurname.pack()
Tsurname.pack()
Lname.pack()
Tname.pack()
Bsave.pack()
Bend.pack()

root.mainloop()
