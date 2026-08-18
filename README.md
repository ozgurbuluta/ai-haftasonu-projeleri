# AI Haftasonu Projeleri

Yapay zekayı gerçekten öğrenmek istiyorsan, bir hafta sonunda bitirebileceğin 5 proje.

Her proje çalışır Python kodu, detaylı açıklamalar ve örnek prompt'lar içeriyor. Temel Python bilgin varsa hemen başlayabilirsin.

---

## Projeler

### 1. [Gelir-Gider Yönetimi](01-gelir-gider-yonetimi/) 💸

Fişlerini, faturalarını veya banka hareketlerini yükle. Yapay zeka harcamalarını okuyup kategorilere ayırsın.

**Öğrenilecekler:** Görsel okuma, structured output, tool calling

---

### 2. [Günlük E-posta Özeti](02-gunluk-e-posta-ozeti/) 📬

Maillerini okuyup önemli olanları ayırsın, kısa bir özet çıkarsın ve cevap vermen gerekenler için taslak hazırlasın.

**Öğrenilecekler:** API kullanımı, tool calling, context management, otomasyon

---

### 3. [Karar Mercii](03-karar-mercii/) 🧠

Bir problemi tek bir yapay zekaya sormak yerine farklı rollerdeki birkaç ajana ver. Biri savunsun, biri eleştirsin, biri sentezlesin.

**Öğrenilecekler:** Multi-agent sistemler, orchestration, prompting, evaluation

---

### 4. [Yönetim Merkezi](04-yonetim-merkezi/) 🗂️

Kontratlarını, faturalarını, sigorta belgelerini yükle. Sonra kendi belgelerine soru sor: "Bu kontratı ne zaman iptal edebilirim?"

**Öğrenilecekler:** RAG (Retrieval-Augmented Generation), embeddings, chunking, retrieval

---

### 5. [Hayat Paneli](05-hayat-paneli/) 🌤️

Takvimini, hava durumunu, görevlerini tek yerde topla. Zamanla kendi hayatındaki örüntüleri görebileceğin bir sisteme dönüştür.

**Öğrenilecekler:** API entegrasyonu, MCP, veri akışları, context engineering

---

## Başlamadan Önce

Projelere başlamak için [KURULUM.md](KURULUM.md) dosyasını takip et:
- Python 3.10+ kurulumu
- Anthropic API key alma
- Virtual environment oluşturma

---

## Skills (Beceriler)

Her projede kullanılan AI kavramlarını derinlemesine öğrenmek için [skills/](skills/) klasörüne bak:

| Beceri | Açıklama |
|--------|----------|
| [API Kullanımı](skills/api-kullanimi.md) | Claude API'yi nasıl çağırırsın |
| [Araç Kullanımı](skills/arac-kullanimi.md) | Tool calling / function calling |
| [Yapılandırılmış Çıktı](skills/yapilandirilmis-cikti.md) | JSON formatında cevap alma |
| [Görsel Okuma](skills/gorsel-okuma.md) | Vision API ile görsel analizi |
| [RAG](skills/rag.md) | Retrieval-Augmented Generation |
| [Embedding](skills/embedding.md) | Metin vektörleri |
| [Çoklu Ajan](skills/coklu-ajan.md) | Multi-agent sistemler |
| [Bağlam Yönetimi](skills/baglam-yonetimi.md) | Context management |
| [MCP](skills/mcp.md) | Model Context Protocol |
| [Değerlendirme](skills/degerlendirme.md) | AI çıktılarını değerlendirme |

---

## Teknik Terimler Hakkında

Bu repoda teknik kavramları zorla Türkçeleştirmiyoruz. İlk geçtiği yerde açıklıyoruz:

> RAG (Retrieval-Augmented Generation / bilgi getirerek üretim)

Sonrasında orijinal terimi kullanıyoruz. Böylece bu kavramları daha sonra araştırabilirsin.

---

## Katkıda Bulunma

Pull request'ler açık! Özellikle:
- Türkçe açıklamaları iyileştirme
- Yeni örnek prompt'lar ekleme
- Hataları düzeltme

---

## Lisans

MIT
