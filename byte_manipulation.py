"""
For a parser to be fast, i think it needs
1. Natively work in bytes ( smaller footprint )
2. Have the ability to jump to different parts really easily.
3. decode encode in different type ( it may be easier to work with different parts of the data)

"""

import mmap

def byte_array():
    a = bytearray(b"Long sequence of text 1")
    print(a)


def memory_map():
    """
    using the native memory_map first and then perhaps will
    experiment with the numpy based map
    """
    with open(f"/opt/freep/prices.csv","rb") as f:
        # file descriptors allow the kernel to track an open file or a kernel
        # think everything in a linux is a file ( of course more nuance required here )
        map_m = mmap.mmap(f.fileno(),0)
        print(map_m)

if __name__ == "__main__":
    memory_map()
