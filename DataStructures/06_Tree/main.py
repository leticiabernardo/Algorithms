#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tree import TreeNode


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Asus"))
    laptop.add_child(TreeNode("Positivo"))

    smartphone = TreeNode("Smartphones")
    smartphone.add_child(TreeNode("iPhone"))
    smartphone.add_child(TreeNode("Samsung"))
    smartphone.add_child(TreeNode("Motorola"))

    root.add_child(laptop)
    root.add_child(smartphone)

    print(smartphone.get_level())

    return root
   

def main():
    root = build_product_tree()
    root.print_tree()
    
if __name__ == "__main__":
    main()
