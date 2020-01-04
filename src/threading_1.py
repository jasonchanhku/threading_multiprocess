#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:24:11 2020

@author: jasonchan
"""
import time

start = time.perf_counter()

def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done sleeping...")
    
do_something()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds(s)")



