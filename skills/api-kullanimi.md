# API Kullanımı

Claude API (Anthropic API) ile programatik olarak Claude'u çağırma.

---

## Ne İşe Yarar?

API (Application Programming Interface) sayesinde:
- Kendi uygulamandan Claude'u çağırabilirsin
- Otomatik işlemler yapabilirsin
- Claude'u diğer sistemlerle entegre edebilirsin

ChatGPT veya Claude.ai web arayüzü yerine kodla konuşuyorsun.

---

## Temel Kullanım

```python
import anthropic

# Client oluştur (API key environment variable'dan alınır)
client = anthropic.Anthropic()

# Mesaj gönder
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Merhaba Claude!"}
    ]
)

# Cevabı al
print(response.content[0].text)
```

---

## Önemli Parametreler

| Parametre | Açıklama |
|-----------|----------|
| `model` | Hangi Claude modeli (sonnet, opus, haiku) |
| `max_tokens` | Maksimum cevap uzunluğu |
| `messages` | Konuşma geçmişi |
| `system` | System prompt (Claude'un rolü) |
| `temperature` | Yaratıcılık seviyesi (0-1) |

---

## System Prompt

Claude'a bir rol vermek için:

```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system="Sen bir finans uzmanısın. Kısa ve net cevaplar ver.",
    messages=[
        {"role": "user", "content": "Enflasyon nedir?"}
    ]
)
```

---

## Çok Turlu Konuşma

Önceki mesajları hatırlatmak için `messages` listesine ekle:

```python
messages = [
    {"role": "user", "content": "Benim adım Ahmet."},
    {"role": "assistant", "content": "Merhaba Ahmet! Nasıl yardımcı olabilirim?"},
    {"role": "user", "content": "Benim adım neydi?"}
]

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=100,
    messages=messages
)
# Cevap: "Adınız Ahmet."
```

---

## İlgili Projeler

- [01-gelir-gider-yonetimi](../01-gelir-gider-yonetimi/) - Temel API çağrısı
- [02-gunluk-e-posta-ozeti](../02-gunluk-e-posta-ozeti/) - System prompt kullanımı
- [05-hayat-paneli](../05-hayat-paneli/) - Uzun context yönetimi

---

## Kaynaklar

- [Anthropic API Docs](https://docs.anthropic.com/en/api/messages)
- [Python SDK](https://github.com/anthropics/anthropic-sdk-python)
- [API Pricing](https://www.anthropic.com/pricing)
