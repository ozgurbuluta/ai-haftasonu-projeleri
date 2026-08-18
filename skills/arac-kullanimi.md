# Araç Kullanımı (Tool Calling)

Claude'a araçlar tanımlayıp kullanmasını sağlama.

---

## Ne İşe Yarar?

Tool calling (araç çağırma) ile Claude:
- Hesap makinesi kullanabilir
- Veritabanı sorgulayabilir
- API çağrısı yapabilir
- Dosya okuyabilir

Claude "ne yapılmalı" karar verir, sen "nasıl yapılacağını" kodlarsın.

---

## Nasıl Çalışır?

1. Claude'a hangi araçların mevcut olduğunu söylersin
2. Claude cevap verirken araç çağırmaya karar verebilir
3. Sen aracı çalıştırırsın
4. Sonucu Claude'a geri gönderirsin
5. Claude son cevabı oluşturur

---

## Temel Kullanım

```python
import anthropic
import json

client = anthropic.Anthropic()

# Araç tanımı
tools = [
    {
        "name": "hesap_makinesi",
        "description": "Matematiksel işlemler yapar",
        "input_schema": {
            "type": "object",
            "properties": {
                "islem": {
                    "type": "string",
                    "description": "Yapılacak işlem: toplama, cikarma, carpma, bolme"
                },
                "sayi1": {"type": "number"},
                "sayi2": {"type": "number"}
            },
            "required": ["islem", "sayi1", "sayi2"]
        }
    }
]

# Claude'u çağır
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    tools=tools,
    messages=[
        {"role": "user", "content": "156 ile 87'yi topla"}
    ]
)

# Claude araç çağırdı mı kontrol et
if response.stop_reason == "tool_use":
    tool_use = response.content[1]  # Tool use block
    tool_name = tool_use.name
    tool_input = tool_use.input

    # Aracı çalıştır
    if tool_name == "hesap_makinesi":
        sonuc = tool_input["sayi1"] + tool_input["sayi2"]

    # Sonucu Claude'a gönder
    # (devam eden mesajlarla)
```

---

## Örnek Araçlar

| Araç | Kullanım |
|------|----------|
| `hava_durumu_al` | Şehrin hava durumunu getir |
| `mail_gonder` | E-posta gönder |
| `veritabani_sorgula` | SQL sorgusu çalıştır |
| `dosya_oku` | Dosya içeriğini oku |

---

## İlgili Projeler

- [01-gelir-gider-yonetimi](../01-gelir-gider-yonetimi/) - Kategori aracı
- [02-gunluk-e-posta-ozeti](../02-gunluk-e-posta-ozeti/) - Mail işleme araçları

---

## Kaynaklar

- [Tool Use Docs](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
