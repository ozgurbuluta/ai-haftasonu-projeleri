"""
RAG (Retrieval-Augmented Generation) Yardımcı Fonksiyonları

Belge parçalama, arama ve ilgili parça bulma işlemleri.
"""

import re
from pathlib import Path

try:
    from PyPDF2 import PdfReader
    PDF_DESTEGI = True
except ImportError:
    PDF_DESTEGI = False


def pdf_oku(dosya_yolu: str) -> str:
    """PDF dosyasını metin olarak oku."""
    if not PDF_DESTEGI:
        raise ImportError("PDF okumak için: pip install PyPDF2")

    reader = PdfReader(dosya_yolu)
    metin = ""
    for sayfa in reader.pages:
        metin += sayfa.extract_text() + "\n"
    return metin


def metin_oku(dosya_yolu: str) -> str:
    """Metin dosyasını oku."""
    with open(dosya_yolu, "r", encoding="utf-8") as f:
        return f.read()


def belge_yukle(dosya_yolu: str) -> str:
    """Dosya türüne göre belgeyi oku."""
    yol = Path(dosya_yolu)

    if yol.suffix.lower() == ".pdf":
        return pdf_oku(dosya_yolu)
    elif yol.suffix.lower() in [".txt", ".md"]:
        return metin_oku(dosya_yolu)
    else:
        raise ValueError(f"Desteklenmeyen dosya türü: {yol.suffix}")


def parcala(metin: str, parca_boyutu: int = 500, ortusme: int = 50) -> list[dict]:
    """
    Metni parçalara böl.

    Args:
        metin: Bölünecek metin
        parca_boyutu: Her parçanın karakter sayısı
        ortusme: Parçalar arası örtüşme (bağlam koruma için)

    Returns:
        Parça listesi: [{"id": 0, "metin": "..."}]
    """
    parcalar = []
    baslangic = 0
    parca_id = 0

    while baslangic < len(metin):
        bitis = baslangic + parca_boyutu
        parca_metni = metin[baslangic:bitis]

        # Kelime ortasında bölmemek için son boşluğu bul
        if bitis < len(metin):
            son_bosluk = parca_metni.rfind(" ")
            if son_bosluk > parca_boyutu // 2:
                parca_metni = parca_metni[:son_bosluk]
                bitis = baslangic + son_bosluk

        parcalar.append({
            "id": parca_id,
            "metin": parca_metni.strip(),
            "baslangic": baslangic,
            "bitis": bitis
        })

        parca_id += 1
        baslangic = bitis - ortusme

    return parcalar


def basit_ara(soru: str, parcalar: list[dict], k: int = 3) -> list[dict]:
    """
    Basit keyword tabanlı arama.

    Soru kelimelerini içeren parçaları skorla ve en alakalıları döndür.
    """
    # Soru kelimelerini çıkar (stop words hariç)
    stop_words = {"bir", "bu", "şu", "ve", "veya", "ile", "için", "de", "da", "mi", "mı", "ne", "nasıl", "hangi"}
    soru_kelimeleri = set(re.findall(r'\w+', soru.lower())) - stop_words

    skorlu_parcalar = []

    for parca in parcalar:
        parca_metin = parca["metin"].lower()
        skor = 0

        # Her eşleşen kelime için +1 skor
        for kelime in soru_kelimeleri:
            if kelime in parca_metin:
                skor += parca_metin.count(kelime)

        if skor > 0:
            skorlu_parcalar.append({
                **parca,
                "skor": skor
            })

    # Skora göre sırala ve ilk k tanesini döndür
    skorlu_parcalar.sort(key=lambda x: x["skor"], reverse=True)
    return skorlu_parcalar[:k]


def baglam_olustur(parcalar: list[dict]) -> str:
    """
    Seçilen parçalardan Claude'a gönderilecek bağlam oluştur.
    """
    baglam_parcalari = []

    for i, parca in enumerate(parcalar, 1):
        baglam_parcalari.append(f"[Parça {i}]\n{parca['metin']}")

    return "\n\n---\n\n".join(baglam_parcalari)
