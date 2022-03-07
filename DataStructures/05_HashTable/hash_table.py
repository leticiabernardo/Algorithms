#!/usr/bin/env python3


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash_key = 0
        for char in key:
            hash_key += ord(char)
        return hash_key % 10

    def __setitem__(self, key, val):
        hash_key = self.get_hash(key)
        self.arr[hash_key] = val

    def __getitem__(self, key):
        hash_key = self.get_hash(key)
        return self.arr[hash_key]

    def __delitem__(self, key):
        hash_key = self.get_hash(key)
        self.arr[hash_key] = None
