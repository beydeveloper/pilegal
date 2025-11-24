<div align="center">
  <img src="pilegal_logo.png" alt="PiLegal Logo" width="180"/>
  
  # 🔍 PiLegal
  ### Herkes İçin Özgür Bilgi Ansiklopedisi
  
  [![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
  [![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
  [![License](https://img.shields.io/badge/Lisans-CC0_1.0-green.svg?style=for-the-badge)](LICENSE)
  [![Veri](https://img.shields.io/badge/Veri-4.1M+-blue?style=for-the-badge)]()
  [![Boyut](https://img.shields.io/badge/Boyut-3.92GB-orange?style=for-the-badge)]()
  
  **4.1+ Milyon Makale** • **Wikipedia Tarzı Arayüz** • **RESTful API**
  
  [📥 Veri İndir](#-hızlı-başlangıç) • [🚀 Kurulum](#-kurulum) • [📡 API](#-api-dokümantasyonu) • [💡 Kullanım](#-kullanım-örnekleri)
</div>

---

## 📖 Proje Hakkında

**PiLegal**, programlama, siber güvenlik, veri bilimi, web geliştirme ve daha birçok teknik alanda **4.1+ milyon** makale içeren kapsamlı bir Türkçe bilgi ansiklopedisidir. Tamamen ücretsiz ve açık kaynaklıdır.

### 🎯 Ne İçin Kullanılır?

- 🔍 **Teknik Araştırma** - Programlama ve teknoloji konularında arama
- 💬 **Bilgi Tabanı** - Projeleriniz için bilgi kaynağı
- 📚 **Öğrenme** - Programlama ve güvenlik öğrenimi
- 🤖 **Yapay Zeka Projeleri** - AI modelleri için eğitim verisi
- 🔎 **Arama Motorları** - Özelleştirilmiş arama sistemleri
- 📊 **Veri Analizi** - Teknik içerik analizi

---

## ✨ Özellikler

### 📦 Veri Seti Özellikleri

- **4,120,756 Makale** - Kapsamlı bilgi tabanı
- **3.92 GB JSONL Format** - Kolay işlenebilir yapı
- **8 Ana Kategori** - Organize edilmiş içerik
- **Yüksek Kalite** - Detaylı ve açıklayıcı metinler
- **Türkçe İçerik** - Türkçe teknik bilgi
- **CC0 Lisanslı** - Tamamen ücretsiz kullanım

### 🖥️ Uygulama Özellikleri

- 🔍 **Güçlü Arama Motoru** - Hash tabanlı hızlı arama
- 📚 **Wikipedia Arayüzü** - Kullanıcı dostu tasarım
- 🚀 **RESTful API** - Kolay entegrasyon
- 🎲 **Rastgele Keşif** - İçerik keşfi
- 📊 **İstatistikler** - Detaylı veri analizi
- ⚡ **Yüksek Performans** - <100ms arama süresi

---

## 📊 Veri Dağılımı

| Kategori | Makale Sayısı | Açıklama |
|----------|---------------|----------|
| 💻 **Programlama** | ~1,500,000 | Python, JavaScript, Java, C++, C#, Go, Rust |
| 🔐 **Siber Güvenlik** | ~800,000 | Exploit analizi, pentesting, güvenlik zafiyetleri |
| 📊 **Veri Bilimi** | ~600,000 | Machine Learning, AI, veri analizi, istatistik |
| 🌐 **Web Geliştirme** | ~500,000 | Frontend, Backend, Full-stack, framework'ler |
| 🗄️ **Veritabanı** | ~300,000 | SQL, NoSQL, MongoDB, PostgreSQL, MySQL |
| 🌍 **Ağ (Network)** | ~200,000 | TCP/IP, routing, protokoller, network güvenliği |
| ⚙️ **Sistem** | ~170,000 | Linux, Windows, sistem yönetimi, DevOps |
| 📚 **Genel** | ~50,756 | Diğer teknik konular |

**Toplam:** 4,120,756 makale | **Dosya Boyutu:** 3.92 GB

---

## 🚀 Hızlı Başlangıç

### 📋 Sistem Gereksinimleri

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- En az 4 GB boş disk alanı
- En az 2 GB RAM (yükleme için)

### 💿 Kurulum

#### 1️⃣ Repository'yi Klonlayın

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

#### 2️⃣ Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

Gerekli paketler:
- `Flask` - Web server
- `flask-cors` - API CORS desteği

#### 3️⃣ Veri Setini İndirin

📥 **İndirme Linki:** [pilegal_data_v1.jsonl (3.92 GB)](https://github.com/beydeveloper/pilegal/releases/download/data/pilegal_data_v1.zip)

**Önemli:** İndirdiğiniz dosyayı proje ana dizinine yerleştirin:

```
pilegal/
├── pilegal_data_v1.jsonl    ← Buraya koyun
├── server.py
├── index.html
├── requirements.txt
└── README.md
```

#### 4️⃣ Sunucuyu Başlatın

```bash
python server.py
```

veya Windows için:

```bash
START_SERVER.bat
```

#### 5️⃣ Tarayıcıda Açın

```
http://localhost:5000
```

🎉 **Tebrikler!** PiLegal çalışıyor.

---

## 📝 Veri Formatı

Her makale JSONL formatında (her satır bir JSON):

```json
{
  "instruction": "Python'da liste nasıl oluşturulur?",
  "output": "Python'da liste oluşturmak için köşeli parantez kullanılır. Örnek: my_list = [1, 2, 3, 4, 5]. Listeler sıralı, değiştirilebilir ve farklı veri tiplerini tutabilen koleksiyonlardır.",
  "category": "programming"
}
```

**Alan Açıklamaları:**
- `instruction`: Soru, başlık veya konu
- `output`: Detaylı açıklama veya cevap
- `category`: İçerik kategorisi

---

## 📡 API Dokümantasyonu

### Base URL
```
http://localhost:5000/api
```

### 🔗 Endpoints

#### 1️⃣ İstatistikler

```http
GET /api/stats
```

**Yanıt:**
```json
{
  "total_records": 4120756,
  "categories": {
    "programming": 1500000,
    "security": 800000,
    "data_science": 600000,
    "web": 500000,
    "database": 300000,
    "network": 200000,
    "system": 170000,
    "general": 50756
  },
  "top_categories": [
    ["programming", 1500000],
    ["security", 800000],
    ["data_science", 600000]
  ]
}
```

#### 2️⃣ Arama

```http
GET /api/search?q=python&page=1&limit=20&category=programming
```

**Parametreler:**
| Parametre | Tip | Zorunlu | Açıklama |
|-----------|-----|---------|----------|
| `q` | string | ✅ | Arama sorgusu |
| `page` | integer | ❌ | Sayfa numarası (varsayılan: 1) |
| `limit` | integer | ❌ | Sayfa başına sonuç (varsayılan: 20, max: 100) |
| `category` | string | ❌ | Kategori filtresi |

**Yanıt:**
```json
{
  "results": [
    {
      "instruction": "Python'da liste nasıl oluşturulur?",
      "output": "Python'da liste oluşturmak için...",
      "category": "programming"
    }
  ],
  "total": 15432,
  "page": 1,
  "limit": 20,
  "total_pages": 772
}
```

#### 3️⃣ Rastgele Makale

```http
GET /api/random
```

**Yanıt:**
```json
{
  "instruction": "SQL Injection nedir?",
  "output": "SQL Injection, veritabanına zararlı SQL kodları...",
  "category": "security"
}
```

#### 4️⃣ Kategoriler

```http
GET /api/categories
```

**Yanıt:**
```json
{
  "categories": [
    {"name": "programming", "label": "Programlama", "count": 1500000},
    {"name": "security", "label": "Güvenlik", "count": 800000}
  ],
  "total": 8
}
```

---

## 💡 Kullanım Örnekleri

### 🐍 Python ile API Kullanımı

```python
import requests

BASE_URL = "http://localhost:5000/api"

# Arama yapma
response = requests.get(f"{BASE_URL}/search", params={
    "q": "machine learning",
    "category": "data_science",
    "limit": 10
})
results = response.json()
print(f"Toplam: {results['total']} sonuç")

for item in results['results']:
    print(f"📖 {item['instruction']}")
    print(f"   {item['output'][:100]}...\n")

# Rastgele makale
random_article = requests.get(f"{BASE_URL}/random").json()
print(f"🎲 Rastgele: {random_article['instruction']}")

# İstatistikler
stats = requests.get(f"{BASE_URL}/stats").json()
print(f"📊 Toplam makale: {stats['total_records']:,}")
```

### 📚 Kategori Bazlı Veri Okuma

```python
import json

def read_by_category(file_path, category, limit=10):
    """Belirli bir kategoriden makaleleri oku"""
    articles = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            if data.get('category') == category:
                articles.append(data)
                if len(articles) >= limit:
                    break
    
    return articles

# Kullanım
programming_articles = read_by_category('pilegal_data_v1.jsonl', 'programming', 5)

for article in programming_articles:
    print(f"📖 {article['instruction']}")
    print(f"   {article['output'][:150]}...\n")
```

### 🔍 Basit Arama Fonksiyonu

```python
import json

def search_articles(file_path, query, max_results=10):
    """Makalelerde arama yap"""
    results = []
    query_lower = query.lower()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            
            # Instruction veya output içinde ara
            if (query_lower in data['instruction'].lower() or 
                query_lower in data['output'].lower()):
                results.append(data)
                
                if len(results) >= max_results:
                    break
    
    return results

# Kullanım
results = search_articles('pilegal_data_v1.jsonl', 'python liste', 5)
print(f"'{query}' için {len(results)} sonuç bulundu\n")

for result in results:
    print(f"📖 {result['instruction']}")
    print(f"📁 Kategori: {result['category']}")
    print(f"   {result['output'][:100]}...\n")
```

### 📊 İstatistik Analizi

```python
import json
from collections import Counter

def analyze_dataset(file_path):
    """Veri seti analizi yap"""
    categories = []
    total_chars = 0
    article_count = 0
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            categories.append(data.get('category', 'unknown'))
            total_chars += len(data.get('output', ''))
            article_count += 1
    
    # İstatistikler
    category_counts = Counter(categories)
    avg_length = total_chars / article_count if article_count > 0 else 0
    
    print(f"📊 Toplam Makale: {article_count:,}")
    print(f"📏 Ortalama Uzunluk: {avg_length:.0f} karakter")
    print(f"\n📚 Kategoriler:")
    
    for category, count in category_counts.most_common():
        percentage = (count / article_count) * 100
        print(f"   {category}: {count:,} ({percentage:.1f}%)")

# Kullanım
analyze_dataset('pilegal_data_v1.jsonl')
```

---

## 🎨 Arayüz Özellikleri

### Wikipedia Tarzı Tasarım

- 📱 **Responsive** - Mobil uyumlu
- 🎯 **Kolay Navigasyon** - Kullanıcı dostu menüler
- 🔍 **Anlık Arama** - Hızlı sonuçlar
- 📑 **Sayfalama** - Organize sonuçlar
- 🎲 **Rastgele Keşif** - İçerik keşfi
- 📊 **Kategori Filtreleme** - Hızlı filtreleme
- 🌙 **Temiz Tasarım** - Minimal ve şık

### ⌨️ Klavye Kısayolları

- `Enter` - Arama yap
- `Esc` - Sonuçları temizle

---

## 🔧 Geliştirici Notları

### Performans

- **Yükleme Süresi:** ~40 saniye (4.1M kayıt + indexleme)
- **RAM Kullanımı:** ~1-2 GB
- **Arama Hızı:** <100ms ortalama (hash-based indexing)
- **Index Oluşturma:** Otomatik (başlangıçta)

### Optimizasyonlar

- ✅ Hash tabanlı arama indexleme
- ✅ Kategori indexleme (O(1) lookup)
- ✅ Query term splitting
- ✅ Sonuç limitleme (max 1000)
- ✅ Cached category counts

### Özelleştirme

`server.py` içinde şunları değiştirebilirsiniz:

```python
DATA_FILE = 'pilegal_data_v1.jsonl'  # Veri dosyası
PORT = 5000  # Port numarası
RESULTS_PER_PAGE = 20  # Sayfa başına sonuç
MAX_RESULTS = 1000  # Maksimum sonuç limiti
```

---

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! İşte nasıl katkıda bulunabilirsiniz:

### Katkı Adımları

1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/harika-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Harika özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/harika-ozellik`)
5. Pull Request açın

### Katkı Alanları

- 🐛 Hata düzeltmeleri
- ✨ Yeni özellikler
- 📝 Dokümantasyon iyileştirmeleri
- 🎨 Arayüz geliştirmeleri
- 🚀 Performans optimizasyonları
- 🌐 Çeviriler
- 💡 Yeni örnekler

---

## 📄 Lisans

Bu proje **Creative Commons Zero v1.0 Universal (CC0 1.0)** lisansı ile lisanslanmıştır.

### Bu Ne Anlama Gelir?

- ✅ **Telif Hakkı Yok** - Tamamen kamu malı
- ✅ **Özgürce Kullanın** - Kişisel veya ticari
- ✅ **Özgürce Değiştirin** - Türev eserler oluşturun
- ✅ **Özgürce Dağıtın** - Herkesle paylaşın
- ✅ **Atıf Gerekmez** - İsteğe bağlı (hoş karşılanır!)

[LICENSE](LICENSE) dosyasını inceleyin.

**Kısacası:** Bu projeyle istediğinizi yapabilirsiniz. Hiçbir kısıtlama yok.

---

## 🌟 Neden CC0?

Bilginin özgür ve herkese açık olması gerektiğine inanıyoruz:

- 🌍 **Evrensel Erişim** - Dünyanın her yerinden erişim
- 🔓 **Gerçek Özgürlük** - Kısıtlama yok
- 🚀 **Maksimum Kullanım** - Her projede kullanılabilir
- 💡 **Bilgi Paylaşımı** - Kamu malına katkı

---

## 👨‍💻 Geliştirici

<div align="center">
  <a href="https://github.com/beydeveloper">
    <img src="https://img.shields.io/badge/GitHub-beydeveloper-181717?style=for-the-badge&logo=github" alt="GitHub"/>
  </a>
  <br><br>
  ❤️ **beydeveloper** tarafından geliştirildi
  <br>
  📧 Instagram: <a href="https://www.instagram.com/beydeveloper/">@beydeveloper</a>
</div>

---

## 🎯 Yol Haritası

### 📦 Mevcut Sürüm: v1.0

- ✅ 4.1M+ makale veri seti
- ✅ Hash-based hızlı arama
- ✅ Wikipedia tarzı arayüz
- ✅ RESTful API
- ✅ 8 kategori desteği
- ✅ JSONL format

### 🚀 Gelecek Özellikler

- 🔄 Gerçek zamanlı veri güncellemeleri
- 🌙 Dark mode (karanlık tema)
- 📱 Mobil uygulama
- 🔍 Gelişmiş arama filtreleri
- 📊 Analytics dashboard
- 🤖 AI tabanlı öneriler
- 🌐 Çok dilli içerik desteği
- 🎙️ Sesli arama
- 📈 Kullanıcı istatistikleri
- 🔐 Kullanıcı hesapları
- ⭐ Favori makaleler

---

## 📈 İstatistikler

<div align="center">

| Metrik | Değer |
|--------|-------|
| **Toplam Makale** | 4,120,756 |
| **Dosya Boyutu** | 3.92 GB (JSONL) |
| **Kategoriler** | 8 ana kategori |
| **Diller** | Türkçe içerik |
| **Arama Hızı** | <100ms ortalama |
| **API Endpoints** | 4 endpoint |
| **Lisans** | CC0 1.0 (Kamu Malı) |
| **Format** | JSONL |
| **Encoding** | UTF-8 |
| **Python Versiyonu** | 3.8+ |

</div>

---



### İletişim

- 📧 Instagram: [@beydeveloper](https://www.instagram.com/beydeveloper/)
- 🐙 GitHub: [@beydeveloper](https://github.com/beydeveloper)

---

## 🙏 Teşekkürler

Özel teşekkürler:

- Tüm açık kaynak veri seti katkıda bulunanlarına
- Flask ve Python topluluklarına
- Wikipedia'ya ilham verdiği için
- Bilgiyi özgür kılan herkese
- Bu projeyi kullanan ve geliştiren herkese

---

## 🔐 Güvenlik

Gü
