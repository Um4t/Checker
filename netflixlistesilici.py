import os

# Silinecek dosyanın yolu
dosya_yolu = "/sdcard/um4tnetflixhits.txt"  # Dosyanın tam yolunu yazabilirsin: örn. "C:/Users/Kullanici/Desktop/sil.txt"

def dosya_sil():
    if os.path.exists(dosya_yolu):
        os.remove(dosya_yolu)
        print(f"✅ {dosya_yolu} başarıyla silindi.")
    else:
        print("❌ Dosya bulunamadı!")

# Çalıştır
dosya_sil()
