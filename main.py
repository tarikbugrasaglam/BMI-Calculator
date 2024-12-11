from importlib.metadata import pass_none
from tkinter import *

#window
window=Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=200)
window.config(padx=20,pady=20)

#boy_label
boy_label=Label(text="Boyunuzu giriniz(cm)", font=('times new roman ', 10, "normal"))
boy_label.pack()

#boy_entry
boy_entry=Entry(width=20)
boy_entry.focus()
boy_entry.pack()

#kilo_label
kilo_label=Label(text="Kilonuzu giriniz(kg)", font=('times new roman ', 10, "normal"))
kilo_label.pack()

#kilo_entry
kilo_entry=Entry(width=20)
kilo_entry.pack()


def calculator():
    try:
        boy_input=float(boy_entry.get())/100
        kilo_input=float(kilo_entry.get())

        hesap_sonucu=(kilo_input/boy_input**2)
        if hesap_sonucu>=40:
            sonuc_label.config(text=f"BMI={hesap_sonucu},Morbid Obez(3.derece obezite)")
        elif hesap_sonucu>35.0:
            sonuc_label.config(text=f"BMI={hesap_sonucu},Aşırı Obez(2.derece obezite)")
        elif hesap_sonucu>30.0:
            sonuc_label.config(text=f"BMI={hesap_sonucu},Obez(1.derece obezite)")
        elif hesap_sonucu>25.0:
            sonuc_label.config(text=f"BMI={hesap_sonucu},Fazla kilolu")
        elif hesap_sonucu>18.5:
            sonuc_label.config(text=f"BMI={hesap_sonucu},Normal kilolu")
        else:
            sonuc_label.config(text=f"BMI={hesap_sonucu},Zayıf")


    except ValueError:
        sonuc_label.config(text="Lutfen sadece sayi giriniz.")
    except ZeroDivisionError:
        sonuc_label.config(text="Boy sıfır olamaz.Tekrar giriniz lütfen.")


#calculate_button
calculate_button=Button(window,text="Hesapla",command=calculator)
calculate_button.pack(pady=10)

#sonuc_label
sonuc_label=Label(window,text="",font=('times new roman ', 12, "normal"))
sonuc_label.pack(pady=10)


window.mainloop()