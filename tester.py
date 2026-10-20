import threading
import time

def calculation(n:int):
    total = 0
    for i in range(n):
        total += i*i

def main():
    start = time.perf_counter()
    iterations = 20_000_000
    threads = []
    for _ in range(4):
        thread = threading.Thread(target=calculation,args=(iterations,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    end = time.perf_counter()
    print(f"Execution completed in {end-start:.6f} seconds")

if __name__ == "__main__":
    main()
