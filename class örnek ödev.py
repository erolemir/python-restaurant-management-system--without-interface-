personel=[]

class Firma():

    def __init__(self):
        self.calisma=True

    def program(self):
        secim=self.menusecim()
        if secim == 1:
            self.calisanekle()
        elif secim == 2:
            self.calisancıkar()
        elif secim == 3:
            self.calisanlistele()
        elif secim == 4:
            self.tümünüsil()
        elif secim == 5:
            self.maashesapla()

    def menusecim(self):
        try:
            secim=int(input("Hoşgeldiniz\n1.Çalışan Ekle\n2.Çalışan Çıkar\n3.Çalışan Listele\n4.Çalışanların Tümünü Sil\n5.Maaş Hesapla\nSeçiminiz : "))
            while secim < 1 or secim > 6 :
                print("Lütfen Tanımlı Araklıktaki Rakamları Yazınız...")
                secim=int(input("0 ve 6 Arasındaki Rakamlardan Birini Giriniz : " ))
            return secim
        except ValueError:
            print("Yazım Hatalarına Dikkat Ediniz...")
            
    def calisanekle(self):
        try:
            ad=str(input("Çalışanın Adını Giriniz : "))
            soyad=str(input("Çalışanın Soyadını Giriniz : "))
            pozisyon=str(input("Çalışanın Pozisyonu : "))
            günsayısı=int(input("Çalışanın Çalıştığı Gün Sayısı : "))
            günlükücret=int(input("Çalışanın Günlük Ücreti : "))
            demirbas=str(input("Zimmetlenen Demirbaşları Giriniz : "))
            calisan=[ad,soyad,pozisyon,günsayısı,günlükücret,demirbas]
            personel.append(calisan)
            print("Çalışan Eklendi....") 
        except ValueError:
            print("Çalışan Eklenemedi Yazım Hatalarına Dikkat Ediniz...")

    def calisancıkar(self):
        try:
            y=int(input("Çıkarmak İstediğiniz Çalışanın ID'sini Giriniz : "))
            personel.remove(personel[y])
            print(personel)
            print("Seçtiğiniz Personel Silindi...")
        except ValueError:
            print("Yazım Hatalarına Dikkat Ediniz...")

    def calisanlistele(self):
    
        for i in range(0,len(personel)):
            print(10*"*",f"\nÇalışanın Adı : {personel[i][0]}\nÇalışanın Soyadı : {personel[i][1]}\nÇalışanın Pozisyonu : {personel[i][2]}\nÇalışanın Çalıştığı Gün Sayısı : {personel[i][3]}\nÇalışanın Günlük Ücreti : {personel[i][4]}\nÇalışanın Maaşı : {personel[i][3] * personel[i][4]}\nÇalışana Zimmetlenen Demirbaşlar : {personel[i][5]}\n",10*"*")

    def tümünüsil(self):

        personel.clear()
        print("Tüm Personel Kaydı Silindi...")

    def maashesapla(self):
        try:
            a=int(input("Çalışanın ID'sini Giriniz :"))
            x=personel[a][3]
            y=personel[a][4]
            print(x*y) 
        except ValueError:
           print("Yazım Hatalarına Dikkat Ediniz...")    

firma=Firma()

while firma.calisma:

    firma.program()
