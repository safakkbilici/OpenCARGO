from kutuphane import *

print("""***********************************

kutuphane ProgramÄ±na HoÅŸgeldiniz.

Ä°ÅŸlemler;

1. KitaplarÄ± GÃ¶ster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil 

5. BaskÄ± YÃ¼kselt

Ã‡Ä±kmak iÃ§in 'q' ya basÄ±n.
***********************************""")

kutuphane = Kutuphane()

while True:
    islem = input("YapacaÄŸÄ±nÄ±z Ä°ÅŸlem:")

    if (islem == "q"):
        print("Program SonlandÄ±rÄ±lÄ±yor.....")
        print("Yine bekleriz....")
        break
    elif (islem == "1"):
        kutuphane.kitaplari_goster()

    elif (islem == "2"):
        isim = input("Hangi kitabÄ± istiyorsunuz ? ")
        print("Kitap SorgulanÄ±yor...")
        time.sleep(2)

        kutuphane.kitap_sorgula(isim)

    elif (islem == "3"):
        isim = input("Ä°sim:")
        yazar = input("Yazar:")
        yayinevi = input("YayÄ±nevi:")
        tur = input("TÃ¼r:")
        baski = int(input("BaskÄ±"))

        yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski)

        print("Kitap ekleniyor....")
        time.sleep(2)

        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi....")


    elif (islem == "4"):
        isim = input("Hangi kitabÄ± silmek istiyorsunuz ?")

        cevap = input("Emin misiniz ? (E/H)")
        if (cevap == "E"):
            print("Kitap Siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap silindi....")


    elif (islem == "5"):
        isim = input("Hangi kitabÄ±n baskÄ±sÄ±nÄ± yÃ¼kseltmek istiyorsunuz ?")
        print("BaskÄ± yÃ¼kseltiliyor....")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("BaskÄ± yÃ¼kseltildi....")

    else:
        print("GeÃ§ersiz Ä°ÅŸlem...")
