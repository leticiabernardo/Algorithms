#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Queue:
    def __init__(self):
        self.queue = []
      
    def enqueue(self, data):
        self.queue.append(data)
      
    def dequeue(self):
        if len(self.queue) < 1:
            raise Exception("empty queue")
        self.queue.pop(0)
  
    def peek(self):
        print(self.queue[0])

    def isEmpty(self):
        return len(self.queue) == 0
