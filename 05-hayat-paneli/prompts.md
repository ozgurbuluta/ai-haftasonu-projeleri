# Örnek Prompt'lar

Hayat Paneli'nde kullanılan ve kullanabileceğin prompt'lar.

---

## Sabah Özeti

```
Sen kişisel bir asistansın. Kullanıcının günlük verilerine bakarak
yararlı bir sabah özeti hazırla.

TARİH: {tarih}
HAVA: {hava}
TAKVİM: {takvim}
GÖREVLER: {gorevler}

Özette şunlar olsun:
1. Günün genel değerlendirmesi
2. Hava durumuna göre öneriler
3. Önceliklendirme önerisi
4. 2-3 somut tavsiye

Samimi ve motive edici ol. Maksimum 300 kelime.
```

---

## Akşam Değerlendirmesi

```
Bugünkü verileri değerlendir:

TAKVİM (planlanan vs gerçekleşen):
{takvim_karsilastirma}

GÖREVLER (tamamlanan / kalan):
{gorev_durumu}

Şunları analiz et:
1. Bugün ne kadar verimli geçti?
2. Hangi görevler kaldı ve neden?
3. Yarın için öğrenilen dersler
4. Kendine notlar

Dürüst ama yapıcı ol.
```

---

## Haftalık Planlama

```
Önümüzdeki haftanın verilerini değerlendir:

TAKVİM:
{haftalik_takvim}

GÖREVLER:
{haftalik_gorevler}

BİLİNEN ETKİNLİKLER:
{bilinen_etkinlikler}

Hazırla:
1. Haftanın en yoğun günleri
2. Boş zaman blokları
3. Öncelik sıralaması
4. Potansiyel çakışmalar
5. Haftalık hedefler önerisi

Tablo formatında özetle.
```

---

## Örüntü Analizi

```
Son 30 günün verilerini analiz et:

VERİLER:
{gecmis_veriler}

Şu örüntüleri bul:
1. En verimli günler/saatler
2. Toplantı yoğunluğu trendi
3. Görev tamamlama oranı
4. Hava durumu - mood ilişkisi (varsa)
5. Tekrar eden engeller

İçgörüleri ve önerileri listele.
```

---

## Bağlam Farkındalığı

Farklı durumlara göre öneriler:

### Yoğun Gün

```
Bugün çok yoğun görünüyor: {etkinlik_sayisi} etkinlik, {gorev_sayisi} görev.

Şunları öner:
- Hangi toplantıları kısaltabilir veya iptal edebilirim?
- Hangi görevler yarına ertelenebilir?
- Gün içinde 15 dakikalık mola ne zaman almalıyım?
```

### Sakin Gün

```
Bugün nispeten sakin: az etkinlik, az görev.

Bu boş zamanı nasıl değerlendirmeliyim?
- Ertelediğim büyük görevler var mı?
- Öğrenme/gelişim için ne yapabilirim?
- Sosyal aktivite önerileri
```

### Hava Değişikliği

```
Hava durumu değişiyor: {onceki} -> {sonraki}

Bu değişiklik programımı nasıl etkiler?
- Dış mekan etkinlikleri risk altında mı?
- Ulaşım planını değiştirmeli miyim?
- Mod/enerji üzerinde beklenen etki
```

---

## Entegrasyon Prompt'ları

### Apple Health / Fitness

```
Bugünkü sağlık verilerini değerlendir:

ADIM: {adim_sayisi}
UYKU: {uyku_suresi}
KALORI: {kalori}

Takvim ve görevlerle birlikte değerlendirince:
- Fiziksel aktivite önerisi
- Enerji yönetimi tavsiyesi
- Mola zamanlaması
```

### Finans Entegrasyonu

```
Bu ayın harcama özeti + takvim:

HARCAMALAR: {harcama_ozeti}
GELİR: {gelir}
TAKVİM: {ozel_etkinlikler}

Şunları değerlendir:
- Önümüzdeki haftada beklenen harcamalar
- Bütçe uyarıları
- Tasarruf fırsatları
```
