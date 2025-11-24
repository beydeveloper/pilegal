<div align="center">
  <img src="pilegal.png" alt="PiLegal Logo" width="150"/>
  
  # 🔍 PiLegal
  ### Özgür Bilgi Ansiklopedisi
  
  [![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
  [![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
  [![Records](https://img.shields.io/badge/Records-4.1M+-blue?style=for-the-badge)]()
  [![Data](https://img.shields.io/badge/Data-3.92GB-orange?style=for-the-badge)]()
  
  **4.1+ Milyon makale** ile kapsamlı bilgi ansiklopedisi
  
  [Demo](http://localhost:5000) • [Kurulum](#-hızlı-başlangıç) • [API](#-api-dokümantasyonu) • [Katkıda Bulun](#-katkıda-bulunma)
</div>

---

## 📖 Hakkında

**PiLegal**, Wikipedia tarzında tasarlanmış, 4.1+ milyon makale içeren özgür bir bilgi ansiklopedisidir. Programlama, siber güvenlik, veri bilimi, web geliştirme ve daha birçok alanda detaylı bilgi sunar.

### ✨ Özellikler

- 🔍 **Güçlü Arama Motoru** - 4.1M+ makale içinde anlık arama
- 📚 **Çok Kategorili İçerik** - Programlama, güvenlik, veri bilimi ve daha fazlası
- 🎨 **Wikipedia Tarzı Arayüz** - Temiz, kullanıcı dostu tasarım
- 🚀 **Hızlı API** - RESTful API ile kolay entegrasyon
- 🎲 **Rastgele Makale** - Keşfetmek için rastgele içerik
- 📊 **Detaylı İstatistikler** - Kategori bazlı analiz

---

## 🚀 Hızlı Başlangıç

### Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- 4 GB+ boş disk alanı

### Kurulum

1. **Repoyu klonlayın**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

2. **Bağımlılıkları yükleyin**
```bash
pip install -r requirements.txt
```

3. **Sunucuyu başlatın**
```bash
python server.py
```

4. **Tarayıcınızda açın**
```
http://localhost:5000
```

### Windows için Hızlı Başlatma

```bash
START_SERVER.bat
```

---

## 📊 İçerik Dağılımı

| Kategori | Makale Sayısı | Açıklama |
|----------|---------------|----------|
| 💻 **Programlama** | ~1.5M | Python, JavaScript, Java, C++ ve daha fazlası |
| 🔐 **Siber Güvenlik** | ~800K | Exploit analizi, penetrasyon testleri, güvenlik |
| 📊 **Veri Bilimi** | ~600K | Machine Learning, AI, veri analizi |
| 🌐 **Web Geliştirme** | ~500K | Frontend, Backend, Full-stack |
| 🗄️ **Veritabanı** | ~300K | SQL, NoSQL, veri modelleme |
| 🔧 **Diğer** | ~400K | Ağ, sistem yönetimi, DevOps |

**Toplam:** 4,120,756 makale | **Boyut:** 3.92 GB

---

## 🔌 API Dokümantasyonu

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### 1️⃣ İstatistikler
```http
GET /api/stats
```

**Örnek Yanıt:**
```json
{
  "total_records": 4120756,
  "categories": {
    "programming": 1500000,
    "security": 800000,
    "data_science": 600000
  },
  "top_categories": [...]
}
```

#### 2️⃣ Arama
```http
GET /api/search?q=python&page=1&limit=20
```

**Parametreler:**
- `q` - Arama sorgusu (zorunlu)
- `page` - Sayfa numarası (varsayılan: 1)
- `limit` - Sayfa başına sonuç (varsayılan: 20)
- `category` - Kategori filtresi (opsiyonel)

**Örnek Yanıt:**
```json
{
  "results": [
    {
      "instruction": "Python'da liste nasıl oluşturulur?",
      "output": "Python'da liste oluşturmak için...",
      "category": "programming"
    }
  ],
  "total": 15000,
  "page": 1,
  "limit": 20,
  "total_pages": 750
}
```

#### 3️⃣ Rastgele Makale
```http
GET /api/random
```

**Örnek Yanıt:**
```json
{
  "instruction": "SQL Injection nedir?",
  "output": "SQL Injection, web uygulamalarında...",
  "category": "security"
}
```

#### 4️⃣ Kategoriler
```http
GET /api/categories
```

**Örnek Yanıt:**
```json
{
  "categories": [
    "programming",
    "security",
    "data_science",
    "web_development"
  ]
}
```

---

## 🎨 Arayüz Özellikleri

### Wikipedia Tarzı Tasarım
- 📱 Responsive (mobil uyumlu)
- 🎯 Kolay navigasyon
- 🔍 Anlık arama
- 📑 Sayfalama
- 🎲 Rastgele makale keşfi
- 📊 Kategori filtreleme

### Klavye Kısayolları
- `Enter` - Arama yap
- `Esc` - Sonuçları temizle

---

## 🗂️ Proje Yapısı

```
pilegal/
├── server.py                    # Flask backend
├── index.html                   # Ana arayüz (Wikipedia tarzı)
├── pilegal.png                  # Logo
├── pilegal_data_v1.jsonl        # Ana veri dosyası (3.92 GB)
├── requirements.txt             # Python bağımlılıkları
├── START_SERVER.bat            # Windows başlatma scripti
├── LICENSE                      # MIT Lisansı
├── README.md                    # Bu dosya
└── data/                        # Ham veri dosyaları (opsiyonel)
```

---

## 🔧 Geliştirici Notları

### Veri Formatı

Her makale JSONL formatında:
```json
{
  "instruction": "Soru veya başlık",
  "output": "Detaylı açıklama veya cevap",
  "category": "Kategori adı"
}
```

### Performans

- **Yükleme Süresi:** ~30 saniye (4.1M kayıt)
- **RAM Kullanımı:** ~2-3 GB
- **Arama Hızı:** <100ms (ortalama)

### Özelleştirme

`server.py` dosyasından aşağıdaki parametreleri değiştirebilirsiniz:
- `DATA_FILE`: Veri dosyası yolu
- Port numarası (varsayılan: 5000)
- CORS ayarları

---

## 📚 Veri Kaynakları

PiLegal, açık kaynak veri setlerini birleştirerek oluşturulmuştur:
- OpenOrca GPT-4
- ShareGPT Vicuna
- OpenAssistant
- Alpaca Dataset
- Dolly-15K
- Code Alpaca
- SQL Context Dataset
- MITRE ATT&CK
- CWE Database
- Ve daha fazlası...

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! İşte nasıl katkıda bulunabilirsiniz:

1. Bu repoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/YeniOzellik`)
5. Pull Request açın

### Katkı Alanları
- 🐛 Bug düzeltmeleri
- ✨ Yeni özellikler
- 📝 Dokümantasyon iyileştirmeleri
- 🌐 Çeviri eklemeleri
- 🎨 Arayüz geliştirmeleri

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Özgürce kullanabilir, değiştirebilir ve dağıtabilirsiniz.

---

## 👨‍💻 Geliştirici

<div align="center">
  <a href="https://github.com/beydeveloper">
    <img src="https://img.shields.io/badge/GitHub-beydeveloper-181717?style=for-the-badge&logo=github" alt="GitHub"/>
  </a>
  
  **beydeveloper** tarafından ❤️ ile geliştirilmiştir
</div>

---

## 🌟 Teşekkürler

Bu projeyi kullandığınız için teşekkür ederiz! Beğendiyseniz ⭐ vermeyi unutmayın.

### İletişim
- 🐛 Bug bildirimi: [Issues](https://github.com/beydeveloper/pilegal/issues)
- 💡 Öneriler: [Discussions](https://github.com/beydeveloper/pilegal/discussions)
- 📧 E-posta: [İletişim için GitHub profili](https://github.com/beydeveloper)

---

<div align="center">
  <sub>4.1M+ makale ile özgür bilgiye erişim</sub>
  
  **PiLegal** • Özgür Bilgi Ansiklopedisi • 2025
</div>
