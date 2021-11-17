# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:29:29 2021

@author: galih-hermawan
"""

import random

def BangkitNama(daftar, jumlah, lBlackList, paksaGabung = False):
    #print("lBlackist Bangkit: ", lBlackList)
    while True:
        # ambil nama acak sebanyak jumlah
        nama = random.sample(daftar, jumlah)
        #print("\nnama awal: ", nama)
        # mencari list nama anti sendiri
        lstAntiSendiri = [i for i,n in enumerate(nama) if n in namaAntiSendiri]
        #print("nama anti sendiri: ", lstAntiSendiri )
        # jika nama anti sendiri ditemukan
        if lstAntiSendiri:
            # indeks nama anti sendiri
            idxAntiSendiri = lstAntiSendiri[0]
            #print("Ada abdul di indeks ", idxAntiSendiri)
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
                        namaPengganti = BangkitNama(daftar, 1, lBlackList, True)[0]
                        # cari nama pengganti yang belum ada di list nama
                        if namaPengganti not in nama:
                            nama[idxAntiSendiri+1] = namaPengganti
                            break
                else:
                    nama[idxAntiSendiri+1] = namaAsmaulHusna
                break
        else:
            #print(nama, " blokir? ", CariNamaTerblokir(nama, lBlackList))
            if not CariNamaTerblokir(nama, lBlackList):
                break
            
    return nama

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

def CariNamaTerblokir(listNama, lBlackList):
    #print("lBlacklist: ", lBlackList)
    lstHasil = [i for i in listNama for j in lBlackList if i==j]
    return lstHasil
    
def ListKataAcak(namaAcak):
    lstIdxAcak = []
    for i, nama in enumerate(lstFormat):
        if nama == namaAcak:
            lstIdxAcak.append(i)
    
    #print("lstIdxAcak: ", lstIdxAcak)
    
    lstIdxAcakJarak = []
    lstAcak = []
    if len(lstIdxAcak) > 1:
        for i in range(len(lstIdxAcak)):

            if i != len(lstIdxAcak)-1:
                lstIdxAcakJarak.append([lstIdxAcak[i], lstIdxAcak[i+1]-lstIdxAcak[i]])
            else:
                lstIdxAcakJarak.append([lstIdxAcak[i], 1])
            # lstIdxAcakJarak = [indeks, jarak]    
    else:
        return [[lstIdxAcak[0], 1]]
    
    totJ = 0           
    
    while len(lstIdxAcakJarak) != 0 :        
        ukuranLstAcak = len(lstAcak)
        s = lstIdxAcakJarak[0]
        idx = s[0]
        j = s[1]

        if j>1:

            if ukuranLstAcak == 0:
                lstAcak.append([idx, 1])
            else:

                totJ += 1 
                lstAcak[ukuranLstAcak-1][1]= totJ
                totJ = 0
        elif j==1:
            totJ += 1
            if totJ <= 1:
                lstAcak.append([idx, totJ])
            else:
                if ukuranLstAcak == 1: totJ += 1
                lstAcak[ukuranLstAcak-1][1]= totJ

        lstIdxAcakJarak.remove([idx, j])  
    return lstAcak

def ListKataAcakBaru(lstSumberFormat):
    lstX = [i for i, st in enumerate(lstSumberFormat) if st == namaRandom]

    # mendeteksi x dan jarak dengan x berikutnya
    lstXTemp = lstX.copy()
    lstXInfo = []
    start = 0
    
    while len(lstXTemp) != 0:
        currData = lstXTemp[start]
        
        if currData == lstX[-1]:
            jarak = 0
        else:
            jarak = lstXTemp[start+1]-lstXTemp[start]
        
        lstXInfo.append([currData, jarak])
        lstXTemp.remove(currData)
        start=0
            
    #print("lst X info: ", lstXInfo)
    
    # menentukan no indeks x start, dan jumlah x berikutnya yang terdekat
    lstJarak = []
    cJarak = 0
    for i, data in enumerate(lstXInfo):
        #print("\ncJarak: ", cJarak)
        idx = data[0]
        jarak = data[1]
        if i == 0:
            lstJarak.append([idx, 1])
        else:
            jarakSebelum = lstXInfo[i-1][1]
            if jarakSebelum == 1:
                lstJarak[cJarak][1] += 1
            else:
                lstJarak.append([idx, 1])
                cJarak += 1
    return lstJarak

# -----------------------------------------------------

daftarNama1 = ("andi", "budi", "gunawan", "sutanto", "rudi", "asep", "sugeng")
daftarNama2 = ("muhammad", "abdullah", "abdul", "zulkarnain", "umar", "ali", "saifullah")
daftarAsmaulHusna = ("aziz", "jabbar", "karim", "majid", 
                     "rafi\'", "rahim", "rahman",
                     "salam", "sami\'", "shabur", "shamad", "syakur")
daftarNamaNabi = ("yusuf", "sulaiman", "ayub", "ibrahim", "yahya", "ismail")
namaAntiSendiri = ("abdul")
karGabung = ("dh", "r", "s", "sh", "sy", "t", "z")


#daftarNamaBaru = daftarNama1 + daftarNama2 + daftarNamaNabi
daftarNamaBaru = daftarNama2
#daftarNamaBaru = daftarNamaNabi

#blackListNama = ["ayub", "ismail"]
#namaBaru3 = BangkitNama(daftarNama3, 3)
#print(f"3 nama baru: {namaBaru3}")

namaRandom = "x"
#format = "x x muhammad x x"
#format = "x"
#format = "x tes x x x"
#format = "tes x"
format = "tes x x"
#format = "x x tes x x jambu duku x"
lstFormat = format.split()
blackListNama = [nama for nama in lstFormat if nama != namaRandom]
jmlWhiteList = len(lstFormat) - len(blackListNama)

# cek : muhammad abdul adrian karim
#namaBaru3b = BangkitNama(daftarNamaBaru, jmlWhiteList, True)
#print(f"Nama baru (gabung): {namaBaru3b}")
#lstAcak = ListKataAcak(namaRandom)
lstAcakBaru = ListKataAcakBaru(lstFormat)
#nLstAcak = len(lstAcak)

#print(lstAcakBaru)

l = []

for x in lstAcakBaru:
    #print("Blacklist lama: ", blackListNama)
    jml = x[1]
    luaran = BangkitNama(daftarNamaBaru, jml, blackListNama, True)
    #print("luaran: ", luaran)
    blackListNama += luaran
    #print("Blacklist baru: ", blackListNama)
    l.append(luaran)
    #print(luaran)

# 2D list ke 1D
listNamaAcak = []
for nama in l:
    listNamaAcak.extend(nama)

j = 0
u = len(listNamaAcak)
lOutput = []
for i in range(len(lstFormat)):
    if lstFormat[i] == namaRandom:
        lOutput.append(listNamaAcak[j])
        j += 1
    else:
        lOutput.append(lstFormat[i])

print("nama 1 : ", " ".join(lOutput))
print("\n----------")


        
