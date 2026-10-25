# Fast byte parser in python
# Idea is to leverage free threading to implement a fast byte sniffer, sort of the basis of many
# text parsing libraries in python

import time
import threading
import queue

master_q = queue.Queue()

def calculate_sum(lines:list[str]):
    """
    In this particular example, the file lines have 3 fields, purchase_price, sell_price, net_fee
    the formula is simple net = sell-(purchase+fee)
    """
    net_val = 0
    for line in lines:
        fields = line.strip().split(",")
        net_val += int(fields[1])-(int(fields[0])+int(fields[2]))
    master_q.put(net_val)


def stream_bytes(file_path:str):
    start = time.perf_counter()
    threads = []

    with open(file_path,"r+") as f:
        count = 0
        processor = []
        for line in f:
            if count == 100:
                batch = processor
                target = threading.Thread(target=calculate_sum,args=(batch,))
                threads.append(target)
                target.start()
                count = 0
                processor = []
            count += 1
            processor.append(line)
        if processor:
            target = threading.Thread(target=calculate_sum,args=(processor,))
            threads.append(target)
            target.start()
    for thread in threads:
        thread.join()
    print(f"Net execution time is {time.perf_counter()-start:.6f}")
def not_threaded(file_path:str):
    start = time.perf_counter()
    with open(file_path,"r") as f:

        count = 0
        processor = []
        for line in f:
            if count == 100:
                calculate_sum(processor)
                count = 0
                processor[:] = []
            count += 1
            processor.append(line)

    print(f"Net execution time is {time.perf_counter()-start:.6f}")



        # f.read() loads in memory directly
        # we're going to try a basic implementation of splitting the load across 4 threads.

if __name__ == "__main__":
    #stream_bytes("/opt/freep/prices.csv")
    not_threaded("/opt/freep/prices.csv")
    print(master_q.queue)
