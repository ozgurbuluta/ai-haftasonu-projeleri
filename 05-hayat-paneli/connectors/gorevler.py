"""
Görev Connector

Gerçek uygulamada Todoist, Things, Notion veya başka bir görev yöneticisine bağlanır.
Bu örnekte simüle edilmiş veri kullanıyoruz.
"""

from datetime import datetime


def gorevler_al(tarih: datetime = None) -> list[dict]:
    """
    Görev listesini döndür.

    Gerçek uygulamada:
    - Todoist API
    - Things API (macOS)
    - Notion API
    - TickTick API
    """

    if tarih is None:
        tarih = datetime.now()

    # Simüle edilmiş görevler
    ornek_gorevler = [
        {
            "baslik": "Proje raporunu tamamla",
            "oncelik": "yuksek",
            "son_tarih": tarih.strftime("%Y-%m-%d"),
            "kategori": "is",
            "tamamlandi": False,
            "notlar": "Finans bölümü eksik"
        },
        {
            "baslik": "E-postaları cevapla",
            "oncelik": "orta",
            "son_tarih": tarih.strftime("%Y-%m-%d"),
            "kategori": "is",
            "tamamlandi": False,
            "notlar": "3 mail bekliyor"
        },
        {
            "baslik": "Market alışverişi",
            "oncelik": "dusuk",
            "son_tarih": tarih.strftime("%Y-%m-%d"),
            "kategori": "kisisel",
            "tamamlandi": False,
            "notlar": "Süt, ekmek, meyve"
        },
        {
            "baslik": "Doktor randevusu al",
            "oncelik": "orta",
            "son_tarih": None,
            "kategori": "saglik",
            "tamamlandi": False,
            "notlar": "Yıllık check-up"
        },
        {
            "baslik": "Fatura öde",
            "oncelik": "yuksek",
            "son_tarih": "2024-01-20",
            "kategori": "finans",
            "tamamlandi": True,
            "notlar": "Elektrik + internet"
        }
    ]

    # Tamamlanmamış görevleri filtrele
    aktif_gorevler = [g for g in ornek_gorevler if not g["tamamlandi"]]

    return aktif_gorevler


def gorevleri_oncelikle(gorevler: list[dict]) -> list[dict]:
    """Görevleri önceliğe göre sırala."""

    oncelik_sirasi = {"yuksek": 0, "orta": 1, "dusuk": 2}

    return sorted(
        gorevler,
        key=lambda g: oncelik_sirasi.get(g["oncelik"], 3)
    )


def bugunku_gorevler(gorevler: list[dict]) -> list[dict]:
    """Sadece bugün bitirilmesi gereken görevleri döndür."""

    bugun = datetime.now().strftime("%Y-%m-%d")

    return [
        g for g in gorevler
        if g.get("son_tarih") == bugun
    ]
