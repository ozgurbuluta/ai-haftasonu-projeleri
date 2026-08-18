# Karar Mercii

Bir kararı farklı bakış açılarına sahip yapay zeka ajanlarına tartıştıran sistem.

---

## Ne Yapıyor?

Bir problemi tek bir AI'a sormak yerine birden fazla "ajan" kullanıyoruz:

1. **Savunucu:** Fikri destekler, avantajlarını ortaya koyar
2. **Eleştirmen:** Riskleri ve dezavantajları gösterir
3. **Sentezci:** Her iki tarafı dinleyip dengeli bir sonuç çıkarır

Bu yaklaşım daha kapsamlı ve dengeli kararlar almana yardımcı olur.

---

## Öğrenilecekler

| Beceri | Bu Projede |
|--------|------------|
| [Çoklu Ajan](../skills/coklu-ajan.md) | Birden fazla AI rolü yönetme |
| [API Kullanımı](../skills/api-kullanimi.md) | Sıralı API çağrıları |
| [Değerlendirme](../skills/degerlendirme.md) | AI çıktılarını değerlendirme |

---

## Çalıştırma

```bash
cd 03-karar-mercii
python main.py
```

---

## Kod Açıklaması

### Ajan Tanımları

Her ajan farklı bir system prompt ile tanımlanıyor:

```python
AJANLAR = {
    "savunucu": "Sen bir savunucu avukatsın. Verilen fikrin...",
    "elestirmen": "Sen şüpheci bir analistin. Her fikrin...",
    "sentezci": "Sen tarafsız bir arabulucusun..."
}
```

### Sıralı Çağrı

Ajanlar sırayla çağrılıyor çünkü:
1. Savunucu ve Eleştirmen birbirinden bağımsız çalışır
2. Sentezci ikisinin çıktısını bekler

```python
savunucu_gorusu = savunucu_ajan(karar)
elestirmen_gorusu = elestirmen_ajan(karar)
sonuc = sentezci_ajan(karar, savunucu_gorusu, elestirmen_gorusu)
```

---

## Örnek Çıktı

```
🎯 KARAR: "Şirketi bırakıp kendi işimi kurmalı mıyım?"

👍 SAVUNUCU:
Kendi işini kurmak özgürlük ve sınırsız büyüme potansiyeli
sunar. Kendi vizyonunu gerçekleştirebilir...

👎 ELEŞTİRMEN:
Finansal risk yüksek. İlk 2 yılda startupların %90'ı
başarısız oluyor. Düzenli gelir kaybı...

⚖️ SENTEZCİ:
Her iki tarafı değerlendirdiğimde önerim şu:
6 aylık acil durum fonu biriktir, ardından...
```

---

## Denemeler

1. **Yeni ajanlar:** "Risk Analisti", "Pazar Uzmanı" gibi roller ekle
2. **Paralel çalıştırma:** asyncio ile ajanları eşzamanlı çalıştır
3. **Puanlama:** Her ajan fikrini 1-10 arası puanlasın
4. **Tarihçe:** Önceki kararları ve sonuçlarını kaydet

---

## Kaynaklar

- [Claude System Prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching#system-prompts)
- [Multi-Agent Patterns](https://docs.anthropic.com/en/docs/build-with-claude/agentic-systems)
