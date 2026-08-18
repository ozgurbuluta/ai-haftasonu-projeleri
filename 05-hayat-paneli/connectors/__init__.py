"""
Hayat Paneli Connector'ları

Her connector farklı bir veri kaynağından veri çeker.
"""

from .takvim import takvim_verileri_al
from .hava import hava_durumu_al
from .gorevler import gorevler_al

__all__ = ["takvim_verileri_al", "hava_durumu_al", "gorevler_al"]
