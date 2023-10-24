""" print("Merhaba Tobeto Ekibi!")

#değiskenler
#metinsel => String
text = "Merhaba Tobeto"
print(text)

#numerik => INT, INTEGER - Tam sayı
studentCount = 45
print(studentCount)

studentCount2 = "50"
##print(studentCount + studentCount2) (bir sayı ile bir metin toplanamaz)

#double,decimal,float => ondalık sayı
averagePoint = 25.5
print(averagePoint)

#boolen => True - False (0,1)
isVerified = True
print(isVerified)

print(type(studentCount))
print(type(studentCount2))
print(type(averagePoint))
print(type(isVerified))

#operatörler - matematiksel ve mantıksal
#matematiksel operatörler + - * / %
number = 10

print(number + number)
print(number - number)
print(number * number)
print(number / 2)
#sol taraftaki değerin sağ taraftaki değere bölümünden kalan sonuç olur (mode)
print(number % 3)

#mantıksal operatörler

print(number == 10)  #true  
print(number == 11)  #false

print(number !=10)   #false
print(number !=11)   #true

print(number > 10)   #false
print(number >= 10)  #true

print(number < 10)   #false
print(number <=10)   #true
 """
#string interpolation => metin birleştirme

hello = "Merhaba"
userName = "Büşra"

totalText = hello +" "+ userName
print(totalText)

totalText = "{message} Sayın {name}".format(message="Selam", name=userName)
print(totalText)

#f-string
totalText = f"Hosşgeldiniz {userName}"
print(totalText) 