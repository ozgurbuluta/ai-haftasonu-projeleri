# Günlük E-posta Özeti

Mailleri okuyup önemli olanları ayıran, özetleyen ve cevap taslakları hazırlayan sistem.

---

## Ne Yapıyor?

Bu proje bir mail listesini alıp:
1. Her mailin önem derecesini belirliyor (yüksek, orta, düşük)
2. Önemli maillerin kısa özetini çıkarıyor
3. Cevap gerektirenlere taslak hazırlıyor
4. Günlük özet raporu oluşturuyor

---

## Öğrenilecekler

| Beceri | Bu Projede |
|--------|------------|
| [API Kullanımı](../skills/api-kullanimi.md) | Claude API çağrıları |
| [Araç Kullanımı](../skills/arac-kullanimi.md) | Mail işleme araçları |
| [Bağlam Yönetimi](../skills/baglam-yonetimi.md) | Uzun mail zincirlerini yönetme |

---

## Çalıştırma

```bash
# Proje klasörüne git
cd 02-gunluk-e-posta-ozeti

# Çalıştır
python main.py
```

---

## Kod Açıklaması

### Önem Sıralaması

Her mail için Claude'a "Bu mail ne kadar acil?" diye soruyoruz:

```python
- yuksek: Bugün cevap verilmeli, iş kaybı riski
- orta: Bu hafta içinde bakılmalı
- dusuk: Bilgi amaçlı, acil değil
```

### Cevap Taslağı

Sadece önemli mailler için cevap taslağı oluşturuyoruz. Bu sayede:
- API maliyetini düşük tutuyoruz
- Gerçekten önemli işlere odaklanıyoruz

---

## Örnek Çıktı

```
📬 GÜNLÜK MAİL ÖZETİ
====================

🔴 YÜKSEK ÖNCELİK (2)

1. Proje Teslimi Hakkında
   Kimden: ahmet@firma.com
   Özet: Yarın saat 17:00'ye kadar proje dokümanları isteniyor
   
   💬 Taslak Cevap:
   "Merhaba Ahmet, dokümanları yarın öğlene kadar..."

🟡 ORTA ÖNCELİK (3)
...
```

---

## Denemeler

1. **Gerçek mail entegrasyonu:** IMAP ile gerçek maillerini bağla
2. **Zamanlama:** Her sabah 08:00'de otomatik çalıştır (cron)
3. **Slack/Telegram bildirimi:** Özeti mesaj olarak gönder
4. **Konu bazlı gruplama:** Aynı konudaki mailleri grupla

---

## Kaynaklar

- [Claude Messages API](https://docs.anthropic.com/en/api/messages)
- [Python imaplib](https://docs.python.org/3/library/imaplib.html) (gerçek mail için)
