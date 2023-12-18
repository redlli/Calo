#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:44:06 2023

@author: deku
"""


from lib import printcolors as pc


def history():
    with open ("History.txt",'r')as file:
        li=file.read()
    pc.out(li,pc.CYAN)
    pc.out("\nPress Enter to go back: ",pc.MAGENTA)