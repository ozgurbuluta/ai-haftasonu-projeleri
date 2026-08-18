"""
Hayat Paneli

Günlük verileri toplayıp kişiselleştirilmiş özet üreten asistan.
"""

import anthropic
from datetime import datetime
from dotenv import load_dotenv
from connectors import takvim_verileri_al, hava_durumu_al, gorevler_al
from connectors.gorevler import gorevleri_oncelikle

load_dotenv()

client = anthropic.Anthropic()


def verileri_topla(sehir: str = "Istanbul") -> dict:
    """Tüm kaynaklardan veri topla."""

    print("📊 Veriler toplanıyor...")

    bugun = datetime.now()

    veriler = {
        "tarih": bugun.strftime("%d %B %Y, %A"),
        "tarih_iso": bugun.strftime("%Y-%m-%d"),
        "saat": bugun.strftime("%H:%M"),
        "hava": hava_durumu_al(sehir),
        "takvim": takvim_verileri_al(bugun),
        "gorevler": gorevleri_oncelikle(gorevler_al(bugun))
    }

    print(f"   ✓ Hava durumu: {veriler['hava']['sehir']}")
    print(f"   ✓ Takvim: {len(veriler['takvim'])} etkinlik")
    print(f"   ✓ Görevler: {len(veriler['gorevler'])} aktif görev")

    return veriler


def takvim_formatla(etkinlikler: list[dict]) -> str:
    """Takvim etkinliklerini okunabilir formata çevir."""

    if not etkinlikler:
        return "Bugün planlanmış etkinlik yok."

    satir = []
    for e in sorted(etkinlikler, key=lambda x: x["baslangic"]):
        konum = f" ({e['konum']})" if e.get("konum") else ""
        satir.append(f"• {e['baslangic']}-{e['bitis']}: {e['baslik']}{konum}")

    return "\n".join(satir)


def gorevler_formatla(gorevler: list[dict]) -> str:
    """Görevleri okunabilir formata çevir."""

    if not gorevler:
        return "Tüm görevler tamamlandı!"

    oncelik_emoji = {"yuksek": "🔴", "orta": "🟡", "dusuk": "🟢"}

    satir = []
    for g in gorevler:
        emoji = oncelik_emoji.get(g["oncelik"], "⚪")
        notlar = f" - {g['notlar']}" if g.get("notlar") else ""
        satir.append(f"{emoji} {g['baslik']}{notlar}")

    return "\n".join(satir)


def gunluk_ozet_olustur(veriler: dict) -> str:
    """Claude ile günlük özet oluştur."""

    print("\n🤖 Günlük özet oluşturuluyor...")

    hava = veriler["hava"]
    takvim_str = takvim_formatla(veriler["takvim"])
    gorevler_str = gorevler_formatla(veriler["gorevler"])

    prompt = f"""Sen kişisel bir asistansın. Kullanıcının günlük verilerine bakarak
yararlı bir sabah özeti hazırla.

TARİH: {veriler['tarih']}
SAAT: {veriler['saat']}

HAVA DURUMU ({hava['sehir']}):
{hava['ikon']} {hava['durum']}, {hava['sicaklik']}°C (hissedilen: {hava['hissedilen']}°C)
Nem: %{hava['nem']}, Rüzgar: {hava['ruzgar']} km/h

BUGÜNKÜ TAKVİM:
{takvim_str}

AKTİF GÖREVLER:
{gorevler_str}

ÖZETİ HAZIRLARKEN:
1. Günün genel bir değerlendirmesini yap
2. Hava durumuna göre pratik öneriler ver
3. Takvim ve görevler arasında önceliklendirme öner
4. Boş zamanları değerlendirme önerileri yap
5. Günü verimli geçirmek için 2-3 somut öneri ver

Samimi ve motive edici bir ton kullan. Türkçe yaz.
Maksimum 300 kelime."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text


def oruntu_analizi(veriler: dict) -> str:
    """Uzun vadeli örüntü analizi (ileri seviye özellik)."""

    # Bu fonksiyon geçmiş verileri de kullanarak
    # tekrar eden kalıpları bulur.
    # Şimdilik sadece placeholder.

    return """
📈 ÖRÜNTÜ ANALİZİ (Demo)

Bu özellik için geçmiş verilerin kaydedilmesi gerekiyor.
İleride şunları görebileceksin:
• Hangi günler daha yoğun
• Ortalama toplantı süren
• En verimli saatlerin
• Hava durumunun moduna etkisi
"""


def main():
    print("=" * 60)
    print("🌅 HAYAT PANELİ")
    print("Günlük Kişisel Asistanın")
    print("=" * 60)
    print()

    # Verileri topla
    veriler = verileri_topla(sehir="Istanbul")

    # Günlük özet oluştur
    ozet = gunluk_ozet_olustur(veriler)

    # Sonuçları göster
    print("\n" + "=" * 60)
    print("📋 GÜNLÜK ÖZETİN")
    print("=" * 60)
    print(ozet)
    print("=" * 60)


if __name__ == "__main__":
    main()
