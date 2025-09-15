
from tkinter import Label, Tk  
import time  

app = Tk()  
app.title("🕒Andrina's Digital Clock")  
app.geometry("300x100")  
app.resizable(False, False)  
app.configure(bg="pink")  

clock_label = Label(app, bg="pink", fg="purple", font=("Helvetica", 40), relief='flat')  
clock_label.place(x=20, y=20)

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

update_time()  
app.mainloop()


