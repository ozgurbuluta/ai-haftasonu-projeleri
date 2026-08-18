# Bağlam Yönetimi (Context Management)

Context window'u etkili kullanma.

---

## Ne İşe Yarar?

Claude'un bir seferde işleyebildiği metin sınırlı (context window). Bağlam yönetimi ile:
- Uzun belgeleri işleyebilirsin
- Konuşma geçmişini tutabilirsin
- Birden fazla kaynağı birleştirebilirsin
- Maliyeti optimize edebilirsin

---

## Context Window Nedir?

```
┌─────────────────────────────────────┐
│  System Prompt                      │
│  + Önceki Mesajlar                  │
│  + Yeni Mesaj                       │  ← Context Window
│  + Claude'un Cevabı                 │     (örn: 200K token)
└─────────────────────────────────────┘
```

Her şey bu pencereye sığmalı.

---

## Token Sayımı

Kaba hesap: 1 token ≈ 4 karakter (İngilizce), Türkçe'de biraz daha az.

```python
# Kaba tahmin
def token_tahmin(metin: str) -> int:
    return len(metin) // 3  # Türkçe için

# Gerçek sayım için anthropic SDK
response = client.messages.count_tokens(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": metin}]
)
print(response.input_tokens)
```

---

## Stratejiler

### 1. Özetleme

Uzun geçmişi özetle:

```python
def gecmisi_ozetle(mesajlar: list) -> str:
    # Eski mesajları Claude'a özetlet
    ozet = claude_cagir(
        f"Bu konuşmayı 2 cümleyle özetle: {mesajlar}"
    )
    return ozet
```

### 2. Sliding Window

Son N mesajı tut:

```python
MAX_MESAJ = 10

def mesaj_ekle(yeni_mesaj):
    mesajlar.append(yeni_mesaj)
    if len(mesajlar) > MAX_MESAJ:
        mesajlar.pop(0)  # En eski mesajı sil
```

### 3. Seçici Dahil Etme

Sadece ilgili bilgiyi dahil et:

```python
# RAG yaklaşımı
alakali_parcalar = ara(soru, tum_belgeler)
# Sadece alakalı parçaları context'e ekle
```

---

## İpuçları

1. **System prompt kısa tut:** Gereksiz detay ekleme
2. **Tekrar etme:** Aynı bilgiyi birden fazla yerde verme
3. **Lazy loading:** Bilgiyi gerektiğinde yükle
4. **Öncelik:** Önemli bilgi başta olsun

---

## Maliyet İlişkisi

```
Daha fazla token = Daha yüksek maliyet
```

Gereksiz context eklemekten kaçın.

---

## İlgili Projeler

- [02-gunluk-e-posta-ozeti](../02-gunluk-e-posta-ozeti/) - Mail zinciri yönetimi
- [05-hayat-paneli](../05-hayat-paneli/) - Çoklu kaynak birleştirme

---

## Kaynaklar

- [Long Context](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
