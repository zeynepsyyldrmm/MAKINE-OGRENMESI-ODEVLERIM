## HMM ile Kelime Tanıma: EV ve OKUL Sınıflandırması
Bu proje, Gizli Markov Modelleri (Hidden Markov Models - HMM) kullanarak basit ses özelliklerinden (Yüksek/Düşük frekans) kelime tanıma işlemini gerçekleştirmektedir.

### Proje Özeti
Sistem, iki farklı kelime için eğitilmiş modelleri yarıştırarak çalışır:
EV Modeli: 2 gizli durumlu (E ve V harfleri için).
OKUL Modeli: 4 gizli durumlu (O, K, U ve L harfleri için).
Gelen ses verisi (test_data), her iki modele de sorulur ve en yüksek olasılık puanını (Log-Likelihood) veren model kazanan kelime olarak seçilir.

Teknik Kurulum
Dil: Python 3.13 (Anaconda Environment).
Kütüphaneler: numpy, hmmlearn.
Model Tipi: CategoricalHMM (Kategorik veriler için optimize edilmiştir).

### Model Parametreleri

1. EV Modeli
Başlangıç Olasılığı: %100 ihtimalle "E" durumundan başlar.
Geçiş Matrisi: Harfler arası geçiş olasılıkları (Örn: E'den V'ye geçiş %40).
Emisyon (Gözlem) Olasılıkları:
E (Sesli): %70 Yüksek (0), %30 Düşük (1) frekans üretir.
V (Sessiz): %10 Yüksek (0), %90 Düşük (1) frekans üretir.

2. OKUL Modeli
Yapı: Sıralı (Left-to-Right) mimari.
Emisyon Karakteristiği: O ve U (Yüksek/Sesli), K ve L (Düşük/Sessiz) ağırlıklıdır.

### Test ve Sonuçlar


Test verisi olarak [0, 1, 1] (Yüksek-Düşük-Düşük) dizisi kullanılmıştır.

ModelLog-Likelihood SkoruSonuç

EV Modeli(-1.3295360273012822)

KAZANAN

OKUL Modeli(-1.822631132895142)

Analiz: Test verisindeki ses dizimi ve uzunluğu, EV modelinin mimarisiyle daha yüksek uyum sağladığı için sistem doğru tahminde bulunmuştur.