#### 25th October
I tried something super trivial today for a test, i.e. passing a file with 10K lines and implementing threads for running some calculations on those lines. Given the simplicity of the operation the threads suffer from thread overhead. All the tests are on the free-threaded ( GIL disabled ) version of python 3.14.

Ofcourse, along the tangent of threads, i now wanted to see "why" is there even the thread, i.e. how does it manifest itself on a system. I also want to see how does it compare against more established threading models as those on c/c++.
