from customtkinter import *
from PIL import Image
from tkinter import PhotoImage
import itertools
from PIL import Image, ImageTk
from tkinter import messagebox

def hesapla():
    try:
        kilo = float(entry1.get())
        boy = float(entry2.get())        
        if kilo <= 0 or boy <= 0:
            messagebox.showerror("Hata", "Kilo ve boy değerleri sıfırdan büyük olmalıdır!")
            return
        bmi = kilo / (boy ** 2)
        if bmi < 18.5:
            sonuc = f"BMI: {bmi:.2f} - Zayıf"
        elif 18.5 <= bmi < 24.9:
            sonuc = f"BMI: {bmi:.2f} - Normal"
        elif 25 <= bmi < 29.9:
            sonuc = f"BMI: {bmi:.2f} - Fazla kilolu"
        else:
            sonuc = f"BMI: {bmi:.2f} - Obez"
        messagebox.showinfo("Sonuç", sonuc)
    except ValueError:
        # Eğer giriş geçerli bir sayı değilse hata mesajı göster
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı giriniz!")
app=CTk()
app.title("Vücut Kitle İndeksi için GUI")
app.geometry("600x700")
app.resizable(0,0) # kullancının tam ekran yapmasını engelledim.
canvas = CTkCanvas(master=app, width=600, height=700)
canvas.grid(row=0, column=0)
label=CTkLabel(master=app, text="Vücut Kitle İndeks Hesaplayıcı", width=200, height=40, bg_color="white", text_color="black",font=("ariel", 20,"bold"))
label.place(relx=0.5, rely=0.2, anchor="center")
background_image = PhotoImage(file="/Users/aliemirsertbas/Desktop/VSCO1prjct/CustomTKprjct.py/bg2.png")  # Resim dosyanızın yolunu burada belirtin
canvas.create_image(0, 0, image=background_image, anchor="nw")
entry1=CTkEntry(master= app,border_width=5,border_color="#FE6100", placeholder_text="lütfen kilonuzu giriniz(kg)", width=200,height=40,bg_color="white",fg_color="white", text_color="black")
entry1.place(relx=0.5, rely=0.5, anchor="center")
entry2=CTkEntry(master=app, border_width=5,border_color="#FE6100", placeholder_text="lütfen boyunuzu giriniz(m)", width=200,height=40,bg_color="white",fg_color="white", text_color="black")
entry2.place(relx=0.5, rely=0.4, anchor="center")
btn=CTkButton(master=app, text="BMI hesapla", hover_color="#FE6100",
              corner_radius=32,
               border_width=2,
              bg_color="white",
               command=hesapla)
btn.place(relx=0.5, rely=0.6, anchor="center", )
app.mainloop()



