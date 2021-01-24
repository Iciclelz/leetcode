class Foo {
public:
    Foo() {
        N = 0;
    }

    void first(function<void()> printFirst) {
        
        std::unique_lock<std::mutex> lock(m);

        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        
        N += 1;

        cv.notify_all();
    }

    void second(function<void()> printSecond) {
        
        std::unique_lock<std::mutex> lock(m);
        while (N < 1) 
        {
            cv.wait(lock);
        }
        
        
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        
        N += 1;
        
        cv.notify_all();
    }

    void third(function<void()> printThird) {
        
        std::unique_lock<std::mutex> lock(m);
        while (N < 2) 
        {
            cv.wait(lock);
        }
        
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
private:
    std::mutex m;
    std::condition_variable cv;
    size_t N;
};