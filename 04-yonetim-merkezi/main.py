"""
Yönetim Merkezi

Belgeler üzerinde soru-cevap yapan RAG sistemi.
"""

import anthropic
from dotenv import load_dotenv
from rag import parcala, basit_ara, baglam_olustur

load_dotenv()

client = anthropic.Anthropic()

# Örnek belgeler (gerçek uygulamada dosyadan okunacak)
ORNEK_BELGELER = {
    "internet_kontrati": """
İNTERNET HİZMET SÖZLEŞMESİ

Taraflar:
- Hizmet Sağlayıcı: TelekomNet A.Ş.
- Abone: [Müşteri Adı]

Sözleşme Tarihi: 01.01.2024
Sözleşme Süresi: 24 ay

MADDE 3 - HİZMET BEDELİ
Aylık hizmet bedeli: 299 TL (KDV dahil)
Kurulum ücreti: 150 TL (tek seferlik)

MADDE 5 - SÖZLEŞMENİN FESHİ
5.1. Abone, sözleşme süresinin bitiminden en az 30 gün önce yazılı
bildirimde bulunarak sözleşmeyi feshedebilir.
5.2. Erken fesih halinde, kalan ay sayısı x 100 TL cayma bedeli uygulanır.
5.3. Yıllık yenileme tarihi her yılın Ocak ayının ilk günüdür.

MADDE 7 - TEKNİK DESTEK
7.1. 7/24 teknik destek hattı: 444 0 XXX
7.2. Arıza bildirimleri 24 saat içinde değerlendirilir.
""",

    "saglik_sigortasi": """
SAĞLIK SİGORTASI POLİÇESİ

Poliçe No: HSP-2024-123456
Sigortalı: [Müşteri Adı]
Başlangıç: 01.03.2024
Bitiş: 01.03.2025

TEMİNATLAR:
- Yatarak tedavi: 500.000 TL (yıllık limit)
- Ayakta tedavi: 50.000 TL (yıllık limit)
- İlaç: 20.000 TL (yıllık limit)
- Diş: 10.000 TL (yıllık limit)

MUAFİYET:
- Ayakta tedavi muafiyeti: İşlem başına 200 TL
- Yatarak tedavi muafiyeti: Yok
- İlaç muafiyeti: %20 katılım payı

KAPSAM DIŞI:
- Estetik operasyonlar
- Doğum kontrol
- Daha önce mevcut rahatsızlıklar (ilk 12 ay)

PRİM:
Aylık prim: 1.250 TL
Ödeme tarihi: Her ayın 15'i
""",

    "kira_sozlesmesi": """
KİRA SÖZLEŞMESİ

Kiralayan: Mehmet Yılmaz
Kiracı: [Müşteri Adı]
Kiralanan: Ataşehir, İstanbul - 2+1 daire

SÖZLEŞMENİN SÜRESİ:
Başlangıç: 01.06.2024
Bitiş: 01.06.2025
Süre: 1 yıl

KİRA BEDELİ:
Aylık kira: 15.000 TL
Depozito: 30.000 TL (2 aylık)
Ödeme günü: Her ayın 1'i

MADDE 8 - TAHLİYE
8.1. Kiracı, sözleşme bitiminden 2 ay önce yazılı bildirimde bulunmalıdır.
8.2. Erken tahliye halinde 1 aylık kira bedeli tazminat olarak ödenir.

MADDE 10 - AİDAT VE GİDERLER
Apartman aidatı kiracıya aittir. (Mevcut aidat: 800 TL/ay)
Su, elektrik, doğalgaz faturaları kiracıya aittir.
"""
}


def soru_cevapla(belgeler: dict, soru: str) -> dict:
    """
    Belgeler üzerinde soru cevapla.

    1. Tüm belgeleri parçala
    2. Soruyla alakalı parçaları bul
    3. Claude'a gönder ve cevap al
    """

    # 1. Tüm belgeleri parçala
    tum_parcalar = []
    for belge_adi, belge_metni in belgeler.items():
        parcalar = parcala(belge_metni, parca_boyutu=400)
        for parca in parcalar:
            parca["belge"] = belge_adi
        tum_parcalar.extend(parcalar)

    print(f"📁 Toplam belge: {len(belgeler)}")
    print(f"📄 Toplam parça: {len(tum_parcalar)}")

    # 2. En alakalı parçaları bul
    print(f"\n🔍 İlgili parçalar aranıyor...")
    alakali_parcalar = basit_ara(soru, tum_parcalar, k=3)

    if not alakali_parcalar:
        return {
            "soru": soru,
            "cevap": "Bu soruyla ilgili belgelerde bilgi bulunamadı.",
            "kaynaklar": []
        }

    print(f"   → {len(alakali_parcalar)} alakalı parça bulundu")

    # 3. Bağlam oluştur ve Claude'a gönder
    baglam = baglam_olustur(alakali_parcalar)

    prompt = f"""Aşağıdaki belge parçalarını kullanarak soruyu cevapla.

BELGELER:
{baglam}

SORU: {soru}

KURALLAR:
- Sadece belgelerdeki bilgiye dayanarak cevap ver
- Tahminde bulunma, emin değilsen "Bu bilgi belgelerde yok" de
- Cevabı kısa ve net tut
- Varsa ilgili madde numarasını belirt"""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}]
    )

    kaynaklar = [
        {"belge": p["belge"], "parca_id": p["id"]}
        for p in alakali_parcalar
    ]

    return {
        "soru": soru,
        "cevap": response.content[0].text,
        "kaynaklar": kaynaklar
    }


def main():
    print("=" * 60)
    print("🗂️  YÖNETİM MERKEZİ")
    print("Belgeleriniz hakkında soru sorun")
    print("=" * 60)
    print()

    # Örnek sorular
    sorular = [
        "İnternet kontratımı ne zaman iptal edebilirim?",
        "Sağlık sigortamda muafiyet tutarı ne kadar?",
        "Kira sözleşmemi erken sonlandırırsam ne olur?",
    ]

    print("📋 Mevcut belgeler:")
    for belge in ORNEK_BELGELER.keys():
        print(f"   • {belge}")
    print()

    # İlk soruyu çalıştır
    soru = sorular[0]
    print(f"❓ Soru: {soru}\n")

    sonuc = soru_cevapla(ORNEK_BELGELER, soru)

    print("\n" + "=" * 60)
    print("💬 CEVAP")
    print("=" * 60)
    print(sonuc["cevap"])

    if sonuc["kaynaklar"]:
        print("\n📚 Kaynaklar:")
        for kaynak in sonuc["kaynaklar"]:
            print(f"   • {kaynak['belge']} (parça {kaynak['parca_id']})")


if __name__ == "__main__":
    main()
