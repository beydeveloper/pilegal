<div align="center">
  <img src="pilegal.png" alt="PiLegal Logo" width="150"/>
  
  # 🔍 PiLegal
  ### Free Knowledge Encyclopedia for Everyone
  
  [![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
  [![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
  [![License](https://img.shields.io/badge/License-CC0_1.0-green.svg?style=for-the-badge)](LICENSE)
  [![Records](https://img.shields.io/badge/Records-4.1M+-blue?style=for-the-badge)]()
  [![Data](https://img.shields.io/badge/Data-3.92GB-orange?style=for-the-badge)]()
  
  **4.1+ Million articles** - Comprehensive knowledge base
  
  [Demo](http://localhost:5000) • [Installation](#-quick-start) • [API](#-api-documentation) • [Contribute](#-contributing)
</div>

---

## 🌍 Available in 30 Languages

<details open>
<summary><b>📖 Read this page in your language</b></summary>

### [🇬🇧 English](#-english) | [🇹🇷 Türkçe](#-türkçe) | [🇩🇪 Deutsch](#-deutsch) | [🇫🇷 Français](#-français) | [🇪🇸 Español](#-español) | [🇮🇹 Italiano](#-italiano)

### [🇷🇺 Русский](#-русский) | [🇨🇳 中文](#-中文) | [🇯🇵 日本語](#-日本語) | [🇰🇷 한국어](#-한국어) | [🇸🇦 العربية](#-العربية) | [🇮🇳 हिन्दी](#-हिन्दी)

### [🇵🇹 Português](#-português) | [🇳🇱 Nederlands](#-nederlands) | [🇵🇱 Polski](#-polski) | [🇸🇪 Svenska](#-svenska) | [🇳🇴 Norsk](#-norsk) | [🇩🇰 Dansk](#-dansk)

### [🇫🇮 Suomi](#-suomi) | [🇬🇷 Ελληνικά](#-ελληνικά) | [🇨🇿 Čeština](#-čeština) | [🇭🇺 Magyar](#-magyar) | [🇷🇴 Română](#-română) | [🇺🇦 Українська](#-українська)

### [🇮🇱 עברית](#-עברית) | [🇮🇩 Indonesia](#-indonesia) | [🇹🇭 ไทย](#-ไทย) | [🇻🇳 Tiếng Việt](#-tiếng-việt) | [🇮🇷 فارسی](#-فارسی) | [🇵🇰 اردو](#-اردو)

</details>

---

## 🇬🇧 English

## 📖 About

**PiLegal** is a free, open-source knowledge encyclopedia containing **4.1+ million articles** across multiple domains including programming, cybersecurity, data science, web development, and more. Designed with a Wikipedia-style interface for ease of use.

### ✨ Features

- 🔍 **Powerful Search Engine** - Instant search across 4.1M+ articles
- 📚 **Multi-Category Content** - Programming, security, data science, and more
- 🎨 **Wikipedia-Style UI** - Clean, user-friendly design
- 🚀 **Fast RESTful API** - Easy integration with your applications
- 🎲 **Random Article Discovery** - Explore random content
- 📊 **Detailed Statistics** - Category-based analytics
- 🌐 **30+ Languages** - Multilingual documentation
- ⚡ **High Performance** - <100ms search response time
- 🔓 **CC0 Licensed** - Completely free to use, modify, and distribute

---

## 🚀 Quick Start

### Requirements

- Python 3.8 or higher
- pip (Python package manager)
- 4 GB+ free disk space

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download the data file**

Download `pilegal_data_v1.jsonl` (3.92 GB) from [Releases](https://github.com/beydeveloper/pilegal/releases) and place it in the project root.

4. **Start the server**
```bash
python server.py
# or use: py server.py (Windows)
```

5. **Open in your browser**
```
http://localhost:5000
```

### Windows Quick Start

Simply double-click:
```
START_SERVER.bat
```

---

## 📊 Content Distribution

| Category | Article Count | Description |
|----------|---------------|-------------|
| 💻 **Programming** | ~1.5M | Python, JavaScript, Java, C++, and more |
| 🔐 **Cybersecurity** | ~800K | Exploit analysis, penetration testing, security |
| 📊 **Data Science** | ~600K | Machine Learning, AI, data analysis |
| 🌐 **Web Development** | ~500K | Frontend, Backend, Full-stack |
| 🗄️ **Database** | ~300K | SQL, NoSQL, data modeling |
| 🔧 **Other** | ~400K | Network, system administration, DevOps |

**Total:** 4,120,756 articles | **Size:** 3.92 GB

---

## 🔌 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### 1️⃣ Statistics
```http
GET /api/stats
```

**Example Response:**
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

#### 2️⃣ Search
```http
GET /api/search?q=python&page=1&limit=20&category=programming
```

**Parameters:**
- `q` - Search query (required)
- `page` - Page number (default: 1)
- `limit` - Results per page (default: 20, max: 100)
- `category` - Category filter (optional)

**Example Response:**
```json
{
  "results": [
    {
      "instruction": "How to create a list in Python?",
      "output": "To create a list in Python...",
      "category": "programming"
    }
  ],
  "total": 15000,
  "page": 1,
  "limit": 20,
  "total_pages": 750
}
```

#### 3️⃣ Random Article
```http
GET /api/random
```

**Example Response:**
```json
{
  "instruction": "What is SQL Injection?",
  "output": "SQL Injection is a code injection technique...",
  "category": "security"
}
```

#### 4️⃣ Categories
```http
GET /api/categories
```

**Example Response:**
```json
{
  "categories": [
    {"name": "programming", "label": "Programming", "count": 1500000},
    {"name": "security", "label": "Security", "count": 800000},
    {"name": "data_science", "label": "Data Science", "count": 600000}
  ],
  "total": 8
}
```

---

## 🎨 Interface Features

### Wikipedia-Style Design
- 📱 Responsive (mobile-friendly)
- 🎯 Easy navigation
- 🔍 Instant search
- 📑 Pagination
- 🎲 Random article discovery
- 📊 Category filtering
- 🌙 Clean, minimal design

### Keyboard Shortcuts
- `Enter` - Perform search
- `Esc` - Clear results

---

## 🗂️ Project Structure

```
pilegal/
├── server.py                    # Flask backend with optimized search
├── index.html                   # Main interface (Wikipedia-style)
├── pilegal.png                  # Logo
├── pilegal_data_v1.jsonl        # Main data file (3.92 GB)
├── requirements.txt             # Python dependencies
├── START_SERVER.bat            # Windows startup script
├── LICENSE                      # CC0 1.0 Universal License
├── README.md                    # This file
├── QUICKSTART.md               # Quick start guide
├── CONTRIBUTING.md             # Contribution guidelines
└── .gitignore                  # Git ignore rules
```

---

## 🔧 Developer Notes

### Data Format

Each article is in JSONL format:
```json
{
  "instruction": "Question or title",
  "output": "Detailed explanation or answer",
  "category": "Category name"
}
```

### Performance

- **Loading Time:** ~40 seconds (4.1M records with indexing)
- **RAM Usage:** ~2-3 GB
- **Search Speed:** <100ms average (with hash-based indexing)
- **Index Build:** Automatic on startup

### Optimization Features

- ✅ Hash-based search indexing
- ✅ Category indexing with O(1) lookup
- ✅ Query term splitting for better matches
- ✅ Result limiting (max 1000) for speed
- ✅ Cached category counts

### Customization

You can modify these parameters in `server.py`:
- `DATA_FILE`: Data file path
- Port number (default: 5000)
- CORS settings
- Result limits

---

## 📚 Data Sources

PiLegal was created by combining open-source datasets:
- OpenOrca GPT-4
- ShareGPT Vicuna
- OpenAssistant
- Alpaca Dataset
- Dolly-15K
- Code Alpaca
- SQL Context Dataset
- MITRE ATT&CK
- CWE Database
- And many more...

All content is aggregated from publicly available datasets and is provided under CC0 1.0 Universal License.

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork this repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Areas
- 🐛 Bug fixes
- ✨ New features
- 📝 Documentation improvements
- 🌐 Translations
- 🎨 UI enhancements
- 🚀 Performance optimizations

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the **Creative Commons Zero v1.0 Universal (CC0 1.0)** license.

### What this means:
- ✅ **No Copyright** - Completely public domain
- ✅ **Use freely** - Personal or commercial use
- ✅ **Modify freely** - Create derivative works
- ✅ **Distribute freely** - Share with anyone
- ✅ **No attribution required** - Though appreciated!

See the [LICENSE](LICENSE) file for full details.

**TLDR:** You can do whatever you want with this project. No strings attached.

---

## 🌟 Why CC0?

We believe knowledge should be free and accessible to everyone. By releasing PiLegal under CC0:

- 🌍 **Universal Access** - No legal barriers anywhere in the world
- 🔓 **True Freedom** - No attribution requirements or restrictions
- 🚀 **Maximum Reuse** - Easy integration into any project
- 💡 **Knowledge Commons** - Contributing to the public domain

---

## 👨‍💻 Developer

<div align="center">
  <a href="https://github.com/beydeveloper">
    <img src="https://img.shields.io/badge/GitHub-beydeveloper-181717?style=for-the-badge&logo=github" alt="GitHub"/>
  </a>
  
  Developed with ❤️ by **beydeveloper**
</div>

---

## 🌟 Support

Thank you for using PiLegal! If you find it helpful:

- ⭐ Star this repository
- 🐛 Report bugs via [Issues](https://github.com/beydeveloper/pilegal/issues)
- 💡 Suggest features via [Discussions](https://github.com/beydeveloper/pilegal/discussions)
- 🔄 Share with others
- 💖 Contribute to the project

### Contact
- 🐛 Bug reports: [GitHub Issues](https://github.com/beydeveloper/pilegal/issues)
- 💡 Feature requests: [GitHub Discussions](https://github.com/beydeveloper/pilegal/discussions)
- 📧 Email: [GitHub Profile](https://github.com/beydeveloper)

---

## 🎯 Roadmap

### Current Version: v1.0
- ✅ 4.1M+ articles database
- ✅ Fast search with indexing
- ✅ Wikipedia-style UI
- ✅ RESTful API
- ✅ 30+ language documentation

### Upcoming Features
- 🔄 Real-time data updates
- 🌙 Dark mode
- 📱 Mobile app
- 🔍 Advanced search filters
- 📊 Analytics dashboard
- 🤖 AI-powered recommendations
- 🌐 Multilingual article content

---

## 📈 Statistics

- **Total Articles:** 4,120,756
- **Total Size:** 3.92 GB (JSONL)
- **Categories:** 8 main categories
- **Languages:** 30+ documentation languages
- **Search Speed:** <100ms average
- **API Endpoints:** 4
- **License:** CC0 1.0 Universal (Public Domain)

---

## 🔗 Related Projects

- [Wikipedia](https://www.wikipedia.org/) - The original encyclopedia everyone can edit
- [DBpedia](https://www.dbpedia.org/) - Structured data from Wikipedia
- [Wikidata](https://www.wikidata.org/) - Free knowledge base
- [OpenAI Datasets](https://github.com/openai) - AI training datasets

---

## 🙏 Acknowledgments

Special thanks to:
- All open-source dataset contributors
- The Flask and Python communities
- Wikipedia for inspiration
- Everyone who contributed to making knowledge free

---

<div align="center">
  
  ### 🔓 Public Domain • No Rights Reserved
  
  **PiLegal** • Free Knowledge Encyclopedia • 2025
  
  <sub>4.1M+ articles • 30+ languages • 100% free</sub>
  
  ---
  
  Made with ❤️ for the global knowledge commons
  
</div>

---
---

## 🇹🇷 Türkçe

## 📖 Hakkında

**PiLegal**, programlama, siber güvenlik, veri bilimi, web geliştirme ve daha birçok alanda **4.1+ milyon makale** içeren özgür, açık kaynaklı bir bilgi ansiklopedisidir.

### ✨ Özellikler

- 🔍 **Güçlü Arama Motoru** - 4.1M+ makale içinde anlık arama
- 📚 **Çok Kategorili İçerik** - Programlama, güvenlik, veri bilimi
- 🎨 **Wikipedia Tarzı Arayüz** - Temiz, kullanıcı dostu tasarım
- 🚀 **Hızlı RESTful API** - Kolay entegrasyon
- ⚡ **Yüksek Performans** - <100ms arama süresi
- 🔓 **CC0 Lisanslı** - Tamamen ücretsiz

### 🚀 Kurulum

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py  # veya: py server.py
```

Tarayıcıda açın: `http://localhost:5000`

### 📊 İçerik
- 💻 Programlama: ~1.5M makale
- 🔐 Siber Güvenlik: ~800K makale
- 📊 Veri Bilimi: ~600K makale
- 🌐 Web: ~500K makale

**Toplam:** 4,120,756 makale | 3.92 GB

---

## 🇩🇪 Deutsch

## 📖 Über das Projekt

**PiLegal** ist eine freie Wissensenzyklopädie mit **4,1+ Millionen Artikeln** zu Programmierung, Cybersicherheit, Datenwissenschaft, Webentwicklung und mehr.

### ✨ Funktionen

- 🔍 **Leistungsstarke Suche** - Über 4,1M+ Artikel
- 📚 **Mehrere Kategorien** - Programmierung, Sicherheit, Datenwissenschaft
- 🎨 **Wikipedia-Stil** - Sauberes Design
- 🚀 **Schnelle API** - Einfache Integration
- ⚡ **Hohe Leistung** - <100ms Antwortzeit
- 🔓 **CC0 Lizenz** - Völlig frei

### 🚀 Installation

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

Browser öffnen: `http://localhost:5000`

### 📊 Inhalt
- 💻 Programmierung: ~1,5M Artikel
- 🔐 Cybersicherheit: ~800K Artikel
- 📊 Datenwissenschaft: ~600K Artikel

**Gesamt:** 4.120.756 Artikel | 3,92 GB

---

## 🇫🇷 Français

## 📖 À Propos

**PiLegal** est une encyclopédie libre contenant **4,1+ millions d'articles** sur la programmation, la cybersécurité, la science des données, le développement web et plus.

### ✨ Fonctionnalités

- 🔍 **Recherche Puissante** - Plus de 4,1M+ articles
- 📚 **Multi-Catégories** - Programmation, sécurité, data science
- 🎨 **Style Wikipedia** - Design propre
- 🚀 **API Rapide** - Intégration facile
- ⚡ **Haute Performance** - <100ms
- 🔓 **Licence CC0** - Totalement libre

### 🚀 Installation

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

Ouvrir: `http://localhost:5000`

### 📊 Contenu
- 💻 Programmation: ~1,5M articles
- 🔐 Cybersécurité: ~800K articles
- 📊 Science des données: ~600K articles

**Total:** 4.120.756 articles | 3,92 GB

---

## 🇪🇸 Español

## 📖 Acerca de

**PiLegal** es una enciclopedia libre con **4,1+ millones de artículos** sobre programación, ciberseguridad, ciencia de datos, desarrollo web y más.

### ✨ Características

- 🔍 **Búsqueda Potente** - Más de 4,1M+ artículos
- 📚 **Multi-Categoría** - Programación, seguridad, ciencia de datos
- 🎨 **Estilo Wikipedia** - Diseño limpio
- 🚀 **API Rápida** - Integración fácil
- ⚡ **Alto Rendimiento** - <100ms
- 🔓 **Licencia CC0** - Totalmente libre

### 🚀 Instalación

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

Abrir: `http://localhost:5000`

### 📊 Contenido
- 💻 Programación: ~1,5M artículos
- 🔐 Ciberseguridad: ~800K artículos
- 📊 Ciencia de datos: ~600K artículos

**Total:** 4.120.756 artículos | 3,92 GB

---

## 🇮🇹 Italiano

## 📖 Informazioni

**PiLegal** è un'enciclopedia libera con **4,1+ milioni di articoli** su programmazione, cybersicurezza, data science, sviluppo web e altro.

### ✨ Caratteristiche

- 🔍 **Ricerca Potente** - Oltre 4,1M+ articoli
- 📚 **Multi-Categoria** - Programmazione, sicurezza, data science
- 🎨 **Stile Wikipedia** - Design pulito
- 🚀 **API Veloce** - Integrazione facile
- ⚡ **Alta Prestazione** - <100ms
- 🔓 **Licenza CC0** - Completamente libero

### 🚀 Installazione

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

Aprire: `http://localhost:5000`

### 📊 Contenuto
- 💻 Programmazione: ~1,5M articoli
- 🔐 Cybersicurezza: ~800K articoli
- 📊 Data science: ~600K articoli

**Totale:** 4.120.756 articoli | 3,92 GB

---

## 🇷🇺 Русский

## 📖 О Проекте

**PiLegal** - свободная энциклопедия с **4,1+ миллиона статей** о программировании, кибербезопасности, науке о данных, веб-разработке и многом другом.

### ✨ Возможности

- 🔍 **Мощный Поиск** - Более 4,1M+ статей
- 📚 **Мульти-Категории** - Программирование, безопасность, data science
- 🎨 **Стиль Wikipedia** - Чистый дизайн
- 🚀 **Быстрое API** - Простая интеграция
- ⚡ **Высокая Производительность** - <100мс
- 🔓 **Лицензия CC0** - Полностью свободно

### 🚀 Установка

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

Открыть: `http://localhost:5000`

### 📊 Содержание
- 💻 Программирование: ~1,5M статей
- 🔐 Кибербезопасность: ~800K статей
- 📊 Наука о данных: ~600K статей

**Всего:** 4.120.756 статей | 3,92 ГБ

---

## 🇨🇳 中文

## 📖 关于

**PiLegal** 是一个包含**410万+篇文章**的自由百科全书，涵盖编程、网络安全、数据科学、Web开发等。

### ✨ 特性

- 🔍 **强大搜索** - 超过410万+篇文章
- 📚 **多类别** - 编程、安全、数据科学
- 🎨 **维基百科风格** - 简洁设计
- 🚀 **快速API** - 轻松集成
- ⚡ **高性能** - <100毫秒
- 🔓 **CC0许可** - 完全免费

### 🚀 安装

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

打开: `http://localhost:5000`

### 📊 内容
- 💻 编程: ~150万篇
- 🔐 网络安全: ~80万篇
- 📊 数据科学: ~60万篇

**总计:** 4,120,756篇文章 | 3.92 GB

---

## 🇯🇵 日本語

## 📖 について

**PiLegal** は、プログラミング、サイバーセキュリティ、データサイエンス、Web開発などに関する**410万件以上の記事**を含む自由な百科事典です。

### ✨ 機能

- 🔍 **強力な検索** - 410万件以上の記事
- 📚 **マルチカテゴリ** - プログラミング、セキュリティ、データサイエンス
- 🎨 **Wikipediaスタイル** - クリーンなデザイン
- 🚀 **高速API** - 簡単な統合
- ⚡ **高性能** - <100ms
- 🔓 **CC0ライセンス** - 完全に自由

### 🚀 インストール

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

開く: `http://localhost:5000`

### 📊 コンテンツ
- 💻 プログラミング: ~150万件
- 🔐 サイバーセキュリティ: ~80万件
- 📊 データサイエンス: ~60万件

**合計:** 4,120,756件の記事 | 3.92 GB

---

## 🇰🇷 한국어

## 📖 소개

**PiLegal**은 프로그래밍, 사이버 보안, 데이터 과학, 웹 개발 등에 관한 **410만개 이상의 문서**를 포함하는 자유 백과사전입니다.

### ✨ 기능

- 🔍 **강력한 검색** - 410만개 이상의 문서
- 📚 **다중 카테고리** - 프로그래밍, 보안, 데이터 과학
- 🎨 **위키백과 스타일** - 깔끔한 디자인
- 🚀 **빠른 API** - 쉬운 통합
- ⚡ **높은 성능** - <100ms
- 🔓 **CC0 라이선스** - 완전히 자유

### 🚀 설치

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

열기: `http://localhost:5000`

### 📊 콘텐츠
- 💻 프로그래밍: ~150만개
- 🔐 사이버 보안: ~80만개
- 📊 데이터 과학: ~60만개

**총:** 4,120,756개 문서 | 3.92 GB

---

## 🇸🇦 العربية

## 📖 حول

**PiLegal** هي موسوعة معرفة حرة تحتوي على **أكثر من 4.1 مليون مقال** حول البرمجة والأمن السيبراني وعلم البيانات وتطوير الويب والمزيد.

### ✨ الميزات

- 🔍 **بحث قوي** - أكثر من 4.1 مليون مقال
- 📚 **فئات متعددة** - البرمجة، الأمان، علم البيانات
- 🎨 **نمط ويكيبيديا** - تصميم نظيف
- 🚀 **API سريع** - تكامل سهل
- ⚡ **أداء عالي** - <100 مللي ثانية
- 🔓 **ترخيص CC0** - حر تماماً

### 🚀 التثبيت

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

فتح: `http://localhost:5000`

### 📊 المحتوى
- 💻 البرمجة: ~1.5 مليون
- 🔐 الأمن السيبراني: ~800 ألف
- 📊 علم البيانات: ~600 ألف

**المجموع:** 4,120,756 مقال | 3.92 جيجابايت

---

## 🇮🇳 हिन्दी

## 📖 परिचय

**PiLegal** एक मुक्त ज्ञान विश्वकोश है जिसमें प्रोग्रामिंग, साइबर सुरक्षा, डेटा विज्ञान, वेब विकास और अधिक पर **41 लाख+ लेख** हैं।

### ✨ विशेषताएं

- 🔍 **शक्तिशाली खोज** - 41 लाख+ लेख
- 📚 **बहु-श्रेणी** - प्रोग्रामिंग, सुरक्षा, डेटा विज्ञान
- 🎨 **विकिपीडिया शैली** - स्वच्छ डिज़ाइन
- 🚀 **तेज़ API** - आसान एकीकरण
- ⚡ **उच्च प्रदर्शन** - <100ms
- 🔓 **CC0 लाइसेंस** - पूरी तरह मुक्त

### 🚀 स्थापना

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

खोलें: `http://localhost:5000`

### 📊 सामग्री
- 💻 प्रोग्रामिंग: ~15 लाख
- 🔐 साइबर सुरक्षा: ~8 लाख
- 📊 डेटा विज्ञान: ~6 लाख

**कुल:** 4,120,756 लेख | 3.92 GB

---

## 🇵🇹 Português

## 📖 Sobre

**PiLegal** é uma enciclopédia livre com **4,1+ milhões de artigos** sobre programação, cibersegurança, ciência de dados, desenvolvimento web e mais.

### ✨ Recursos

- 🔍 **Busca Poderosa** - Mais de 4,1M+ artigos
- 📚 **Multi-Categoria** - Programação, segurança, ciência de dados
- 🎨 **Estilo Wikipedia** - Design limpo
- 🚀 **API Rápida** - Integração fácil
- ⚡ **Alto Desempenho** - <100ms
- 🔓 **Licença CC0** - Totalmente livre

### 🚀 Instalação

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

Abrir: `http://localhost:5000`

### 📊 Conteúdo
- 💻 Programação: ~1,5M artigos
- 🔐 Cibersegurança: ~800K artigos
- 📊 Ciência de dados: ~600K artigos

**Total:** 4.120.756 artigos | 3,92 GB

---

## 🇳🇱 Nederlands

## 📖 Over

**PiLegal** is een vrije encyclopedie met **4,1+ miljoen artikelen** over programmeren, cyberbeveiliging, datascience, webontwikkeling en meer.

### ✨ Kenmerken

- 🔍 **Krachtig Zoeken** - Meer dan 4,1M+ artikelen
- 📚 **Multi-Categorie** - Programmeren, beveiliging, datascience
- 🎨 **Wikipedia-Stijl** - Schoon ontwerp
- 🚀 **Snelle API** - Gemakkelijke integratie
- ⚡ **Hoge Prestatie** - <100ms
- 🔓 **CC0 Licentie** - Volledig vrij

### 🚀 Installatie

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

Openen: `http://localhost:5000`

### 📊 Inhoud
- 💻 Programmeren: ~1,5M artikelen
- 🔐 Cyberbeveiliging: ~800K artikelen
- 📊 Datascience: ~600K artikelen

**Totaal:** 4.120.756 artikelen | 3,92 GB

---

## 🇵🇱 Polski

## 📖 O Projekcie

**PiLegal** to wolna encyklopedia z **4,1+ milionami artykułów** o programowaniu, cyberbezpieczeństwie, nauce o danych, rozwoju stron internetowych i nie tylko.

### ✨ Funkcje

- 🔍 **Potężne Wyszukiwanie** - Ponad 4,1M+ artykułów
- 📚 **Multi-Kategoria** - Programowanie, bezpieczeństwo, data science
- 🎨 **Styl Wikipedia** - Czysty design
- 🚀 **Szybkie API** - Łatwa integracja
- ⚡ **Wysoka Wydajność** - <100ms
- 🔓 **Licencja CC0** - Całkowicie darmowe

### 🚀 Instalacja

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

Otwórz: `http://localhost:5000`

### 📊 Zawartość
- 💻 Programowanie: ~1,5M artykułów
- 🔐 Cyberbezpieczeństwo: ~800K artykułów
- 📊 Nauka o danych: ~600K artykułów

**Razem:** 4.120.756 artykułów | 3,92 GB

---

## 🇸🇪 Svenska

## 📖 Om

**PiLegal** är en fri encyklopedi med **4,1+ miljoner artiklar** om programmering, cybersäkerhet, datavetenskap, webbutveckling och mer.

### ✨ Funktioner

- 🔍 **Kraftfull Sökning** - Över 4,1M+ artiklar
- 📚 **Multi-Kategori** - Programmering, säkerhet, datavetenskap
- 🎨 **Wikipedia-Stil** - Ren design
- 🚀 **Snabb API** - Enkel integration
- ⚡ **Hög Prestanda** - <100ms
- 🔓 **CC0 Licens** - Helt fri

### 🚀 Installation

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

Öppna: `http://localhost:5000`

### 📊 Innehåll
- 💻 Programmering: ~1,5M artiklar
- 🔐 Cybersäkerhet: ~800K artiklar
- 📊 Datavetenskap: ~600K artiklar

**Totalt:** 4.120.756 artiklar | 3,92 GB

---

## 🇳🇴 Norsk

## 📖 Om

**PiLegal** er et fritt leksikon med **4,1+ millioner artikler** om programmering, cybersikkerhet, datavitenskap, webutvikling og mer.

### ✨ Funksjoner

- 🔍 **Kraftig Søk** - Over 4,1M+ artikler
- 📚 **Multi-Kategori** - Programmering, sikkerhet, datavitenskap
- 🎨 **Wikipedia-Stil** - Rent design
- 🚀 **Rask API** - Enkel integrasjon
- ⚡ **Høy Ytelse** - <100ms
- 🔓 **CC0 Lisens** - Helt gratis

### 🚀 Installasjon

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

Åpne: `http://localhost:5000`

### 📊 Innhold
- 💻 Programmering: ~1,5M artikler
- 🔐 Cybersikkerhet: ~800K artikler
- 📊 Datavitenskap: ~600K artikler

**Totalt:** 4.120.756 artikler | 3,92 GB

---

## 🇩🇰 Dansk

## 📖 Om

**PiLegal** er en fri encyklopædi med **4,1+ millioner artikler** om programmering, cybersikkerhed, datavidenskab, webudvikling og mere.

### ✨ Funktioner

- 🔍 **Kraftfuld Søgning** - Over 4,1M+ artikler
- 📚 **Multi-Kategori** - Programmering, sikkerhed, datavidenskab
- 🎨 **Wikipedia-Stil** - Rent design
- 🚀 **Hurtig API** - Let integration
- ⚡ **Høj Ydeevne** - <100ms
- 🔓 **CC0 Licens** - Helt gratis

### 🚀 Installation

```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
pip install -r requirements.txt
python server.py
```

Åbn: `http://localhost:5000`

---

## 🇫🇮 Suomi

## 📖 Tietoja

**PiLegal** on vapaa tietosanakirja, jossa on **4,1+ miljoonaa artikkelia** ohjelmoinnista, kyberturvallisuudesta, datatiedestä, web-kehityksestä ja muusta.

### ✨ Ominaisuudet

- 🔍 **Tehokas Haku** - Yli 4,1M+ artikkelia
- 📚 **Moni-Kategoria** - Ohjelmointi, turvallisuus, datatiede
- 🚀 **Nopea API** - Helppo integrointi
- 🔓 **CC0 Lisenssi** - Täysin ilmainen

---

## 🇬🇷 Ελληνικά

## 📖 Σχετικά

**PiLegal** είναι μια ελεύθερη εγκυκλοπαίδεια με **4,1+ εκατομμύρια άρθρα** για προγραμματισμό, κυβερνοασφάλεια, επιστήμη δεδομένων και περισσότερα.

---

## 🇨🇿 Čeština

## 📖 O Projektu

**PiLegal** je svobodná encyklopedie s **4,1+ miliony článků** o programování, kybernetické bezpečnosti, datové vědě a více.

---

## 🇭🇺 Magyar

## 📖 Rólunk

**PiLegal** egy szabad enciklopédia **4,1+ millió cikkel** programozásról, kiberbiztonságról, adattudományról és még sokról.

---

## 🇷🇴 Română

## 📖 Despre

**PiLegal** este o enciclopedie liberă cu **4,1+ milioane de articole** despre programare, securitate cibernetică, știința datelor și mai mult.

---

## 🇺🇦 Українська

## 📖 Про Проект

**PiLegal** - вільна енциклопедія з **4,1+ мільйона статей** про програмування, кібербезпеку, науку про дані та багато іншого.

---

## 🇮🇱 עברית

## 📖 אודות

**PiLegal** היא אנציקלופדיה חופשית עם **4.1+ מיליון מאמרים** על תכנות, אבטחת סייבר, מדע הנתונים ועוד.

---

## 🇮🇩 Indonesia

## 📖 Tentang

**PiLegal** adalah ensiklopedia bebas dengan **4,1+ juta artikel** tentang pemrograman, keamanan siber, ilmu data, pengembangan web dan lainnya.

### ✨ Fitur

- 🔍 **Pencarian Kuat** - Lebih dari 4,1M+ artikel
- 📚 **Multi-Kategori** - Pemrograman, keamanan, ilmu data
- 🚀 **API Cepat** - Integrasi mudah
- 🔓 **Lisensi CC0** - Sepenuhnya gratis

---

## 🇹🇭 ไทย

## 📖 เกี่ยวกับ

**PiLegal** เป็นสารานุกรมเสรีที่มี**บทความมากกว่า 4.1 ล้าน**เกี่ยวกับการเขียนโปรแกรม ความปลอดภัยทางไซเบอร์ วิทยาศาสตร์ข้อมูล และอื่นๆ

---

## 🇻🇳 Tiếng Việt

## 📖 Giới Thiệu

**PiLegal** là bách khoa toàn thư mở với **hơn 4,1 triệu bài viết** về lập trình, an ninh mạng, khoa học dữ liệu và nhiều hơn nữa.

---

## 🇮🇷 فارسی

## 📖 درباره

**PiLegal** یک دانشنامه آزاد با **بیش از 4.1 میلیون مقاله** در مورد برنامه‌نویسی، امنیت سایبری، علم داده و موارد دیگر است.

---

## 🇵🇰 اردو

## 📖 تعارف

**PiLegal** ایک آزاد دائرۃ المعارف ہے جس میں پروگرامنگ، سائبر سیکیورٹی، ڈیٹا سائنس اور مزید کے بارے میں **41 لاکھ سے زیادہ مضامین** ہیں۔

---

[⬆️ Back to top](#-pilegal)
