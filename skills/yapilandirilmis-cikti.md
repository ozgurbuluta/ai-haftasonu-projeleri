# Yapılandırılmış Çıktı (Structured Output)

Claude'dan düz metin yerine JSON formatında cevap alma.

---

## Ne İşe Yarar?

Normal cevap:
> "Toplam tutar 156.50 TL, tarih 15 Ocak 2024, mağaza Migros."

Yapılandırılmış cevap:
```json
{
  "tutar": 156.50,
  "tarih": "2024-01-15",
  "magaza": "Migros"
}
```

Yapılandırılmış çıktı ile:
- Veriyi programatik olarak işleyebilirsin
- Veritabanına kaydedebilirsin
- Başka sistemlere gönderebilirsin

---

## Yöntem 1: Prompt ile

En basit yöntem - prompt'ta JSON isteme:

```python
prompt = """Bu harcamayı analiz et: "Migros - 156.50 TL"

JSON formatında döndür:
{
    "tutar": <sayı>,
    "magaza": "<isim>"
}

Sadece JSON döndür, başka bir şey yazma."""

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=256,
    messages=[{"role": "user", "content": prompt}]
)

# Parse et
import json
data = json.loads(response.content[0].text)
print(data["tutar"])  # 156.50
```

---

## Yöntem 2: Tool ile (Daha Güvenilir)

Araç tanımı kullanarak şema zorla:

```python
tools = [{
    "name": "harcama_kaydet",
    "description": "Harcama bilgisini kaydeder",
    "input_schema": {
        "type": "object",
        "properties": {
            "tutar": {"type": "number"},
            "magaza": {"type": "string"},
            "kategori": {
                "type": "string",
                "enum": ["market", "restoran", "ulasim", "diger"]
            }
        },
        "required": ["tutar", "magaza", "kategori"]
    }
}]
```

Bu yöntemde Claude şemaya uymak zorunda.

---

## İpuçları

1. **Örnek ver:** Prompt'ta istediğin formatın örneğini göster
2. **Strict ol:** "Sadece JSON döndür" de
3. **Parse et:** `json.loads()` ile Python dict'e çevir
4. **Hata yakala:** Bazen format bozuk olabilir

```python
try:
    data = json.loads(response.content[0].text)
except json.JSONDecodeError:
    # Hata durumunda ne yapılacak
    pass
```

---

## İlgili Projeler

- [01-gelir-gider-yonetimi](../01-gelir-gider-yonetimi/) - Harcama JSON'u

---

## Kaynaklar

- [Structured Output Docs](https://docs.anthropic.com/en/docs/build-with-claude/structured-output)
