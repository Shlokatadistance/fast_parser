#include <chrono>
#include <iostream>
#include <thread>

int main(){
    const int n = 500;
    auto start = std::chrono::steady_clock::now();

    for (int i = 0; i < n; ++i){
        std::thread t([] {});
        t.join();
    }

    auto elapsed = std::chrono::steady_clock::now() - start;
    std::cout << std::chrono::duration<double>(elapsed).count() / n << "seconds per start/join \n" << std::endl;
    return 0;
}
