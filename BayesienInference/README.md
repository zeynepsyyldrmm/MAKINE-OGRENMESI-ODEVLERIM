# Uzak Bir Galaksinin Parlaklık Analizi (Bayesyen Çıkarım ile Parametre Tahmini)

## Problem Tanımı
Bu projede, laboratuvar ortamında deney yapılamayan ve sadece gürültülü gözlem verilerine dayanılan astronomi alanındaki bir problemi modelledik. Amacımız, Bayesyen çıkarım yöntemlerini kullanarak, gürültülü bir veri setinin arkasındaki gök cisminin gerçek parlaklığını ve veri setindeki belirsizliği tahmin etmektir. Kesin bir nokta tahmini yerine, belirsizlikleri yönetebilen olasılıksal bir model (Posterior dağılımı) oluşturulması hedeflenmiştir.

## Veri
Çalışmada kullanılan veri, bilinen kontrol değişkenleri (Gerçek Parlaklık\mu = 150.0, Gözlem Hatası\sigma = 10.0) üzerinden sentetik olarak üretilmiştir. 

Analiz, toplam 50 gözlemden (n_{obs} = 50) oluşan ve rastgele normal dağılımla gürültü eklenmiş bu veri seti üzerinden yürütülmüştür.

## Yöntem
Parametre tahmini için Bayes Teoremi (Log-Prior, Log-Likelihood ve Log-Posterior fonksiyonları) kullanılmıştır. Parametre uzayını keşfetmek ve hedef dağılımı maksimize etmek amacıyla Markov Chain Monte Carlo (MCMC) simülasyonu tercih edilmiş olup, Python'ın `emcee` kütüphanesi ile 32 gezgin (walker) 2000 adım boyunca çalıştırılmıştır. İlk 500 adım "burn-in" (ısınma) aşaması olarak veri setinden çıkarılmıştır.

## Sonuçlar
MCMC simülasyonu sonucunda elde edilen parametrelerin gerçek değerlerle karşılaştırması aşağıdadır:

| Değişken | Gerçek Değer (Girdi) | Tahmin Edilen (Median) | Alt Sınır (%16) | Üst Sınır (%84) | Mutlak Hata |
| :--- | :--- | :--- | :--- | :--- | :--- |
| \mu (Parlaklık) | 150.0 | 147.79 | 146.43 | 149.07 | 2.21 |
| \sigma (Hata Payı) | 10.0 | 9.49 | 8.55 | 10.53 | 0.51 |

## Yorum ve Tartışma
* **Prior Etkisi:** Analizde parlaklık için çok dar bir prior seçilseydi (örneğin 100-110 arası), model gerçek değeri (150) bulmak yerine bu dar ön bilgi aralığına sıkışacak ve gerçekliği reddedecekti. Geniş prior seçimi, verinin model üzerindeki etkisini artırmıştır.
* **Veri Miktarının Etkisi:** Gözlem sayısı 50 yerine 5 olsaydı, posterior dağılımının genişliği ciddi oranda artardı. Veri sayısı azaldığında kanıt azalacağı için, modelin tahminlerindeki belirsizlik (güven aralığı) büyür.