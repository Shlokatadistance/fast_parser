import threading
import statistics
import time
from timeit import repeat

def no_op():
    pass

def benchmark():
    repeats = 7
    n = 500
    samples = []
    for _ in range(repeats):
        start = time.perf_counter()
        for _ in range(n):
            thread = threading.Thread(target=no_op)
            thread.start()
            thread.join()
        samples.append(time.perf_counter()-start)

    median_val = statistics.median(samples)
    print(f"Median value is {median_val:.4f}s; {median_val/n * 1e6:.1f} micro seconds per thread")

if __name__ == "__main__":
    benchmark()
