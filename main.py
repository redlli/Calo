#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 00:06:04 2023

@author: deku
"""

from lib import artwork
from lib import printcolors as pc
#from Tools import Campero as t
import manu as m
from Tools import History as h
#import argparse

def start():
    pc.out(artwork.a,pc.GREEN)
    pc.out(artwork.b,pc.MAGENTA)
    pc.out(artwork.c,pc.MAGENTA)
    pc.out(artwork.a,pc.GREEN)
    pc.out(artwork.e,pc.RED)
    
def linc(*argv):
    with open("Readme.txt","r") as file:
        li=file.read()
    pc.out(li,pc.CYAN)
    pc.out("\nPress Enter to go back: ",pc.MAGENTA)
    argv=input()
    if argv=="":
        main()
    else:
       pc.exit()
        
        
        
def hepl():
    with open ("Help.txt",'r')as file:
        li=file.read()
    pc.out(li,pc.CYAN)
    
    pc.out("\nPress Enter to go back: ",pc.MAGENTA)
    argv=input()
    if argv=="":
        main()
    else:
        pc.exit()
               
#=========================================================================
#Mai Function start here

def main(*argv):
    start()
    pc.newl()
    # h=int(input("Enter Option: "))
    pc.out("Enter Option: ",pc.MAGENTA)
    argv=input()
    match argv:
        case "1":
            m.maino()
            main()
        case "2": 
            h.history()
            main()
        case "3":
            pc.out("GUI",pc.CYAN)
            main()
        case "4":
            
            hepl()
        case "5":
            linc()
            main()
            
        case "":
            # pc.out("Exiting\nHave a great day....\n",pc.CYAN)
            # pc.out(artwork.a,pc.GREEN)
            pc.exit()
        
    
        case _:
            
            pc.out("wrong Option\n",pc.CYAN)
            main()
            






main()