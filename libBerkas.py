# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 22:49:59 2021

@author: galih-hermawan
Github: https://github.com/galihboy/
Web: http://galih.eu

Modul untuk pembacaan isi file dan dikonversi ke format list

"""
import os

def PeriksaBerkas(namaFile):
    # periksa apakah file valid
    if os.path.isfile(namaFile):
        return True
    else:
        try:
            file1 = open(namaFile, "r", encoding='utf-8')
            file1.closed()
        except FileNotFoundError:
            print(f"Berkas {namaFile} tidak ditemukan.")
            return False
        except OSError:
            print(f"Terdapat kesalahan OS saat membuka file {namaFile}")
            return False
        except Exception as err:
            print(f"Terdapat kesalahan tak terduga saat membuka file {namaFile} - ",repr(err))
            return False                
        else:
            return True

# membersihkan list dari empty string/values
def BersihkanEmptyList(daftar):
    return [x for x in daftar if x]

# membaca isi file dan dikembalikan dalam bentuk list
def BacaBerkas(namaFile):
    statusFile = PeriksaBerkas(namaFile)
    isi = []
    if statusFile:
        file1 = open(namaFile, "r", encoding='utf-8')
        with file1:
            # pisah data file per baris dan hapus data kosong
            isi = file1.read().strip().split("\n")
    
        file1.close()  
    return BersihkanEmptyList(isi)

if __name__ == "__main__":
    print("libBerkas.py")