class Human:
    #property attribute => nitelik,özellik
    # name = "Büşra"
    # age = 29

    #method davranış
    
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def talk(self,message):
        print("Yapıcı Bloğu Çalıştır")

    def walk (self):
        print(f"{self.name} is Walking")

    #instance üretmek =>  örnek ürettiğimizi belirtiyoruz
human1 = Human("Şeyma",24)
human1.name = "Şeyma"
human1.age = 24
human1.talk("Merhaba")
human1.walk()