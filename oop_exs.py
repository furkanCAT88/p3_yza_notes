"""
Veri analizi aracı
    - sayı listesi tutma
    - bu sayıların toplamını hesapla
    - ortalamasını bul
    - en büyük ve en küçük değerleri göster
"""
class veri_analizi_araci:

  def __init__(self, veriler):
    self.veriler=veriler
  
  def verileri_göster(self):
    print(f"veriler: {self.veriler}")
  
  def toplam_hesapla(self):
    toplam = sum(self.veriler)
    print(f"toplam: {toplam}")
  def ortalama_hesapla(self):
    ortalama=sum(self.veriler)/len(self.veriler)
    print(f"ortalama: {ortalama}")
  def maksimum_bul(self):
    maksimum = max(self.veriler)
    print(f"maksimum değer: {maksimum}")
  def minimum_bul(self):
    minimum = min(self.veriler)
    print(f"minimum değer: {minimum}")

analiz1 = veri_analizi_araci([10,20,30,40,50])

analiz1.verileri_göster()
analiz1.toplam_hesapla()
analiz1.ortalama_hesapla()
analiz1.maksimum_bul()
analiz1.minimum_bul()