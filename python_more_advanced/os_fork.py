#!/usr/bin/env python
#coding=utf8

import os
from time import sleep

#创建子进程之前声明的变量
source = 10

try:
    pid = os.fork()

    if pid == 0: #子进程
        print "this is child process, pid is %s" % os.getpid()
        print 'in child process, use os.getppid() to get father process pid: %s' % os.getppid()
        #在子进程中source自减1
        source = source - 1
        sleep(5)
    else: #父进程
        print "this is parent process, child process's pid is %s" % pid
        print 'use os.getpid() to get current process pid, %s' % os.getpid()
    print source
except OSError, e:
    pass
