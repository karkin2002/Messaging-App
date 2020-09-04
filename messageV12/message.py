from tkinter import *
import tkinter.font as font
import datetime
from network import Network
from chatClass import chatString
from userClass import saveData
from saving import *

def menuClick(event=None):
    global userIP, userPort, name, userClass, menu, n, root
    name = nameEntry.get()
    userClass = roleEntry.get()
    userIP = hostIPEntry.get()
    userPort = int(portEntry.get())
    createNewSave("lastUserData.pkl",name,userClass,userIP,userPort)
    n = Network(userIP, userPort)
    menu = False
    root.destroy()


user = loadSave("lastUserData.pkl")
menu = True
while menu:
    root = Tk()
    root.title("Messages Options")
    root.pack_propagate(0)
    # root.configure(bg='#dedede')
    root.resizable(width=False, height=False)

    userIP = None
    userPort = None


    name = Message(root,text="Name:").grid(row=0,column=0)
    role = Label(root,text=  "Role:").grid(row=1,column=0)
    hostIPText = Label(root,text="Host IP:").grid(row=2,column=0)
    portText = Label(root,text=  "Port:").grid(row=3,column=0)

    nameEntry = Entry(root,width = 20)
    roleEntry = Entry(root,width = 20)
    hostIPEntry = Entry(root,width = 20)
    portEntry = Entry(root,width = 20)

    nameEntry.insert(0, user.name)
    roleEntry.insert(0, user.role)
    hostIPEntry.insert(0, user.hostIP)
    portEntry.insert(0, user.port)

    nameEntry.grid(row=0,column=1)
    roleEntry.grid(row=1,column=1)
    hostIPEntry.grid(row=2,column=1)
    portEntry.grid(row=3,column=1)

    root.bind('<Return>', menuClick)

    root.mainloop()















root = Tk()
root.title("Messages")
root.pack_propagate(0)
root.configure(bg='#dedede')
root.resizable(width=False, height=False)

def update():
    global chat, definitionText
    definitionText.config(state=NORMAL)
    definitionText.delete('1.0', END)
    definitionText.insert("1.0",chat.message)
    definitionText.see(END)
    definitionText.config(state=DISABLED)


def clock():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    welcomeMessage.config(state=NORMAL)
    welcomeMessage.delete('1.0', END)
    welcomeMessage.insert("1.0",f" Welcome to messages                                       Time: {time} ")
    welcomeMessage.config(state=DISABLED)
    
    
    global chat
    newMessage = chatString(None)
    
    if chat.message != n.send(newMessage).message:
        chat = n.send(newMessage)
        update()
    
    root.after(1000, clock)


def myClick(event=None):
    global chat
    if enterText.get() != "" and len(enterText.get()) <= 300:
        newMessage = chatString(f"{name} [{userClass}]: {enterText.get()}\n")
        chat = n.send(newMessage)
        enterText.delete(0,END)
    update()


# name = nameEntry.get()
# userClass = roleEntry.get()
chat = n.getP()

fontLarge = font.Font(family='bahnschrift',size=14,weight=font.BOLD)
fontSmall = font.Font(family='bahnschrift',size=11)

## Welcome bar widget
frame1 = LabelFrame(root)

welcomeMessage = Text(frame1, width=51,height=1,font=fontLarge,bg="gray")
welcomeMessage.insert("1.0", " Welcome to messages                                       Time:")
welcomeMessage.config(state=DISABLED)

frame1.grid(row=0,column=0)
welcomeMessage.grid(row=0,column=0)


## Text Widget
descriptionFrame = Frame(root)

definitionFrame = LabelFrame(descriptionFrame)
scroll = Scrollbar(definitionFrame)
definitionText = Text(definitionFrame, width=61, height=40, yscrollcommand=scroll.set,font=fontSmall,bg="#dddddd")
scroll.config(command=definitionText.yview)

definitionText.delete("1.0", END)   # an example of how to delete all current text
# definitionText.insert("1.0", "No new messages...") # an example of how to add new text to the text area

descriptionFrame.grid(row=1,column=0)
definitionFrame.pack(fill=BOTH, expand=True)
scroll.pack(side=RIGHT, fill=Y)
definitionText.pack(side=LEFT, fill=BOTH, expand=True)

definitionText.config(state=DISABLED)

## Entry Widgets
frame2 = LabelFrame(root)
enterText = Entry(frame2,width = 55, borderwidth=5,font=fontSmall)
sendButton = Button(frame2,text="Send",width = 6,command=myClick,font=fontSmall)

frame2.grid(row=2,column=0)
enterText.grid(row=0,column=0)
sendButton.grid(row=0,column=1)

root.bind('<Return>', myClick)

clock()
update()

root.mainloop()