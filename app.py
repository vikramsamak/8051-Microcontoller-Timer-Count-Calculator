from tkinter import*
from tkinter import ttk
import customtkinter

def timercountcalc():
    time=timeentry.get()
    dutycycle=dutycycleentry.get()
    mode=mcom.get()
    
    time=int(time)
    dutycycle=int(dutycycle)
   
    c1=((dutycycle*time)/100)
    c2=time-c1
    
    tonentry.delete(0,END)
    tonentry.insert(0,c1)
        
    tofentry.delete(0,END)
    tofentry.insert(0,c2)
   
    if mode=="Mode1":
       
        tc1d=65536-((c1*(10**(-3)))/(1.085*(10**(-6))))
        tc1d=round(tc1d)
        
        tc2d=65536-((c2*(10**(-3)))/(1.085*(10**(-6))))
        tc2d=round(tc2d)
    
        tc1h=hex(tc1d)
        tc2h=hex(tc2d)
        
        tonhexcount=list(tc1h)
        tonth=tonhexcount[2]+tonhexcount[3]
        tontl=tonhexcount[4]+tonhexcount[5]
        
        tofhexcount=list(tc2h)
        tofth=tofhexcount[2]+tofhexcount[3]
        toftl=tofhexcount[4]+tofhexcount[5]
        
        tonthentry.delete(0,END)
        tonthentry.insert(0,tonth)

        tontlentry.delete(0,END)
        tontlentry.insert(0,tontl)

        tofthentry.delete(0,END)
        tofthentry.insert(0,tofth)

        toftlentry.delete(0,END)
        toftlentry.insert(0,toftl)
    if mode=="Mode2":
        
        tc1d=256-((c1*(10**(-6)))/(1.085*(10**(-6))))
        tc1d=round(tc1d)
        #print(tc1d)
       
        tc2d=256-((c2*(10**(-6)))/(1.085*(10**(-6))))
        tc2d=round(tc2d)
        #print(tc1d)
       
        tc1h=hex(tc1d)
        #print(tc1h)
        
        tonhexcount=list(tc1h)
        #print(tonhexcount)
        tonthtl=tonhexcount[2]+tonhexcount[3]
        #print(tonthtl)
        
        tc2h=hex(tc2d)
        print(tc2h)

        tofhexcount=list(tc2h)
        #print(tofhexcount)
        tofthtl=tofhexcount[2]+tofhexcount[3]
        #print(tofthtl)
        
        
        tonthentry.delete(0,END)
        tonthentry.insert(0,tonthtl)
        tontlentry.delete(0,END)
        
        tofthentry.delete(0,END)
        tofthentry.insert(0,tofthtl)
        toftlentry.delete(0,END)
        
window=customtkinter.CTk()
window.geometry("300x600")
window.title("8051 TIMER COUNT CALCULATOR")

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

timelabel=customtkinter.CTkLabel(window,text="Enter Time(ms/us)")
timelabel.pack()

timeentry=customtkinter.CTkEntry(window,width=280)
timeentry.pack()

dutycyclelable=customtkinter.CTkLabel(window,text="Enter Duty Cycle (Percentage)")
dutycyclelable.pack()

dutycycleentry=customtkinter.CTkEntry(window,width=280)
dutycycleentry.pack()

modelabel=customtkinter.CTkLabel(window,text="Select Mode")
modelabel.pack()

mcom=ttk.Combobox(window)
mcom['values']=('Mode1','Mode2')
mcom.current()
mcom.pack()

calculatebutton=customtkinter.CTkButton(window,text="Calculate",width=280,command=timercountcalc)
calculatebutton.pack(pady=10)

tonms=customtkinter.CTkLabel(window,text="TON(ms/us)")
tonms.pack()

tonentry=customtkinter.CTkEntry(window,width=280)
tonentry.pack()

tofms=customtkinter.CTkLabel(window,text="TOF(ms/us)")
tofms.pack()

tofentry=customtkinter.CTkEntry(window,width=280)
tofentry.pack()

tonframe=LabelFrame(window,text="For TON")
tonframe.pack()

tonthlabel=customtkinter.CTkLabel(tonframe,text="TH")
tonthlabel.pack()

tonthentry=customtkinter.CTkEntry(tonframe,width=280)
tonthentry.pack()

tontllable=customtkinter.CTkLabel(tonframe,text="TL")
tontllable.pack()

tontlentry=customtkinter.CTkEntry(tonframe,width=280)
tontlentry.pack()

tofframe=LabelFrame(window,text="For TOFF")
tofframe.pack()

tofthlabel=customtkinter.CTkLabel(tofframe,text="TH")
tofthlabel.pack()

tofthentry=customtkinter.CTkEntry(tofframe,width=280)
tofthentry.pack()

toftlalbel=customtkinter.CTkLabel(tofframe,text="TL")
toftlalbel.pack()

toftlentry=customtkinter.CTkEntry(tofframe,width=280)
toftlentry.pack()

window.mainloop()