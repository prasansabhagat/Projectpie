import tkinter as tkt
from tkinter import *
import base64
import random

root = tkt.Tk()
root.geometry("800x800")
root.title("Message Encryption and Decryption")  


Tops = Frame(root, width=800)
Tops.pack()

area = Frame(root, width=800)
area.pack(side=LEFT)


maintxt = Label(Tops, font=('helvetica', 30, 'bold'),
                text="Message Encryption and Decryption",
                fg="Black", bg="#BBBBFF")
maintxt.pack()



Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()



lMsg = Label(area, font=('arial', 10, 'bold'),
                text="Message",bd=5, fg="Black")
lMsg.grid(row=0, column=0)

txtMsg = Entry(area, font=('arial', 8),
                textvariable=Msg, insertwidth=4,
                justify='right',bd=5, bg="#BBBBFF")
txtMsg.grid(row=0, column=1)



lKey = Label(area, font=('arial', 10, 'bold'),
             text="Key(only integer)", bd=5, fg="Black")
lKey.grid(row=1, column=0)

txtKey = Entry(area, font=('arial', 8),
                textvariable=key, insertwidth=4,
               justify='right', bd=5, bg="#BBBBFF")
txtKey.grid(row=1, column=1)



lResult = Label(area, font=('arial', 10, 'bold'),
                text="Result(Encrypted/Decrypted message)", bd=5, fg="Black")
lResult.grid(row=1, column=2)

txtResult = Entry(area, font=('arial', 8),
               textvariable=Result, insertwidth=4,
                  justify='right', bd=5, bg="#BBBBFF")
txtResult.grid(row=1, column=3)



lMode = Label(area, font=('arial', 10, 'bold'),
              text="'e' for encrypt and 'd' for decrypt", bd=5, fg="Black")
lMode.grid(row=2, column=0)

txtMode = Entry(area, font=('arial', 8),
                textvariable=mode, insertwidth=4,
                justify='right', bd=5, bg="#BBBBFF")
txtMode.grid(row=2, column=1)


def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        print("enc:", enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#chr()- integer to character
#ord()- reverse

def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)


def Results():
    msg = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode(k, msg))
    else:
        Result.set(decode(k, msg))



def qExit():
    root.destroy()



def Reset():

    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")




btnTotal = Button(area, padx=6, pady=3, bd=5, fg="black",
                  font=('arial', 10), width=10,
                  text="Show Message", bg="powder blue",
                  command=Results).grid(row=7, column=1)


btnReset = Button(area,  padx=6, pady=3, bd=5,
                  fg="black", font=('arial', 10),
                  width=10, text="Reset", bg="green",
                  command=Reset).grid(row=7, column=2)


btnExit = Button(area, padx=6, pady=3, bd=5,
                 fg="black", font=('arial', 10),
                 width=10, text="Exit", bg="red",
                 command=qExit).grid(row=7, column=3)



root.mainloop()     
