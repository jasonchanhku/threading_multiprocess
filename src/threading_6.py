#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 18:05:35 2020

Map method to run functions over list of values

@author: jasonchan
"""

import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...\n")
    time.sleep(seconds)
    return f"Done sleeping...{seconds}"

# best to use with a context manager, can handle its own exit on its own
with concurrent.futures.ThreadPoolExecutor() as executor:
    # submit method schedules a function to be executed and returns a future object
    # can also run submit multiple times if needed using a loop / list comprehension
    secs = [5,4,3,2,1]
    # maps runs do something with every value of secs. Map returns results instead of future objects
    # returns in order of started
    results = executor.map(do_something, secs)
    
    for result in results:
        print(result)

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds(s)")