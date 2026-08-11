import matplotlib.pyplot as plt
#örnek veri seti tüm sorular için

aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"]
satislar = [120, 150, 170, 160, 200, 220]
karlar = [20, 35, 40, 30, 50, 60]
reklam = [5, 8, 10, 7, 12, 15]

# SORU 1
# Aylar ve satışlar verisini kullanarak basit bir çizgi grafiği oluşturun.

plt.plot(aylar,satislar,color="red",linestyle = "--", marker = "o")
plt.title("aylara göre satıslar")
plt.ylabel("satislar")
plt.xlabel("aylar")
plt.grid(True)
plt.show()

# SORU 2
# Aylar ve kârlar verisini kullanarak çizgi grafiği oluşturun.
# Çizgi rengi kırmızı olsun.

plt.plot(aylar,karlar,color="red")
plt.title("aylar ve karlar")
plt.xlabel("aylar")
plt.ylabel("karlar")
plt.show()

# SORU 4
# Aylar ve satışlar verisini kullanarak sütun grafiği oluşturun.

plt.bar(aylar, satislar,color="green",)
plt.title("aylar ve satişlar")
plt.xlabel("aylar")
plt.ylabel("satişlar")
plt.show()

# SORU 6
# Satışlar verisini kullanarak pasta grafiği oluşturun.
# Ay isimlerini etiket olarak gösterin ve yüzdeleri ekrana yazdırın.

plt.pie(satislar, labels=aylar, autopct="%1.1f%%")
plt.title("satışların aylara göre dağılımı")
plt.axis("equal")
plt.show()

# SORU 7
# Reklam ve satışlar verisini kullanarak scatter plot oluşturun.

plt.scatter(reklam,satislar,color="red", s=100)
plt.title("reklam ve satış ilişkisi")
plt.xlabel("reklam harcaması")
plt.ylabel("satislar")
plt.show()

# SORU 9
# Aynı figür içinde 1 satır 2 sütun olacak şekilde iki grafik oluşturun.
# Solda satışlar için line plot, sağda kârlar için bar chart gösterin.

plt.subplot(1,2,1)
plt.plot(aylar,satislar,marker="o")
plt.title("satislar")

plt.subplot(1,2,2)
plt.bar(aylar,karlar,color="orange")
plt.title("karlar")
plt.show

