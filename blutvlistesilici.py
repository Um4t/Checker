import os

dosya_yolu = "/sdcard/um4tblutvhits.txt"

if os.path.exists(dosya_yolu):
    try:
        os.remove(dosya_yolu)
        print(f"✅ {dosya_yolu} başarıyla silindi.")
    except PermissionError:
        print("❌ İzin hatası! Dosyayı silmek için izin gerekli.")
    except Exception as e:
        print(f"❌ Hata: {e}")
else:
    print("❌ Dosya bulunamadı!")
