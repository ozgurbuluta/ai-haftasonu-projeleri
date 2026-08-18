# Yönetim Merkezi

Kontrat, fatura, sigorta ve diğer kişisel belgelerini yükleyip bunlar hakkında soru sorabildiğin sistem.

---

## Ne Yapıyor?

Bu proje bir RAG (Retrieval-Augmented Generation) sistemi:

1. **Belge yükleme:** PDF veya metin dosyalarını yükle
2. **Parçalama:** Belgeler küçük parçalara bölünür
3. **Arama:** Soruna en uygun parçalar bulunur
4. **Cevaplama:** Claude parçaları kullanarak cevap verir

Örnek sorular:
- "Bu kontratı ne zaman iptal edebilirim?"
- "Sigorta poliçemdeki muafiyet tutarı ne?"
- "Geçen ayki elektrik faturam ne kadardı?"

---

## Öğrenilecekler

| Beceri | Bu Projede |
|--------|------------|
| [RAG](../skills/rag.md) | Bilgi getirme ile cevaplama |
| [Embedding](../skills/embedding.md) | Metin vektörleri (opsiyonel) |
| [Bağlam Yönetimi](../skills/baglam-yonetimi.md) | Context window kullanımı |

---

## Çalıştırma

```bash
cd 04-yonetim-merkezi

# Örnek belgelerle çalıştır
python main.py

# Kendi belgelerinle (PDF)
python main.py --dosya belge.pdf --soru "Sorum nedir?"
```

---

## Kod Açıklaması

### Chunking (Parçalama)

Belgeler doğrudan Claude'a gönderilemeyecek kadar uzun olabilir. Bu yüzden parçalara bölüyoruz:

```python
def parcala(metin: str, parca_boyutu: int = 500) -> list[str]:
    """Metni belirli boyutta parçalara böl."""
    parcalar = []
    for i in range(0, len(metin), parca_boyutu):
        parcalar.append(metin[i:i + parca_boyutu])
    return parcalar
```

### Basit Arama

Bu projede basit keyword arama kullanıyoruz. İleri seviye için embedding eklenebilir.

```python
def en_alakali_parcalar(soru: str, parcalar: list[str], k: int = 3):
    """Soruyla en alakalı parçaları bul."""
    # Basit: soru kelimelerini içeren parçaları bul
    # İleri: embedding similarity kullan
```

### RAG Cevaplama

İlgili parçaları bulduktan sonra Claude'a gönderiyoruz:

```python
prompt = f"""Şu belge parçalarını kullanarak soruyu cevapla:

{parcalar}

Soru: {soru}

Sadece belgelerdeki bilgiye dayanarak cevap ver.
Emin değilsen "Bu bilgi belgelerde yok" de.
"""
```

---

## Örnek Çıktı

```
📁 Yüklenen belgeler: 3
📄 Toplam parça: 24

❓ Soru: Bu kontratı ne zaman iptal edebilirim?

🔍 İlgili parçalar bulunuyor...
   → Parça 7: "...iptal için 30 gün önceden..."
   → Parça 12: "...yıllık yenileme tarihi..."

💬 Cevap:
Kontratı yıllık yenileme tarihinden 30 gün önce
yazılı bildirimle iptal edebilirsiniz. Mevcut
dönem için ücret iadesi yapılmamaktadır.
```

---

## Denemeler

1. **Embedding ekle:** Voyage AI veya OpenAI embedding ile daha iyi arama
2. **Kaynak göster:** Hangi belgeden/sayfadan geldiğini belirt
3. **Çoklu format:** Word, Excel dosyaları desteği
4. **Özet çıkar:** "Bu belgenin özeti nedir?" sorusunu destekle

---

## Embedding Ekleme (Opsiyonel)

Daha doğru sonuçlar için embedding kullanabilirsin:

```python
# Voyage AI ile
from voyageai import Client as VoyageClient

voyage = VoyageClient()
embeddings = voyage.embed(parcalar, model="voyage-2")
```

---

## Kaynaklar

- [RAG Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/retrieval-augmented-generation)
- [PyPDF2 Docs](https://pypdf2.readthedocs.io/)
- [Voyage AI](https://www.voyageai.com/) (embedding için)
