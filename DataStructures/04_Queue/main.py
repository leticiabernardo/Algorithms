#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from queue import Queue


def main():
    q = Queue()
    print(q.isEmpty())
    q.enqueue('1')
    q.enqueue('2')
    q.enqueue('3')
    q.dequeue()
    print(q.peek())
    print(q.isEmpty())
    
if __name__ == "__main__":
    main()
