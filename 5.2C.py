from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

##hardware
ledred = LED(18)
ledgreen = LED(23)
ledblue = LED(24)

##GUI Definitions
win = Tk()
win.title("5.2Ctask")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

##EVENT FUNCTIONS
def ledTogglered():
    if ledred.is_lit:
        ledred.off()
        ledButtonred["text"] = "Turn red LED on"
    else:    
        ledred.on()
        ledButtonred["text"] = "Turn red LED off"
        
def ledTogglegreen():     
    if ledgreen.is_lit:
        ledgreen.off()
        ledButtongreen["text"] = "Turn green LED on"
    else:
        ledgreen.on()
        ledButtongreen["text"] = "Turn green LED off"
        
def ledToggleblue():     
    if ledblue.is_lit:
        ledblue.off()
        ledButtonblue["text"] = "Turn blue LED on"
    else:
        ledblue.on()
        ledButtonblue["text"] = "Turn blue LED off"
                
def close():
    RPi.GPIO.cleanup()
    win.destroy()
        
    
##WIDGETS
ledButtonred=Button(win, text='RED', font=myFont, command=ledTogglered, bg = 'pink', height=1, width=24)
ledButtonred.grid(row=0, column=1)
ledButtongreen=Button(win, text='GREEN', font=myFont, command=ledTogglegreen, bg = 'lightgreen', height=1, width=24)
ledButtongreen.grid(row=1, column=1)
ledButtonblue=Button(win, text='BLUE', font=myFont, command=ledToggleblue, bg = 'skyblue', height=1, width=24)
ledButtonblue.grid(row=2, column=1)

exitButton=Button(win, text='Exit', font=myFont, command=close, bg = 'grey', height=1, width=24)
exitButton.grid(row=3, column=1)    

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()