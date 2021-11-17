# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 12:37:02 2021

@author: galih-hermawan
Github: https://github.com/galihboy/
Web: http://galih.eu
"""

import random
daftarNama = ("andi", "budi", "gunawan", "tanto", "rudi", "yanto", "sugeng")

nama = random.choice(daftarNama)
print(f"nama: {nama}")

lstNama = random.choices(daftarNama, k=3)
print(f"nama (list): {lstNama}")

jmlNama = 3
lstNama = random.sample(daftarNama, jmlNama)
print(f"nama (list): {lstNama}")     

# gabung isi list dalam sebuah string
nama_lengkap = " ".join(lstNama)
nama_lengkap = nama_lengkap.title() # huruf kapital di setiap awal kata
print(f"nama lengkap: {nama_lengkap}")