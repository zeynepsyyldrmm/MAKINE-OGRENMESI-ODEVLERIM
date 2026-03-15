# MLE ile Akıllı Şehir Planlaması: Trafik Yoğunluğu Modellemesi

**Öğrenci Adı Soyadı:** Zeynep Sude Yıldırım

**Öğrenci Numarası:** 24290564

**Ders:** Makine Öğrenmesi

## Problem Tanımı
Bu projenin amacı, akıllı şehir planlaması kapsamında bir belediyenin ulaşım departmanı için trafik yoğunluğu modeli oluşturmaktır. Şehrin en yoğun caddesinden bir dakikada geçen araç sayısı verileri kullanılarak, gelecekteki trafiği tahmin etmek için Maximum Likelihood Estimation (MLE) yöntemiyle Poisson Dağılımı'nın en uygun $\lambda$ (lambda) parametresi bulunmaya çalışılmıştır.

## Veri
Çalışmada kullanılan veri seti, caddeden 1 dakikada geçen araç sayılarını gösteren 14 adet gözlemden oluşmaktadır: `{12, 15, 10, 8, 14, 11, 13, 16, 9, 12, 11, 14, 10, 15}`. Ek olarak, modelin hassasiyetini test etmek amacıyla "200" değerinde bir aykırı değer (outlier) senaryoya dahil edilmiştir.

## Yöntem
Modelin parametre tahmini iki aşamayla gerçekleştirilmiştir:
1. **Teorik (Analitik) Çözüm:** Poisson dağılımı için Likelihood (Olabilirlik) fonksiyonu oluşturulmuş, logaritması alınarak (Log-Likelihood) $\lambda$'ya göre türevi sıfıra eşitlenmiştir. Bu yöntemle $\hat{\lambda}_{MLE}$ değerinin verilerin aritmetik ortalamasına eşit olduğu ispatlanmıştır.
2. **Sayısal (Numerical) Çözüm:** Python üzerinde `scipy.optimize` kütüphanesi kullanılarak Negatif Log-Likelihood fonksiyonu minimize edilmiş ve sayısal türev yoluyla parametre tahmini yapılmıştır.

## Sonuçlar
* Analitik ve sayısal tahmin yöntemleri birbirini doğrulamış ve veri seti olmadan $\lambda$ değeri **12.14** olarak bulunmuştur.
* Modelin PMF (Olasılık Kütle Fonksiyonu) grafiği ile gerçek verinin histogramı üst üste çizdirildiğinde, veri sayısının (n=14) az olmasından kaynaklı istatistiksel gürültüler (sivri çubuklar) görülse de, modelin verinin merkezini ve yayılımını başarılı bir şekilde yakaladığı tespit edilmiştir.

## Yorum ve Tartışma (Outlier Analizi)
Veri setine "200" araçlık hatalı bir gözlem (outlier) eklendiğinde, sadece aritmetik ortalamaya dayanan MLE yönteminin bu durumdan çok sert etkilendiği görülmüştür. Tepe noktası (ortalama) 12 civarından aniden 25'e fırlamıştır. Gerçek hayatta bir belediye sadece bu modele bakarak trafik planlaması yaparsa (örneğin yolu gereksiz yere 4 şeride çıkarmak), sahadaki gerçeklikle uyuşmayan, bütçe israfına yol açacak hatalı bir mühendislik kararı almış olur. Bu durum, MLE yönteminin aykırı değerlere karşı ne kadar hassas olduğunu kanıtlamaktadır.