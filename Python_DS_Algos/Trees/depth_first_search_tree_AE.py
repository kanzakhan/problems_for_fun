'''
Depth First Search - Tree

The class Node, with attribute name and (optional) children, forms a simple Tree
like structure. Implement DFS, where you navigate the tree L to R, and store the
names of all of the visited nodes in the input array for the DFS function. 
'''

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            print("Children: ", child.name)
            child.depthFirstSearch(array)
        return array

# ______________________________________________________________________________
# Testing:

import unittest

test1 = Node("A")
test1.addChild("B").addChild("C")
test1.children[0].addChild("D")

test2 = Node("A")
test2.addChild("B").addChild("C").addChild("D").addChild("E")
test2.children[1].addChild("F")

test3 = Node("A")
test3.addChild("B")
test3.children[0].addChild("C")
test3.children[0].children[0].addChild("D").addChild("E")
test3.children[0].children[0].children[0].addChild("F")

test4 = Node("A")
test4.addChild("B").addChild("C").addChild("D")
test4.children[0].addChild("E").addChild("F")
test4.children[2].addChild("G").addChild("H")
test4.children[0].children[1].addChild("I").addChild("J")
test4.children[2].children[0].addChild("K")

test5 = Node("A")
test5.addChild("B").addChild("C").addChild("D").addChild("L").addChild("M")
test5.children[0].addChild("E").addChild("F").addChild("O")
test5.children[1].addChild("P")
test5.children[2].addChild("G").addChild("H")
test5.children[0].children[0].addChild("Q").addChild("R")
test5.children[0].children[1].addChild("I").addChild("J")
test5.children[2].children[0].addChild("K")
test5.children[4].addChild("S").addChild("T").addChild("U").addChild("V")
test5.children[4].children[0].addChild("W").addChild("X")
test5.children[4].children[0].children[1].addChild("Y").addChild("Z")


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(test1.depthFirstSearch([]), ["A", "B", "D", "C"])

    def test_case_2(self):
        self.assertEqual(test2.depthFirstSearch([]), 
                            ["A", "B", "C", "F", "D", "E"])

    def test_case_3(self):
        self.assertEqual(test3.depthFirstSearch([]), 
                            ["A", "B", "C", "D", "F", "E"])

    def test_case_4(self):
        self.assertEqual(test4.depthFirstSearch([]), 
                        ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])

    def test_case_5(self):
        self.assertEqual(
            test5.depthFirstSearch([]),
            [
                "A",
                "B",
                "E",
                "Q",
                "R",
                "F",
                "I",
                "J",
                "O",
                "C",
                "P",
                "D",
                "G",
                "K",
                "H",
                "L",
                "M",
                "S",
                "W",
                "X",
                "Y",
                "Z",
                "T",
                "U",
                "V",
            ],
        )
