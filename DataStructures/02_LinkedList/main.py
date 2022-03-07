#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from linked_list import LinkedList


def main():
    ll = LinkedList()
    ll.insert_values(["madrid", "viena", "las vegas", "los angeles"])
    ll.insert_at(0, "miami")
    ll.print_list()

if __name__ == "__main__":
    main()
