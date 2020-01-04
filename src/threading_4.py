#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:46:39 2020

Passing arguments of function

@author: jasonchan
"""

import threading
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...\n")
    time.sleep(seconds)
    print("Done sleeping...\n")
    
threads = []
    
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    # cant join in for loop it would join on thread before looping through
    threads.append(t)
    
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds(s)")

# If sequentially, it would take 10 seconds bu this only takes 1 second
