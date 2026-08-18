# Örnek Prompt'lar

Bu projede kullanabileceğin prompt'lar.

---

## Mail Önceliklendirme

```
Bu e-postayı analiz et:

Kimden: {kimden}
Konu: {konu}
İçerik: {icerik}

Önem derecesini belirle:
- yuksek: Bugün cevap verilmeli, iş kaybı riski
- orta: Bu hafta içinde bakılmalı
- dusuk: Bilgi amaçlı, acil değil

JSON döndür: {"onem": "...", "neden": "..."}
```

---

## Cevap Taslağı

```
Bu e-postaya profesyonel bir cevap yaz:

[mail içeriği]

Kurallar:
- Kısa ve öz (3-5 cümle)
- Profesyonel ama samimi
- Somut taahhüt içersin
```

---

## Mail Zinciri Özeti

Uzun mail zincirleri için:

```
Bu e-posta zincirini özetle:

[tüm mailler]

Şunları belirt:
1. Konunun özeti (1 cümle)
2. Kimlerin dahil olduğu
3. Mevcut durum
4. Benden beklenen eylem
```

---

## Günlük Özet Oluşturma

```
Bu maillerin günlük özetini çıkar:

[mail listesi]

Format:
1. Bugün cevaplanması gerekenler
2. Bu hafta takip edilecekler
3. Bilgi amaçlı olanlar

Her kategori için en önemli 3 madde.
```

---

## Otomatik Kategorileme

```
Bu maili kategorile:

[mail]

Kategoriler:
- is: İş ile ilgili, proje, toplantı
- kisisel: Arkadaş, aile
- finans: Banka, fatura, ödeme
- pazarlama: Newsletter, reklam, promosyon
- sosyal: LinkedIn, Twitter bildirimleri
- diger

JSON döndür: {"kategori": "...", "alt_kategori": "..."}
```

---

## Akıllı Filtre

Gereksiz mailleri filtrele:

```
Bu mail kutusundaki gereksiz/düşük öncelikli mailleri belirle:

[mail listesi]

Gereksiz kriterleri:
- Okunmamış promosyon
- Otomatik bildirim
- Artık takip etmediğim konular

Liste halinde döndür: mail ID'leri ve nedenleri
```
