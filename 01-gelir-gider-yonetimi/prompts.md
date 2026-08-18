# Örnek Prompt'lar

Bu projede kullanabileceğin prompt'lar.

---

## Temel Harcama Analizi

```
Sen bir harcama analiz asistanısın. Verilen harcama bilgisini analiz edip JSON formatında döndür.

Çıktı formatı:
{
    "tutar": <sayı>,
    "para_birimi": "TRY",
    "tarih": "YYYY-MM-DD",
    "magaza": "<mağaza adı>",
    "kategori": "<kategori>",
    "aciklama": "<kısa açıklama>"
}

Kategoriler: market, restoran, ulasim, eglence, fatura, saglik, diger

Sadece JSON döndür.
```

---

## Görsel Okuma İçin

Fiş fotoğrafı yüklerken kullanılacak prompt:

```
Bu fiş fotoğrafını analiz et. Şu bilgileri çıkar:
- Mağaza adı
- Toplam tutar
- Tarih
- Alınan ürünler (varsa)

JSON formatında döndür.
```

---

## Banka Ekstresi İçin

```
Bu banka ekstresindeki tüm harcamaları listele. Her biri için:
- Tarih
- Açıklama
- Tutar
- Kategori tahmini

JSON array formatında döndür.
```

---

## Bütçe Analizi

```
Bu ayın harcamalarını analiz et:

[harcama listesi]

Şunları hesapla:
1. Kategori bazlı toplam
2. En çok harcama yapılan gün
3. Ortalama günlük harcama
4. Geçen aya göre değişim (varsa)

Kısa bir özet yaz.
```

---

## Tasarruf Önerisi

```
Bu harcama verilerine bakarak:

[harcama listesi]

3 somut tasarruf önerisi ver. Her öneri için:
- Hangi kategoride
- Tahmini aylık tasarruf miktarı
- Nasıl uygulanacağı
```
