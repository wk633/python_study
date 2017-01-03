import time, threading

def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 1:
        n += 1
        print 'thread %s >> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s end' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name="customizedThread")
t.start()
t.join()
print 'thread %s end' % threading.current_thread().name
