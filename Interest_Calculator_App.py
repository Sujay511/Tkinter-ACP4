from tkinter import *

window=Tk()
window.title("Interest Calculator App")
window.geometry("400x400")

frame=Frame(master=window,height=400,width=400,bg="grey")

lbl=Label(frame,text="Full Name",bg="white",fg="black")
lbl1=Label(frame,text="Principal Amount",bg="white",fg="black")
lbl2=Label(frame,text="Time Period",bg="white",fg="black")
lbl3=Label(frame,text="Rate of Intrest",bg="white",fg="black")

entry=Entry(frame)
entry1=Entry(frame)
entry2=Entry(frame)
entry3=Entry(frame)



    
def calculation():
    try:
        global p,t,r
        p=int(entry1.get())
        t=int(entry2.get())
        r=int(entry3.get())
        si=(p*t*r)/100
        greet="Hey "+entry.get()
        message="\nThe Simple interest is:",si
        textbox.insert(END,greet)
        textbox.insert(END,message)
    except ValueError:
        print("Please check and enter the values once again.")


textbox=Text(bg="white",fg="black")
btn=Button(frame,text="Calculate Intrest",bg="light blue",relief=RAISED,command=calculation)



frame.place(x=20,y=0)
lbl.place(x=20,y=20)
entry.place(x=150,y=20)
lbl1.place(x=20,y=70)
entry1.place(x=150,y=70)
lbl2.place(x=20,y=130)
entry2.place(x=150,y=130)
lbl3.place(x=20,y=190)
entry3.place(x=150,y=190)
textbox.place(x=0,y=310)
btn.place(x=150,y=250)

window.mainloop()

    
