# Kurulum Rehberi

Projeleri çalıştırmak için gereken her şey burada.

---

## 1. Python Kurulumu

Python 3.10 veya üstü gerekiyor. Kontrol etmek için:

```bash
python3 --version
```

Eğer kurulu değilse:
- **macOS:** `brew install python@3.12`
- **Ubuntu/Debian:** `sudo apt install python3.12`
- **Windows:** [python.org](https://www.python.org/downloads/) adresinden indir

---

## 2. Anthropic API Key Alma

Claude API kullanmak için bir API key gerekiyor:

1. [console.anthropic.com](https://console.anthropic.com/) adresine git
2. Hesap oluştur veya giriş yap
3. "API Keys" bölümünden yeni bir key oluştur
4. Key'i güvenli bir yere kaydet (bir daha göremezsin)

### Ücretsiz Kredi

Yeni hesaplara genellikle $5 ücretsiz kredi veriliyor. Bu projeler için fazlasıyla yeterli.

---

## 3. Projeyi İndir

```bash
git clone https://github.com/KULLANICI_ADIN/ai-haftasonu-projeleri.git
cd ai-haftasonu-projeleri
```

---

## 4. Virtual Environment Oluştur

Her proje için ayrı bir ortam oluşturabilirsin, ama tek bir ortam da yeterli:

```bash
# Ortam oluştur
python3 -m venv venv

# Aktif et (macOS/Linux)
source venv/bin/activate

# Aktif et (Windows)
venv\Scripts\activate
```

Terminalde `(venv)` görüyorsan ortam aktif demektir.

---

## 5. Bağımlılıkları Kur

```bash
pip install -r requirements.txt
```

---

## 6. API Key'i Ayarla

İki yöntem var:

### Yöntem 1: Environment Variable (Önerilen)

```bash
# macOS/Linux
export ANTHROPIC_API_KEY="sk-ant-..."

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="sk-ant-..."
```

Bu yöntemi her terminal oturumunda tekrarlamalısın. Kalıcı yapmak için `.bashrc` veya `.zshrc` dosyana ekle.

### Yöntem 2: .env Dosyası

Proje klasöründe `.env` dosyası oluştur:

```
ANTHROPIC_API_KEY=sk-ant-...
```

**Önemli:** `.env` dosyasını asla Git'e commit etme! (`.gitignore`'a ekli olmalı)

---

## 7. Test Et

Her şey doğru kurulduysa şu kod çalışmalı:

```python
import anthropic

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=100,
    messages=[{"role": "user", "content": "Merhaba!"}]
)
print(message.content[0].text)
```

---

## Sorun Giderme

### "API key not found" hatası
- Environment variable doğru ayarlandı mı kontrol et
- `.env` dosyası proje klasöründe mi bak
- Terminal'i yeniden başlat

### "Module not found" hatası
- Virtual environment aktif mi kontrol et: `(venv)` görüyor olmalısın
- `pip install -r requirements.txt` komutunu tekrar çalıştır

### Rate limit hatası
- Claude API'nin rate limitleri var. Biraz bekle ve tekrar dene.
- Ücretsiz tier'da dakikada ~60 istek yapabilirsin

---

## Sonraki Adım

Kurulum tamamsa ilk projeye başla: [01-gelir-gider-yonetimi](01-gelir-gider-yonetimi/)
