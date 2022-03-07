#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Stack:
    def __init__(self):
        self.stack = []
      
    def push(self, data):
        if data not in self.stack:
            self.stack.insert(0, data)
          
    def pop(self):
        if len(self.stack) < 0:
            raise Exception("Empty stack")
          
        return self.stack.pop(0)
  
    def get(self):
        return self.stack[0]
  
    def isEmpty(self):
        return len(self.stack) <= 0
