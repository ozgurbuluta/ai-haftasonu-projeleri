"""
Karar Mercii

Farklı perspektiflerden karar değerlendirme sistemi.
"""

import anthropic
from dotenv import load_dotenv
from agents import SAVUNUCU, ELESTIRMEN, SENTEZCI

load_dotenv()

client = anthropic.Anthropic()


def ajan_calistir(sistem_promptu: str, kullanici_mesaji: str) -> str:
    """Tek bir ajanı çalıştır ve cevabını al."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        system=sistem_promptu,
        messages=[{"role": "user", "content": kullanici_mesaji}]
    )

    return response.content[0].text


def karar_degerlendir(karar: str) -> dict:
    """Bir kararı tüm ajanlarla değerlendir."""

    print("🎯 Karar değerlendiriliyor...\n")

    # 1. Savunucu görüşü
    print("👍 Savunucu düşünüyor...")
    savunucu_gorusu = ajan_calistir(
        SAVUNUCU,
        f"Bu kararı değerlendir:\n\n{karar}"
    )

    # 2. Eleştirmen görüşü
    print("👎 Eleştirmen düşünüyor...")
    elestirmen_gorusu = ajan_calistir(
        ELESTIRMEN,
        f"Bu kararı değerlendir:\n\n{karar}"
    )

    # 3. Sentezci her iki görüşü alıp sonuç çıkarır
    print("⚖️ Sentezci değerlendiriyor...")
    sentez_promptu = f"""Değerlendirilecek karar:
{karar}

SAVUNUCU GÖRÜŞÜ:
{savunucu_gorusu}

ELEŞTİRMEN GÖRÜŞÜ:
{elestirmen_gorusu}

Bu iki görüşü değerlendirip dengeli bir sonuç çıkar."""

    sentez = ajan_calistir(SENTEZCI, sentez_promptu)

    return {
        "karar": karar,
        "savunucu": savunucu_gorusu,
        "elestirmen": elestirmen_gorusu,
        "sentez": sentez
    }


def sonuclari_yazdir(sonuclar: dict):
    """Sonuçları güzel formatla yazdır."""

    print("\n" + "=" * 60)
    print("🎯 KARAR")
    print("=" * 60)
    print(sonuclar["karar"])

    print("\n" + "-" * 60)
    print("👍 SAVUNUCU")
    print("-" * 60)
    print(sonuclar["savunucu"])

    print("\n" + "-" * 60)
    print("👎 ELEŞTİRMEN")
    print("-" * 60)
    print(sonuclar["elestirmen"])

    print("\n" + "=" * 60)
    print("⚖️ SENTEZ VE ÖNERİ")
    print("=" * 60)
    print(sonuclar["sentez"])
    print("=" * 60)


# Örnek kararlar
ORNEK_KARARLAR = [
    "Şirketteki işimi bırakıp kendi startup'ımı kurmalı mıyım?",
    "Yazılım geliştirme yerine ürün yöneticiliğine geçmeli miyim?",
    "İstanbul'dan taşınıp uzaktan çalışarak Antalya'ya yerleşmeli miyim?",
]


def main():
    print("=" * 60)
    print("🧠 KARAR MERCİİ")
    print("Farklı perspektiflerden karar değerlendirme")
    print("=" * 60)
    print()

    # Örnek bir karar seç veya kullanıcıdan al
    print("Örnek kararlar:")
    for i, karar in enumerate(ORNEK_KARARLAR, 1):
        print(f"  {i}. {karar}")
    print()

    # İlk örneği kullan (veya input() ile kullanıcıdan al)
    secilen_karar = ORNEK_KARARLAR[0]
    print(f"Seçilen: {secilen_karar}\n")

    # Değerlendirmeyi çalıştır
    sonuclar = karar_degerlendir(secilen_karar)

    # Sonuçları yazdır
    sonuclari_yazdir(sonuclar)


if __name__ == "__main__":
    main()
