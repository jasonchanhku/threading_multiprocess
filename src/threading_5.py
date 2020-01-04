#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:49:20 2020

Using Thread pool executor

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
    results = [executor.submit(do_something, sec) for sec in secs]
    #results = [executor.submit(do_something, 1) for _ in range(10)]
    # to get the results as they are completed, use as.completed method
    # prints order as they complete
    
    # need to use map method to runs this 
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    
    
#==============================================================================
#     f1 = executor.submit(do_something, 1)
#     f2 = executor.submit(do_something, 1)
#     print(f1.result())
#     print(f2.result())
#==============================================================================
    
#==============================================================================
# threads = []
#     
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     # cant join in for loop it would join on thread before looping through
#     threads.append(t)
#     
# for thread in threads:
#     thread.join()
# 
#==============================================================================
finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds(s)")

# If sequentially, it would take 10 seconds bu this only takes 1 second