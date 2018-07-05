#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

# Durum 0 torbasına 50 beyaz ve 50 siyah bilye koyalım
durum_torbasi_0 = []
for i in range(0, 50):
    durum_torbasi_0.append("Beyaz")
    durum_torbasi_0.append("Siyah")

# Durum 0 torbasını karıştırıp bilyeleri rastgele sırayalım.
random.shuffle(durum_torbasi_0)

# Durum 1 torbasına 65 siyah, 35 beyaz bilye koyalım
durum_torbasi_1 = []
for i in range(0,50):
    durum_torbasi_1.append("Siyah")
for i in range(0,50):
    durum_torbasi_1.append("Beyaz")

# Durum 1 torbasını karıştırıp bilyeleri rastgele sırayalım.
random.shuffle(durum_torbasi_1)


# Durum 0 torbasından bilye çek
def durum_torbasi_0_bilye_cek():
    if len(durum_torbasi_0) == 0: # Torbada bilye kalmadı ise sonlandır.
        sonuc()
        exit()
    global dt_0_cekilen_bilye
    # Torbadan bilye çek.
    # Torba rastlantısal sıralandığı için listenin ilk öğesi çekilir.
    dt_0_cekilen_bilye = durum_torbasi_0[0]
    del durum_torbasi_0[0] # Çekilen bilyeyi torbadan çıkar.
    toplam_cekilen_bilye_0.append(dt_0_cekilen_bilye) # çekilen bilyeleri bir yerde topla

# Durum 1 torbasından bilye çek
def durum_torbasi_1_bilye_cek():
    if len(durum_torbasi_1) == 0: # Torbada bilye kalmadı ise sonlandır.
        sonuc()
        exit()
    global dt_1_cekilen_bilye
    # Torbadan bilye çek.
    # Torba rastlantısal sıralandığı için listenin ilk öğesi çekilir.
    dt_1_cekilen_bilye = durum_torbasi_1[0]
    del durum_torbasi_1[0] # Çekilen bilyeyi torbadan çıkar.
    toplam_cekilen_bilye_1.append(dt_1_cekilen_bilye) # çekilen bilyeleri bir yerde topla

def sonuc():
    # Durum 0 torbasından çekilenler
    bilye_sayisi_0 = len(toplam_cekilen_bilye_0)
    beyaz_bilye_sayisi_0 = toplam_cekilen_bilye_0.count("Beyaz")
    siyah_bilye_sayisi_0 = toplam_cekilen_bilye_0.count("Siyah")
    beyaz_bilye_orani_0 = float(beyaz_bilye_sayisi_0 / bilye_sayisi_0) * 100
    siyah_bilye_orani_0 = float(siyah_bilye_sayisi_0 / bilye_sayisi_0) * 100

    # Durum 1 torbasından çekilenler
    bilye_sayisi_1 = len(toplam_cekilen_bilye_1)
    beyaz_bilye_sayisi_1 = toplam_cekilen_bilye_1.count("Beyaz")
    siyah_bilye_sayisi_1 = toplam_cekilen_bilye_1.count("Siyah")
    beyaz_bilye_orani_1 = float(beyaz_bilye_sayisi_1 / bilye_sayisi_1) * 100
    siyah_bilye_orani_1 = float(siyah_bilye_sayisi_1 / bilye_sayisi_1) * 100

    # Sonuçları ekrana yaz.
    print("Durum 0 Torbası Çekilen Bilye =", bilye_sayisi_0)
    print("Durum 0 Torbası Çekilen Beyaz Bilye Oranı = ", format(beyaz_bilye_orani_0, '.2f'))
    print("Durum 0 Torbası Çekilen Siyah Bilye Oranı = ", format(siyah_bilye_orani_0, '.2f'))
    print()
    print("Durum 1 Torbası Çekilen Bilye =", bilye_sayisi_1)
    print("Durum 1 Torbası Çekilen Beyaz Bilye Oranı = ", format(beyaz_bilye_orani_1, '.2f'))
    print("Durum 1 Torbası Çekilen Siyah Bilye Oranı = ", format(siyah_bilye_orani_1, '.2f'))


# Torbadan bilye cekme sayısı
sayi = 200

toplam_cekilen_bilye_0 = []
toplam_cekilen_bilye_1 = []

# Hangi torbadan başlanacak? Rastlantısal torba seçimi
durum = random.randint(0,1)

for x in range(0, sayi):
    if durum == 0:
        durum_torbasi_0_bilye_cek()
        cekilen_bilye = dt_0_cekilen_bilye
    elif durum == 1:
        durum_torbasi_1_bilye_cek()
        cekilen_bilye = dt_1_cekilen_bilye

    if cekilen_bilye == "Beyaz":
        durum = 0
    elif cekilen_bilye == "Siyah":
        durum = 1

sonuc()

exit()
