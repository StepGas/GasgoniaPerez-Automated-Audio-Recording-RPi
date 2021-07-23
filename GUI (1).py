import os
import smtplib
import imghdr
from email.message import EmailMessage
from tkinter import *
from PIL import ImageTk,Image

EMAIL_ADDRESS='gasgoniarpi@gmail.com'
EMAIL_PASSWORD='2018100891'

root=Tk()
root.attributes('-fullscreen',True)
def Start():
    LTitle.pack_forget()
    Linst1.pack_forget()
    Linst2.pack_forget()
    BStart.pack_forget()
    Lcredit.pack_forget()
    
    L1.pack()
    LRec1.pack()
    Image1.pack()
    BRec1.pack()
    LReminder.pack()
def Rec1():
    LRec1.pack_forget()
    os.system("arecord -d 10 -f cd -c 1 upperleft.wav")
    BRec1.pack_forget()
    LReminder.pack_forget()
    Image1.pack_forget()
    
    LPlay1.pack()
    BPlay1.pack()
def Play1():
    os.system("aplay upperleft.wav")
    LConfirmNext.pack()
    BNext2.pack()
    BRe1.pack()
def Next2():
    L1.pack_forget()
    LPlay1.pack_forget()
    BPlay1.pack_forget()
    LConfirmNext.pack_forget()
    BNext2.pack_forget()
    BRe1.pack_forget()
    
    L2.pack()
    LRec1.pack()
    Image2.pack()
    BRec2.pack()
    LReminder.pack()
def Rec2():
    LRec1.pack_forget()
    os.system("arecord -d 10 -f cd -c 1 upperright.wav")
    BRec2.pack_forget()
    LReminder.pack_forget()
    Image2.pack_forget()
    
    LPlay1.pack()
    BPlay2.pack()   
def Play2():
    os.system("aplay upperright.wav")
    LConfirmNext.pack()
    BNext3.pack()
    BRe2.pack()
def Next3():
    L2.pack_forget()
    LPlay1.pack_forget()
    BPlay2.pack_forget()
    LConfirmNext.pack_forget()
    BNext3.pack_forget()
    BRe2.pack_forget()
    
    L3.pack()
    LRec1.pack()
    Image3.pack()
    BRec3.pack()
    LReminder.pack()
def Rec3():
    LRec1.pack_forget()
    os.system("arecord -d 10 -f cd -c 1 middleleft.wav")
    BRec3.pack_forget()
    LReminder.pack_forget()
    Image3.pack_forget()
    
    LPlay1.pack()
    BPlay3.pack()   
def Play3():
    os.system("aplay middleleft.wav")
    LConfirmNext.pack()
    BNext4.pack()
    BRe3.pack()
def Next4():
    L3.pack_forget()
    LPlay1.pack_forget()
    BPlay3.pack_forget()
    LConfirmNext.pack_forget()
    BNext4.pack_forget()
    BRe3.pack_forget()
    
    L4.pack()
    LRec1.pack()
    Image4.pack()
    BRec4.pack()
    LReminder.pack()
def Rec4():
    LRec1.pack_forget()
    os.system("arecord -d 10 -f cd -c 1 middleright.wav")
    BRec4.pack_forget()
    LReminder.pack_forget()
    Image4.pack_forget()
    
    LPlay1.pack()
    BPlay4.pack()   
def Play4():
    os.system("aplay middleright.wav")
    LConfirmNext.pack()
    BNext5.pack()
    BRe4.pack()
def Next5():
    L4.pack_forget()
    LPlay1.pack_forget()
    BPlay4.pack_forget()
    LConfirmNext.pack_forget()
    BNext5.pack_forget()
    BRe4.pack_forget()
    
    L5.pack()
    LRec1.pack()
    Image5.pack()
    BRec5.pack()
    LReminder.pack()
def Rec5():
    LRec1.pack_forget()
    os.system("arecord -d 10 -f cd -c 1 bottomleft.wav")
    BRec5.pack_forget()
    LReminder.pack_forget()
    Image5.pack_forget()
    
    LPlay1.pack()
    BPlay5.pack()
def Play5():
    os.system("aplay bottomleft.wav")
    LConfirmNext.pack()
    BNext6.pack()
    BRe5.pack()
def Next6():
    L5.pack_forget()
    LPlay1.pack_forget()
    BPlay5.pack_forget()
    LConfirmNext.pack_forget()
    BNext6.pack_forget()
    BRe5.pack_forget()
    
    L6.pack()
    LRec1.pack()
    Image6.pack()
    BRec6.pack()
    LReminder.pack()
def Rec6():
    LRec1.pack_forget()
    os.system("arecord -d 10 -f cd -c 1 bottomright.wav")
    BRec6.pack_forget()
    LReminder.pack_forget()
    Image6.pack_forget()
    
    LPlay1.pack()
    BPlay6.pack()   
def Play6():
    L6.pack_forget()
    os.system("aplay bottomright.wav")
    LConfirm.pack()
    BSend.pack()
    BRe6.pack()
def ReStart():
    LPlay1.pack_forget()
    BPlay1.pack_forget()
    LConfirmNext.pack_forget()
    BNext2.pack_forget()
    BRe1.pack_forget()
    Start()
def ReNext2():
    LPlay1.pack_forget()
    BPlay2.pack_forget()
    LConfirmNext.pack_forget()
    BNext3.pack_forget()
    BRe2.pack_forget()
    Next2()
def ReNext3():
    LPlay1.pack_forget()
    BPlay3.pack_forget()
    LConfirmNext.pack_forget()
    BNext4.pack_forget()
    BRe3.pack_forget()
    Next3()
def ReNext4():
    LPlay1.pack_forget()
    BPlay4.pack_forget()
    LConfirmNext.pack_forget()
    BNext5.pack_forget()
    BRe4.pack_forget()
    Next4()
def ReNext5():
    LPlay1.pack_forget()
    BPlay5.pack_forget()
    LConfirmNext.pack_forget()
    BNext6.pack_forget()
    BRe5.pack_forget()
    Next5()
def ReNext6():
    LPlay1.pack_forget()
    BPlay6.pack_forget()
    LConfirm.pack_forget()
    BSend.pack_forget()
    BRe6.pack_forget()
    Next6()
def Send():
    LConfirm.pack_forget()
    LPlay1.pack_forget()
    BPlay6.pack_forget()
    BSend.pack_forget()
    BRe6.pack_forget()
    
    fileopen=open('/home/pi/Desktop/Doctor/Info.txt','r')
    filelist=fileopen.readlines()
    infolist=[]
    for line in filelist:
        infolist.append(line.strip())
        
    msg=EmailMessage()
    msg['Subject']='Cough Recording '+infolist[1]+', '+infolist[2]
    msg['From']=EMAIL_ADDRESS
    msg['To']=infolist[0]
    msg.set_content('Here are the recordings :)')
    files=['/home/pi/upperleft.wav','/home/pi/upperright.wav','/home/pi/middleleft.wav','/home/pi/middleright.wav','/home/pi/bottomleft.wav','/home/pi/bottomright.wav']
    for file in files:
        with open(file,'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
        msg.add_attachment(file_data, maintype='Audio',subtype='wav', filename=file_name[9:])
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(msg)
    LSent.pack()
    Bclose.pack()

def close():
    os.system('sudo shutdown -h now')

def end():
    root.destroy()
    
#Buttons
BStart = Button(root, text="Start",font=("Arial", 25), padx=40, pady=30, command=Start)
BRec1 = Button(root, text="Record", padx=40, pady=30, command=Rec1, activebackground="red", activeforeground='white')
BRec2 = Button(root, text="Record", padx=40, pady=30, command=Rec2, activebackground="red", activeforeground='white')
BRec3 = Button(root, text="Record", padx=40, pady=30, command=Rec3, activebackground="red", activeforeground='white')
BRec4 = Button(root, text="Record", padx=40, pady=30, command=Rec4, activebackground="red", activeforeground='white')
BRec5 = Button(root, text="Record", padx=40, pady=30, command=Rec5, activebackground="red", activeforeground='white')
BRec6 = Button(root, text="Record", padx=40, pady=30, command=Rec6, activebackground="red", activeforeground='white')

BPlay1 = Button(root, text="Play", padx=40, pady=30, command=Play1)
BPlay2 = Button(root, text="Play", padx=40, pady=30, command=Play2)
BPlay3 = Button(root, text="Play", padx=40, pady=30, command=Play3)
BPlay4 = Button(root, text="Play", padx=40, pady=30, command=Play4)
BPlay5 = Button(root, text="Play", padx=40, pady=30, command=Play5)
BPlay6 = Button(root, text="Play", padx=40, pady=30, command=Play6)

BNext2 = Button(root, text="Next", padx=20, pady=10, command=Next2)
BNext3 = Button(root, text="Next", padx=20, pady=10, command=Next3)
BNext4 = Button(root, text="Next", padx=20, pady=10, command=Next4)
BNext5 = Button(root, text="Next", padx=20, pady=10, command=Next5)
BNext6 = Button(root, text="Next", padx=20, pady=10, command=Next6)

BRe1=Button(root, text="Re-record",padx=20,pady=10, command=ReStart)
BRe2=Button(root, text="Re-record",padx=20,pady=10, command=ReNext2)
BRe3=Button(root, text="Re-record",padx=20,pady=10, command=ReNext3)
BRe4=Button(root, text="Re-record",padx=20,pady=10, command=ReNext4)
BRe5=Button(root, text="Re-record",padx=20,pady=10, command=ReNext5)
BRe6=Button(root, text="Re-record",padx=20,pady=10, command=ReNext6)

BSend = Button(root, text="Send to Doctor", padx=20, pady=10, command=Send,activebackground="red", activeforeground='white')

Bend = Button(root, text="Close Program", padx=15, pady=7, command=end)
Bclose = Button(root, text="Close Device", padx=15, pady=7, command=close)
#Labels
L1=Label(root,text="Part 1:")
L2=Label(root,text="Part 2:")
L3=Label(root,text="Part 3:")
L4=Label(root,text="Part 4:")
L5=Label(root,text="Part 5:")
L6=Label(root,text="Part 6:")
LTitle= Label(root,text="Welcome to the Automated Stethoscope Recording Application\n\n\n",font=("Arial", 40))
Linst1= Label(root,text="Please follow the instructions shown on the program.",font=("Arial", 20))
Linst2= Label(root,text="There will be 6 parts to the recording. Press Start to begin.\n\n\n",font=("Arial", 20))
LReminder= Label(root, text="Please cough while the app is recording. Recording is ongoing when the button is red and pressed.")
LRec1= Label(root,text="Please place the stethoscope diaphragm at the red dot on your body and click record")
LPlay1= Label(root,text="Click Play to listen to the recording")
LConfirmNext= Label(root,text="If you are satisfied with the recording, press Next.")
LConfirm= Label(root,text="If you are satisfied and would like to send the recording to your doctor, press Send. The Process may take a few seconds.\n The automated email is sending if the send button is still red.")
LSent= Label(root, text="Your recordings have been recieved by your doctor! Thank you for using our program.")
Lcredit=Label(root,text="This Device and Application was created and Programed by Gasgonia, and Perez")
#Images
i1= ImageTk.PhotoImage(Image.open('/home/pi/Pictures/image1.jpg'))
i2= ImageTk.PhotoImage(Image.open('/home/pi/Pictures/image2.jpg'))
i3= ImageTk.PhotoImage(Image.open('/home/pi/Pictures/image3.jpg'))
i4= ImageTk.PhotoImage(Image.open('/home/pi/Pictures/image4.jpg'))
i5= ImageTk.PhotoImage(Image.open('/home/pi/Pictures/image5.jpg'))
i6= ImageTk.PhotoImage(Image.open('/home/pi/Pictures/image6.jpg'))
Image1= Label(image=i1)
Image2= Label(image=i2)
Image3= Label(image=i3)      
Image4= Label(image=i4)
Image5= Label(image=i5)
Image6= Label(image=i6)
#Display
LTitle.pack()
Linst1.pack()
Linst2.pack()
BStart.pack()
Lcredit.pack()
#Bend.pack()
#BSend.pack()
#BPlay6.pack()
root.mainloop()