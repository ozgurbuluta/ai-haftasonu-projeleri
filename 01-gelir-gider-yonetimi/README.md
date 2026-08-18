# Gelir-Gider Yönetimi

Fiş, fatura ve banka hareketlerini okuyup harcamalarını kategorize eden uygulama.

---

## Ne Yapıyor?

Bu proje bir harcama metnini (veya görselini) alıp:
1. İçindeki bilgileri çıkarıyor (tutar, tarih, mağaza)
2. Otomatik kategorize ediyor (market, ulaşım, eğlence, vb.)
3. Yapılandırılmış JSON formatında döndürüyor

---

## Öğrenilecekler

| Beceri | Bu Projede |
|--------|------------|
| [Görsel Okuma](../skills/gorsel-okuma.md) | Fiş fotoğrafından bilgi çıkarma |
| [Yapılandırılmış Çıktı](../skills/yapilandirilmis-cikti.md) | JSON formatında cevap alma |
| [Araç Kullanımı](../skills/arac-kullanimi.md) | Claude'a araç tanımlama |

---

## Çalıştırma

```bash
# Proje klasörüne git
cd 01-gelir-gider-yonetimi

# Çalıştır
python main.py
```

---

## Kod Açıklaması

### Structured Output

Claude'dan düz metin yerine JSON formatında cevap almak için `response_format` kullanıyoruz:

```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[...],
    # Claude'a JSON döndürmesini söylüyoruz
    response_format={"type": "json"}
)
```

### Kategori Sistemi

Prompt'ta kategorileri açıkça tanımlıyoruz:

```
Kategoriler: market, restoran, ulasim, eglence, fatura, saglik, diger
```

Claude bu kategorilerden birini seçmek zorunda kalıyor.

---

## Örnek Çıktı

```json
{
  "tutar": 156.50,
  "para_birimi": "TRY",
  "tarih": "2024-01-15",
  "magaza": "Migros",
  "kategori": "market",
  "aciklama": "Haftalık market alışverişi"
}
```

---

## Denemeler

Projeyi geliştirmek için şunları deneyebilirsin:

1. **Görsel okuma ekle:** `main.py`'deki metin yerine gerçek fiş fotoğrafı yükle
2. **Çoklu harcama:** Bir banka ekstresinden tüm harcamaları çıkar
3. **Özet rapor:** Ay sonunda kategori bazlı toplam harcama hesapla
4. **Bütçe uyarısı:** Bir kategoride limit aşılınca uyar

---

## Kaynaklar

- [Claude Vision API](https://docs.anthropic.com/en/docs/build-with-claude/vision)
- [Structured Output](https://docs.anthropic.com/en/docs/build-with-claude/structured-output)
