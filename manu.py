#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:12:49 2023

@author: deku
"""

from lib import printcolors as pc
from lib import artwork


from Tools import Campero as c
from Tools import History as h
from Tools import Trip as t
from Tools import Simpalo as s




def maino(*argv):
    pc.out(artwork.a,pc.GREEN)
    pc.out(artwork.b,pc.MAGENTA)
    pc.out(artwork.c,pc.MAGENTA)
    pc.out(artwork.a,pc.GREEN)
    pc.out(artwork.f,pc.RED)
    pc.out("Enter Option: ",pc.MAGENTA)
    argv=input()
    match argv:
        case "1":
            c.calo()
            maino()
        case "2": 
            s.start()
            maino()
            # print("Simplao")
            #history()
        case "3":
            t.calo()
            maino()
        case "4":
            h.history()
            maino()
        case "5":
            print("working..........")
            maino()
            #linc()
            
        case "":
            pc.out("Going back to main Manue\n",pc.CYAN)
            pc.out(artwork.a,pc.GREEN)
            
        
    
        case _:
            maino()
            pc.out("wrong Option",pc.CYAN)
    


