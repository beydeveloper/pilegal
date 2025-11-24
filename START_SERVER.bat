@echo off
chcp 65001 >nul 2>&1
cls
echo ╔════════════════════════════════════════════════╗
echo ║          🔍 PiLegal - Bilgi Ansiklopedisi     ║
echo ║              by beydeveloper                   ║
echo ╚════════════════════════════════════════════════╝
echo.

REM Python kurulu mu kontrol et
python --version >nul 2>&1
if errorlevel 1 (
    echo [❌] Python bulunamadı! Lütfen Python yükleyin.
    echo https://www.python.org/downloads/
    pause
    exit /b
)

echo [✓] Python bulundu
echo [⏳] Gerekli kütüphaneler kontrol ediliyor...
pip install -q flask flask-cors


echo [✓] Kütüphaneler hazır
echo [⏳] Sunucu başlatılıyor...
echo.
echo ╔════════════════════════════════════════════════╗
echo ║  ✅ Sunucu Hazır!                             ║
echo ║  🌐 URL: http://localhost:5000                ║
echo ║  📊 4.1M+ makale yükleniyor...                ║
echo ║  ⏸️  Durdurmak için: Ctrl+C                   ║
echo ╚════════════════════════════════════════════════╝
echo.

python server.py

pause
