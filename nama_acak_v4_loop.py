# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:02:39 2021

@author: galih-hermawan
Github: https://github.com/galihboy/
Web: http://galih.eu
"""

# ambil fungsi dari libNamaAcak
from libNamaAcak import CetakNama, ValidasiAbdul
# ambil variable berisi list nama dari file2 yang sudah dibuat
from libNamaAcak import daftarNamaNabi, daftarNamaSahabat, \
                        daftarNamaLaki, daftarNamaIslam, daftarAsmaulHusna

# fungsi untuk mencetak menu
def CekFormatMenu(str_gabungan_nomor):
    lstMenuDaftar = ['1', '2', '3', '4']
    lstMenuPilihan = str_gabungan_nomor.split() 
    lstHasil = [i for i in lstMenuPilihan for j in lstMenuDaftar if i==j]
    return lstHasil

# list untuk menyimpan data file nama
lstDaftar = [daftarNamaLaki, daftarNamaNabi, daftarNamaSahabat, daftarNamaIslam]

while True:
    print("\nPembangkitan Nama Acak.")
    print("-----------------------")
    print("Daftar sumber nama ada 4, isi nomor dan gunakan spasi jika memilih lebih dari 1, ")
    print("misal: 1 4 [untuk memilih nama pada kelompok 1 dan 4]")
    print("[1] Nama laki-laki umum.")
    print("[2] Nama nabi.")
    print("[3] Nama sahabat.")
    print("[4] Nama Islam.")
    
    pilNama = input("Nomor pilihan (kosongkan untuk keluar): ")
    
    if not pilNama.strip(): break
    lstMenu = CekFormatMenu(pilNama.strip())
    
    charAcak = "x"
    
    if lstMenu:
        print(f"Pilihan menu yang valid: {' '.join(lstMenu)}")
        
        lstSumber = []
        for i in lstMenu:
            lstSumber += lstDaftar[int(i)-1]
        
        while True:
            print(f"\nPilih format nama, dimana nama acak ditandai oleh '{charAcak}'")
            print("Contoh: \n\t'x x' (dua nama acak), \
                  \n\t'abdullah x x' (nama 'abdullah' diikuti dua nama acak)")
            strFormat = input("Masukkan format nama (kosongkan untuk keluar): ")
            strFormat = strFormat.strip().lower()
            
            if not strFormat: break
        
            jmlNama = input("Jumlah nama yang diinginkan: ")    
            if not jmlNama.isdigit():
                jmlNama = "1"
            
            for i in range(int(jmlNama)):
                nama = CetakNama(lstSumber, strFormat, charAcak)
                #namaBaru = ValidasiAbdul(sumber, nama, strFormat, charAcak)
                namaBaru = ValidasiAbdul(lstSumber, nama, strFormat, charAcak, True)
                print(f"{i+1}. {namaBaru}")
        
    else:
        print("Pilihan menu tidak valid.")
