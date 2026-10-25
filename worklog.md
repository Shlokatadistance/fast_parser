#### 25th October
I tried something super trivial today for a test, i.e. passing a file with 10K lines and implementing threads for running some calculations on those lines. Given the simplicity of the operation the threads suffer from thread overhead. All the tests are on the free-threaded ( GIL disabled ) version of python 3.14.
