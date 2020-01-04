#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:34:25 2020

Older way to do threading to understand. Using the threading module

@author: jasonchan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 17:24:11 2020

@author: jasonchan
"""

import threading
import time

start = time.perf_counter()

def do_something():
    print("Sleeping 1 second...\n")
    time.sleep(1)
    print("Done sleeping...\n")
    
t1 = threading.Thread(target=do_something)
t2 =  threading.Thread(target=do_something)

# join helps finish before printing finish time

t1.start()
t2.start()

t1.join()
t2.join()


finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds(s)")



