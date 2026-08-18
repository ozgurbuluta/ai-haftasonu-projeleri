# Örnek Prompt'lar

Yönetim Merkezi'nde kullanılan ve kullanabileceğin prompt'lar.

---

## RAG Cevaplama Prompt'u

```
Aşağıdaki belge parçalarını kullanarak soruyu cevapla.

BELGELER:
{belgeler}

SORU: {soru}

KURALLAR:
- Sadece belgelerdeki bilgiye dayanarak cevap ver
- Tahminde bulunma, emin değilsen "Bu bilgi belgelerde yok" de
- Cevabı kısa ve net tut
- Varsa ilgili madde numarasını belirt
```

---

## Belge Özeti

```
Bu belgeyi özetle:

{belge}

Özette şunlar olsun:
1. Belge türü (kontrat, fatura, poliçe, vb.)
2. Taraflar
3. Önemli tarihler
4. Anahtar maddeler/tutarlar
5. Dikkat edilecekler

Maksimum 200 kelime.
```

---

## Belge Karşılaştırma

```
Bu iki belgeyi karşılaştır:

BELGE 1:
{belge1}

BELGE 2:
{belge2}

Karşılaştırma kriterleri:
- Fiyat/tutar farkları
- Süre farkları
- Kapsam farkları
- Avantaj/dezavantajlar

Tablo formatında özetle.
```

---

## Kritik Tarih Çıkarma

```
Bu belgeden tüm önemli tarihleri çıkar:

{belge}

Her tarih için:
- Tarih
- Ne için (son ödeme, yenileme, iptal süresi, vb.)
- Kaçırırsam ne olur

JSON formatında döndür.
```

---

## Maddeler Arası Çelişki Kontrolü

```
Bu belgedeki maddeleri incele ve olası çelişkileri bul:

{belge}

Kontrol et:
- Süre tutarsızlıkları
- Tutar tutarsızlıkları
- Karşılıklı çelişen maddeler
- Belirsiz ifadeler

Sorunları listele ve önerilerde bulun.
```

---

## Yasal Terim Açıklama

```
Bu belgede geçen yasal terimleri basit Türkçeyle açıkla:

{belge}

Format:
- **Terim**: [tanım] → [basit açıklama]

Örnek:
- **Muafiyet**: Sigorta kapsamı dışında kalan tutar → İlk X TL'yi sen ödersin
```

---

## Yenileme Hatırlatıcı

```
Bu belgeleri analiz et ve önümüzdeki 90 gün içinde yapılması gerekenleri listele:

{belgeler}

Her madde için:
- Tarih
- Belge adı
- Ne yapılmalı
- Yapılmazsa sonuç

Takvim formatında döndür.
```

---

## Fiyat Analizi

```
Bu belgelerdeki tüm finansal yükümlülükleri çıkar:

{belgeler}

Kategorile:
- Aylık sabit giderler
- Yıllık ödemeler
- Tek seferlik ödemeler
- Değişken giderler

Toplam aylık ve yıllık maliyeti hesapla.
```
