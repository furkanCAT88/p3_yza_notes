# ============================================================
# SORU 1
# Bir değişken tanımlayalım: ad = "Kaan", yas = 25, ortalama = 3.45
# Bu değişkenlerin tiplerini type() ile yazdıralım.
# ============================================================
ad = "kaan"
yas = 25
ortalama = 3.45
print(type(ad))
print(type(yas))
print(type(ortalama))

# ============================================================
# SORU 2
# Kullanıcıdan yaş bilgisini input() ile alalım.
# Bu yaşın tipini ekrana basalım ve 5 yıl ekleyip sonucu yazdıralım.
# Not: input() her zaman string döndürür, int'e çevirmeyi unutmayalım.
# ============================================================

yas = int(input("yaşınızı giriniz"))
#input her zaman string çevirdiğinden dolayı int a çevirmeliyiz aldığımız sayıyı
print(type(yas))



# ============================================================
# SORU 3
# Bir ürün fiyatı (float) alalım. %18 KDV hesaplayalım.
# Toplam fiyatı 2 basamak olacak şekilde yazdıralım.
# ============================================================


fiyat = float(input("ürünün fiyatını giriniz"))
fiyat = fiyat + (fiyat * 0.18)
print(round(fiyat,2))

# ============================================================
# SORU 4
# Bir liste oluşturalım: sayilar = [10, 20, 30, 40, 50] 
# - İlk elemanı yazdıralım
# - Son elemanı yazdıralım
# - 2. indexten sona kadar olan parçayı yazdıralım
# - Listeye 60 ekleyelim
# - Listedeki 20 değerini silelim
# ============================================================

sayilar = [10,20,30,40,50]
print(sayilar[0])
print(sayilar[-1])
print(sayilar[2:])

sayilar.append(60)
sayilar.remove(20)

# ============================================================
# SORU 5
# Bir tuple(değiştirilemez liste) oluşturalım: koordinat = (12, 34)
# - Tuple içindeki değerleri unpacking ile x ve y değişkenlerine alalım
# - x ve y'yi yazdıralım
# - Tuple'ın değiştirilemediğini göstermek için (yorum satırıyla) örnek verelim
# ============================================================
koordinat = (12,34)
x, y = koordinat
print(x)
print(y)


# SORU 6
# Bir sözlük (dictionary) oluşturalım:
# ogrenci = {"isim": "Ayşe", "yas": 22, "bolum": "Yazılım"}
# - Öğrencinin ismini yazdıralım
# - "not" anahtarı ile 90 ekleyelim
# - "yas" değerini 23 yaparak güncelleyelim
# - Tüm anahtarları ve tüm değerleri yazdıralım
# ============================================================
ogrenci = {"isim": "Ayşe", "yas": 22, "bolum": "Yazılım"}
print(ogrenci["isim"])

ogrenci["not"] = 90
ogrenci["yas"] = 23

print("anahtarlar", list(ogrenci.keys()))
print("değerler: ", list(ogrenci.values()))


# ============================================================
# SORU 7
# Set oluşturalım ve tekrar edenleri temizleyelim:
# liste = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]
# - listeyi set'e çevirip benzersiz isimleri yazdıralım
# - benzersiz isim sayısını yazdıralım
# ============================================================
liste = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]
benzersiz = set(liste)
print(benzersiz)
print(len(benzersiz))

#while döngüsü ile basit chatbot
giris = ""
while giris != "q": 

    giris = input("Çıkmak için q yazın: ")
    print(f"Kullanıcı mesajı: {giris}")

    # chatbota soruyu gönder
    # chatbot bize cevaı return eder
    # chatbotun cevabını ekrana yazdırıyoruz
    print("chatbot: merhaba")


# ============================================================
# SORU 1 (IF)
# Kullanıcıdan bir sayı alın.
# Sayı pozitifse "Pozitif", negatifse "Negatif", sıfırsa "Sıfır" yazdırın.
# ============================================================
sayi = input("bir sayi giriniz:")
if sayi>0:
    print("pozitif")
elif sayi<0:
    print("negatif")
else:
    print("sıfır")


# ============================================================
# SORU 2 (FOR)
# 1'den 10'a kadar (10 dahil) sayıları yazdırın.
# Ayrıca bu sayıların toplamını hesaplayıp ekrana yazdırın.
# ============================================================
for i in range(11):
    print(i)
    toplam = toplam + i
print(toplam)


# ============================================================
# SORU 3 (WHILE)
# Kullanıcıdan "q" yazana kadar sürekli giriş alın.
# Kullanıcı her giriş yaptığında "Girdiniz: ..." şeklinde ekrana yazdırın.
# Kullanıcı "q" yazarsa döngü bitsin ve "Çıkış yapıldı" yazsın.
# ============================================================

giris = ""
while giris != "q":
    giris =input(" giriş yapınız")
    if giris != "q":
        print(f"giris yaptınız: {giris}")
print("cıkış yaptınız")

# ============================================================
# SORU 4 (NESTED)
# 1'den 20'ye kadar sayıları dolaşın.
# Eğer sayı çiftse "Çift", tekse "Tek" yazdırın.
# Ayrıca sayı 10'dan büyükse yanına "Büyük", değilse "Küçük/Eşit" yazdırın.
# Örnek çıktı: 12 -> Çift - Büyük
# ============================================================

for i in range (20):
    if i%2==0:
        print("sayı çift")
    else:
        print("tek")
    if i>10:
        print("büyük")
    else :
        print("küçük veya eşit")


"""
Kullanıcıdan vize notu ve final notu alalım
- Ortalama hesaplaması
- harf notu belirleme
- sonucu ekrana yazdırma
"""
vize_notu = int(input("vize notunu giriniz"))
final_notu = int(input("final notunu giriniz"))

def ort_hesapla(vize: float,final: float) -> float:
    ort =(vize * 0.4) + (final * 0.6)
    return ort
def harf_notu_belirleme(ort:float):
    if ort>85:
        return "A"
    elif ort>=75:
        return "B"
    elif ort >= 50:
        return "c"
    else:
        return "F"
    
def sonucu_yazdir(isim:str, ort:float, harf:str):
    print(f"öğrenci: {isim}")
    print(f"ortalama: {ort}")
    print(f"harf notu: {harf}")

isim = input("öğrenci ismini giriniz")
vize = float(input("vize notunuzu giriniz"))
final = float(input("final notunuzu giriniz"))

ortalama= ortalama_hesapla(vize=vize, final=final)
harf= harf_notu_belirleme(ortalama=ortalama)
sonucu_yazdir(isim=isim, ort=ort, harf=harf)


# SORU 1
# "notlar.txt" adında bir dosya oluşturun ve içine
# 5 öğrencinin notunu yazın. Her not ayrı satırda olsun.

with open("notlar.txt","w",encoding="utf-8") as dosya:
    dosya.write("70\n")
    dosya.write("80\n")
    dosya.write("50\n")
    dosya.write("78\n")
    dosya.write("59\n")

# SORU 2
# Bu dosyayı okuyun ve:
# - Notların ortalamasını hesaplayın
# - En yüksek notu bulun
# - En düşük notu bulun
notlar = []
with open("notlar.txt","r",encoding="utf-8") as dosya:
    for satir in dosya:
        notlar.append(int(satir.strip()))
ortalama= sum(notlar)/len(notlar)
en_yüksek = max(notlar)
en_düsük = min(notlar)


# SORU 3
# Eğer ortalama 50'den büyükse "Sınıf geçti"
# değilse "Sınıf kaldı" sonucunu
# "sonuc.txt" dosyasına kaydedin.

if ortalama >50 :
    sonuc = "sınıfı geçti"
else :
    sonuc = "sınıfta kaldı"
with open ("sonuc.txt", "w",encoding="utf-8")as dosya:
    dosya.write(f"ortalama: {ortalama}")
    dosya.write(f"sonuc: {sonuc}")

"""
Bozuk veri temizleme
veri:
        70
        85
        abc
        90
        50
        hata
        60
Amaç:
    - dosyayı oku
    - sayıya çevrilemeyen satıları atla
    - geçerli notları topla
    - ortalama hesapla
"""
notlar = []
hata_sayisi = 0
with open("notlar.txt","r",encoding="utf-8") as dosya:
    for satir in dosya:
        try:
            not_degeri = int(satir.strip())
            notlar.append(not_degeri)
        except ValueError:
            print(f"hatalı veri bulunud: {satir.strip()}")
            hata_sayisi += 1
toplam = sum(notlar)
ortalama = toplam/len(notlar)
