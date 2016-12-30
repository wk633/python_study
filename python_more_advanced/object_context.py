# -*- coding: utf-8 -*-
from telnetlib import Telnet
from sys import stdin, stdout
from collections import deque

class TelnetClient(object):
    def __init__(self, addr, port=23):
        self.addr = addr
        self.port = port
        self.tn = None
    def start(self):
        # user
        t = self.tn.read_until('login: ')
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)

        # password
        t = self.tn.read_until('password: ')
        if t.startswith(user[:-1]):
            t = t[len(uesr) + 1]
        stdout.write(t)
        self.tn.write(stdin.readline())

        t = self.tn.read_until('$ ')
        stdout.write(t)
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput)
            t = self.tn.read_until('$ ')
            stdout.write(t[len(uinput)+1:])

    # def cleanup(self):
    #     self.tn.close()
    #     self.tn = None
    #     with open(self.addr + '_history.txt', 'w') as f:
    #         f.writelines(self.history)

    def __enter__(self):
        self.tn = Telnet(self.addr, self.port)
        self.history = deque()
    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type  错误类型
        # exc_val   错误值
        # exc_tb    错误栈
        self.tn.close()
        self.tn = None
        with open(self.addr + '_history.txt', 'w') as f:
            f.writelines(self.history)

with TelnetClient('127.0.0.1') as client:
    client.start()

# client = TelnetClient('127.0.0.1')
# print '\n start...'
# client.start()
# print '\ncleanup...'
