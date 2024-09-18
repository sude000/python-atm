"""
Bankamatik Uygulamasi
- Hesap bilgileri tutulacak
- menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonlari tanimlanacak
- çekilmek istenen tutar hesapta yoksa ek hesabin kullanilmak istendiği sorulacak
"""
# dataset
kullanicilar = {
    10100: {
        "name": "Sude",
        "surname": "Guler",
        "password": "spacelover2",
        "balance": 4500,
        "additional account balance": 3000
    },
    10101: {
        "name": "Halil",
        "surname": "Dogan",
        "password": "fishlover3",
        "balance": 1200,
        "additional account balance": 2100
    },
    10102: {
        "name": "Emirhan",
        "surname": "Durmaz",
        "password": "hasansever4",
        "balance": 5700,
        "additional account balance": 4300
    }
}

# işlem fonksiyonları
def paraCekme():
    print("\n********** PARA ÇEKME **********\n")
    print(f"Mevcut bakiyeniz: {kullanicilar[kartNo]["balance"]}")

    cekilecek_tutar = int(input("Çekmek istediğiniz miktari girin >> "))

    if cekilecek_tutar <= kullanicilar[kartNo]["balance"]:
        print(f"İŞLEM BAŞARİLİ! \nKalan Bakiyeniz: {kullanicilar[kartNo]["balance"]-cekilecek_tutar}")
    else:
        print(f"İŞLEM BAŞARİSİZ! Yetersiz Bakiye. Ek hesabinizi kullanmak ister misiniz? \nEk Hesap Bakiyeniz: {kullanicilar[kartNo]["additional account balance"]}\n")
        ek_hesap_izni = input("YES/NO >> ")
        ek_hesap_izni.lower()

        while (ek_hesap_izni == "yes" or ek_hesap_izni == "no") == False:
            ek_hesap_izni = input("YES/NO >> ")
            ek_hesap_izni.lower()
        
        if ek_hesap_izni == "yes":
            print(f"İŞLEM BAŞARILI! \nMevcut hesap bakiyeniz bitmiştir. Kalan Ek Hesap Bakiyeniz: {kullanicilar[kartNo]["additional account balance"]-(cekilecek_tutar-kullanicilar[kartNo]["balance"])}")

        if ek_hesap_izni == "no":
            print("İşlem İptal Edildi!")

def paraYatirma():
    print("\n********** PARA YATIRMA **********\n")
    print(f"Mevcut bakiyeniz: {kullanicilar[kartNo]["balance"]}")

    yatirilacak_tutar = int(input("Yatirmak istediğiniz miktari girin >> "))
    print(f"İŞLEM BAŞARILI! \nToplam Bakiyeniz: {kullanicilar[kartNo]["balance"] + yatirilacak_tutar}")

def bakiyeSorgula():
    print("\n********** BAKİYE SORGULAMA **********\n")
    print(f"Mevcut bakiyeniz: {kullanicilar[kartNo]["balance"]}")

# hoşgeldin ekranı
print("***************************************************")   
for i in range(4):
    print("*                                                 *")
print("*         SUBANK Kullanicisi Hoşgeldiniz!         *")
for i in range(4):
    print("*                                                 *")
print("***************************************************")



# kimlik doğrulama ve giriş işlemi
kartNo = int(input("Lütfen kart numaranizi giriniz >> "))
if (kartNo in kullanicilar) == True:
    sifre = input("Lütfen şifrenizi giriniz >> ")
    
    while (kullanicilar[kartNo]["password"] == sifre) == False:
        print("Şifreniz hatalidir.")
        sifre = input("Lütfen tekrar şifrenizi giriniz >> ")
    
    # kullanıcı işlemleri başlıyor
    if kullanicilar[kartNo]["password"] == sifre :
            print(f"Hoşgeldiniz {kullanicilar[kartNo]["name"]}!\n")
            print("Lütfen yapmak istediğiniz işlemi seçiniz: \n1- Para Çekme \n2- Para Yatirma\n3- Bakiye Sorgulama")
            islem = int(input("İşlem numaranizi giriniz >> "))

            while (islem == 1 or islem == 2 or islem == 3) == False:
                islem = int(input("Hatali işlem girdiniz! Lütfen işlem numaranizi giriniz >> "))

            if islem == 1:
                paraCekme()

            if islem == 2:
                paraYatirma()

            if islem == 3:
                bakiyeSorgula()
             
else:
    print("Kart numaranizi yanlis girdiniz. Lütfen tekrar deneyiniz!")
