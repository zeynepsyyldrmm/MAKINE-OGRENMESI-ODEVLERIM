import numpy as np
from hmmlearn import hmm
#ev kelimesi içn model tanınmmı
#n_component=2 olmalı çünkü iki güzlü durum var

model_ev = hmm.CategoricalHMM(n_components=2)
model_ev.startprob_ = np.array([1.0, 0.0]) #e durumundan başladığı için

model_ev.transmat_ = np.array([
    [0.6, 0.4], # e durumundan e durumuna geçiş ve e durumundan v durumuna geçiş
    [0.2, 0.8]  # v durumundan e durumuna geçiş ve v durumundan v durumuna geçiş
])

model_ev.emissionprob_ = np.array([
    [0.7, 0.3], #e için [high, low]
    [0.1, 0.9] #v için [high, low]
])

model_okul = hmm.CategoricalHMM(n_components=4)

model_okul.startprob_ = np.array([1.0, 0.0, 0.0, 0.0]) #o durumunDAN BAŞLADIĞI İÇİN

model_okul.transmat_ = np.array([
    #her harfte %70 ihtimalle kalıyoruz ve %30 ihtimalle diğer harfe geçiyoruz
    [0.7, 0.3, 0.0, 0.0],
    [0.0, 0.7, 0.3, 0.0],
    [0.0, 0.0, 0.7, 0.3],
    [0.0, 0.0, 0.0, 1.0]
])

model_okul.emissionprob_ = np.array([
    #o ve u HIGH
    #k ve l LOW
    [0.8, 0.2], #o için [high, low],
    [0.2, 0.8], #k için [high, low],
    [0.8, 0.2], #u için [high, low],
    [0.2, 0.8]  #l için [high, low]    
])

test_data = np.array([[0, 1, 1]]).T

score_ev = model_ev.score(test_data)

score_okul = model_okul.score(test_data)

print(f"EV Modeli Skoru: {score_ev}")
print(f"OKUL Modeli Skoru: {score_okul}")

if score_ev > score_okul:
    print("Bu kelime EV'dir.")
else:
    print("Bu kelime OKUL'dur.") 