"""
Takvim Connector

Gerçek uygulamada Google Calendar veya başka bir takvim API'sine bağlanır.
Bu örnekte simüle edilmiş veri kullanıyoruz.
"""

from datetime import datetime, timedelta


def takvim_verileri_al(tarih: datetime = None) -> list[dict]:
    """
    Belirli bir günün takvim etkinliklerini döndür.

    Gerçek uygulamada:
    - Google Calendar API
    - Microsoft Outlook API
    - Apple Calendar
    - iCal dosyası
    """

    if tarih is None:
        tarih = datetime.now()

    # Simüle edilmiş takvim verileri
    ornek_etkinlikler = [
        {
            "baslik": "Takım Toplantısı",
            "baslangic": "09:00",
            "bitis": "10:00",
            "konum": "Online - Zoom",
            "tur": "toplanti",
            "notlar": "Sprint planning görüşülecek"
        },
        {
            "baslik": "Müşteri Görüşmesi",
            "baslangic": "14:00",
            "bitis": "15:00",
            "konum": "Ofis - Toplantı Odası A",
            "tur": "toplanti",
            "notlar": "Yeni proje teklifi sunumu"
        },
        {
            "baslik": "Öğle Yemeği",
            "baslangic": "12:30",
            "bitis": "13:30",
            "konum": None,
            "tur": "kisisel",
            "notlar": None
        },
        {
            "baslik": "Spor Salonu",
            "baslangic": "18:00",
            "bitis": "19:30",
            "konum": "FitLife Gym",
            "tur": "kisisel",
            "notlar": "Bacak günü"
        }
    ]

    return ornek_etkinlikler


def bos_araliklari_bul(etkinlikler: list[dict]) -> list[dict]:
    """Takvimde boş zamanları bul."""

    # Basit implementasyon: çalışma saatleri içindeki boşluklar
    calisma_baslangic = 9
    calisma_bitis = 18

    # Etkinlikleri saate göre sırala
    dolu_saatler = set()
    for etkinlik in etkinlikler:
        baslangic = int(etkinlik["baslangic"].split(":")[0])
        bitis = int(etkinlik["bitis"].split(":")[0])
        for saat in range(baslangic, bitis):
            dolu_saatler.add(saat)

    bos_araliklar = []
    for saat in range(calisma_baslangic, calisma_bitis):
        if saat not in dolu_saatler:
            bos_araliklar.append({
                "baslangic": f"{saat:02d}:00",
                "bitis": f"{saat+1:02d}:00"
            })

    return bos_araliklar
