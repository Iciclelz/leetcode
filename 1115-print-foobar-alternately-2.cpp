class FooBar {
private:
    int n;
    std::mutex m;
    std::condition_variable cv;
    bool is_foo;

public:
    FooBar(int n) {
        this->n = n;
        this->is_foo = true;
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            
            std::unique_lock<std::mutex> lock(m);
            cv.wait(lock, [this]{ return this->is_foo; });
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
    
            is_foo = false;
            cv.notify_all();
        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            
            std::unique_lock<std::mutex> lock(m);
            cv.wait(lock, [this]{ return !this->is_foo; });

        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            
            is_foo = true;
            cv.notify_all();
        }
    }
};