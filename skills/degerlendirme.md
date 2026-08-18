# Değerlendirme (Evaluation)

AI çıktılarının kalitesini ölçme.

---

## Ne İşe Yarar?

Değerlendirme olmadan:
- "Bu cevap iyi mi?" bilemezsin
- Geliştirmeleri ölçemezsin
- Üretimde sorunları farkedemezsin

"Yapay zekanın not defteri."

---

## Değerlendirme Türleri

### 1. İnsan Değerlendirmesi

En güvenilir ama yavaş ve pahalı:

```
Cevap kalitesi: ⭐⭐⭐⭐☆ (4/5)
Doğruluk: ⭐⭐⭐⭐⭐ (5/5)
Faydalılık: ⭐⭐⭐☆☆ (3/5)
```

### 2. Otomatik Metrikler

Hızlı ama yüzeysel:

```python
# BLEU, ROUGE gibi metrikler
from rouge_score import rouge_scorer

scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'])
scores = scorer.score(referans, tahmin)
```

### 3. LLM-as-Judge

Claude'u değerlendirici olarak kullan:

```python
def degerlendir(soru: str, cevap: str) -> dict:
    prompt = f"""Bu cevabı değerlendir:

Soru: {soru}
Cevap: {cevap}

1-5 arası puanla:
- Doğruluk: Bilgi doğru mu?
- Bütünlük: Soru tam cevaplandı mı?
- Netlik: Anlaşılır mı?

JSON döndür: {{"dogruluk": X, "butunluk": Y, "netlik": Z}}"""

    return claude_cagir(prompt)
```

---

## Değerlendirme Kriterleri

| Kriter | Açıklama |
|--------|----------|
| Doğruluk | Bilgi faktüel olarak doğru mu? |
| Alakalılık | Soruya uygun mu? |
| Bütünlük | Eksik bilgi var mı? |
| Tutarlılık | Çelişki var mı? |
| Güvenlik | Zararlı içerik var mı? |

---

## Test Seti Oluşturma

```python
test_seti = [
    {
        "soru": "Türkiye'nin başkenti neresi?",
        "beklenen": "Ankara",
        "kategori": "bilgi"
    },
    {
        "soru": "2+2 kaç eder?",
        "beklenen": "4",
        "kategori": "matematik"
    }
]

# Test et
sonuclar = []
for test in test_seti:
    cevap = claude_cagir(test["soru"])
    dogru = test["beklenen"].lower() in cevap.lower()
    sonuclar.append({"test": test, "cevap": cevap, "dogru": dogru})
```

---

## İpuçları

1. **Çeşitlilik:** Farklı türde sorular test et
2. **Edge case:** Zor durumları dahil et
3. **Baseline:** Karşılaştırma için referans tut
4. **Sürekli:** Düzenli olarak değerlendir

---

## İlgili Projeler

- [03-karar-mercii](../03-karar-mercii/) - Ajan çıktılarını değerlendirme

---

## Kaynaklar

- [Anthropic Eval](https://docs.anthropic.com/en/docs/build-with-claude/develop-tests)
