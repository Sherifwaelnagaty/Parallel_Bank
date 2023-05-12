import threading
import time
from tkinter import simpledialog
from tkinter import *
from PIL import ImageTk, Image


class BankAccount:
    def __init__(self, accountName, balance, lock):
        self.accountName = accountName
        self.balance = balance
        self.accountLock = lock


accountsList = []


def createAccount():

    def func():

        accountName = textField.get()
        if len(accountName) > 0:
            accountsList.append(
                BankAccount(accountName=accountName, balance=0, lock=threading.Lock()))
            successLabel["text"] = "Account Created Successfully"
            successLabel["fg"] = "green"

        else:
            successLabel["text"] = "You Cannot leave this field empty"
            successLabel["fg"] = "red"

    root1 = Tk()
    root1.title("Create Bank Account")
    root1.geometry("500x500")

    # resized_image = img.resize((200, 200), Image.ANTIALIAS)
    depositImage = PhotoImage(
        file="bank.png", master=root1)
    depositImage = depositImage.subsample(x=2, y=2)

    frame = Frame(root1, borderwidth=50)

    imageLabel = Label(frame, image=depositImage)

    textField = Entry(frame, width=30)
    submitButton = Button(frame, command=func, text="Create Account", width=15,
                          height=1, font="2", bg="blue", fg="white")

    textLabel = Label(frame, text="Enter The Account Name")
    successLabel = Label(frame, text="")
    # the order of elements depends on the pack() order
    frame.pack()
    frame.place(relx=.5, rely=.5, anchor=CENTER)
    imageLabel.pack()
    textLabel.pack()
    textField.pack()
    submitButton.pack()
    submitButton.place(relx=.5, rely=1.1, anchor=CENTER)
    successLabel.pack()
    root1.mainloop()


def deposit():

    def func():
        start_time = time.time()
        accountName = accountField.get()
        accountExists = False
        for i in range(len(accountsList)):
            if (accountName == accountsList[i].accountName):
                # account exists
                # acquire the lock
                if accountsList[i].accountLock.locked():
                    print("Cannot Deposit Now Another Thread Currently Has The Lock")
                accountsList[i].accountLock.acquire()
                accountExists = True
                depositedMoney = int(moneyField.get())
                accountsList[i].balance += depositedMoney
                successLabel["text"] = "Deposited Successfully"
                successLabel["fg"] = "green"
                # release the lock
                accountsList[i].accountLock.release()
        if (accountExists == False):
            successLabel["text"] = "Account Doesn't Exist"
            successLabel["fg"] = "red"
            
        end_time = time.time()    
        elapsed_time = end_time - start_time
        print(f"Time taken: {elapsed_time:.6f} seconds")    

    root2 = Tk()
    root2.title("Deposit")
    root2.geometry("500x500")

    # resized_image = img.resize((200, 200), Image.ANTIALIAS)
    depositImage = PhotoImage(
        file="deposit.png", master=root2)
    depositImage = depositImage.subsample(x=7, y=7)

    frame = Frame(root2, borderwidth=50)

    imageLabel = Label(frame, image=depositImage)

    moneyLabel = Label(frame, text="Enter An Amount To Deposit")
    accountLabel = Label(frame, text="Enter Your Account Name")
    successLabel = Label(frame, text="")

    accountField = Entry(frame, width=30)
    moneyField = Entry(frame, width=30)

    submitButton = Button(frame, command=func, text="Deposit", width=6,
                          height=1, font="2", bg="blue", fg="white")

    # the order of elements depends on the pack() order
    frame.pack()
    frame.place(relx=.5, rely=.5, anchor=CENTER)
    imageLabel.pack()
    accountLabel.pack()
    accountField.pack()
    moneyLabel.pack()
    moneyField.pack()
    submitButton.pack()
    submitButton.place(relx=.5, rely=1.1, anchor=CENTER)
    successLabel.pack()
    root2.mainloop()


def withdrawal():

    def func():
        accountName = accountField.get()
        accountExists = False
        for i in range(len(accountsList)):
            if (accountName == accountsList[i].accountName):
                # account exists
                accountExists = True
                withdrawMoney = int(moneyField.get())
                if (accountsList[i].balance - withdrawMoney >= 0):
                    # acquire the lock
                    if accountsList[i].accountLock.locked():
                        print(
                            "Cannot Withdraw Now Another Thread Currently Has The Lock")

                    accountsList[i].accountLock.acquire()
                    accountsList[i].balance -= withdrawMoney
                    successLabel["text"] = "Withdrawed Successfully"
                    successLabel["fg"] = "green"
                    # release the lock
                    accountsList[i].accountLock.release()
                else:
                    successLabel["text"] = "You Don't Have Enough Cash To Withdraw"
                    successLabel["fg"] = "red"
        if (accountExists == False):
            successLabel["text"] = "Account Doesn't Exist"
            successLabel["fg"] = "red"

    root3 = Tk()
    root3.title("Withdraw")
    root3.geometry("500x500")

    # resized_image = img.resize((200, 200), Image.ANTIALIAS)
    withdrawImage = PhotoImage(
        file="withdrawal.png", master=root3)
    withdrawImage = withdrawImage.subsample(x=8, y=8)

    frame = Frame(root3, borderwidth=50)

    imageLabel = Label(frame, image=withdrawImage)

    moneyLabel = Label(frame, text="Enter An Amount To Withdraw")
    accountLabel = Label(frame, text="Enter Your Account Name")
    successLabel = Label(frame, text="")

    accountField = Entry(frame, width=30)
    moneyField = Entry(frame, width=30)

    submitButton = Button(frame, command=func, text="Withdraw", width=8,
                          height=1, font="2", bg="blue", fg="white")

    # the order of elements depends on the pack() order
    frame.pack()
    frame.place(relx=.5, rely=.5, anchor=CENTER)
    imageLabel.pack()
    accountLabel.pack()
    accountField.pack()
    moneyLabel.pack()
    moneyField.pack()
    submitButton.pack()
    submitButton.place(relx=.5, rely=1.1, anchor=CENTER)
    successLabel.pack()
    root3.mainloop()

def balance():
    def func():
        accountName = accountField.get()
        accountExists = False
        for i in range(len(accountsList)):
            if (accountName == accountsList[i].accountName):
                # account exists
                # acquire the lock
                if accountsList[i].accountLock.locked():
                    print(
                        "Cannot Get Balance Now Another Thread Currently Has The Lock")
                accountsList[i].accountLock.acquire()
                accountExists = True
                successLabel["text"] = "Your Current Balance Is: " + \
                    str(accountsList[i].balance)
                successLabel["fg"] = "green"
                # release the lock
                accountsList[i].accountLock.release()
        if (accountExists == False):
            successLabel["text"] = "Account Doesn't Exist"
            successLabel["fg"] = "red"

    root3 = Tk()
    root3.title(" Balance")
    root3.geometry("500x500")

    depositImage = PhotoImage(
        file="balance.png", master=root3)
    depositImage = depositImage.subsample(x=20, y=20)

    frame = Frame(root3, borderwidth=50)

    imageLabel = Label(frame, image=depositImage)

    accountLabel = Label(frame, text="Enter Your Account Name")
    successLabel = Label(frame, text="")

    accountField = Entry(frame, width=30)

    submitButton = Button(frame, command=func, text="Check Balance", width=12,
                          height=1, font="2", bg="blue", fg="white")

    # the order of elements depends on the pack() order
    frame.pack()
    frame.place(relx=.5, rely=.5, anchor=CENTER)
    imageLabel.pack()
    accountLabel.pack()
    accountField.pack()
    submitButton.pack()
    submitButton.place(relx=.5, rely=1.1, anchor=CENTER)
    successLabel.pack()
    root3.mainloop()

def mainscreen():
    def func():
        t1 = threading.Thread(target=createAccount)
        t1.start()
    def func1():
        t2 = threading.Thread(target=deposit)
        t2.start()
    def func2():
        t3 = threading.Thread(target=withdrawal)
        t3.start()
    def func3():
        t4 = threading.Thread(target=balance)
        t4.start()

    window = Tk()

    # Set the title of the window
    window.title("Bank Account")

    # Set the size of the window
    window.geometry("500x500")

    # Create a label for the window
    label = Label(text="Welcome to Bank Account", font=("Arial", 18))
    label.pack(pady=20)

    # Create the buttons
    button1 = Button(text="Create Account",height=2, font="2",padx=10,pady=10,command=func)
    button1.pack(pady=10)

    button2 = Button(text="Deposit", width=12,height=2, font="2",padx=10,pady=10,command=func1)
    button2.pack(pady=10)

    button3 = Button(text="Withdraw", width=12,height=2, font="2",padx=10,pady=10,command=func2)
    button3.pack(pady=10)

    button4 = Button(text="Check Balance", width=12, height=2, font="2",padx=10,pady=10,command=func3)
    button4.pack(pady=10)

    # Run the main loop
    window.mainloop()

t = threading.Thread(target=mainscreen)
t.start()