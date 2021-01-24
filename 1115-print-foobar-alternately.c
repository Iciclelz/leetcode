typedef struct {
    int n;
    pthread_mutex_t mutex;
    pthread_cond_t cv;
    int is_foo;
} FooBar;

FooBar* fooBarCreate(int n) {
    FooBar* obj = (FooBar*) malloc(sizeof(FooBar));
    obj->n = n;
    pthread_mutex_init(&obj->mutex, 0);
    pthread_cond_init(&obj->cv, 0);
    obj->is_foo = 1;
    return obj;
}

void foo(FooBar* obj) {
    
    for (int i = 0; i < obj->n; i++) {
        pthread_mutex_lock(&obj->mutex);
        while (!obj->is_foo)
        {
            pthread_cond_wait(&obj->cv, &obj->mutex);
        }
        // printFoo() outputs "foo". Do not change or remove this line.
        printFoo();
        
        obj->is_foo = 0;
        pthread_cond_signal(&obj->cv);
        pthread_mutex_unlock(&obj->mutex);
    }
}

void bar(FooBar* obj) {
    
    for (int i = 0; i < obj->n; i++) {
        pthread_mutex_lock(&obj->mutex);
        while (obj->is_foo)
        {
            pthread_cond_wait(&obj->cv, &obj->mutex);
        }
        // printBar() outputs "bar". Do not change or remove this line.
        printBar();
        
        obj->is_foo = 1;
        pthread_cond_signal(&obj->cv);
        pthread_mutex_unlock(&obj->mutex);
    }
}

void fooBarFree(FooBar* obj) {
    pthread_mutex_lock(&obj->mutex);
    pthread_cond_destroy(&obj->cv);
    pthread_mutex_unlock(&obj->mutex);
    
    pthread_mutex_destroy(&obj->mutex);
    free(obj);
}