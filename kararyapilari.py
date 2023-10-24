Not = int(input("Lütfen notunuzu giriniz."))
#print(type(Not))
NotAsInteger = int(Not)
#75print(type(NotAsInteger))


if Not > 80 : 
    print("Harika,geçtiniz.")
    if NotAsInteger > 90:
        print("Bravo.")
#elseif        
elif Not > 50 :
    print("Başarılı.")
else:
    print("Kaldınız.")