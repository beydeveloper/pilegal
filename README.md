<div align="center">
  <img src="pilegal_logo.png" alt="PiLegal Logo" width="150"/>
  
  # 🔍 PiLegal
  ### Free Knowledge Encyclopedia for Everyone
  
  [![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
  [![Flask](https://img.shields.io/badge/Flask-3.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
  [![License](https://img.shields.io/badge/License-CC0_1.0-green.svg?style=for-the-badge)](LICENSE)
  [![Records](https://img.shields.io/badge/Records-4.1M+-blue?style=for-the-badge)]()
  [![Data](https://img.shields.io/badge/Data-3.92GB-orange?style=for-the-badge)]()
  
  **4.1+ Million articles** - Comprehensive knowledge base
  
  [Data Download](https://github.com/beydeveloper/pilegal/releases/download/data/pilegal_data_v1.zip) • [Installation](#-quick-start) • [API](#-api-documentation) • [Contribute](#-contributing)
</div>

---

## 🌍 Available in 29 Languages

<details open>
<summary><b>📖 Read this page in your language</b></summary>

### [🇬🇧 English](#-english) | [🇹🇷 Türkçe](#-türkçe) | [🇩🇪 Deutsch](#-deutsch) | [🇫🇷 Français](#-français) | [🇪🇸 Español](#-español) | [🇮🇹 Italiano](#-italiano)

### [🇷🇺 Русский](#-русский) | [🇨🇳 中文](#-中文) | [🇯🇵 日本語](#-日本語) | [🇰🇷 한국어](#-한국어) | [🇸🇦 العربية](#-العربية) | [🇮🇳 हिन्दी](#-हिन्दी)

### [🇵🇹 Português](#-português) | [🇳🇱 Nederlands](#-nederlands) | [🇵🇱 Polski](#-polski) | [🇸🇪 Svenska](#-svenska) | [🇳🇴 Norsk](#-norsk) | [🇩🇰 Dansk](#-dansk)

### [🇫🇮 Suomi](#-suomi) | [🇬🇷 Ελληνικά](#-ελληνικά) | [🇨🇿 Čeština](#-čeština) | [🇭🇺 Magyar](#-magyar) | [🇷🇴 Română](#-română) | [🇺🇦 Українська](#-українська)

### [🇮🇩 Indonesia](#-indonesia) | [🇹🇭 ไทย](#-ไทย) | [🇻🇳 Tiếng Việt](#-tiếng-việt) | [🇮🇷 فارسی](#-فارسی) | [🇵🇰 اردو](#-اردو)

</details>

---

## 🇬🇧 English

## 📖 About

**PiLegal** is a free, open-source knowledge encyclopedia containing **4.1+ million articles** across multiple domains including programming, cybersecurity, data science, web development, and more.

### ✨ Features

- 🔍 **Powerful Search Engine** - Instant search across 4.1M+ articles
- 📚 **Multi-Category Content** - Programming, security, data science, and more
- 🎨 **Clean User Interface** - User-friendly design
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

Download `pilegal_data_v1.jsonl` (3.92 GB) from the link below and place it in the project root directory:

📥 **Download Link:** [Click here to download](https://github.com/beydeveloper/pilegal/releases)

**Important:** After downloading, move the file to your project folder:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Place the downloaded file here
├── server.py
├── index.html
└── ...
```

The file should be in the same directory as `server.py`.

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

### Clean Modern Design
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
- **RAM Usage:** ~0-2 GB
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
- 📧 İnstagram: [İnstagram Profile](https://www.instagram.com/beydeveloper/)
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
  
  
  
</div>

---
---

## 🇹🇷 Türkçe

## 📖 Hakkında

**PiLegal**, programlama, siber güvenlik, veri bilimi, web geliştirme ve daha birçok alanda **4.1+ milyon makale** içeren özgür, açık kaynaklı bir bilgi ansiklopedisidir.

### ✨ Özellikler

- 🔍 **Güçlü Arama Motoru** - 4.1M+ makale içinde anlık arama
- 📚 **Çok Kategorili İçerik** - Programlama, güvenlik, veri bilimi
- 🎨 **Temiz Arayüz** - Kullanıcı dostu tasarım
- 🚀 **Hızlı RESTful API** - Kolay entegrasyon
- ⚡ **Yüksek Performans** - <100ms arama süresi
- 🔓 **CC0 Lisanslı** - Tamamen ücretsiz

### 🚀 Kurulum

**1. Repoyu klonlayın:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

**3. Veri dosyasını indirin:**

`pilegal_data_v1.jsonl` dosyasını (3.92 GB) aşağıdaki linkten indirin:

📥 **İndirme Linki:** [Buradan indirebilirsiniz](https://github.com/beydeveloper/pilegal/releases)

**Önemli:** İndirdikten sonra dosyayı proje dizinine koyun:
```
pilegal/
├── pilegal_data_v1.jsonl    ← İndirilen dosyayı buraya koyun
├── server.py
├── index.html
└── ...
```

Dosya `server.py` ile aynı dizinde olmalıdır.

**4. Sunucuyu başlatın:**
```bash
python server.py  # veya: py server.py
```

**5. Tarayıcıda açın:** `http://localhost:5000`

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
- 🎨 **Sauberes Design** - Benutzerfreundlich
- 🚀 **Schnelle API** - Einfache Integration
- ⚡ **Hohe Leistung** - <100ms Antwortzeit
- 🔓 **CC0 Lizenz** - Völlig frei

### 🚀 Installation

**1. Repository klonen:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Abhängigkeiten installieren:**
```bash
pip install -r requirements.txt
```

**3. Datendatei herunterladen:**

Laden Sie `pilegal_data_v1.jsonl` (3,92 GB) herunter:

📥 **Download-Link:** [Hier herunterladen](https://github.com/beydeveloper/pilegal/releases)

**Wichtig:** Legen Sie die Datei nach dem Download in das Projektverzeichnis:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Heruntergeladene Datei hier platzieren
├── server.py
├── index.html
└── ...
```

**4. Server starten:**
```bash
python server.py
```

**5. Browser öffnen:** `http://localhost:5000`

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
- 🎨 **Design Moderne** - Interface propre
- 🚀 **API Rapide** - Intégration facile
- ⚡ **Haute Performance** - <100ms
- 🔓 **Licence CC0** - Totalement libre

### 🚀 Installation

**1. Cloner le dépôt:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Installer les dépendances:**
```bash
pip install -r requirements.txt
```

**3. Télécharger le fichier de données:**

Téléchargez `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Lien de téléchargement:** [Cliquez ici](https://github.com/beydeveloper/pilegal/releases)

**Important:** Placez le fichier dans le répertoire du projet après téléchargement:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Placez le fichier téléchargé ici
├── server.py
├── index.html
└── ...
```

**4. Démarrer le serveur:**
```bash
python server.py
```

**5. Ouvrir:** `http://localhost:5000`

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
- 🎨 **Diseño Moderno** - Interfaz limpia
- 🚀 **API Rápida** - Integración fácil
- ⚡ **Alto Rendimiento** - <100ms
- 🔓 **Licencia CC0** - Totalmente libre

### 🚀 Instalación

**1. Clonar el repositorio:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Instalar dependencias:**
```bash
pip install -r requirements.txt
```

**3. Descargar el archivo de datos:**

Descargue `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Enlace de descarga:** [Haga clic aquí](https://github.com/beydeveloper/pilegal/releases)

**Importante:** Coloque el archivo en el directorio del proyecto después de descargarlo:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Coloque el archivo descargado aquí
├── server.py
├── index.html
└── ...
```

**4. Iniciar el servidor:**
```bash
python server.py
```

**5. Abrir:** `http://localhost:5000`

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
- 🎨 **Design Moderno** - Interfaccia pulita
- 🚀 **API Veloce** - Integrazione facile
- ⚡ **Alta Prestazione** - <100ms
- 🔓 **Licenza CC0** - Completamente libero

### 🚀 Installazione

**1. Clonare il repository:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Installare le dipendenze:**
```bash
pip install -r requirements.txt
```

**3. Scaricare il file dati:**

Scarica `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Link di download:** [Clicca qui](https://github.com/beydeveloper/pilegal/releases)

**Importante:** Posiziona il file nella directory del progetto dopo il download:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Posiziona il file scaricato qui
├── server.py
├── index.html
└── ...
```

**4. Avviare il server:**
```bash
python server.py
```

**5. Aprire:** `http://localhost:5000`

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
- 🎨 **Современный Дизайн** - Чистый интерфейс
- 🚀 **Быстрое API** - Простая интеграция
- ⚡ **Высокая Производительность** - <100мс
- 🔓 **Лицензия CC0** - Полностью свободно

### 🚀 Установка

**1. Клонировать репозиторий:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Установить зависимости:**
```bash
pip install -r requirements.txt
```

**3. Скачать файл данных:**

Скачайте `pilegal_data_v1.jsonl` (3,92 ГБ):

📥 **Ссылка для скачивания:** [Нажмите здесь](https://github.com/beydeveloper/pilegal/releases)

**Важно:** Поместите файл в каталог проекта после загрузки:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Поместите загруженный файл сюда
├── server.py
├── index.html
└── ...
```

**4. Запустить сервер:**
```bash
python server.py
```

**5. Открыть:** `http://localhost:5000`

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
- 🎨 **现代设计** - 简洁界面
- 🚀 **快速API** - 轻松集成
- ⚡ **高性能** - <100毫秒
- 🔓 **CC0许可** - 完全免费

### 🚀 安装

**1. 克隆仓库:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. 安装依赖:**
```bash
pip install -r requirements.txt
```

**3. 下载数据文件:**

下载 `pilegal_data_v1.jsonl` (3.92 GB):

📥 **下载链接:** [点击这里下载](https://github.com/beydeveloper/pilegal/releases)

**重要:** 下载后将文件放入项目目录:
```
pilegal/
├── pilegal_data_v1.jsonl    ← 将下载的文件放在这里
├── server.py
├── index.html
└── ...
```

**4. 启动服务器:**
```bash
python server.py
```

**5. 打开:** `http://localhost:5000`

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
- 🎨 **モダンなデザイン** - クリーンなインターフェース
- 🚀 **高速API** - 簡単な統合
- ⚡ **高性能** - <100ms
- 🔓 **CC0ライセンス** - 完全に自由

### 🚀 インストール

**1. リポジトリをクローン:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. 依存関係をインストール:**
```bash
pip install -r requirements.txt
```

**3. データファイルをダウンロード:**

`pilegal_data_v1.jsonl` (3.92 GB) をダウンロード:

📥 **ダウンロードリンク:** [ここをクリック](https://github.com/beydeveloper/pilegal/releases)

**重要:** ダウンロード後、ファイルをプロジェクトディレクトリに配置:
```
pilegal/
├── pilegal_data_v1.jsonl    ← ダウンロードしたファイルをここに配置
├── server.py
├── index.html
└── ...
```

**4. サーバーを起動:**
```bash
python server.py
```

**5. 開く:** `http://localhost:5000`

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
- 🎨 **모던 디자인** - 깔끔한 인터페이스
- 🚀 **빠른 API** - 쉬운 통합
- ⚡ **높은 성능** - <100ms
- 🔓 **CC0 라이선스** - 완전히 자유

### 🚀 설치

**1. 저장소 복제:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. 종속성 설치:**
```bash
pip install -r requirements.txt
```

**3. 데이터 파일 다운로드:**

`pilegal_data_v1.jsonl` (3.92 GB) 다운로드:

📥 **다운로드 링크:** [여기를 클릭](https://github.com/beydeveloper/pilegal/releases)

**중요:** 다운로드 후 파일을 프로젝트 디렉토리에 배치:
```
pilegal/
├── pilegal_data_v1.jsonl    ← 다운로드한 파일을 여기에 배치
├── server.py
├── index.html
└── ...
```

**4. 서버 시작:**
```bash
python server.py
```

**5. 열기:** `http://localhost:5000`

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
- 🎨 **تصميم عصري** - واجهة نظيفة
- 🚀 **API سريع** - تكامل سهل
- ⚡ **أداء عالي** - <100 مللي ثانية
- 🔓 **ترخيص CC0** - حر تماماً

### 🚀 التثبيت

**1. استنساخ المستودع:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. تثبيت التبعيات:**
```bash
pip install -r requirements.txt
```

**3. تنزيل ملف البيانات:**

قم بتنزيل `pilegal_data_v1.jsonl` (3.92 جيجابايت):

📥 **رابط التنزيل:** [انقر هنا للتنزيل](https://github.com/beydeveloper/pilegal/releases)

**مهم:** ضع الملف في دليل المشروع بعد التنزيل:
```
pilegal/
├── pilegal_data_v1.jsonl    ← ضع الملف المحمل هنا
├── server.py
├── index.html
└── ...
```

**4. بدء الخادم:**
```bash
python server.py
```

**5. فتح:** `http://localhost:5000`

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
- 🎨 **आधुनिक डिज़ाइन** - स्वच्छ इंटरफ़ेस
- 🚀 **तेज़ API** - आसान एकीकरण
- ⚡ **उच्च प्रदर्शन** - <100ms
- 🔓 **CC0 लाइसेंस** - पूरी तरह मुक्त

### 🚀 स्थापना

**1. रिपॉजिटरी क्लोन करें:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. निर्भरताएं स्थापित करें:**
```bash
pip install -r requirements.txt
```

**3. डेटा फ़ाइल डाउनलोड करें:**

`pilegal_data_v1.jsonl` (3.92 GB) डाउनलोड करें:

📥 **डाउनलोड लिंक:** [यहां क्लिक करें](https://github.com/beydeveloper/pilegal/releases)

**महत्वपूर्ण:** डाउनलोड के बाद फ़ाइल को प्रोजेक्ट डायरेक्टरी में रखें:
```
pilegal/
├── pilegal_data_v1.jsonl    ← डाउनलोड की गई फ़ाइल यहां रखें
├── server.py
├── index.html
└── ...
```

**4. सर्वर प्रारंभ करें:**
```bash
python server.py
```

**5. खोलें:** `http://localhost:5000`

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
- 🎨 **Design Moderno** - Interface limpa
- 🚀 **API Rápida** - Integração fácil
- ⚡ **Alto Desempenho** - <100ms
- 🔓 **Licença CC0** - Totalmente livre

### 🚀 Instalação

**1. Clonar o repositório:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Instalar dependências:**
```bash
pip install -r requirements.txt
```

**3. Baixar o arquivo de dados:**

Baixe `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Link de download:** [Clique aqui](https://github.com/beydeveloper/pilegal/releases)

**Importante:** Coloque o arquivo no diretório do projeto após o download:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Coloque o arquivo baixado aqui
├── server.py
├── index.html
└── ...
```

**4. Iniciar o servidor:**
```bash
python server.py
```

**5. Abrir:** `http://localhost:5000`

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
- 🎨 **Modern Ontwerp** - Schone interface
- 🚀 **Snelle API** - Gemakkelijke integratie
- ⚡ **Hoge Prestatie** - <100ms
- 🔓 **CC0 Licentie** - Volledig vrij

### 🚀 Installatie

**1. Repository klonen:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Afhankelijkheden installeren:**
```bash
pip install -r requirements.txt
```

**3. Gegevensbestand downloaden:**

Download `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Downloadlink:** [Klik hier](https://github.com/beydeveloper/pilegal/releases)

**Belangrijk:** Plaats het bestand in de projectmap na het downloaden:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Plaats het gedownloade bestand hier
├── server.py
├── index.html
└── ...
```

**4. Server starten:**
```bash
python server.py
```

**5. Openen:** `http://localhost:5000`

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
- 🎨 **Nowoczesny Design** - Czysty interfejs
- 🚀 **Szybkie API** - Łatwa integracja
- ⚡ **Wysoka Wydajność** - <100ms
- 🔓 **Licencja CC0** - Całkowicie darmowe

### 🚀 Instalacja

**1. Sklonuj repozytorium:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Zainstaluj zależności:**
```bash
pip install -r requirements.txt
```

**3. Pobierz plik danych:**

Pobierz `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Link do pobrania:** [Kliknij tutaj](https://github.com/beydeveloper/pilegal/releases)

**Ważne:** Umieść plik w katalogu projektu po pobraniu:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Umieść pobrany plik tutaj
├── server.py
├── index.html
└── ...
```

**4. Uruchom serwer:**
```bash
python server.py
```

**5. Otwórz:** `http://localhost:5000`

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
- 🎨 **Modern Design** - Rent gränssnitt
- 🚀 **Snabb API** - Enkel integration
- ⚡ **Hög Prestanda** - <100ms
- 🔓 **CC0 Licens** - Helt fri

### 🚀 Installation

**1. Klona repository:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Installera beroenden:**
```bash
pip install -r requirements.txt
```

**3. Ladda ner datafilen:**

Ladda ner `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Nedladdningslänk:** [Klicka här](https://github.com/beydeveloper/pilegal/releases)

**Viktigt:** Placera filen i projektkatalogen efter nedladdning:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Placera nedladdad fil här
├── server.py
├── index.html
└── ...
```

**4. Starta servern:**
```bash
python server.py
```

**5. Öppna:** `http://localhost:5000`

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
- 🎨 **Moderne Design** - Rent grensesnitt
- 🚀 **Rask API** - Enkel integrasjon
- ⚡ **Høy Ytelse** - <100ms
- 🔓 **CC0 Lisens** - Helt gratis

### 🚀 Installasjon

**1. Klone repository:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Installer avhengigheter:**
```bash
pip install -r requirements.txt
```

**3. Last ned datafilen:**

Last ned `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Nedlastingslenke:** [Klikk her](https://github.com/beydeveloper/pilegal/releases)

**Viktig:** Plasser filen i prosjektmappen etter nedlasting:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Plasser nedlastet fil her
├── server.py
├── index.html
└── ...
```

**4. Start serveren:**
```bash
python server.py
```

**5. Åpne:** `http://localhost:5000`

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
- 🎨 **Moderne Design** - Rent interface
- 🚀 **Hurtig API** - Let integration
- ⚡ **Høj Ydeevne** - <100ms
- 🔓 **CC0 Licens** - Helt gratis

### 🚀 Installation

**1. Klon repository:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Installer afhængigheder:**
```bash
pip install -r requirements.txt
```

**3. Download datafilen:**

Download `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Downloadlink:** [Klik her](https://github.com/beydeveloper/pilegal/releases)

**Vigtigt:** Placér filen i projektmappen efter download:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Placér downloadet fil her
├── server.py
├── index.html
└── ...
```

**4. Start serveren:**
```bash
python server.py
```

**5. Åbn:** `http://localhost:5000`

---

## 🇫🇮 Suomi

## 📖 Tietoja

**PiLegal** on vapaa, avoimen lähdekoodin tietosanakirja, joka sisältää **yli 4,1 miljoonaa artikkelia** useilla aloilla, mukaan lukien ohjelmointi, kyberturvallisuus, datatiede, web-kehitys ja paljon muuta.

### ✨ Ominaisuudet

- 🔍 **Tehokas Hakukone** - Välitön haku yli 4,1M+ artikkelista
- 📚 **Moniluokkainen Sisältö** - Ohjelmointi, turvallisuus, datatiede ja lisää
- 🎨 **Moderni Käyttöliittymä** - Puhdas, käyttäjäystävällinen suunnittelu
- 🚀 **Nopea RESTful API** - Helppo integrointi sovelluksiisi
- 🎲 **Satunnaisten Artikkelien Löytäminen** - Tutustu satunnaiseen sisältöön
- 📊 **Yksityiskohtaiset Tilastot** - Luokkakohtainen analytiikka
- 🌐 **29 Kieltä** - Monikielinen dokumentaatio
- ⚡ **Korkea Suorituskyky** - <100ms hakuvastausaika
- 🔓 **CC0-Lisensoitu** - Täysin ilmainen käyttää, muokata ja levittää

### 🚀 Asennus

**Vaatimukset:**
- Python 3.8 tai uudempi
- pip (Python-paketinhallinta)
- 4 GB+ vapaata levytilaa

**Asennusohjeet:**

**1. Kloonaa repositorio:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Asenna riippuvuudet:**
```bash
pip install -r requirements.txt
```

**3. Lataa datatiedosto:**

Lataa `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Latauslinkki:** [Klikkaa tästä](https://github.com/beydeveloper/pilegal/releases)

**Tärkeää:** Sijoita tiedosto projektihakemistoon latauksen jälkeen:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Sijoita ladattu tiedosto tähän
├── server.py
├── index.html
└── ...
```

**4. Käynnistä palvelin:**
```bash
python server.py
```

**5. Avaa selaimessa:** `http://localhost:5000`

### 📊 Sisältöjakauma
- 💻 **Ohjelmointi:** ~1,5M artikkelia - Python, JavaScript, Java, C++
- 🔐 **Kyberturvallisuus:** ~800K artikkelia - Haavoittuvuusanalyysi, tunkeutumistestaus
- 📊 **Datatiede:** ~600K artikkelia - Koneoppiminen, tekoäly, data-analyysi
- 🌐 **Web-Kehitys:** ~500K artikkelia - Frontend, Backend, Full-stack
- 🗄️ **Tietokanta:** ~300K artikkelia - SQL, NoSQL, tietomallinnus
- 🔧 **Muut:** ~400K artikkelia - Verkko, järjestelmähallinta, DevOps

**Yhteensä:** 4 120 756 artikkelia | **Koko:** 3,92 GB

### 📄 Lisenssi

Tämä projekti on lisensoitu **Creative Commons Zero v1.0 Universal (CC0 1.0)** -lisenssillä.

**Mitä tämä tarkoittaa:**
- ✅ Ei tekijänoikeuksia - Täysin julkinen
- ✅ Käytä vapaasti - Henkilökohtaiseen tai kaupalliseen käyttöön
- ✅ Muokkaa vapaasti - Luo johdannaisteoksia
- ✅ Levitä vapaasti - Jaa kenen tahansa kanssa
- ✅ Nimeämistä ei vaadita - Vaikka arvostetaan!

---

## 🇬🇷 Ελληνικά

## 📖 Σχετικά με το Έργο

**PiLegal** είναι μια ελεύθερη εγκυκλοπαίδεια ανοιχτού κώδικα που περιέχει **πάνω από 4,1 εκατομμύρια άρθρα** σε διάφορους τομείς, συμπεριλαμβανομένου του προγραμματισμού, της κυβερνοασφάλειας, της επιστήμης δεδομένων, της ανάπτυξης ιστού και πολλά άλλα.

### ✨ Χαρακτηριστικά

- 🔍 **Ισχυρή Μηχανή Αναζήτησης** - Άμεση αναζήτηση σε 4,1M+ άρθρα
- 📚 **Περιεχόμενο Πολλαπλών Κατηγοριών** - Προγραμματισμός, ασφάλεια, επιστήμη δεδομένων
- 🎨 **Μοντέρνα Διεπαφή** - Καθαρός, φιλικός προς το χρήστη σχεδιασμός
- 🚀 **Γρήγορο RESTful API** - Εύκολη ενσωμάτωση με τις εφαρμογές σας
- 🎲 **Ανακάλυψη Τυχαίων Άρθρων** - Εξερευνήστε τυχαίο περιεχόμενο
- 📊 **Λεπτομερή Στατιστικά** - Ανάλυση βάσει κατηγορίας
- 🌐 **29 Γλώσσες** - Πολύγλωσση τεκμηρίωση
- ⚡ **Υψηλή Απόδοση** - Χρόνος απόκρισης αναζήτησης <100ms
- 🔓 **Άδεια CC0** - Εντελώς ελεύθερο για χρήση, τροποποίηση και διανομή

### 🚀 Εγκατάσταση

**Απαιτήσεις:**
- Python 3.8 ή νεότερη έκδοση
- pip (διαχειριστής πακέτων Python)
- 4 GB+ ελεύθερος χώρος στο δίσκο

**Οδηγίες Εγκατάστασης:**

**1. Κλωνοποίηση αποθετηρίου:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Εγκατάσταση εξαρτήσεων:**
```bash
pip install -r requirements.txt
```

**3. Λήψη αρχείου δεδομένων:**

Κατεβάστε το `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Σύνδεσμος λήψης:** [Κάντε κλικ εδώ](https://github.com/beydeveloper/pilegal/releases)

**Σημαντικό:** Τοποθετήστε το αρχείο στον κατάλογο του έργου μετά τη λήψη:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Τοποθετήστε το ληφθέν αρχείο εδώ
├── server.py
├── index.html
└── ...
```

**4. Εκκίνηση διακομιστή:**
```bash
python server.py
```

**5. Ανοίξτε στο πρόγραμμα περιήγησης:** `http://localhost:5000`

### 📊 Κατανομή Περιεχομένου
- 💻 **Προγραμματισμός:** ~1,5M άρθρα - Python, JavaScript, Java, C++
- 🔐 **Κυβερνοασφάλεια:** ~800K άρθρα - Ανάλυση ευπαθειών, δοκιμές διείσδυσης
- 📊 **Επιστήμη Δεδομένων:** ~600K άρθρα - Μηχανική μάθηση, τεχνητή νοημοσύνη
- 🌐 **Ανάπτυξη Ιστού:** ~500K άρθρα - Frontend, Backend, Full-stack
- 🗄️ **Βάσεις Δεδομένων:** ~300K άρθρα - SQL, NoSQL, μοντελοποίηση δεδομένων
- 🔧 **Άλλα:** ~400K άρθρα - Δίκτυα, διαχείριση συστημάτων, DevOps

**Σύνολο:** 4.120.756 άρθρα | **Μέγεθος:** 3,92 GB

### 📄 Άδεια Χρήσης

Αυτό το έργο είναι αδειοδοτημένο με την άδεια **Creative Commons Zero v1.0 Universal (CC0 1.0)**.

**Τι σημαίνει αυτό:**
- ✅ Χωρίς πνευματικά δικαιώματα - Εντελώς στο δημόσιο τομέα
- ✅ Χρήση ελεύθερα - Προσωπική ή εμπορική χρήση
- ✅ Τροποποίηση ελεύθερα - Δημιουργία παράγωγων έργων
- ✅ Διανομή ελεύθερα - Κοινή χρήση με οποιονδήποτε
- ✅ Δεν απαιτείται αναφορά - Αν και εκτιμάται!

---

## 🇨🇿 Čeština

## 📖 O Projektu

**PiLegal** je svobodná encyklopedie s otevřeným zdrojovým kódem obsahující **více než 4,1 milionu článků** v různých oblastech včetně programování, kybernetické bezpečnosti, datové vědy, webového vývoje a mnoha dalších.

### ✨ Funkce

- 🔍 **Výkonný Vyhledávač** - Okamžité vyhledávání ve více než 4,1M+ článcích
- 📚 **Víceúrovňový Obsah** - Programování, bezpečnost, datová věda a další
- 🎨 **Moderní Rozhraní** - Čistý, uživatelsky přívětivý design
- 🚀 **Rychlé RESTful API** - Snadná integrace s vašimi aplikacemi
- 🎲 **Objevování Náhodných Článků** - Prozkoumejte náhodný obsah
- 📊 **Podrobné Statistiky** - Analýza založená na kategoriích
- 🌐 **29 Jazyků** - Vícejazyčná dokumentace
- ⚡ **Vysoký Výkon** - Doba odezvy vyhledávání <100ms
- 🔓 **Licence CC0** - Zcela zdarma k použití, úpravám a distribuci

### 🚀 Instalace

**Požadavky:**
- Python 3.8 nebo vyšší
- pip (správce balíčků Pythonu)
- 4 GB+ volného místa na disku

**Pokyny k instalaci:**

**1. Klonovat repozitář:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Nainstalovat závislosti:**
```bash
pip install -r requirements.txt
```

**3. Stáhnout datový soubor:**

Stáhněte `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Odkaz ke stažení:** [Klikněte zde](https://github.com/beydeveloper/pilegal/releases)

**Důležité:** Po stažení umístěte soubor do adresáře projektu:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Umístěte stažený soubor sem
├── server.py
├── index.html
└── ...
```

**4. Spustit server:**
```bash
python server.py
```

**5. Otevřete v prohlížeči:** `http://localhost:5000`

### 📊 Rozdělení Obsahu
- 💻 **Programování:** ~1,5M článků - Python, JavaScript, Java, C++
- 🔐 **Kybernetická Bezpečnost:** ~800K článků - Analýza zranitelností, penetrační testování
- 📊 **Datová Věda:** ~600K článků - Strojové učení, umělá inteligence, analýza dat
- 🌐 **Webový Vývoj:** ~500K článků - Frontend, Backend, Full-stack
- 🗄️ **Databáze:** ~300K článků - SQL, NoSQL, datové modelování
- 🔧 **Ostatní:** ~400K článků - Sítě, správa systémů, DevOps

**Celkem:** 4 120 756 článků | **Velikost:** 3,92 GB

### 📄 Licence

Tento projekt je licencován pod licencí **Creative Commons Zero v1.0 Universal (CC0 1.0)**.

**Co to znamená:**
- ✅ Bez autorských práv - Zcela ve veřejné doméně
- ✅ Používejte volně - Osobní nebo komerční použití
- ✅ Upravujte volně - Vytvářejte odvozená díla
- ✅ Distribuujte volně - Sdílejte s kýmkoli
- ✅ Není vyžadována atribuce - I když je vítána!

---

## 🇭🇺 Magyar

## 📖 A Projektről

**PiLegal** egy szabad, nyílt forráskódú tudásenciklopédia, amely **több mint 4,1 millió cikket** tartalmaz különböző területeken, beleértve a programozást, kiberbiztonsági, adattudományt, webfejlesztést és még sok mást.

### ✨ Jellemzők

- 🔍 **Erőteljes Keresőmotor** - Azonnali keresés több mint 4,1M+ cikkben
- 📚 **Többkategóriás Tartalom** - Programozás, biztonság, adattudomány és több
- 🎨 **Modern Felület** - Tiszta, felhasználóbarát dizájn
- 🚀 **Gyors RESTful API** - Könnyű integráció az alkalmazásaival
- 🎲 **Véletlenszerű Cikkek Felfedezése** - Fedezzen fel véletlenszerű tartalmat
- 📊 **Részletes Statisztikák** - Kategória alapú elemzés
- 🌐 **29 Nyelv** - Többnyelvű dokumentáció
- ⚡ **Nagy Teljesítmény** - <100ms keresési válaszidő
- 🔓 **CC0 Licenc** - Teljesen ingyenesen használható, módosítható és terjeszthető

### 🚀 Telepítés

**Követelmények:**
- Python 3.8 vagy újabb
- pip (Python csomagkezelő)
- 4 GB+ szabad lemezterület

**Telepítési útmutató:**

**1. Repository klónozása:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Függőségek telepítése:**
```bash
pip install -r requirements.txt
```

**3. Adatfájl letöltése:**

Töltse le a `pilegal_data_v1.jsonl` fájlt (3,92 GB):

📥 **Letöltési link:** [Kattintson ide](https://github.com/beydeveloper/pilegal/releases)

**Fontos:** A letöltés után helyezze el a fájlt a projekt könyvtárában:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Helyezze ide a letöltött fájlt
├── server.py
├── index.html
└── ...
```

**4. Szerver indítása:**
```bash
python server.py
```

**5. Nyissa meg a böngészőben:** `http://localhost:5000`

### 📊 Tartalomelosztás
- 💻 **Programozás:** ~1,5M cikk - Python, JavaScript, Java, C++
- 🔐 **Kiberbiztonság:** ~800K cikk - Sebezhetőség-elemzés, behatolási tesztelés
- 📊 **Adattudomány:** ~600K cikk - Gépi tanulás, mesterséges intelligencia
- 🌐 **Webfejlesztés:** ~500K cikk - Frontend, Backend, Full-stack
- 🗄️ **Adatbázis:** ~300K cikk - SQL, NoSQL, adatmodellezés
- 🔧 **Egyéb:** ~400K cikk - Hálózat, rendszeradminisztráció, DevOps

**Összesen:** 4 120 756 cikk | **Méret:** 3,92 GB

### 📄 Licenc

Ez a projekt a **Creative Commons Zero v1.0 Universal (CC0 1.0)** licenc alatt van licencelve.

**Mit jelent ez:**
- ✅ Nincs szerzői jog - Teljesen nyilvános tulajdon
- ✅ Szabadon használható - Személyes vagy kereskedelmi használatra
- ✅ Szabadon módosítható - Származékos művek létrehozása
- ✅ Szabadon terjeszthető - Megosztás bárkivel
- ✅ Nem szükséges forrásmegjelölés - Bár értékeljük!

---

## 🇷🇴 Română

## 📖 Despre Proiect

**PiLegal** este o enciclopedie liberă cu sursă deschisă care conține **peste 4,1 milioane de articole** în diverse domenii, inclusiv programare, securitate cibernetică, știința datelor, dezvoltare web și multe altele.

### ✨ Caracteristici

- 🔍 **Motor de Căutare Puternic** - Căutare instantanee în peste 4,1M+ articole
- 📚 **Conținut Multi-Categorie** - Programare, securitate, știința datelor și mai mult
- 🎨 **Interfață Modernă** - Design curat, prietenos cu utilizatorul
- 🚀 **API RESTful Rapid** - Integrare ușoară cu aplicațiile dumneavoastră
- 🎲 **Descoperirea Articolelor Aleatorii** - Explorați conținut aleatoriu
- 📊 **Statistici Detaliate** - Analiză bazată pe categorii
- 🌐 **29 de Limbi** - Documentație multilingvă
- ⚡ **Performanță Înaltă** - Timp de răspuns la căutare <100ms
- 🔓 **Licență CC0** - Complet gratuit pentru utilizare, modificare și distribuire

### 🚀 Instalare

**Cerințe:**
- Python 3.8 sau mai nou
- pip (manager de pachete Python)
- 4 GB+ spațiu liber pe disc

**Instrucțiuni de instalare:**

**1. Clonați repository-ul:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Instalați dependențele:**
```bash
pip install -r requirements.txt
```

**3. Descărcați fișierul de date:**

Descărcați `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Link de descărcare:** [Faceți clic aici](https://github.com/beydeveloper/pilegal/releases)

**Important:** Plasați fișierul în directorul proiectului după descărcare:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Plasați fișierul descărcat aici
├── server.py
├── index.html
└── ...
```

**4. Porniți serverul:**
```bash
python server.py
```

**5. Deschideți în browser:** `http://localhost:5000`

### 📊 Distribuția Conținutului
- 💻 **Programare:** ~1,5M articole - Python, JavaScript, Java, C++
- 🔐 **Securitate Cibernetică:** ~800K articole - Analiză vulnerabilități, testare penetrare
- 📊 **Știința Datelor:** ~600K articole - Învățare automată, inteligență artificială
- 🌐 **Dezvoltare Web:** ~500K articole - Frontend, Backend, Full-stack
- 🗄️ **Baze de Date:** ~300K articole - SQL, NoSQL, modelare date
- 🔧 **Altele:** ~400K articole - Rețele, administrare sisteme, DevOps

**Total:** 4 120 756 articole | **Dimensiune:** 3,92 GB

### 📄 Licență

Acest proiect este licențiat sub licența **Creative Commons Zero v1.0 Universal (CC0 1.0)**.

**Ce înseamnă acest lucru:**
- ✅ Fără drepturi de autor - Complet în domeniu public
- ✅ Utilizați liber - Utilizare personală sau comercială
- ✅ Modificați liber - Creați lucrări derivate
- ✅ Distribuiți liber - Partajați cu oricine
- ✅ Nu este necesară atribuirea - Deși este apreciată!

---

## 🇺🇦 Українська

## 📖 Про Проект

**PiLegal** - це вільна енциклопедія з відкритим вихідним кодом, що містить **понад 4,1 мільйона статей** у різних галузях, включаючи програмування, кібербезпеку, науку про дані, веб-розробку та багато іншого.

### ✨ Можливості

- 🔍 **Потужна Пошукова Система** - Миттєвий пошук серед понад 4,1M+ статей
- 📚 **Багатокатегорійний Контент** - Програмування, безпека, наука про дані та більше
- 🎨 **Сучасний Інтерфейс** - Чистий, зручний дизайн
- 🚀 **Швидке RESTful API** - Легка інтеграція з вашими додатками
- 🎲 **Відкриття Випадкових Статей** - Досліджуйте випадковий контент
- 📊 **Детальна Статистика** - Аналіз на основі категорій
- 🌐 **29 Мов** - Багатомовна документація
- ⚡ **Висока Продуктивність** - Час відповіді пошуку <100мс
- 🔓 **Ліцензія CC0** - Повністю безкоштовно для використання, зміни та розповсюдження

### 🚀 Встановлення

**Вимоги:**
- Python 3.8 або новіший
- pip (менеджер пакетів Python)
- 4 ГБ+ вільного місця на диску

**Інструкції з встановлення:**

**1. Клонувати репозиторій:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Встановити залежності:**
```bash
pip install -r requirements.txt
```

**3. Завантажити файл даних:**

Завантажте `pilegal_data_v1.jsonl` (3,92 ГБ):

📥 **Посилання для завантаження:** [Натисніть тут](https://github.com/beydeveloper/pilegal/releases)

**Важливо:** Помістіть файл у каталог проекту після завантаження:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Помістіть завантажений файл сюди
├── server.py
├── index.html
└── ...
```

**4. Запустити сервер:**
```bash
python server.py
```

**5. Відкрийте у браузері:** `http://localhost:5000`

### 📊 Розподіл Контенту
- 💻 **Програмування:** ~1,5M статей - Python, JavaScript, Java, C++
- 🔐 **Кібербезпека:** ~800K статей - Аналіз вразливостей, тестування на проникнення
- 📊 **Наука про Дані:** ~600K статей - Машинне навчання, штучний інтелект
- 🌐 **Веб-Розробка:** ~500K статей - Frontend, Backend, Full-stack
- 🗄️ **Бази Даних:** ~300K статей - SQL, NoSQL, моделювання даних
- 🔧 **Інше:** ~400K статей - Мережі, системне адміністрування, DevOps

**Усього:** 4 120 756 статей | **Розмір:** 3,92 ГБ

### 📄 Ліцензія

Цей проект ліцензовано під ліцензією **Creative Commons Zero v1.0 Universal (CC0 1.0)**.

**Що це означає:**
- ✅ Без авторських прав - Повністю у суспільному надбанні
- ✅ Використовуйте вільно - Особисте або комерційне використання
- ✅ Змінюйте вільно - Створюйте похідні роботи
- ✅ Поширюйте вільно - Діліться з ким завгодно
- ✅ Не потрібна атрибуція - Хоча вітається!

---

## 🇮🇩 Indonesia

## 📖 Tentang

**PiLegal** adalah ensiklopedia pengetahuan bebas dan open-source yang berisi **lebih dari 4,1 juta artikel** di berbagai bidang termasuk pemrograman, keamanan siber, ilmu data, pengembangan web, dan banyak lagi.

### ✨ Fitur

- 🔍 **Mesin Pencari Kuat** - Pencarian instan di lebih dari 4,1M+ artikel
- 📚 **Konten Multi-Kategori** - Pemrograman, keamanan, ilmu data, dan lebih banyak lagi
- 🎨 **Antarmuka Modern** - Desain bersih dan ramah pengguna
- 🚀 **RESTful API Cepat** - Integrasi mudah dengan aplikasi Anda
- 🎲 **Penemuan Artikel Acak** - Jelajahi konten acak
- 📊 **Statistik Terperinci** - Analitik berbasis kategori
- 🌐 **29 Bahasa** - Dokumentasi multibahasa
- ⚡ **Kinerja Tinggi** - Waktu respons pencarian <100ms
- 🔓 **Berlisensi CC0** - Sepenuhnya gratis untuk digunakan, dimodifikasi, dan didistribusikan

### 🚀 Instalasi

**Persyaratan:**
- Python 3.8 atau lebih tinggi
- pip (pengelola paket Python)
- 4 GB+ ruang disk kosong

**Petunjuk instalasi:**

**1. Clone repository:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Instal dependensi:**
```bash
pip install -r requirements.txt
```

**3. Unduh file data:**

Unduh `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Link unduhan:** [Klik di sini](https://github.com/beydeveloper/pilegal/releases)

**Penting:** Letakkan file di direktori proyek setelah mengunduh:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Letakkan file yang diunduh di sini
├── server.py
├── index.html
└── ...
```

**4. Jalankan server:**
```bash
python server.py
```

**5. Buka di browser:** `http://localhost:5000`

### 📊 Distribusi Konten
- 💻 **Pemrograman:** ~1,5M artikel - Python, JavaScript, Java, C++
- 🔐 **Keamanan Siber:** ~800K artikel - Analisis kerentanan, pengujian penetrasi
- 📊 **Ilmu Data:** ~600K artikel - Machine learning, AI, analisis data
- 🌐 **Pengembangan Web:** ~500K artikel - Frontend, Backend, Full-stack
- 🗄️ **Database:** ~300K artikel - SQL, NoSQL, pemodelan data
- 🔧 **Lainnya:** ~400K artikel - Jaringan, administrasi sistem, DevOps

**Total:** 4.120.756 artikel | **Ukuran:** 3,92 GB

### 📄 Lisensi

Proyek ini dilisensikan di bawah lisensi **Creative Commons Zero v1.0 Universal (CC0 1.0)**.

**Apa artinya ini:**
- ✅ Tanpa hak cipta - Sepenuhnya domain publik
- ✅ Gunakan dengan bebas - Penggunaan pribadi atau komersial
- ✅ Modifikasi dengan bebas - Buat karya turunan
- ✅ Distribusikan dengan bebas - Bagikan dengan siapa saja
- ✅ Tidak diperlukan atribusi - Meskipun dihargai!

---

## 🇹🇭 ไทย

## 📖 เกี่ยวกับโครงการ

**PiLegal** เป็นสารานุกรมความรู้เสรีและโอเพนซอร์สที่มี**บทความมากกว่า 4.1 ล้านบทความ**ในหลากหลายสาขา รวมถึงการเขียนโปรแกรม ความปลอดภัยทางไซเบอร์ วิทยาศาสตร์ข้อมูล การพัฒนาเว็บ และอื่นๆ อีกมากมาย

### ✨ คุณสมบัติ

- 🔍 **เครื่องมือค้นหาที่ทรงพลัง** - ค้นหาทันทีในบทความมากกว่า 4.1M+
- 📚 **เนื้อหาหลายหมวดหมู่** - การเขียนโปรแกรม ความปลอดภัย วิทยาศาสตร์ข้อมูล และอื่นๆ
- 🎨 **อินเทอร์เฟซทันสมัย** - การออกแบบที่สะอาดและเป็นมิตรกับผู้ใช้
- 🚀 **RESTful API ที่รวดเร็ว** - บูรณาการได้ง่ายกับแอปพลิเคชันของคุณ
- 🎲 **การค้นพบบทความแบบสุ่ม** - สำรวจเนื้อหาแบบสุ่ม
- 📊 **สถิติโดยละเอียด** - การวิเคราะห์ตามหมวดหมู่
- 🌐 **29 ภาษา** - เอกสารหลายภาษา
- ⚡ **ประสิทธิภาพสูง** - เวลาตอบสนองการค้นหา <100ms
- 🔓 **ใบอนุญาต CC0** - ฟรีโดยสมบูรณ์สำหรับการใช้งาน แก้ไข และแจกจ่าย

### 🚀 การติดตั้ง

**ข้อกำหนด:**
- Python 3.8 หรือสูงกว่า
- pip (ตัวจัดการแพ็คเกจ Python)
- พื้นที่ดิสก์ว่าง 4 GB+

**คำแนะนำการติดตั้ง:**

**1. โคลนรีพอสิทอรี:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. ติดตั้ง dependencies:**
```bash
pip install -r requirements.txt
```

**3. ดาวน์โหลดไฟล์ข้อมูล:**

ดาวน์โหลด `pilegal_data_v1.jsonl` (3.92 GB):

📥 **ลิงก์ดาวน์โหลด:** [คลิกที่นี่](https://github.com/beydeveloper/pilegal/releases)

**สำคัญ:** วางไฟล์ในไดเรกทอรีโครงการหลังจากดาวน์โหลด:
```
pilegal/
├── pilegal_data_v1.jsonl    ← วางไฟล์ที่ดาวน์โหลดไว้ที่นี่
├── server.py
├── index.html
└── ...
```

**4. เริ่มเซิร์ฟเวอร์:**
```bash
python server.py
```

**5. เปิดในเบราว์เซอร์:** `http://localhost:5000`

### 📊 การกระจายเนื้อหา
- 💻 **การเขียนโปรแกรม:** ~1.5M บทความ - Python, JavaScript, Java, C++
- 🔐 **ความปลอดภัยทางไซเบอร์:** ~800K บทความ - การวิเคราะห์ช่องโหว่ การทดสอบการเจาะระบบ
- 📊 **วิทยาศาสตร์ข้อมูล:** ~600K บทความ - การเรียนรู้ของเครื่อง AI การวิเคราะห์ข้อมูล
- 🌐 **การพัฒนาเว็บ:** ~500K บทความ - Frontend, Backend, Full-stack
- 🗄️ **ฐานข้อมูล:** ~300K บทความ - SQL, NoSQL, การสร้างแบบจำลองข้อมูล
- 🔧 **อื่นๆ:** ~400K บทความ - เครือข่าย การบริหารระบบ DevOps

**รวมทั้งหมด:** 4,120,756 บทความ | **ขนาด:** 3.92 GB

### 📄 ใบอนุญาต

โครงการนี้ได้รับอนุญาตภายใต้ใบอนุญาต **Creative Commons Zero v1.0 Universal (CC0 1.0)**

**หมายความว่าอย่างไร:**
- ✅ ไม่มีลิขสิทธิ์ - เป็นสาธารณสมบัติโดยสมบูรณ์
- ✅ ใช้งานได้อย่างอิสระ - การใช้งานส่วนบุคคลหรือเชิงพาณิชย์
- ✅ แก้ไขได้อย่างอิสระ - สร้างงานต่อยอด
- ✅ แจกจ่ายได้อย่างอิสระ - แบ่งปันกับใครก็ได้
- ✅ ไม่จำเป็นต้องระบุแหล่งที่มา - แม้ว่าจะชื่นชม!

---

## 🇻🇳 Tiếng Việt

## 📖 Giới Thiệu

**PiLegal** là một bách khoa toàn thư tri thức miễn phí và mã nguồn mở chứa **hơn 4,1 triệu bài viết** về nhiều lĩnh vực khác nhau bao gồm lập trình, an ninh mạng, khoa học dữ liệu, phát triển web và nhiều hơn nữa.

### ✨ Tính Năng

- 🔍 **Công Cụ Tìm Kiếm Mạnh Mẽ** - Tìm kiếm tức thì trong hơn 4,1M+ bài viết
- 📚 **Nội Dung Đa Danh Mục** - Lập trình, bảo mật, khoa học dữ liệu và nhiều hơn nữa
- 🎨 **Giao Diện Hiện Đại** - Thiết kế sạch sẽ, thân thiện với người dùng
- 🚀 **RESTful API Nhanh** - Tích hợp dễ dàng với ứng dụng của bạn
- 🎲 **Khám Phá Bài Viết Ngẫu Nhiên** - Khám phá nội dung ngẫu nhiên
- 📊 **Thống Kê Chi Tiết** - Phân tích dựa trên danh mục
- 🌐 **29 Ngôn Ngữ** - Tài liệu đa ngôn ngữ
- ⚡ **Hiệu Suất Cao** - Thời gian phản hồi tìm kiếm <100ms
- 🔓 **Giấy Phép CC0** - Hoàn toàn miễn phí để sử dụng, sửa đổi và phân phối

### 🚀 Cài Đặt

**Yêu cầu:**
- Python 3.8 trở lên
- pip (trình quản lý gói Python)
- 4 GB+ dung lượng đĩa trống

**Hướng dẫn cài đặt:**

**1. Clone repository:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Cài đặt các dependencies:**
```bash
pip install -r requirements.txt
```

**3. Tải file dữ liệu:**

Tải xuống `pilegal_data_v1.jsonl` (3,92 GB):

📥 **Link tải xuống:** [Nhấp vào đây](https://github.com/beydeveloper/pilegal/releases)

**Quan trọng:** Đặt file vào thư mục dự án sau khi tải xuống:
```
pilegal/
├── pilegal_data_v1.jsonl    ← Đặt file đã tải ở đây
├── server.py
├── index.html
└── ...
```

**4. Khởi động server:**
```bash
python server.py
```

**5. Mở trong trình duyệt:** `http://localhost:5000`

### 📊 Phân Bố Nội Dung
- 💻 **Lập Trình:** ~1,5M bài viết - Python, JavaScript, Java, C++
- 🔐 **An Ninh Mạng:** ~800K bài viết - Phân tích lỗ hổng, kiểm tra thâm nhập
- 📊 **Khoa Học Dữ Liệu:** ~600K bài viết - Machine learning, AI, phân tích dữ liệu
- 🌐 **Phát Triển Web:** ~500K bài viết - Frontend, Backend, Full-stack
- 🗄️ **Cơ Sở Dữ Liệu:** ~300K bài viết - SQL, NoSQL, mô hình hóa dữ liệu
- 🔧 **Khác:** ~400K bài viết - Mạng, quản trị hệ thống, DevOps

**Tổng cộng:** 4.120.756 bài viết | **Kích thước:** 3,92 GB

### 📄 Giấy Phép

Dự án này được cấp phép theo giấy phép **Creative Commons Zero v1.0 Universal (CC0 1.0)**.

**Điều này có nghĩa là gì:**
- ✅ Không có bản quyền - Hoàn toàn thuộc phạm vi công cộng
- ✅ Sử dụng tự do - Sử dụng cá nhân hoặc thương mại
- ✅ Sửa đổi tự do - Tạo các tác phẩm phái sinh
- ✅ Phân phối tự do - Chia sẻ với bất kỳ ai
- ✅ Không yêu cầu ghi công - Mặc dù được đánh giá cao!

---

## 🇮🇷 فارسی

## 📖 درباره پروژه

**PiLegal** یک دانشنامه دانش آزاد و منبع باز است که **بیش از 4.1 میلیون مقاله** در زمینه‌های مختلف از جمله برنامه‌نویسی، امنیت سایبری، علم داده، توسعه وب و موارد دیگر دارد.

### ✨ ویژگی‌ها

- 🔍 **موتور جستجوی قدرتمند** - جستجوی فوری در بیش از 4.1M+ مقاله
- 📚 **محتوای چند دسته‌ای** - برنامه‌نویسی، امنیت، علم داده و بیشتر
- 🎨 **رابط کاربری مدرن** - طراحی تمیز و کاربرپسند
- 🚀 **API RESTful سریع** - یکپارچه‌سازی آسان با برنامه‌های شما
- 🎲 **کشف مقالات تصادفی** - محتوای تصادفی را کاوش کنید
- 📊 **آمار دقیق** - تحلیل بر اساس دسته‌بندی
- 🌐 **29 زبان** - مستندات چند زبانه
- ⚡ **عملکرد بالا** - زمان پاسخ جستجو <100ms
- 🔓 **مجوز CC0** - کاملاً رایگان برای استفاده، تغییر و توزیع

### 🚀 نصب

**الزامات:**
- Python 3.8 یا بالاتر
- pip (مدیر بسته Python)
- 4 GB+ فضای خالی دیسک

**دستورالعمل نصب:**

**1. کلون کردن مخزن:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. نصب وابستگی‌ها:**
```bash
pip install -r requirements.txt
```

**3. دانلود فایل داده:**

دانلود `pilegal_data_v1.jsonl` (3.92 GB):

📥 **لینک دانلود:** [اینجا کلیک کنید](https://github.com/beydeveloper/pilegal/releases)

**مهم:** پس از دانلود، فایل را در دایرکتوری پروژه قرار دهید:
```
pilegal/
├── pilegal_data_v1.jsonl    ← فایل دانلود شده را اینجا قرار دهید
├── server.py
├── index.html
└── ...
```

**4. راه‌اندازی سرور:**
```bash
python server.py
```

**5. در مرورگر باز کنید:** `http://localhost:5000`

### 📊 توزیع محتوا
- 💻 **برنامه‌نویسی:** ~1.5M مقاله - Python, JavaScript, Java, C++
- 🔐 **امنیت سایبری:** ~800K مقاله - تحلیل آسیب‌پذیری، تست نفوذ
- 📊 **علم داده:** ~600K مقاله - یادگیری ماشین، هوش مصنوعی، تحلیل داده
- 🌐 **توسعه وب:** ~500K مقاله - Frontend, Backend, Full-stack
- 🗄️ **پایگاه داده:** ~300K مقاله - SQL, NoSQL, مدل‌سازی داده
- 🔧 **سایر:** ~400K مقاله - شبکه، مدیریت سیستم، DevOps

**مجموع:** 4,120,756 مقاله | **حجم:** 3.92 GB

### 📄 مجوز

این پروژه تحت مجوز **Creative Commons Zero v1.0 Universal (CC0 1.0)** منتشر شده است.

**این به چه معناست:**
- ✅ بدون حق نسخه‌برداری - کاملاً در حوزه عمومی
- ✅ استفاده آزاد - استفاده شخصی یا تجاری
- ✅ تغییر آزاد - ایجاد آثار مشتق
- ✅ توزیع آزاد - به اشتراک‌گذاری با هر کسی
- ✅ نیازی به ذکر منبع نیست - اگرچه قدردانی می‌شود!

---

## 🇵🇰 اردو

## 📖 تعارف

**PiLegal** ایک آزاد اور اوپن سورس علمی دائرۃ المعارف ہے جس میں پروگرامنگ، سائبر سیکیورٹی، ڈیٹا سائنس، ویب ڈویلپمنٹ اور بہت کچھ سمیت مختلف شعبوں میں **4.1 ملین سے زیادہ مضامین** ہیں۔ استعمال میں آسانی کے لیے وکی پیڈیا طرز کے انٹرفیس کے ساتھ ڈیزائن کیا گیا ہے۔

### ✨ خصوصیات

- 🔍 **طاقتور تلاش کا انجن** - 4.1M+ مضامین میں فوری تلاش
- 📚 **کثیر زمرہ مواد** - پروگرامنگ، سیکیورٹی، ڈیٹا سائنس اور مزید
- 🎨 **جدید انٹرفیس** - صاف، صارف دوست ڈیزائن
- 🚀 **تیز RESTful API** - آپ کی ایپلیکیشنز کے ساتھ آسان انضمام
- 🎲 **بے ترتیب مضامین کی دریافت** - بے ترتیب مواد دریافت کریں
- 📊 **تفصیلی اعدادوشمار** - زمرہ پر مبنی تجزیات
- 🌐 **29 زبانیں** - کثیر لسانی دستاویزات
- ⚡ **اعلیٰ کارکردگی** - تلاش کے جواب کا وقت <100ms
- 🔓 **CC0 لائسنس** - استعمال، تبدیلی اور تقسیم کے لیے مکمل طور پر مفت

### 🚀 تنصیب

**تقاضے:**
- Python 3.8 یا اس سے اوپر
- pip (Python پیکیج مینیجر)
- 4 GB+ خالی ڈسک کی جگہ

**تنصیب کی ہدایات:**

**1. Repository کلون کریں:**
```bash
git clone https://github.com/beydeveloper/pilegal.git
cd pilegal
```

**2. Dependencies انسٹال کریں:**
```bash
pip install -r requirements.txt
```

**3. ڈیٹا فائل ڈاؤن لوڈ کریں:**

`pilegal_data_v1.jsonl` (3.92 GB) ڈاؤن لوڈ کریں:

📥 **ڈاؤن لوڈ لنک:** [یہاں کلک کریں](https://github.com/beydeveloper/pilegal/releases)

**اہم:** ڈاؤن لوڈ کرنے کے بعد فائل کو پروجیکٹ ڈائریکٹری میں رکھیں:
```
pilegal/
├── pilegal_data_v1.jsonl    ← ڈاؤن لوڈ شدہ فائل یہاں رکھیں
├── server.py
├── index.html
└── ...
```

**4. سرور شروع کریں:**
```bash
python server.py
```

**5. براؤزر میں کھولیں:** `http://localhost:5000`

### 📊 مواد کی تقسیم
- 💻 **پروگرامنگ:** ~1.5M مضامین - Python, JavaScript, Java, C++
- 🔐 **سائبر سیکیورٹی:** ~800K مضامین - کمزوری کا تجزیہ، دخول کی جانچ
- 📊 **ڈیٹا سائنس:** ~600K مضامین - مشین لرننگ، AI، ڈیٹا تجزیہ
- 🌐 **ویب ڈویلپمنٹ:** ~500K مضامین - Frontend, Backend, Full-stack
- 🗄️ **ڈیٹا بیس:** ~300K مضامین - SQL, NoSQL، ڈیٹا ماڈلنگ
- 🔧 **دیگر:** ~400K مضامین - نیٹ ورک، سسٹم ایڈمنسٹریشن، DevOps

**کل:** 4,120,756 مضامین | **سائز:** 3.92 GB

### 📄 لائسنس

یہ پروجیکٹ **Creative Commons Zero v1.0 Universal (CC0 1.0)** لائسنس کے تحت لائسنس یافتہ ہے۔

**اس کا کیا مطلب ہے:**
- ✅ کوئی کاپی رائٹ نہیں - مکمل طور پر عوامی ڈومین
- ✅ آزادانہ استعمال - ذاتی یا تجارتی استعمال
- ✅ آزادانہ ترمیم - مشتق کام بنائیں
- ✅ آزادانہ تقسیم - کسی کے ساتھ بھی شیئر کریں
- ✅ حوالہ کی ضرورت نہیں - اگرچہ قدردانی کی جاتی ہے!

---

[⬆️ Back to top](#-pilegal)



