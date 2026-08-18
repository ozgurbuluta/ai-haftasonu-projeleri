# Çoklu Ajan (Multi-Agent Systems)

Birden fazla AI rolünü koordine etme.

---

## Ne İşe Yarar?

Tek bir AI yerine birden fazla "ajan" kullanmak:
- Farklı bakış açıları sağlar
- Daha kapsamlı analiz yapar
- Hataları yakalar
- Karmaşık görevleri böler

"Tek kişi yerine bir ekip."

---

## Temel Yaklaşımlar

### 1. Rol Bazlı

Her ajan farklı bir uzmanlık:

```python
AJANLAR = {
    "hukuk": "Sen bir avukatsın. Yasal açıdan değerlendir.",
    "finans": "Sen bir muhasebecisın. Mali açıdan değerlendir.",
    "teknik": "Sen bir mühendissin. Teknik açıdan değerlendir."
}
```

### 2. Tartışma Bazlı

Ajanlar birbirinin çıktısını görür:

```
Ajan A: Fikri savun
Ajan B: A'nın argümanlarını eleştir
Ajan C: A ve B'yi sentezle
```

### 3. İş Bölümü

Her ajan bir adımı yapar:

```
Ajan 1: Veri topla
Ajan 2: Analiz et
Ajan 3: Rapor yaz
```

---

## Basit Uygulama

```python
def ajan_calistir(rol: str, gorev: str) -> str:
    """Belirli bir rolle Claude çağır."""
    return client.messages.create(
        model="claude-sonnet-4-20250514",
        system=rol,
        messages=[{"role": "user", "content": gorev}]
    ).content[0].text

# Kullanım
sonuc_a = ajan_calistir(
    "Sen iyimser bir danışmansın.",
    "Bu iş fikrini değerlendir: ..."
)

sonuc_b = ajan_calistir(
    "Sen kötümser bir danışmansın.",
    "Bu iş fikrini değerlendir: ..."
)

# Sonuçları birleştir
final = ajan_calistir(
    "Sen tarafsız bir sentezcisin.",
    f"Bu iki görüşü değerlendir:\n\nİyimser: {sonuc_a}\n\nKötümser: {sonuc_b}"
)
```

---

## Orkestrasyon Kalıpları

| Kalıp | Açıklama |
|-------|----------|
| Sıralı | A → B → C |
| Paralel | A, B, C aynı anda |
| Döngüsel | A → B → A → B (iterasyon) |
| Hiyerarşik | Supervisor + Worker'lar |

---

## İpuçları

1. **Net roller:** Her ajanın görevi açık olmalı
2. **Bağlam paylaş:** Gerekli bilgiyi her ajana ver
3. **Çıktı formatı:** Ajanlar arası iletişim için format belirle
4. **Maliyet:** Her ajan ayrı API çağrısı = maliyet

---

## İlgili Projeler

- [03-karar-mercii](../03-karar-mercii/) - Üç ajanlı karar sistemi

---

## Kaynaklar

- [Agentic Systems](https://docs.anthropic.com/en/docs/build-with-claude/agentic-systems)
