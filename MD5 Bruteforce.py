import hashlib
import os 
import sys
import datetime
startTime=datetime.datetime
def error(msg)  : print("[!]"+msg)
def errorExit(msg) : raise SystemExit("[!]"+msg)
def md5(string) : return hashlib.md5(string).hexdigest()

def xpermutation(characters,size):
    if size ==0:
        yield []
    else:
        for x in range(len(characters)):
            for y in xpermutation(characters[:x]+characters[x:],size-1):
                yield[characters[x]]+y

def bruteforce(hash):
    attempt=0
    charcters=list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    maxlength=range(0,25)
    stringbuilder=""
    for length in maxlength:
        for x in xpermutation(charcters,length):
            permutation=stringbuilder+" ".join(x)
            attempt=attempt+1
            if md5(permutation)==hash:
                end_time=str(datetime.datetime.now()-startTime).split(".")[0]
                print("["+str(attempt)+"]"+permutation+"CRACKED"+end_time)
                input("\n press <ENTER> to exit")
                sys.exit()
            else:
                print("["+str(attempt)+"]"+permutation)
    errorExit("md5 crack failed") 
if os.name=="nt"    : os.system('cls')
else    : os.system('clear')
if sys.version_info.major !=2 or sys.version_info.minor !=2:
    errorExit("needs version 2.7 of python")
if len(sys.argv)==2:
    if len(sys.argv[1])==32 and sys.argv[1].isalnum():
        bruteforce(sys.argv[1])
    else:
        error("invalid md5 hash")
        errorExit("usage: python MD5 Bruteforce.py")
else:
    error("neccessary arugements not found")
    errorExit("usage:python  MD5 Bruteforce.py")

