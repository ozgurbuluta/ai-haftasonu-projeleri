"""
Günlük E-posta Özeti

Mailleri analiz edip özetleyen ve cevap taslağı hazırlayan sistem.
"""

import json
import anthropic
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = anthropic.Anthropic()

# Simüle edilmiş mail verileri
ORNEK_MAILLER = [
    {
        "id": 1,
        "kimden": "ahmet.yilmaz@firma.com",
        "konu": "ACİL: Proje Teslimi Hakkında",
        "tarih": "2024-01-15 09:30",
        "icerik": """Merhaba,

Yarın saat 17:00'ye kadar Q4 proje raporunun teslim edilmesi gerekiyor.
Finans ekibi rakamları bekliyor. Lütfen en kısa sürede gönderir misin?

Teşekkürler,
Ahmet"""
    },
    {
        "id": 2,
        "kimden": "newsletter@techblog.com",
        "konu": "Bu Haftanın En İyi Yazıları",
        "tarih": "2024-01-15 07:00",
        "icerik": """Merhaba,

Bu hafta en çok okunan yazılarımız:
- AI ile Verimlilik Artırma
- Python 3.13 Yenilikleri
- Uzaktan Çalışma Trendleri

Keyifli okumalar!"""
    },
    {
        "id": 3,
        "kimden": "zeynep.kara@musteri.com",
        "konu": "Toplantı Talebi",
        "tarih": "2024-01-15 11:45",
        "icerik": """Merhaba,

Önümüzdeki hafta yeni proje hakkında görüşmek isteriz.
Salı veya Çarşamba uygun olur mu?

Saygılarımla,
Zeynep Kara
ABC Şirketi"""
    },
    {
        "id": 4,
        "kimden": "insan.kaynaklari@sirket.com",
        "konu": "Yıllık İzin Bildirimi",
        "tarih": "2024-01-15 08:00",
        "icerik": """Değerli Çalışanımız,

2024 yılı için kalan izin gününüz: 14 gün.
İzin planlamanızı bu ay içinde yapmanızı rica ederiz.

İK Departmanı"""
    },
    {
        "id": 5,
        "kimden": "fatih.demir@ekip.com",
        "konu": "Code Review Bekliyor",
        "tarih": "2024-01-15 14:20",
        "icerik": """Hey,

PR #234'ü açtım, authentication modülündeki değişiklikler.
Bugün bakabilir misin? Yarın deploy etmemiz lazım.

Fatih"""
    }
]


def mail_analiz_et(mail: dict) -> dict:
    """Tek bir maili analiz et: önem, özet, cevap gerekli mi."""

    prompt = f"""Bu e-postayı analiz et:

Kimden: {mail['kimden']}
Konu: {mail['konu']}
Tarih: {mail['tarih']}
İçerik:
{mail['icerik']}

Şu bilgileri JSON formatında döndür:
{{
    "onem": "yuksek/orta/dusuk",
    "onem_nedeni": "<neden bu önemde>",
    "ozet": "<1-2 cümlelik özet>",
    "cevap_gerekli": true/false,
    "eylem": "<yapılması gereken şey, varsa>"
}}

Önem kriterleri:
- yuksek: Bugün cevap verilmeli, iş kaybı veya müşteri kaybı riski
- orta: Bu hafta içinde bakılmalı, toplantı/proje ile ilgili
- dusuk: Bilgi amaçlı, newsletter, duyuru

Sadece JSON döndür."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(response.content[0].text)


def cevap_taslagi_olustur(mail: dict, analiz: dict) -> str:
    """Yüksek öncelikli mailler için cevap taslağı oluştur."""

    prompt = f"""Bu e-postaya profesyonel bir cevap taslağı yaz:

Kimden: {mail['kimden']}
Konu: {mail['konu']}
İçerik:
{mail['icerik']}

Analiz: {analiz['ozet']}
Eylem: {analiz.get('eylem', 'Belirtilmedi')}

Kurallar:
- Kısa ve öz ol (3-5 cümle)
- Profesyonel ama samimi
- Somut bir taahhüt veya soru içersin
- Sadece cevap metnini yaz, başka açıklama ekleme"""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text


def gunluk_ozet_olustur(analizler: list[dict]) -> str:
    """Tüm analizlerden günlük özet raporu oluştur."""

    yuksek = [a for a in analizler if a["analiz"]["onem"] == "yuksek"]
    orta = [a for a in analizler if a["analiz"]["onem"] == "orta"]
    dusuk = [a for a in analizler if a["analiz"]["onem"] == "dusuk"]

    rapor = []
    rapor.append("=" * 50)
    rapor.append(f"📬 GÜNLÜK MAİL ÖZETİ - {datetime.now().strftime('%d.%m.%Y')}")
    rapor.append("=" * 50)
    rapor.append("")

    if yuksek:
        rapor.append(f"🔴 YÜKSEK ÖNCELİK ({len(yuksek)})")
        rapor.append("-" * 30)
        for item in yuksek:
            rapor.append(f"\n📧 {item['mail']['konu']}")
            rapor.append(f"   Kimden: {item['mail']['kimden']}")
            rapor.append(f"   Özet: {item['analiz']['ozet']}")
            if item.get("taslak"):
                rapor.append(f"\n   💬 Taslak Cevap:")
                for line in item["taslak"].split("\n"):
                    rapor.append(f"   {line}")
        rapor.append("")

    if orta:
        rapor.append(f"🟡 ORTA ÖNCELİK ({len(orta)})")
        rapor.append("-" * 30)
        for item in orta:
            rapor.append(f"\n📧 {item['mail']['konu']}")
            rapor.append(f"   Kimden: {item['mail']['kimden']}")
            rapor.append(f"   Özet: {item['analiz']['ozet']}")
        rapor.append("")

    if dusuk:
        rapor.append(f"🟢 DÜŞÜK ÖNCELİK ({len(dusuk)})")
        rapor.append("-" * 30)
        for item in dusuk:
            rapor.append(f"📧 {item['mail']['konu']}")
        rapor.append("")

    cevap_bekleyen = sum(1 for a in analizler if a["analiz"].get("cevap_gerekli"))
    rapor.append("=" * 50)
    rapor.append(f"📊 Toplam: {len(analizler)} mail | Cevap bekleyen: {cevap_bekleyen}")
    rapor.append("=" * 50)

    return "\n".join(rapor)


def main():
    print("Mailler analiz ediliyor...\n")

    sonuclar = []

    for mail in ORNEK_MAILLER:
        print(f"  Analiz: {mail['konu'][:40]}...")
        analiz = mail_analiz_et(mail)

        sonuc = {
            "mail": mail,
            "analiz": analiz,
            "taslak": None
        }

        # Yüksek öncelikli ve cevap gerektiren mailler için taslak oluştur
        if analiz["onem"] == "yuksek" and analiz.get("cevap_gerekli"):
            print(f"    → Cevap taslağı oluşturuluyor...")
            sonuc["taslak"] = cevap_taslagi_olustur(mail, analiz)

        sonuclar.append(sonuc)

    # Günlük özet oluştur ve yazdır
    print("\n")
    ozet = gunluk_ozet_olustur(sonuclar)
    print(ozet)


if __name__ == "__main__":
    main()
