#!/usr/bin/env python
# coding: utf-8

# ### QT interval hesaplama  Nedir:
# -------------------------------------
# 
# * QT aralığı, kalbin elektriksel aktivitesinin süresini temsil eden elektrokardiyogram (EKG) üzerinde bir zaman ölçüsüdür. Özellikle Q dalgasının başlangıcından T dalgasının sonuna kadar olan süreyi ifade eder. Bu, kalbin elektriksel işleyişini değerlendirmek için temel bir parametredir. QT aralığının hesaplanması, potansiyel kalp anormalliklerini değerlendirmede yardımcı olur ve bireyin kalp hızına dayalı düzeltme formülleri kullanılarak ayarlanabilir.

# ### Geleneksel kod

# In[ ]:


try:
   
    baslangic = float(input("baslangic degerini girin: "))
    bitis = float(input("Bitis degerini girin: "))
   
    interval = abs(bitis - baslangic)
    print("Interval:", interval)

except ValueError:
    print("Hata: Gecersiz bir deger girdiniz.")


# ### Fonksyonlu kod

# In[ ]:


def interval_hesaplama(baslangic,bitis):
    return abs(bitis-baslangic)

try:
    
    baslangic = float(input("baslangic degerini girin: "))
    bitis = float(input("Bitis degerini girin: "))
   
    interval = interval_hesaplama(baslangic,bitis)
    print("Interval:", interval)

except ValueError:
    print("Hata: Gecersiz bir deger girdiniz.")


# ### Tkinter kod

# In[6]:


import tkinter as tk
from tkinter import messagebox

def interval_hesaplama():
    try:
        baslangic = float(entry_baslangic.get())
        bitis = float(entry_bitis.get())
        interval = abs(bitis - baslangic)
        result_label.config(text=f"Interval: {interval}")
    except ValueError:
        messagebox.showerror("Hata: Geçersiz bir değer girdiniz.")

# Tkinter penceresi:
root = tk.Tk()
root.title("Interval Hesaplama Programı")

# Giris alanlari ve etiketleri:
label_baslangic = tk.Label(root, text="Başlangıç Değeri:")
label_baslangic.grid(row=0, column=0, padx=10, pady=10)

entry_baslangic = tk.Entry(root, width=10)
entry_baslangic.grid(row=0, column=1, padx=10, pady=10)

label_bitis = tk.Label(root, text="Bitiş Değeri:")
label_bitis.grid(row=1, column=0, padx=10, pady=10)

entry_bitis = tk.Entry(root, width=10)
entry_bitis.grid(row=1, column=1, padx=10, pady=10)

# Hesapla butonu
calculate_button = tk.Button(root, text="Hesapla", command=interval_hesaplama)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Sonuc etiketi
result_label = tk.Label(root, text="Interval: ")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Pencereyi calistir
root.mainloop()


# In[ ]:




