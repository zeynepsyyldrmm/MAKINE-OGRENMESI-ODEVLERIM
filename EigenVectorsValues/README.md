# Ödev Raporu: Özdeğerler ve Özvektörler (Eigenvalues and Eigenvectors)

## 1. Kısa Tanımlar

* **Matris Manipülasyonu:** 

    Makine öğrenmesi algoritmaları, devasa veri setleriyle çalışırken verileri ve model ağırlıklarını (skaler sayılar yerine) matrisler halinde tutar. Matris manipülasyonu, bu büyük veri yığınları üzerinde aynı anda ve son derece hızlı doğrusal cebir işlemleri yapabilmemizi sağlayan temel donanımdır.
* **Özvektör (Eigenvector):** 

    Geometrik olarak incelendiğinde; karesel bir matris uzaydaki vektörleri dönüştürürken (çarparken), yönünü (doğrultusunu) kesinlikle değiştirmeyen, sadece kendi ekseni üzerinde uzayan, kısalan veya ters yöne dönen bu özel vektörlere özvektör denir.
* **Özdeğer (Eigenvalue):** 

    Bir matris dönüşümü sırasında, o matrisin özvektörünün boyunun ne kadar uzadığını, kısaldığını (ölçeklendiğini) belirten ve doğrusal dönüşümün çarpanını ifade eden skaler sayısal değere özdeğer adı verilir.

## 2. Makine Öğrenmesi ile İlişkisi

Gerçek dünyadaki veri setleri genellikle çok sayıda özellik barındırır ve yüksek boyutludur. Bu karmaşıklığı yönetmek ve verinin içindeki asıl deseni (örüntüyü) bulmak için, veri setini temsil eden kovaryans matrisinin özdeğerleri ve özvektörleri hesaplanır. Bu hesaplama sonucunda ortaya çıkan özvektörler, verinin uzayda en çok hangi yönlere doğru dağıldığını, yani verinin 'ana iskeletini' gösterir. Özdeğerler ise bu yönlerin ne kadar fazla bilgi (varyans) içerdiğini belirtir. Özellikle PCA (Temel Bileşenler Analizi) gibi yaklaşımlarda, en büyük özdeğere sahip olan özvektör verideki en kritik bilgiyi taşıyan temel bileşen olarak seçilir ve bu sayede minimum veri kaybıyla boyut indirgeme (dimensionality reduction) işlemleri gerçekleştirilir.

## 3. Kullanıldığı Yöntemler ve Yaklaşımlar

Makine öğrenmesinde matris manipülasyonu, özdeğer ve özvektör hesaplamaları ağırlıklı olarak aşağıdaki alanlarda ve algoritmalarda kullanılmaktadır:

* **Temel Bileşenler Analizi (PCA - Principal Component Analysis):** Boyut indirgeme için kullanılır. Verideki en önemli özellikleri seçmemizi sağlar.
* **Tekil Değer Ayrışımı (SVD - Singular Value Decomposition):** Tavsiye sistemlerinde (örneğin Netflix'in sana film önermesi) ve veri sıkıştırmada sıklıkla kullanılır.
* **Görüntü İşleme (Örn: Eigenfaces):** Yüz tanıma sistemlerinde yüzün en ayırt edici özelliklerini çıkarmak için kullanılır.

## 4. Kaynakça

* Introduction to Matrices and Matrix Arithmetic for Machine Learning - MachineLearningMastery.com
* Gentle Introduction to Eigenvalues and Eigenvectors for Machine Learning - MachineLearningMastery.com
* https://www.fullstack.com/labs/resources/blog/linear-algebra-essentials-for-machine-learning-developers 
* https://jonathan-hui.medium.com/machine-learning-linear-algebra-eigenvalue-and-eigenvector-f8d0493564c9 
* https://machinelearningmastery.com/introduction-matrices-machine-learning/ 
* https://machinelearningmastery.com/introduction-to-eigendecomposition-eigenvalues-and-eigenvectors/ 


## 5. Custom Fonksiyon ile Numpy `eig` Karşılaştırması

Hazırlanan Python kodunda, özdeğerleri sıfırdan hesaplamak için sayısal analiz yöntemlerinden biri olan **QR İterasyonu** kullanılmıştır. Matris ardışık olarak Q ve R matrislerine ayrıştırılıp ters sırayla çarpıldığında, matrisin köşegen elemanları özdeğerlere yakınsamaktadır.

**Karşılaştırma Sonucu:**
Kendi yazdığımız iteratif algoritma ile Numpy'ın donanım seviyesinde optimize edilmiş `np.linalg.eig` fonksiyonu aynı matris üzerinde test edilmiştir. Sonuçlar incelendiğinde, iki yöntemin bulduğu özdeğerlerin virgülden sonraki çok küçük hassasiyetler dışında **birebir aynı** olduğu görülmüştür. Bu durum, Numpy'ın arka planda kullandığı LAPACK kütüphanesinin de benzer iteratif sayısal yaklaşımları (çok daha optimize ve hızlı bir şekilde) kullandığını kanıtlamaktadır.