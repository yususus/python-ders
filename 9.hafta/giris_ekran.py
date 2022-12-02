# giriş yaptıktan sonra doğru ise o ekranı kapatıp
# başka pencere açan uygulama
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
#window name
root.title("giriş ekranı")
#window size and location
root.geometry("300x300+540+300")



isim_var = tk.StringVar()
sifre_var =tk.StringVar()


def submit():
    if isim_var.get() == "yusuf" and sifre_var.get() == "aydin":
        tk.messagebox.showinfo(
            "Tebrikler Doğru")
        root.destroy()
#only closes if true
    else:
        tk.messagebox.showerror(
            title="yanlış", message="tekrar dene")





name_label = tk.Label(root, text="Kullanici adi")
name_entry = tk.Entry(root, textvariable=isim_var)

password_label = tk.Label(root, text="Sifre")
password_entry = tk.Entry(root, textvariable=sifre_var, show="*")

sub_buton = tk.Button(root, text="Giris", command=submit)


name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)

sub_buton.grid(row=2,column=1)


root.mainloop()