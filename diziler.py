sayilar = [100,200,300,400,"Merhaba"]
#programcılar saymjaya sıfırdan başlar. 
print(sayilar[0])
print(sayilar)

#append listenin sonuna eleman ekler
sayilar.append(100)
print(sayilar)

#pop indexe göre siler (default son index)
sayilar.pop(2)
print(sayilar)

#remove değere göre silme işlemini yapar
sayilar.remove(100)
print(sayilar)

#extend append in aksine çoklu veri eklemeyi sağlar
sayilar.extend([10,20,30])
print(sayilar)

#clear silme işleminde kullanılır
sayilar.clear()
print(sayilar)


sayilar.reverse