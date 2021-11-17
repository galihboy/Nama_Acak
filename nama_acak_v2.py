# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 12:52:15 2021

@author: galih-hermawan
"""

import random

# fungsi untuk membangkitkan nama acak
def BangkitNama(daftar, jumlah, paksaGabung = False):
    while True:
        # ambil nama acak sebanyak jumlah
        nama = random.sample(daftar, jumlah)
        # mencari list nama anti sendiri
        lstAntiSendiri = [i for i,n in enumerate(nama) if n in namaAntiSendiri]
        # jika nama anti sendiri ditemukan
        if lstAntiSendiri:
            # indeks nama anti sendiri
            idxAntiSendiri = lstAntiSendiri[0]
            # jika posisi nama anti sendiri di nama paling belakang
            if idxAntiSendiri == jumlah-1:
                #print("abdul di indeks terakhir")
                pass
            # jika nama abdul ada di depan, nama belakang diganti nama asmaul husna
            else:
                namaAsmaulHusna = random.choice(daftarAsmaulHusna)
                # jika nama asmaul husna dapat digabung dengan abdul
                # dan pilihan paksa gabung : True
                karCari = CariKarakter(namaAsmaulHusna)
                if paksaGabung and karCari != "":
                    nama[idxAntiSendiri] = "abdu" + karCari + namaAsmaulHusna
                    while True:
                        namaPengganti = BangkitNama(daftar, 1)[0]
                        # cari nama pengganti yang belum ada di list nama
                        if namaPengganti not in nama:
                            nama[idxAntiSendiri+1] = namaPengganti
                            break
                else:
                    nama[idxAntiSendiri+1] = namaAsmaulHusna
                break
        else:
            break
            
    return nama

# fungsi untuk memeriksa karakter/string awal nama asmaul husna
def CariKarakter(nama):
    for i in range(2,0,-1):
        try:
            cek = nama[0:i]
            karGabung.index(cek)
        except ValueError:
            hasil = ""
        else:
            hasil = cek
            break
    return hasil
        
    
daftarNama = ("andi", "budi", "gunawan", "tanto", "rudi", "yanto", "sugeng")
daftarNama2 = ("muhammad", "abdul", "zulkarnain", "rahman", "rahim", "umar")
daftarNama3 = ("muhammad", "abdul", "zulkarnain", "umar", "ali", "saifullah")
daftarAsmaulHusna = ("aziz", "jabbar", "karim", "majid", 
                     "rafi\'", "rahim", "rahman",
                     "salam", "sami\'", "shabur", "shamad", "syakur")

namaAntiSendiri = ("abdul")
karGabung = ("dh", "n", "r", "s", "sh", "sy", "t", "z")

#nama = random.choice(daftarNama2)
#lstNama = random.choices(daftarNama2)

#jmlNama = 3
#banyakNama = random.sample(daftarNama2, jmlNama)

#namaAbdul = "abdul " + random.choice(daftarAsmaulHusna)
#lstNamaAbdul = namaAbdul.split()

# print(f"1 nama: {nama}")
# print(f"1 nama (list): {lstNama}")
# print(f"{jmlNama} nama (list): {banyakNama}")     
# print("\n---------")

# print(f"Nama abdul: {namaAbdul}")
# print(f"Nama abdul (list): {lstNamaAbdul}")

#namaBaru = BangkitNama(daftarNama3, 1)
#print(f"1 nama baru: {namaBaru}")

#namaBaru2 = BangkitNama(daftarNama3, 2)
#print(f"2 nama baru: {namaBaru2}")

#namaBaru3 = BangkitNama(daftarNama3, 3)
#print(f"3 nama baru: {namaBaru3}")

banyakNama = 3 # jumlah kata (nama) dalam satu string (kalimat)

lstNamaBaru3 = BangkitNama(daftarNama3, banyakNama)
strNama3 = " ".join(lstNamaBaru3).title()
print(f"3 nama baru: {strNama3}")

lstNamaBaru3 = BangkitNama(daftarNama3, banyakNama, True)
strNama3 = " ".join(lstNamaBaru3).title()
print(f"3 nama baru (gabung): {strNama3}")