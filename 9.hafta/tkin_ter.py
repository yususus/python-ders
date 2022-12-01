from tkinter import *

window=Tk()
window.geometry("600x400")

#window geometry ile pencere boyutu ayarlanıyor

window.title("merhaba guı")
lbl = Label(window, text="merhaba")
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="Merhaba2")
lbl2.grid(column=1, row=0)


btn = Button(window, text="tıkla")
btn.grid(column=1, row=1)

btn2 = Button(window, text="renkli tıklama",
              bg="aqua", fg="blue",
              width=10, height=10)
btn2.grid(column=1, row=3)





window.mainloop()