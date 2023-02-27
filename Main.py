from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title("")
window.geometry("650x160")
window.configure(bg="black")
window.resizable(True, True)

clock_label = Label(window, bg="black", fg="cyan", font=("ds-digital", 100, "bold"), relief="flat")
clock_label.anchor="center"

def update_label():
    current_time = strftime("%I:%M:%S %p")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)
    clock_label.pack(anchor="center")

update_label()
window.mainloop()