#for

#start => döngümüzün başlangıç değerini belirtir.(0)
#stop => döngümüzün biteceği değeri belirtir.
#step => döngümüzün artış miktarını belirler. (1)

""" for i in range (10):
    print(i) """

""" biggestValue = 0
for i in range (5):
    sayi = int(input (f"{i}. sayıyı giriniz."))  
    if sayi > biggestValue:
        biggestValue = sayi
print(f"Girdiğiniz sayılar arasında en büyük olan: {biggestValue}") """

""" forRangeMin = int (input("Döngünün alt limitini belirleyiniz."))
forRangeMax = int (input("Döngünün üst limitini belirleyiniz."))

for i in range(forRangeMin, forRangeMax+1):
    if i % 2 == 0:
        print (i) """

""" sayilar = []

for i in range(3):
    sayilar.append(int(input(f"{i+1}. sayiyi giriniz.")))

    #sort küçükten büyüğe sıralar
    sayilar.sort(reverse=True)
    
    print(sayilar)
 """

ogrenciler = [ "Güneş", "Recep", "Betül", "Yunus", "İrem"]

""" #lenght 
print(len(ogrenciler))

for i in range (len(ogrenciler)):
    print(f"{i+1}. Öğrenci: {ogrenciler[i]}")

for ogrenci in ogrenciler:
    print (f"öğrenci : {ogrenci}")
 """
#break : ilgili döngünün o anda kırılmasını sağlar

for i in range (len(ogrenciler)):
    if i>3:
        break
        print (f"{i+1}. Öğrenci: {ogrenciler[i]}")

#continue : iterasoyundaki current değeri atla, bir sonraki değer ile devam et

for ogrenci in ogrenciler:
    if ogrenci == "Recep":
        continue
    print(f"Öğrenci: {ogrenci}")

#WHILE
i = 0
while i < 10:
    print("Merhaba")