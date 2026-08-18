# RAG (Retrieval-Augmented Generation)

Bilgi getirerek cevap üretme - Claude'u kendi belgelerinle güçlendirme.

---

## Ne İşe Yarar?

Claude'un eğitim verisinde olmayan bilgileri kullanmasını sağlar:
- Şirket içi dokümanlar
- Kişisel belgeler
- Güncel veriler
- Özel bilgi tabanları

"Kendi belgelerine soru sor" sistemi.

---

## Nasıl Çalışır?

1. **İndeksleme:** Belgeleri parçalara böl ve kaydet
2. **Arama:** Kullanıcı sorusuna en alakalı parçaları bul
3. **Cevaplama:** Bulunan parçaları Claude'a ver, cevap oluştur

```
Kullanıcı Sorusu → Arama → İlgili Parçalar → Claude → Cevap
```

---

## Temel Uygulama

```python
def rag_cevapla(soru: str, belgeler: list[str]) -> str:
    # 1. Belgeleri parçala
    parcalar = []
    for belge in belgeler:
        parcalar.extend(parcala(belge, parca_boyutu=500))

    # 2. İlgili parçaları bul
    alakali = ara(soru, parcalar, k=3)

    # 3. Claude'a gönder
    prompt = f"""Bu belge parçalarını kullanarak soruyu cevapla:

{alakali}

Soru: {soru}

Sadece belgelerdeki bilgiye dayanarak cevap ver."""

    return claude_cagir(prompt)
```

---

## Parçalama (Chunking)

Belgeler genelde context window'a sığmayacak kadar uzun. Parçalama stratejileri:

| Strateji | Açıklama |
|----------|----------|
| Sabit boyut | Her parça N karakter |
| Cümle bazlı | Cümle sınırlarında böl |
| Paragraf bazlı | Paragraf sınırlarında böl |
| Semantic | Anlam gruplarına göre böl |

---

## Arama Yöntemleri

| Yöntem | Zorluk | Kalite |
|--------|--------|--------|
| Keyword | Kolay | Düşük |
| TF-IDF | Orta | Orta |
| Embedding | Zor | Yüksek |

Basit projelerde keyword yeterli. Büyük sistemlerde embedding kullan.

---

## İpuçları

1. **Örtüşme:** Parçalar arası biraz örtüşme koy (bağlam için)
2. **Metadata:** Her parçanın hangi belgeden geldiğini tut
3. **Kaynak göster:** Cevabın hangi belgeden geldiğini belirt
4. **Hallucination:** "Bilmiyorum" demeyi öğret

---

## İlgili Projeler

- [04-yonetim-merkezi](../04-yonetim-merkezi/) - Tam RAG implementasyonu

---

## Kaynaklar

- [RAG Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/retrieval-augmented-generation)
