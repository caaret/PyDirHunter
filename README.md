# 🔍 PyDirHunter
Python tabanlı, hızlı ve hafif bir Web Dizin Keşif Aracı.

## 📌 Nedir?
PyDirHunter, hedef web sunucularındaki gizli dizinleri ve kritik dosyaları (yapılandırma dosyaları, yedekler, yönetim panelleri vb.) bulmak için tasarlanmış bir "Directory Brute Forcing" aracıdır.

## 🚀 Özellikler
- **Hızlı Tarama:** Verimli HTTP istek yönetimi.
- **Kritik Dosya Listesi:** En yaygın zafiyet noktalarını içeren dahili kelime listesi.
- **Canlı Geri Bildirim:** Bulunan her dizini anında durum koduyla birlikte gösterir.
- **Hata Yönetimi:** Bağlantı hatalarına ve zaman aşımlarına karşı dirençli yapı.

## 🛠️ Kurulum
Bu aracı kullanmak için `requests` kütüphanesine ihtiyacınız vardır:
```bash
pip install requests
