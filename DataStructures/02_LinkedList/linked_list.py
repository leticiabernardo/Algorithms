#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
      
class LinkedList:
    def __init__(self):
        self.head = None
      
    def insert_at_begining(self, data):
        self.head = Node(data, self.head)
      
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
      
        itr = self.head
        while itr.next:
            itr = itr.next
      
        itr.next = Node(data, None)
      
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_len(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
          
        return count
  
    def remove_at(self, idx):
        if idx < 0 or self.get_len() == 0:
            raise Exception("there are no items in the list")
        if idx > self.get_len() -1:
            raise Exception("the index does not exist")
 
        if idx == 0:
            self.head = self.head.next
            return
 
        itr = self.head
        count = 0
        while itr:
            if count == idx - 1:
                if itr.next is not None:
                    itr.next = itr.next.next
                itr = None
                break
          
            count += 1
            itr = itr.next
          
    def insert_at(self, idx, data):
        if idx == 0:
            self.insert_at_begining(data)
            return
      
        count = 0
        itr = self.head
        while itr:
            if count == idx-1:
                node = Node(data, itr.next)
                itr.next = node
                break
              
            itr = itr.next
            count += 1

    def print_list(self):
        if self.head is None:
            print("Empty list")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
          
        print(llstr)
        
    def search(self, data):
        itr = self.head
        while itr:
            if (itr.data == data):
                return itr.data
          
            itr = itr.next
          
        raise Exception("not found")
