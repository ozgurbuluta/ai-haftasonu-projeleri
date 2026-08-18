# MCP (Model Context Protocol)

AI'ı dış sistemlerle bağlama standardı.

---

## Ne İşe Yarar?

MCP (Model Context Protocol) ile Claude:
- Veritabanlarına bağlanabilir
- API'lere erişebilir
- Dosya sistemini okuyabilir
- Üçüncü parti servisleri kullanabilir

"Claude'a süper güçler vermek."

---

## Nasıl Çalışır?

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Claude    │ ←→  │  MCP Host   │ ←→  │   Server    │
│             │     │ (orchestrator)│    │ (Gmail, DB) │
└─────────────┘     └─────────────┘     └─────────────┘
```

MCP, Claude ile dış sistemler arasında standart bir köprü.

---

## Örnek Kullanım

Claude Desktop veya Claude Code ile:

```json
// claude_desktop_config.json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/folder"]
    }
  }
}
```

Artık Claude dosyalarını okuyabilir.

---

## Hazır MCP Sunucuları

| Sunucu | Özellik |
|--------|---------|
| filesystem | Dosya okuma/yazma |
| github | Repo, PR, issue |
| slack | Mesaj okuma/gönderme |
| postgres | Veritabanı sorguları |
| google-drive | Doküman erişimi |

---

## Kendi Sunucunu Yaz

```python
from mcp.server import Server

server = Server("my-server")

@server.tool()
async def hava_durumu_al(sehir: str) -> str:
    """Şehrin hava durumunu getirir."""
    # API çağrısı yap
    return f"{sehir}: 20°C, Güneşli"

# Sunucuyu başlat
server.run()
```

---

## Avantajlar

1. **Standart:** Bir kez yaz, her yerde kullan
2. **Güvenlik:** İzin kontrolü merkezi
3. **Modüler:** İhtiyacın olan sunucuları ekle
4. **Topluluk:** Hazır sunucular mevcut

---

## Claude Code'da

Claude Code otomatik olarak MCP desteği sunar:

```bash
# MCP sunucusu ekle
claude mcp add github

# Artık "GitHub'daki PR'ları listele" diyebilirsin
```

---

## İlgili Projeler

- [05-hayat-paneli](../05-hayat-paneli/) - API bağlantıları (MCP benzeri)

---

## Kaynaklar

- [MCP Docs](https://modelcontextprotocol.io/)
- [MCP Servers](https://github.com/modelcontextprotocol/servers)
