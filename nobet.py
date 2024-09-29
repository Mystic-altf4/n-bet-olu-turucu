import os
sabah = ["Merih Sedef Odağ", "Pınar Karakaş Eroğlu", "Ayşe Merve Güneş", "Ayşegül Altınsoy"]
oglen = ["Yağmur Aksoy Bezgin", "Güler Murat", "Hatice Kübra Şanlı", "Gonca Çinkaya"]
nobet = 0
kasim = 1
x = 4
file_path = "a.txt"
with open(file_path, 'r+') as file:
    file.truncate(0) 
with open(file_path, 'a') as file:
        file.write(f"KASIM AYI İÇİN NÖBET LİSTESİ\n")
        file.write(f"BİR GÜN İÇİN İKİ KİŞİ GÖSTERİLİR\n")
        file.write(f"----------------------------------\n")
for i in range(21):
    
    if nobet > 3:
        nobet = 0
    with open(file_path, 'a') as file:
        file.write(f"{sabah[nobet]} adlı sayın hocamız {kasim} Kasım 2024 tarihinde nöbetçidir\n")
        file.write(f"{oglen[nobet]} adlı sayın hocamız {kasim} Kasım 2024 tarihinde nöbetçidir\n")
    nobet += 1
    kasim += 1
    x += 1
    if x % 5 == 0:
        kasim += 2
    
    
