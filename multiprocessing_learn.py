"""
The multiprocessing module in Python is used to create multiple processes that can run in parallel. 
Unlike threads, each process has its own memory space and operates independently, allowing true parallelism on multi-core systems.
Each process runs independently with its own memory space.

Why Use multiprocessing?
To bypass the Global Interpreter Lock (GIL) and achieve true parallelism.
For CPU-intensive tasks like mathematical computations, image processing, or machine learning model training..  
"""
from multiprocessing import Process

def compute_square(num):
    print(f"Square of {num} is {num * num}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    processes = []

    # Create and start multiple processes
    for num in numbers:
        process = Process(target=compute_square, args=(num,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print("All processes completed!")


# Always wrap your multiprocessing code in a if __name__ == "__main__": block 
# to avoid issues when spawning processes, especially on Windows.