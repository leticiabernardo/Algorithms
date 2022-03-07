#!/usr/bin/env python3
from hash_table import HashTable
from hash_table_with_collision import HashTable as HashTableCollision


def main():
    print("Simple Hash Table")
    t = HashTable()
    t['test 1'] = 120
    t['test 2'] = 130
    print(t['test 2'])
    del(t['test 1'])
    print(t.arr)

    print("*" * 50)
    print("Hash Table with Collision")
    tc = HashTableCollision()
    tc["march 6"] = 120
    tc["march 6"] = 17
    tc['march 179'] = 1
    tc['march 278'] = 2
    print(tc.arr)

if __name__ == "__main__":
    main()
