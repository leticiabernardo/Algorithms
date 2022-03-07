#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from stack import Stack


def main():
    s = Stack()
    print(s.isEmpty())
    s.push('1')
    s.push('2')
    s.push('3')
    s.pop()
    print(s.get())
    print(s.isEmpty())
    
if __name__ == "__main__":
    main()
