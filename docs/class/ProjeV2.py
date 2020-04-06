#%%
import pandas as pd
import numpy as np
import gmaps
import requests
from datetime import timedelta,date
import random
import string

apiKey = "AIzaSyAZ0Vm2FHhuEIKR8aTDR5ebwaW89Lfgiuk"
"""
distance = pd.read_excel('mesafe.xlsx')
distance = distance.set_index('Şehir', drop=True, append=False, inplace=False, verify_integrity=False)
np.fill_diagonal(distance.values, 0)
distance.to_pickle("./deneme.pkl")"""
distance = pd.read_pickle("./mesafe.pkl")

#%%
def get_lat_lng(apiKey, address):
    
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ','+'), apiKey))
    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        output_address = resp_json_payload["results"][0]["formatted_address"]        
        lat = resp_json_payload['results'][0]['geometry']['location']['lat']
        lng = resp_json_payload['results'][0]['geometry']['location']['lng']
        gmaps.configure(api_key=apiKey)
        #location = (lat, lng)
        
    except:
        print('***********HATA: {} Adres bulunamadı.***********'.format(address))
        lat = 0
        lng = 0
    return lat, lng, output_address





#%%
            
class Koli:
    global distance
    currentCity = None
    def __init__(self):
        # Burda aldığımız bilgileri databaseye kaydetcez.
        self.takipNo = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        # 10 haneli rastgele string oluşturdum
        # Takip No 'da databaseye atılıp kargoyla ilişkilendirilecek
        hata = 1
        while hata == 1:
            try:
                self.kilo = float(input("Kolinin ağırlığını kg cinsinden giriniz : "))
                self.desi = float(input('Kolinin desisini giriniz (Desi hesaplamak için -1 giriniz) : '))
                if self.desi == -1.:
                    witdh = float(input('Please enter the witdh of the package (cm) : '))
                    height = float(input('Please enter the height of the package (cm) : '))
                    depth = float(input('Please enter the depth of the package (cm) : '))
                    self.desi = (witdh*height*depth)/1000
                
                if self.kilo > 0 and self.desi > 0:
                    hata = 0
                else:
                    print("Ölçüler 0'dan küçük olamaz.")
            except:
                print("Yanlış giriş yaptınız.")
    

    
    
    @staticmethod
    def ucretHesapla(self,currentCity,nextCity,active = 1):
        if active == 0:
            hata = 1
            while hata == 1:
                try:
                    kilo = float(input("Kolinin ağırlığını kg cinsinden giriniz : "))
                    desi = float(input('Kolinin desisini giriniz (Desi hesaplamak için -1 giriniz) : '))
                    if desi == -1.:
                        witdh = float(input('Please enter the witdh of the package (cm) : '))
                        height = float(input('Please enter the height of the package (cm) : '))
                        depth = float(input('Please enter the depth of the package (cm) : '))
                        desi = (witdh*height*depth)/1000
                    
                    if kilo > 0 and desi > 0:
                        hata = 0
                    else:
                        print("Ölçüler 0'dan küçük olamaz.")
                except:
                    print("Yanlış giriş yaptınız.")
        
            ucret = 15 + (max(desi/3,kilo)*distance.loc[currentCity,nextCity]) / 100
            return ucret
        else:
            ucret = 15 + (max(self.desi/3,self.kilo)*distance.loc[currentCity,nextCity]) / 100
            return ucret
    
    def getCurrentCity(self):
        return self.currentCity
    
    def setCurrentCity(self,newCity):
        self.currentCity = newCity
    
    def getTakipNo(self):
        return self.takipNo
    

#%%

class Belge:
    global distance
    currentCity = None
    def __init__(self):
        self.takipNo = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    
    # Bunun __init__'ine gerek yok
    
    @staticmethod
    def ucretHesapla(self,currentCity,nextCity):
        ucret = 20 + distance.loc[currentCity,nextCity]/100
        return ucret

    def getCurrentCity(self):
        return self.currentCity
    
    def setCurrentCity(self,newCity):
        self.currentCity = newCity
        
    def getTakipNo(self):
        return self.takipNo
    


#%%

class Hizmet:
    global distance
    
    def kargoTakip(self):
        hata = 1
        while hata == 1:
            takipNo = input('10 Haneli Kargo Takip Numaranızı giriniz : ')
            database = [] # yanda hata çıkmasın diye koydum silincek
            if takipNo in database:
                pass # Burda databaseden bilgi çekcez
                # hata olmadığı için hata = 0 yapıp çıkcaz döngüden
            else:
                print("Bu numaraya ait ait bir kargo bulunmuyor.")
    
    def tahminiVaris(self,currentCity,nextCity):
        if currentCity == nextCity:
            print("Kargonuzun gün içinde elinize ulaşması bekleniyor.")
        day = int(round(distance.loc[currentCity][nextCity]/250, 0))
        end = date.today() + timedelta(days=day)
        print("Kargonuzun tahmini teslim günü :",end)
        return end # Duruma göre print veya return yaparız
    
    def ucretHesapla(self):
        currentCity = input("Çıkış ili giriniz : ").lower()
        nextCity = input("Varış ili giriniz : ").lower()
        tur = input("Kargo türünü giriniz (Belge, Koli): ").lower()
        if tur == "koli":
            ucret = Koli.ucretHesapla(currentCity, nextCity,0)
        elif tur == "belge":
            ucret = Belge.ucretHesapla(currentCity, nextCity,0)
        print("Ücret :",ucret)
        return ucret # Opsiyonel
    
    
    def kuryeCagir(self):
        # Bu düzenlenecek
        name = input("İsminiz : ")
        lastName = input("Soy isminiz : ")
        TC = input("TC Kimlik Numaranız : ")
        no = input("Telefon Numaranızı giriniz : +90")
        dg = input("Doğum yılınız (Gün.Ay.Yıl Şeklinde) : ").split(".")
        tur = input("Kargo türünü giriniz (Belge,Koli) : ").lower()
        if tur == "paket":
            koli = Koli()
        elif tur == "dosya":
            belge = Belge()

#%%
        
    