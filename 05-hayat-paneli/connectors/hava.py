"""
Hava Durumu Connector

Gerçek uygulamada OpenWeatherMap veya başka bir hava API'sine bağlanır.
Bu örnekte simüle edilmiş veri kullanıyoruz.
"""

import os
import random


def hava_durumu_al(sehir: str = "Istanbul") -> dict:
    """
    Şehrin hava durumunu döndür.

    Gerçek uygulamada:
    - OpenWeatherMap API
    - Weather API
    - AccuWeather API
    """

    api_key = os.getenv("WEATHER_API_KEY")

    if api_key:
        # Gerçek API çağrısı yapılabilir
        return _gercek_hava_al(sehir, api_key)

    # Simüle edilmiş hava verisi
    return _mock_hava_al(sehir)


def _mock_hava_al(sehir: str) -> dict:
    """Mock hava verisi döndür."""

    durumlar = [
        {"durum": "Güneşli", "ikon": "☀️"},
        {"durum": "Parçalı bulutlu", "ikon": "⛅"},
        {"durum": "Bulutlu", "ikon": "☁️"},
        {"durum": "Yağmurlu", "ikon": "🌧️"},
    ]

    secilen = random.choice(durumlar)

    return {
        "sehir": sehir,
        "sicaklik": random.randint(5, 25),
        "hissedilen": random.randint(3, 27),
        "durum": secilen["durum"],
        "ikon": secilen["ikon"],
        "nem": random.randint(40, 80),
        "ruzgar": random.randint(5, 30),
        "tahmin": [
            {"saat": "12:00", "sicaklik": random.randint(10, 20), "durum": "Parçalı bulutlu"},
            {"saat": "15:00", "sicaklik": random.randint(8, 18), "durum": "Bulutlu"},
            {"saat": "18:00", "sicaklik": random.randint(5, 15), "durum": "Yağmur ihtimali"},
        ]
    }


def _gercek_hava_al(sehir: str, api_key: str) -> dict:
    """
    OpenWeatherMap API'den gerçek veri al.

    Not: Bu fonksiyon gerçek API çağrısı yapar.
    Kullanmak için WEATHER_API_KEY environment variable'ı set edin.
    """

    try:
        import requests

        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": sehir,
            "appid": api_key,
            "units": "metric",
            "lang": "tr"
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        return {
            "sehir": data["name"],
            "sicaklik": round(data["main"]["temp"]),
            "hissedilen": round(data["main"]["feels_like"]),
            "durum": data["weather"][0]["description"],
            "ikon": _hava_ikonu(data["weather"][0]["main"]),
            "nem": data["main"]["humidity"],
            "ruzgar": round(data["wind"]["speed"] * 3.6),  # m/s -> km/h
            "tahmin": []  # Forecast için ayrı API çağrısı gerekir
        }

    except Exception as e:
        print(f"Hava API hatası: {e}")
        return _mock_hava_al(sehir)


def _hava_ikonu(durum: str) -> str:
    """Hava durumuna göre emoji döndür."""
    ikonlar = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌦️",
        "Thunderstorm": "⛈️",
        "Snow": "🌨️",
        "Mist": "🌫️",
        "Fog": "🌫️",
    }
    return ikonlar.get(durum, "🌡️")
