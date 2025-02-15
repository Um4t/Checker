import os
import base64
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

KEY = 7  # XOR işlemi için anahtar

# Şifreleme fonksiyonu
def ninja_encode(file_path):
    """Dosyayı şifreleyerek ENCODEUM4T_<orijinal_dosya_adı> olarak kaydeder."""
    output_file = f"ENCODEUM4T_{os.path.basename(file_path)}.py"  # .py olarak kaydedilecek

    with open(file_path, "rb") as f:
        data = f.read()

    # XOR işlemi uygula ve Base64 ile encode et
    encoded_data = base64.b64encode(bytes([b ^ KEY for b in data])).decode()

    # Şifrelenmiş içeriği yeni bir .py dosyası olarak kaydet
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"import base64\nKEY={KEY}\n")
        f.write("exec(bytes([b ^ KEY for b in base64.b64decode('''" + encoded_data + "''')]))")

    return output_file

# /start komutu
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        'Merhaba! Şifreleme işlemi yapmak için dosyanızı gönderin. Dosyanız şifrelendikten sonra size geri gönderilecektir.'
    )

# Dosya gönderildiğinde şifreleme işlemi yapılacak
async def handle_file(update: Update, context: CallbackContext) -> None:
    # Kullanıcının gönderdiği dosyayı al
    file = update.message.document

    if file is None:
        await update.message.reply_text("Hata: Lütfen geçerli bir dosya gönderin!")
        return

    file_id = file.file_id
    file_name = file.file_name

    try:
        # Dosyanın Telegram'dan indirilecek dosyasını al
        new_file = await context.bot.get_file(file_id)

        # Dosyayı indir
        file_path = f"./{file_name}"
        await new_file.download_to_drive(file_path)  # Dosyayı doğru şekilde indiriyoruz
        await update.message.reply_text(f"Dosya alındı: {file_name}\nŞifreleme işlemi başlatılıyor...")

        # Dosyayı şifrele
        encrypted_file = ninja_encode(file_path)

        # Şifreli dosyayı geri gönder
        with open(encrypted_file, "rb") as f:
            await update.message.reply_document(f, filename=os.path.basename(encrypted_file))
    except Exception as e:
        await update.message.reply_text(f"Bir hata oluştu: {str(e)}")

# Mesajları dinleme ve yönlendirme
def main() -> None:
    # Telegram Bot API token'ını terminal üzerinden al
    TOKEN = input("Telegram Bot API Token'ınızı girin: ")

    # Application oluşturuluyor
    application = Application.builder().token(TOKEN).build()

    # Komutlar
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_file))  # Tüm dosyalar

    # Botu başlat
    application.run_polling()
    print("BOT ÇALIŞIYOR")  # Bot çalıştığını terminalde bildirecek

if __name__ == '__main__':
    main()