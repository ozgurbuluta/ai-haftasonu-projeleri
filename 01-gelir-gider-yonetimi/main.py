"""
Gelir-Gider Yönetimi

Harcama metinlerini okuyup kategorize eden uygulama.
"""

import json
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

# Örnek harcama verileri (gerçek uygulamada bunlar fiş/fatura olacak)
ORNEK_HARCAMALAR = [
    "Migros Ataşehir - 156.50 TL - 15.01.2024 - Market alışverişi",
    "Uber - 45.00 TL - 15.01.2024 - Kadıköy'den Beşiktaş'a",
    "Netflix - 99.99 TL - 01.01.2024 - Aylık abonelik",
    "Eczane Sağlık - 234.00 TL - 14.01.2024 - İlaç alımı",
    "Starbucks - 78.00 TL - 15.01.2024 - Kahve ve tatlı",
]

SISTEM_PROMPTU = """Sen bir harcama analiz asistanısın. Verilen harcama bilgisini analiz edip JSON formatında döndür.

Çıktı formatı:
{
    "tutar": <sayı>,
    "para_birimi": "TRY",
    "tarih": "YYYY-MM-DD",
    "magaza": "<mağaza adı>",
    "kategori": "<kategori>",
    "aciklama": "<kısa açıklama>"
}

Kategoriler (sadece bunlardan birini seç):
- market: Süpermarket, bakkal, manav
- restoran: Yeme-içme, kafe, fast-food
- ulasim: Taksi, toplu taşıma, benzin
- eglence: Sinema, konser, abonelikler (Netflix, Spotify)
- fatura: Elektrik, su, doğalgaz, internet
- saglik: Eczane, hastane, doktor
- diger: Yukarıdakilere uymayan

Sadece JSON döndür, başka bir şey yazma."""


def harcama_analiz_et(harcama_metni: str) -> dict:
    """Tek bir harcamayı analiz et ve yapılandırılmış veri döndür."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=256,
        messages=[
            {"role": "user", "content": harcama_metni}
        ],
        system=SISTEM_PROMPTU
    )

    # Claude'un cevabını JSON olarak parse et
    cevap_metni = response.content[0].text
    return json.loads(cevap_metni)


def tum_harcamalari_analiz_et(harcamalar: list[str]) -> list[dict]:
    """Birden fazla harcamayı analiz et."""
    sonuclar = []

    for harcama in harcamalar:
        print(f"Analiz ediliyor: {harcama[:50]}...")
        sonuc = harcama_analiz_et(harcama)
        sonuclar.append(sonuc)
        print(f"  → {sonuc['kategori']}: {sonuc['tutar']} {sonuc['para_birimi']}")

    return sonuclar


def kategori_ozeti(harcamalar: list[dict]) -> dict:
    """Kategori bazlı toplam hesapla."""
    ozet = {}

    for h in harcamalar:
        kategori = h["kategori"]
        tutar = h["tutar"]

        if kategori not in ozet:
            ozet[kategori] = 0
        ozet[kategori] += tutar

    return ozet


def main():
    print("=" * 50)
    print("Gelir-Gider Yönetimi")
    print("=" * 50)
    print()

    # Tüm harcamaları analiz et
    print("Harcamalar analiz ediliyor...\n")
    sonuclar = tum_harcamalari_analiz_et(ORNEK_HARCAMALAR)

    # Detaylı sonuçları göster
    print("\n" + "=" * 50)
    print("Detaylı Sonuçlar")
    print("=" * 50)
    print(json.dumps(sonuclar, indent=2, ensure_ascii=False))

    # Kategori özeti
    print("\n" + "=" * 50)
    print("Kategori Özeti")
    print("=" * 50)
    ozet = kategori_ozeti(sonuclar)

    toplam = 0
    for kategori, tutar in sorted(ozet.items(), key=lambda x: x[1], reverse=True):
        print(f"  {kategori:12} : {tutar:>10.2f} TL")
        toplam += tutar

    print("-" * 30)
    print(f"  {'TOPLAM':12} : {toplam:>10.2f} TL")


if __name__ == "__main__":
    main()
