# -*- coding: utf-8 -*-
from lib import printcolors as pc
import datetime

def calo(base):
    # pc.out("Enter Number: ",pc.CYAN)
    #a=int(input())
    # base=int()
    
    op=input("Enter Opration")
    if op=="-":
        while base!="":
            
            new=int(input())
            base=base-new
            print(base)
            save=str(base)
            save2=str(new)
            xo=save+op+save2+"\n"
            with open('History.txt', 'a') as f:
                f.write(xo)
            calo(base)
    elif op=="+":
        while base!="":
            
            new=int(input())
            base=base+new
            print(base)
            save=str(base)
            save2=str(new)
            xo=save+op+save2+"\n"
            with open('History.txt', 'a') as f:
                f.write(xo)
            calo(base)
    elif op=="*":
        while base!="":
            # sys.stdout = open('History.txt','wt')
            new=int(input())
            base=base*new
            print(base)
            save=str(base)
            save2=str(new)
            xo=save+op+save2+"\n"
            with open('History.txt', 'a') as f:
                f.write(xo)
            calo(base)
    elif op=="/":
        while base!="":
            # sys.stdout = open('History.txt','wt')
            new=int(input())
            base=base/new
            print(base)
            save=str(base)
            save2=str(new)
            xo=save+op+save2+"\n"
            with open('History.txt', 'a') as f:
                f.write(xo)
            calo(base)
    
    elif op=="":
        print("Going back to main manue........")
        return 0
    else:
        print("Wrong poration")
        calo(base)

        
def start():
    date=str(datetime.datetime.now())
    h=date+"\n-----------------------------------------------------\n"
    with open('History.txt', 'a') as f:
        f.write(h)
    pc.out("Enter Base Value: ",pc.CYAN)       
    base=int(input()) 
    calo(base)