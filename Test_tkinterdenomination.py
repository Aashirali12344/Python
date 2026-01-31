from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

try:
    upload = Image.open("codingal.png")
    upload = upload.resize((300, 300))
    image = ImageTk.PhotoImage(upload)

    label_img= Label(root, image=image, bg='light blue')
    label_img.place(x=180, y=20)
except:
    pass

label1 = Label(
    root,
    text="Hey User! Welcome to Denomination Counter Application",
    bg='light blue',
    font=('Arial', 11)
)
label1.place(relx=0.5, y=340, anchor=CENTER)


def topwin():
    top =Toplevel(root)
    top.title("Currency Denomination Counter")
    top.configure(bg='grey')
    top.geometry('600x400')

    Label(top, text="Enter Amount", bg='grey', font=('Arial', 12)).place(x=230, y=40)

    entry = Entry(top)
    entry.place(x=200, y=80)
    Label(top, text="2000  :", bg='grey').place(x=180, y=200)
    Label(top, text="500  :", bg='grey').place(x=180, y=230)
    Label(top, text="100  :", bg='grey').place(x=180, y=260)

    t1 = Entry(top, width=10)
    t2 = Entry(top, width=10)
    t3 = Entry(top, width=10)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    def calculate():
        try:
            amount = int(entry.get())
            if amount < 0:
                raise ValueError
            n2000 = amount // 2000
            amount %= 2000
            n500 = amount // 500
            amount %= 500

            n100 = amount //100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(0, n2000)
            t2.insert(0, n500)
            t3.insert(0, n100)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid postive number")
    Button(top, text="Calculate", command=calculate).place(x=240, y=120)


def msg():
    messagebox.showinfo(
        "Alert",
        "Do you want to  calculate the denomination count"
    )

    topwin()

button1 = Button(
    root,
    text="Lets get started!",
    command=msg,
    bg='brown',
    fg='white'
)
button1.place(x=260, y=360)

root.mainloop()
