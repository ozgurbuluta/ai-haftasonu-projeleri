# Hayat Paneli

Takvim, hava durumu, görevler ve aktivite verilerini bir araya getirip hayatındaki örüntüleri gösteren kişisel panel.

---

## Ne Yapıyor?

Bu proje farklı veri kaynaklarını bir araya getiriyor:

1. **Veri toplama:** Takvim, hava durumu, görevler
2. **Birleştirme:** Tüm verileri tek bir context'te topla
3. **Analiz:** Claude'a gününü/haftanı özetle
4. **Örüntüler:** Zamanla tekrar eden kalıpları fark et

"Bugün nasıl bir gün?" sorusuna kapsamlı cevap veren bir asistan.

---

## Öğrenilecekler

| Beceri | Bu Projede |
|--------|------------|
| [API Kullanımı](../skills/api-kullanimi.md) | Birden fazla API entegrasyonu |
| [MCP](../skills/mcp.md) | Model Context Protocol |
| [Bağlam Yönetimi](../skills/baglam-yonetimi.md) | Farklı kaynakları birleştirme |

---

## Çalıştırma

```bash
cd 05-hayat-paneli

# Mock verilerle çalıştır
python main.py

# Gerçek hava durumu verisiyle (API key gerekli)
export WEATHER_API_KEY="your_key"
python main.py --gercek-hava
```

---

## Kod Açıklaması

### Connector Yapısı

Her veri kaynağı için bir connector:

```python
# connectors/takvim.py
def takvim_verileri_al() -> list[dict]:
    """Bugünkü etkinlikleri döndür."""
    pass

# connectors/hava.py
def hava_durumu_al(sehir: str) -> dict:
    """Anlık hava durumu."""
    pass
```

### Veri Birleştirme

Tüm connector'lardan gelen veriler tek bir sözlükte toplanıyor:

```python
veriler = {
    "tarih": "2024-01-15",
    "hava": hava_durumu_al("Istanbul"),
    "takvim": takvim_verileri_al(),
    "gorevler": gorevler_al()
}
```

### Context Engineering

Claude'a tüm verileri mantıklı bir sırayla gönderiyoruz:

```python
prompt = f"""
BUGÜN: {veriler['tarih']}
HAVA: {veriler['hava']['durum']}, {veriler['hava']['sicaklik']}°C
TAKVİM: {format_takvim(veriler['takvim'])}
GÖREVLER: {format_gorevler(veriler['gorevler'])}

Bu bilgilere göre bugünümü özetle ve öneriler ver.
"""
```

---

## Örnek Çıktı

```
🌅 GÜNLÜK ÖZET - 15 Ocak 2024, Pazartesi

☀️ Hava: Parçalı bulutlu, 12°C
   → Öğleden sonra yağmur bekleniyor, şemsiye al

📅 Bugünkü Programın:
   09:00 - Takım toplantısı (online)
   14:00 - Müşteri görüşmesi (ofis)
   18:00 - Spor salonu

✅ Öncelikli Görevler:
   • Proje raporu (bugün son gün!)
   • E-postaları cevapla (3 bekliyor)

💡 Öneriler:
   - Müşteri toplantısından önce raporu bitir
   - Toplantı arası 30 dk boş, e-postalar için ideal
   - Hava yağışlı olacak, spor çantanı sabah al
```

---

## Denemeler

1. **Gerçek API'ler:** Google Calendar, Todoist, Apple Health bağla
2. **Haftalık özet:** Pazartesi sabahı haftalık plan oluştur
3. **Geçmiş analizi:** "Geçen ay kaç saat toplantı yaptım?" gibi sorular
4. **Bildirimler:** Önemli değişikliklerde (hava, iptal) uyarı gönder

---

## API Entegrasyonları (Opsiyonel)

### Hava Durumu

```python
# OpenWeatherMap (ücretsiz tier)
import requests

def hava_al(sehir: str) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {"q": sehir, "appid": API_KEY, "units": "metric"}
    return requests.get(url, params=params).json()
```

### Google Calendar

```python
# Google Calendar API
from googleapiclient.discovery import build

service = build('calendar', 'v3', credentials=creds)
events = service.events().list(calendarId='primary').execute()
```

---

## Kaynaklar

- [OpenWeatherMap API](https://openweathermap.org/api)
- [Google Calendar API](https://developers.google.com/calendar)
- [MCP Connectors](https://modelcontextprotocol.io/)
