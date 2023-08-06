# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 19:25:54 2022

@author: franc
"""




import subprocess
import os

basis = """

import asyncio
from kasa import SmartPlug

dev = SmartPlug("abcde")

asyncio.run(dev.update())

a = True
while(a):
    try:
        asyncio.run(dev.turn_option())
        a = False
    except:
        0

"""


class SmartPlug:

    
    def __init__(self,ip_address):
        self.basis = basis.replace("abcde",ip_address)
        self.status = False
        self.change_status()

        
    def change_status(self):
        
        if(self.status):
            option = "on"
        else:
            option = "off"

        basis2 = self.basis.replace("option",option)
        file = open("tplink.py","w")
        file.write(basis2)
        file.close()

        p = subprocess.call(f"python tplink.py",shell=False)
        os.remove("tplink.py")


    def __call__(self,s):
        
        s = s == 1
        if( s & (self.status == False) ):
            self.status = True
            self.change_status()
        elif( (s == False) & self.status ):
            self.status = False
            self.change_status()
