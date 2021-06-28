from tkinter import *
import tkinter.messagebox as box

root = Tk()
root.geometry("644x344")
root.resizable(0, 0)
Label(root, text="Welcome to traveler agency", font="comicsansns 13 bold", pady=10).grid(row=0, column=3)
name = Label(root, text="Name").grid(row=1, column=2)
phone = Label(root, text="phone").grid(row=2, column=2)
gender = Label(root, text="gender").grid(row=3, column=2)
emergency = Label(root, text="Emergency Contact").grid(row=4, column=2)
paymentmode = Label(root, text="Payment mode").grid(row=5, column=2)

nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emergencyValue = StringVar()
paymentmode = StringVar()
foodchain = IntVar()

nameentry = Entry(root, textvariable=nameValue)
phoneentry = Entry(root, textvariable=phoneValue)
genderentry = Entry(root, textvariable=genderValue)
emergencyentry = Entry(root, textvariable=emergencyValue)
paymentmodeentry = Entry(root, textvariable=paymentmode)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

# checkbox
foodService = Checkbutton(text="Want to book your meal?", variable=foodchain)
foodService.grid(row=6, column=3)


def sub():
    print("Submitting Forms")

    print(
        f"{nameValue.get(), phoneValue.get(), genderValue.get(), emergencyValue.get(), paymentmode.get(), foodchain.get()}\n")

    with open("records.txt", "a") as f:
        f.write(
            f"{nameValue.get(), phoneValue.get(), genderValue.get(), emergencyValue.get(), paymentmode.get(), foodchain.get()}\n")


btn = Button(root, text="Submit Data", command=sub)
btn.grid(row=7, column=3)

root.mainloop()
