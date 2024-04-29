#main page

import tkinter as tk
import tkinter.messagebox as mb

#아니면 그냥 from tkinter as tk로 쓰면 tkinter에 있는 모든 클래스와 메소드에 접근 가능

class NewWindow(tk.Toplevel):
    def __init__(self, master, msg):
        super().__init__(master=master)
        self.title("Confirmation Window")
        self.geometry("300x200")
        label = tk.Label(self, text=msg, fg = '#ffc107',
                         font="Arial 14 bold", bg='#607b8d')
        x = master.winfo_x()
        y = master.winfo_y()
        self.geometry("+%d+%d" % (x + 300, y))
        self.configure(bg='#607b8d')
        self.resizable(False, False)
        label.place(relx=0.5, rely=0.5, anchor="center")
        
        #새로운 창에서 아래 리스트바 보임
        cities = ['Seoul', 'Busan', 'Daegu', 'Incheon', 'Gwangju', 'Daejeon', 'Ulsan', 'Jeju']
        listVar = tk.StringVar(value=cities)
        citiesList = tk.Listbox(root, listvariable=listVar, selectmode='single', font="Arial 14 bold")
        citiesList.pack(fill=tk.BOTH, expand=True, padx=20, pady=40)


root = tk.Tk()
root.geometry("400x400")
root.title("GUIUniApp")
root.configure(bg="#607b8d")
root.resizable(False, False)


# For making label
# label = tk.Label(root, text="Welcome to GUIUniApp",
#                  padx = 20, pady = 20,
#                  bg="pink",
#                  font= "Arial 14 bold"
#                  )

# label.place(relx=0.5, rely=0.5, anchor="center")

#For making box 
box = tk.LabelFrame(root, text="Info Messeage",
                    bg='#607b8d', fg='white', padx=20,  pady=20, font="Arial 14 bold")

box.columnconfigure(0, weight=1)
box.columnconfigure(1, weight=3)
box.place(relx=0.5, rely=0.5, anchor="center")

emailLbl = tk.Label(box, text="Email:", justify='left', fg='#ffc107', 
                    font="Arial 14 bold", bg='#607b8d')
emailLbl.grid(column=0, row=0,padx=5, pady=5, sticky=tk.W)

passwordLbl = tk.Label(box, text="Password:", justify='left', fg='#ffc107',
                       font="Arial 14 bold", bg='#607b8d')
passwordLbl.grid(column=0, row=1,padx=5, pady=5, sticky=tk.W)

emailText = tk.StringVar()
emailField = tk.Entry(box, textvariable=emailText, font="Arial 14 bold")    
emailField.grid(column=1, row=0, padx=5, pady=5)
emailField.focus()

passwordTxt = tk.StringVar()
passwordField = tk.Entry(box, textvariable=passwordTxt, font="Arial 14 bold", show='*') 
passwordField.grid(column=1, row=1, padx=5, pady=5)

cancelBtn = tk.Button(box, text="Cancel") 
cancelBtn.grid(column=1, row=3, padx=5, pady=5, sticky=tk.W)


def clear():
    emailField.delete(0, tk.END)
    passwordField.delete(0, tk.END)
        
def login():
    if(emailText.get() == "zzz" and passwordTxt.get() == "111"):
        info = "Login Successful"
        mb.showinfo(title="Login Confirmation", message=info)
        NewWindow(root, info)
        clear()
    else:
        info = "Incorrect email or password"
        mb.showerror(title="Login Error", message=info)
        clear()

loginBtn = tk.Button(box, text="Login", command = login)
loginBtn.grid(column=1, row=3, padx=5, pady=5, sticky=tk.E)

#For making message box 
# message = tk.Message(box, text="TKinter is the name Tkinter comes from Tk interface...",                    
#                     fg='#ffc107', font="Arial 12 bold",
#                     aspect=300, justify='left',bg='#607b8d')

# message.pack(pady=10, padx=10)
                    
root.mainloop()
