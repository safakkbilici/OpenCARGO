import sqlite3

import time

class Kitap():

    def __init__(self,isim,yazar,yayinevi,tur,baski):

        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__(self):

        return "Kitap Ismi: {}\nYazar: {}\nyayinevi: {}\ntur: {}\nbaski: {}\n".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski)


class Kutuphane():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("Kutuphane.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists kitaplar (isim TEXT,yazar TEXT,yayinevi TEXT,tur TEXT,baski INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitaplari_goster(self):

        sorgu =  "Select * From kitaplar"

        self.cursor.execute(sorgu)

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Kutuphanede kitap bulunmuyor...")
        else:
            for i in kitaplar:

                kitap = Kitap(i[0],i[1],i[2],i[3],i[4]) #DEMETİN INDEXLERINE ULAŞMA
                print(kitap)

    def kitap_sorgula(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,)) #DEMET OLARAK GÖNDERME!!!
        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Boyle bir kitap bulunmuyor.....")
        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4]) #O İSİMDEKİ 0. KİTABIN ÖZELLİKLERİNE ULAŞMA

            print(kitap)
    def kitap_ekle(self,kitap):

        sorgu = "Insert into kitaplar Values(?,?,?,?,?)" #SORU İŞARETİ KULLANIMI 

        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski))

        self.baglanti.commit()

    def kitap_sil(self,isim):

        sorgu = "Delete From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,)) #YİNE DEMET

        self.baglanti.commit()

    def baski_yukselt(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))


        kitaplar = self.cursor.fetchall() #O İSİMDE HEPSİNİ ALIR

        if (len(kitaplar) == 0):
            print("Boyle bir kitap bulunmuyor...")
        else:
            baski = kitaplar[0][4]

            baski += 1

            sorgu2 = "Update kitaplar set baski = ? where isim = ?"

            self.cursor.execute(sorgu2,(baski,isim))

            self.baglanti.commit() #DEĞİŞİKLİKTEN SONRA COMMİTLE