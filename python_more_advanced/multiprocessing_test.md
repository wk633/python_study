从multiprocessing里引入Process类，可以实现跨平台


理解join的作用
> Using the term join to mean "wait for a thread to complete" is common across many programming languages, so Python just adopted it as well.

http://www.cnblogs.com/lipijin/p/3709903.html

自己的理解join就是用来阻塞住主进程，被join的进程搞定了再往下走。
