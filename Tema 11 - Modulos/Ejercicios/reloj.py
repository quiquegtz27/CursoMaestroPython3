# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 20:33:19 2021

@author: ENRIQUE
"""

import datetime
import time
import os

while True:
    os.system("cls")
    dt = datetime.datetime.now()
    print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
    time.sleep(1)
    