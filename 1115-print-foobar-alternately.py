class FooBar:
    def __init__(self, n):
        self.n = n
        self.cv = threading.Condition()
        self.is_foo = True

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            with self.cv:
                
                self.cv.wait_for(lambda : self.is_foo)
                
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                
                self.is_foo = False
                self.cv.notify()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            with self.cv:
                self.cv.wait_for(lambda : not self.is_foo)
                
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                
                self.is_foo = True
                self.cv.notify()