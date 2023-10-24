sayi1 = int (input("Sayı 1 :"))
sayi2 = int (input("Sayı 2 :"))
sayi3 = int (input("Sayı 3 :"))

if sayi1 > sayi2 and sayi1 > sayi3:
    print("En Büyük Sayı :", sayi1)
elif sayi2 > sayi3:
    print("En Büyük Sayı:", sayi2)
else:
    print("En Büyük Sayı:", sayi3)