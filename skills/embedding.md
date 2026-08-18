# Embedding

Metni sayısal vektöre çevirme - anlamsal benzerlik hesaplama.

---

## Ne İşe Yarar?

Embedding (metin vektörü) ile:
- Benzer metinleri bulabilirsin
- Semantic arama yapabilirsin
- Metinleri kategorize edebilirsin
- RAG sistemlerinde arama yapabilirsin

"Elma" ve "armut" kelimelerinin "araba"dan daha yakın olduğunu anlarsın.

---

## Nasıl Çalışır?

```
"Merhaba dünya" → [0.1, -0.3, 0.8, ...] (1536 boyutlu vektör)
```

Benzer anlamlı metinler yakın vektörler üretir.

---

## Temel Kullanım (Voyage AI)

```python
from voyageai import Client

voyage = Client()

# Tek metin
embedding = voyage.embed(
    ["Bu bir örnek metin"],
    model="voyage-2"
).embeddings[0]

# Çoklu metin
embeddings = voyage.embed(
    ["Metin 1", "Metin 2", "Metin 3"],
    model="voyage-2"
).embeddings
```

---

## Benzerlik Hesaplama

```python
import numpy as np

def cosine_similarity(vec1, vec2):
    """İki vektör arasındaki benzerlik (0-1)."""
    dot = np.dot(vec1, vec2)
    norm = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    return dot / norm

# Kullanım
skor = cosine_similarity(embedding1, embedding2)
# 0.95 = çok benzer, 0.3 = farklı
```

---

## RAG'da Kullanım

```python
def semantic_ara(soru: str, parcalar: list[dict], k: int = 3):
    # 1. Sorunun embedding'ini al
    soru_emb = embed(soru)

    # 2. Her parça ile benzerlik hesapla
    for parca in parcalar:
        parca["skor"] = cosine_similarity(soru_emb, parca["embedding"])

    # 3. En benzer k parçayı döndür
    return sorted(parcalar, key=lambda x: x["skor"], reverse=True)[:k]
```

---

## Embedding Sağlayıcılar

| Sağlayıcı | Model | Boyut |
|-----------|-------|-------|
| Voyage AI | voyage-2 | 1024 |
| OpenAI | text-embedding-3-small | 1536 |
| Cohere | embed-english-v3 | 1024 |

---

## İpuçları

1. **Önbellek:** Aynı metinleri tekrar embed etme, kaydet
2. **Batch:** Çok metin varsa toplu gönder
3. **Normalize:** Bazı modeller normalize etmiyor, elle yap
4. **Maliyet:** Embedding API'leri genelde ucuz ama dikkat et

---

## İlgili Projeler

- [04-yonetim-merkezi](../04-yonetim-merkezi/) - Opsiyonel embedding

---

## Kaynaklar

- [Voyage AI](https://www.voyageai.com/)
- [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
