# Görsel Okuma (Vision)

Claude'a resim gönderip analiz ettirme.

---

## Ne İşe Yarar?

Claude Vision ile:
- Fotoğraftaki metni okuyabilirsin (OCR)
- Görsel içeriği tanımlayabilirsin
- Diyagram/grafik analizi yapabilirsin
- Fiş/fatura/belge okuyabilirsin

---

## Temel Kullanım

```python
import anthropic
import base64

client = anthropic.Anthropic()

# Görseli base64'e çevir
def gorsel_yukle(dosya_yolu: str) -> str:
    with open(dosya_yolu, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")

gorsel_data = gorsel_yukle("fis.png")

# Claude'a gönder
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": gorsel_data
                    }
                },
                {
                    "type": "text",
                    "text": "Bu fişi oku ve JSON formatında döndür."
                }
            ]
        }
    ]
)
```

---

## Desteklenen Formatlar

| Format | Media Type |
|--------|------------|
| PNG | `image/png` |
| JPEG | `image/jpeg` |
| GIF | `image/gif` |
| WebP | `image/webp` |

---

## URL ile Görsel

Dosya yerine URL de kullanabilirsin:

```python
content = [
    {
        "type": "image",
        "source": {
            "type": "url",
            "url": "https://example.com/gorsel.png"
        }
    },
    {
        "type": "text",
        "text": "Bu görselde ne var?"
    }
]
```

---

## İpuçları

1. **Kalite önemli:** Bulanık görseller zor okunur
2. **Boyut:** Çok büyük görseller token harcar
3. **Spesifik ol:** "Ne görüyorsun?" yerine "Fiyatı bul" de
4. **Birden fazla:** Aynı mesajda birden fazla görsel gönderebilirsin

---

## Örnek Kullanımlar

- **Fiş okuma:** Tutar, tarih, mağaza çıkarma
- **Belge analizi:** Form, kontrat okuma
- **Ürün tanıma:** Fotoğraftan ürün bilgisi
- **Grafik okuma:** Chart'tan veri çıkarma

---

## İlgili Projeler

- [01-gelir-gider-yonetimi](../01-gelir-gider-yonetimi/) - Fiş/fatura okuma

---

## Kaynaklar

- [Vision Docs](https://docs.anthropic.com/en/docs/build-with-claude/vision)
