from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Uygulama")
win.geometry("500x500")


def hesapla():

    if v.get() == 1:

        if x.get() == 1:

            yenifiyat = int(kullanıcı.get()) * 1 / 100 + int(kullanıcı.get())

            messagebox.showinfo("Sonuç", yenifiyat)

        elif x.get() == 2:

            yenifiyat = int(kullanıcı.get()) * 10 / 100 + int(kullanıcı.get())

            messagebox.showinfo("Sonuç", yenifiyat)

        elif x.get() == 3:

            yenifiyat = int(kullanıcı.get()) * 20 / 100 + int(kullanıcı.get())

            messagebox.showinfo("Sonuç", yenifiyat)

    elif v.get() == 2:

        if x.get() == 1:

            yenifiyat = int(kullanıcı.get()) - int(kullanıcı.get()) * 1 / 100

            messagebox.showinfo("Sonuç", yenifiyat)

        elif x.get() == 2:

            yenifiyat = int(kullanıcı.get()) - int(kullanıcı.get()) * 10 / 100

            messagebox.showinfo("Sonuç", yenifiyat)

        elif x.get() == 3:

            yenifiyat = int(kullanıcı.get()) - int(kullanıcı.get()) * 20 / 100

            messagebox.showinfo("Sonuç", yenifiyat)
baslikLabel = Label(win, text="KDV HESAPLAMA")
kullanıcı = Entry(win)
v = IntVar()
x = IntVar()
kdvDahil = Radiobutton(win, text="KDV Dahil", variable=v, value=1)
kdvDahilDegil = Radiobutton(win, text="KDV Dahil Degil", variable=v, value=2)
yüzde1 = Radiobutton(win, text="1", variable=x, value=1)
yüzde10 = Radiobutton(win, text="10", variable=x, value=2)
yüzde20 = Radiobutton(win, text="20", variable=x, value=3)
hesaplaButton = Button(win, text="Hesapla", command=hesapla)
baslikLabel.place(x=190, y=0)
kullanıcı.place(x=0, y=50)
kdvDahil.place(x=0, y=100)
kdvDahilDegil.place(x=0, y=140)
yüzde1.place(x=250, y=50)
yüzde10.place(x=250, y=100)
yüzde20.place(x=250, y=150)
hesaplaButton.place(x=250, y=250)

win.mainloop()