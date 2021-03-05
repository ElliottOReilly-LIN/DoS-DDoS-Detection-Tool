from tkinter import *
from dosAttack import runSingleDoS
from multiIPAttack import runMultiDos
from DDoS_attack import dosDetect


window = Tk()
window.configure(background="#0892d0")
window.geometry("720x720")


def runSDoS():
    runSingleDoS()


def runMDoS():
    runMultiDoS()


def runSocketGrab():
    dosDetect()


logo = PhotoImage(file='ddos.png')
Label(window, text=" This is the DoS / DDoS \n Attack Inspector Tool!  ", pady=10, font=('Arial', 20, 'bold')).pack()
window.title("Elliott O'Reilly Cyber Security DoS Tool")
Label(window, image=logo).pack()

Label(window, text="    Choose your attack vecotors:   ", bd=4, pady=10, fg='#00ff66', font=('Arial', 14, 'bold')).pack()

Button(window, text="  Begin Single IP DoS  ", bd=4, command=runSDoS).pack()
Button(window, text="  Stop Single IP DoS   ", bd=4, command=window.destroy).pack()

Button(window, text="  Begin Multi IP DoS   ", bd=4, command=runMDoS).pack()
Button(window, text="  Stop Multi IP DoS    ", bd=4, command=window.destroy).pack()

Button(window, text="  Begin DDoS IP Scan  ", bd=4, command=runSocketGrab).pack()
Button(window, text="  Stop DDoS IP Scan   ", bd=4, command=window.destroy).pack()
Label(window, text="  Start the Defense\n Detection Subsytem!!  ", bd=4, pady=10, fg='#00ff66', font=('Arial', 14, 'bold')).pack()
Button(window, text="  Begin tcpDump analytics", bd=6, pady=10, command=runSocketGrab).pack()
Button(window, text="  Stop tcpDump analytics   ", bd=6, pady=10, command=window.destroy).pack()
window.mainloop()
