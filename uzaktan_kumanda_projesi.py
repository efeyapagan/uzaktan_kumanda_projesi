import random
import time

class Kumanda():

    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_listesi=["Trt"], kanal="Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if self.tv_durum == "Açık":
            print("Televizyon zaten açık.")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if self.tv_durum == "Kapalı":
            print("Televizyon zaten kapalı.")
        else:
            print("Televizyon kapatılıyor...")
            self.tv_durum = "Kapalı"

    def tv_acik_mi(self):
        if self.tv_durum != "Açık":
            print("⚠️ Televizyon kapalı! Bu işlemi gerçekleştiremezsiniz.")
            return False
        return True

    def ses_ayarlari(self):
        while True:
            cevap = input("Sesi Azalt : < \nSesi Arttır : > \nÇıkış : çıkış\n")
            if cevap == "<":
                if self.tv_ses > 0:
                    self.tv_ses -= 1
                    print("Ses:", self.tv_ses)
            elif cevap == ">":
                if self.tv_ses < 100:
                    self.tv_ses += 1
                    print("Ses:", self.tv_ses)
            elif cevap.lower() == "çıkış":
                print("Ses güncellendi:", self.tv_ses)
                break
            else:
                print("Geçersiz giriş.")

    def kanal_ekle(self, yeni_kanal):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(yeni_kanal)
        print("Kanal eklendi:", yeni_kanal)

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi) - 1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal:", self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return f"TV Durumu: {self.tv_durum}\nTV Ses: {self.tv_ses}\nKanal Listesi: {self.kanal_listesi}\nAktif Kanal: {self.kanal}"


print("""
📺 Televizyon Kumandası Uygulaması 📺

1. TV Aç
2. TV Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısını Öğren
6. Rastgele Kanal Geç
7. TV Bilgilerini Göster
8. Çıkış (q)

""")

kumanda = Kumanda()

while True:
    işlem = input("İşlem seçiniz: ")

    if işlem == "q":
        print("Program sonlandırılıyor...")
        time.sleep(1)
        break

    elif işlem == "1":
        kumanda.tv_ac()

    elif işlem == "2":
        kumanda.tv_kapat()

    elif işlem == "3":
        if kumanda.tv_acik_mi():
            kumanda.ses_ayarlari()

    elif işlem == "4":
        if kumanda.tv_acik_mi():
            kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak giriniz: ")
            kanal_listesi = kanal_isimleri.split(",")
            for kanal in kanal_listesi:
                kumanda.kanal_ekle(kanal.strip())

    elif işlem == "5":
        if kumanda.tv_acik_mi():
            print("Kanal sayısı:", len(kumanda))

    elif işlem == "6":
        if kumanda.tv_acik_mi():
            kumanda.rastgele_kanal()

    elif işlem == "7":
        if kumanda.tv_acik_mi():
            print(kumanda)

    else:
        print("Geçersiz işlem girdiniz.")
