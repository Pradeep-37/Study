# Multithreading enables multiple tasks to run simultanuosly. The ability of a processor to execute multiple threads is known as multithreading
import threading

def even():
    for i in range(0,20,2):
        print("even no:", i)
        
def odd():
    for i in range(1,20,2):
        print("odd no:", i)
        
t1 = threading.Thread(target=even)
t2 = threading.Thread(target=odd)

t1.start()                    # Start the threads
t2.start()

t1.join()                     # Wait for both threads to complete
t2.join()


"""
When to Use Multithreading
*I/O-bound tasks (e.g., reading/writing files, network requests).
*Not suitable for CPU-bound tasks because Python's Global Interpreter Lock (GIL) prevents 
true parallel execution of threads for CPU-intensive operations.  
    
"""