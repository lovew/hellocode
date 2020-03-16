# myfun.py

__all__ = ["myhello1"]

def myhello1(x):
    myhello2(x)

def myhello2(b):
    unsafe(b)

def unsafe(a):
    print(a)
