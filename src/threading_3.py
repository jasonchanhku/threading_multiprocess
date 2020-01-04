#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:42:34 2020

Creating many threads in a loop

@author: jasonchan
"""

import threading
import time

start = time.perf_counter()

def do_something():
    print("Sleeping 1 second...\n")
    time.sleep(1)
    print("Done sleeping...\n")
    
threads = []
    
for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    # cant join in for loop it would join on thread before looping through
    threads.append(t)
    
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds(s)")

# If sequentially, it would take 10 seconds bu this only takes 1 second
