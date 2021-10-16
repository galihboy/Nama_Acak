# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 22:54:45 2021

@author: galih-hermawan
Github: https://github.com/galihboy/
Web: http://galih.eu

Modul untuk pemrosesan pembangkitan nama acak

"""

import random
from libBerkas import BacaBerkas

# fungsi untuk mencari karakter yang dapat digabung -> lookup var "karGabung"
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

# explorasi & inventarisir indeks nama acak dan jumlahnya
def ListKataAcak(lstSumberFormat, namaRandom):
    lstX = [i for i, st in enumerate(lstSumberFormat) if st == namaRandom]

    # mendeteksi x dan jarak dengan x berikutnya
    lstXTemp = lstX.copy()
    lstXInfo = []
    
    while len(lstXTemp) != 0:
        currData = lstXTemp[0]
        
        if currData == lstX[-1]:
            jarak = 0
        else:
            jarak = lstXTemp[1]-lstXTemp[0]
        
        lstXInfo.append([currData, jarak])
        lstXTemp.remove(currData)
    #print(lstXInfo)
    '''
    contoh:
        strFormat = "ABDUL x x Hermawan"
        output = [[1, 1], [2, 0]]
        makna = x pertama ada di indeks ke-1, jarak dengan x berikutnya 1
                x kedua ada di indeks ke-2, jarak dengan x berikutnya 0 (alias tidak ada)
    '''
                
    # menentukan no indeks x start, dan jumlah x berikutnya yang terdekat
    lstJarak = []
    cJarak = 0
    for i, data in enumerate(lstXInfo):
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
    
    #print(lstJarak)
    '''
    contoh:
        strFormat = "ABDUL x x Hermawan"
        output sebelumnya di lstXInfo = [[1, 1], [2, 0]]
        output lstJarak = [[1, 2]]
        makna = indeks ke-1 s/d 2 (dua nama) adalah sekelompok, supaya dapat menghasilkan
                2 nama acak yang berdampingan
    '''
    return lstJarak

# fungsi untuk mengambil nama secara acak dari sumber sebanyak jml (jumlah yang ditetapkan)
def AcakNama(sumber, jml):
    oNama = random.sample(sumber, jml)
    return oNama
    
# fungsi untuk memeriksa apakah daftar nama hasil pengacakan ada di daftar blokir
# luaran berupa list
def CekTerblokir(sumberAcak, lstBlokir):
    lstHasil = [i for i in sumberAcak for j in lstBlokir if i == j]
    
    return lstHasil

# fungsi untuk mengembalikan nama sebanyak jml (jumlah) dari sumber data
# dan mencocokkan dengan data di list nama yang diblokir
def AmbilNama(sumber, lstBlokir, jml):
    sumberBaru = sumber.copy()
    while True:
        # jika data sumber lebih dari satu dilakukan pengambilan acak
        if len(sumberBaru) > 1:
            sumberAcak = AcakNama(sumberBaru, jml)
            bTerblokir = CekTerblokir(sumberAcak, lstBlokir)
            if len(bTerblokir) > 0:
                for s in bTerblokir:
                    sumberBaru.remove(s)
            else:
                # tidak ada yang terblokir
                for s in sumberAcak:
                    sumberBaru.remove(s)
                return sumberAcak
        # jika data sumber tinggal satu, langsung dikeluarkan
        else:
            return sumberBaru

# fungsi untuk mencetak nama dengan mencocokkan daftar nama hasil pengacakan
# dan posisi indeks nama acak di format masukan
def CetakNama(sumber, strFormat, charAcak):
    strFormat = strFormat.lower()
    lstFormat = strFormat.split()

    lstBlokir = [i for i in lstFormat if i != charAcak]
    lstAcak = ListKataAcak(lstFormat, charAcak)
    
    # looping x sesuai nomor indeks dan jumlahnya
    lstBlokirBaru = lstBlokir.copy()
    lstNamaBaru = []
    for i in lstAcak:
        jml = i[1]
        lstNama = AmbilNama(sumber, lstBlokirBaru, jml)
        lstBlokirBaru += lstNama
        lstNamaBaru += lstNama    
    
    j = 0
    lOutput = []
    ukuranNamaBaru = len(lstNamaBaru)
    
    # mengeluarkan string nama sesuai urutan indeks
    for i in range(len(lstFormat)):
        if lstFormat[i] == charAcak:
            if j < ukuranNamaBaru:
                lOutput.append(lstNamaBaru[j])
                j += 1
            else:
                lOutput.append("-")
        else:
            lOutput.append(lstFormat[i])
    
    strNama = " ".join(lOutput) 
    return strNama

# penanganan nama yang mengandung ABDUL
# gabungAbdul: True (pemaksaan penggabungan nama abdul dengan nama asmaul husna jika memungkinkan)
#               False (tidak dilakukan penggabungan)
# output: string nama
def ValidasiAbdul(sumber, nama, strFormat, charAcak, gabungAbdul = False):
    strFormat = strFormat.lower()
    lstFormat = strFormat.split()
    lstNamaMasukan = nama.split()

    # daftar blokir awal
    lstBlokir = [i for i in lstFormat if i != charAcak]    
    # daftar (posisi) indeks nama "abdul"
    idxAbdul = [i for i, data in enumerate(lstNamaMasukan) if data.lower() == "abdul"]    
    # jika abdul tidak ditemukan, keluarkan nama semula
    if not idxAbdul: return nama.title()
    
    # abdul di posisi terakhir - ganti dengan nama lain
    if idxAbdul[0] == len(lstNamaMasukan)-1:
        lstBlokirBaru = lstNamaMasukan.copy()
        namaPengganti = AmbilNama(sumber, lstBlokirBaru, 1)[0]
        lstNamaMasukan[idxAbdul[0]] = namaPengganti
        lOutput = lstNamaMasukan
    else:
        # cek apa sebelah kanan abdul ada di daftar blokir
        nextAbdul = idxAbdul[0]+1 
        if lstNamaMasukan[nextAbdul] in lstBlokir:
            # jika ya, ganti dengan nama lain
            lstBlokirBaru = lstNamaMasukan.copy()
            namaPengganti = AmbilNama(sumber, lstBlokirBaru, 1)[0]
            lstNamaMasukan[idxAbdul[0]] = namaPengganti
            lOutput = lstNamaMasukan
        else:
            # jika tidak diblokir, isi dengan nama asmaul husna
            lstBlokirBaru = lstNamaMasukan.copy()
            namaAsmaulHusna = AmbilNama(daftarAsmaulHusna, lstBlokirBaru, 1)[0]
            if gabungAbdul:
                # jika nama asmaul husna dapat digabung dengan abdul
                # dan pilihan gabungAbdul : True
                karCari = CariKarakter(namaAsmaulHusna)
                if karCari != "":
                    lstNamaMasukan[idxAbdul[0]] = "abdu" + karCari + namaAsmaulHusna
                else:
                    lstNamaMasukan[nextAbdul] = namaAsmaulHusna
            else:
                lstNamaMasukan[nextAbdul] = namaAsmaulHusna
            lOutput = lstNamaMasukan
            
        strOutput = " ".join(lOutput)
        return strOutput.title()

#-----------------------------------

# nama file nama
namaFileAsmaulHusna = "nama_asmaul_husna.txt"
namaFileLaki = "nama_laki.txt"
namaFileNabi = "nama_nabi.txt"
namaFileSahabat = "nama_sahabat_nabi.txt"
namaFileIslam = "nama_islam.txt"

# huruf awal nama asmaul husna yang dapat digabung dengan nama: abdul
karGabung = ("dh", "n", "r", "s", "sh", "sy", "t", "z")

# daftar nama dari file
daftarAsmaulHusna = BacaBerkas(namaFileAsmaulHusna)
daftarNamaLaki = BacaBerkas(namaFileLaki)
daftarNamaNabi = BacaBerkas(namaFileNabi)
daftarNamaSahabat = BacaBerkas(namaFileSahabat)
daftarNamaIslam =  BacaBerkas(namaFileIslam)


if __name__ == "__main__" :
    # print(daftarAsmaulHusna)
    # print(daftarNamaLaki)
    # print(daftarNamaNabi)
    # print(daftarNamaSahabat)
    # print(daftarNamaIslam)
    
    # contoh penetapan dari satu sumber data
    #sumber = daftarNamaLaki
    #sumber = daftarNamaIslam
    
    # contoh sumber data gabungan
    #sumber = daftarNamaNabi + daftarNamaIslam
    sumber = daftarNamaLaki + daftarNamaSahabat + daftarNamaIslam
    
    # karakter (string) yang jadi simbol nama acak
    charAcak = "x" 
    # selain kata yang terdapat dalam charAcak (misal: X), dianggap nama permanen
    #strFormat = "ABDUL x x x Hermawan"
    #strFormat = "x tes x x x"
    #strFormat = "x ABDULLAH x x CAHYONO"
    strFormat = "x x abdul x"

    jmlNama = 50
    print(f"Contoh {jmlNama} nama acak.")
    print("-------------------------------")
    for i in range(jmlNama):
        nama = CetakNama(sumber, strFormat, charAcak)
        #print("\nNama awal: ", nama)
        #namaBaru = ValidasiAbdul(sumber, nama, strFormat, charAcak)
        namaBaru = ValidasiAbdul(sumber, nama, strFormat, charAcak, True)
        print(f"{i+1}. {namaBaru}")
