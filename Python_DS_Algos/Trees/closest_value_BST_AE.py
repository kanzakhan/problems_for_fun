'''
Find Closest Value in BST - Easy

Given a target value and a BST, return a value in the tree that is closest to 
the target.
'''
import unittest

def findClosestValueInBst(tree, target):
    # start by assuming initial diff between target and BST node value is inf 
	return traverseTree(tree, target, float("inf"))
	
def childCloserToTarget(node, target):
	# target smaller than current value
	if target < node.value:
		return node.left
	# target larger than current value
	elif target > node.value:
		return node.right
	# target equals current value - can stop searching
	else: return None

def traverseTree(tree, target, smallestDiff):
	closestValue = None
	node = tree
	
	# stop at leaf nodes, or when current node value == target
	while node != None:
		# check value at current node to see if closest
		currentDiff = abs(target - node.value)
		if currentDiff <= smallestDiff:
			closestValue = node.value
			smallestDiff = currentDiff
		
		# since BST, choose child based on which closer to target
		node = childCloserToTarget(node, target)
		
	return closestValue

# ______________________________________________________________________________
# Test Code

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self


test = (
    BST(100)
    .insert(5)
    .insert(15)
    .insert(5)
    .insert(2)
    .insert(1)
    .insert(22)
    .insert(1)
    .insert(1)
    .insert(3)
    .insert(1)
    .insert(1)
    .insert(502)
    .insert(55000)
    .insert(204)
    .insert(205)
    .insert(207)
    .insert(206)
    .insert(208)
    .insert(203)
    .insert(-51)
    .insert(-403)
    .insert(1001)
    .insert(57)
    .insert(60)
    .insert(4500)
)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(findClosestValueInBst(test, 100), 100)

    def test_case_2(self):
        self.assertEqual(findClosestValueInBst(test, 208), 208)

    def test_case_3(self):
        self.assertEqual(findClosestValueInBst(test, 4500), 4500)

    def test_case_4(self):
        self.assertEqual(findClosestValueInBst(test, 4501), 4500)

    def test_case_5(self):
        self.assertEqual(findClosestValueInBst(test, -70), -51)

    def test_case_6(self):
        self.assertEqual(findClosestValueInBst(test, 2000), 1001)

    def test_case_7(self):
        self.assertEqual(findClosestValueInBst(test, 6), 5)

    def test_case_8(self):
        self.assertEqual(findClosestValueInBst(test, 30000), 55000)

    def test_case_9(self):
        self.assertEqual(findClosestValueInBst(test, -1), 1)

    def test_case_10(self):
        self.assertEqual(findClosestValueInBst(test, 29751), 55000)

    def test_case_11(self):
        self.assertEqual(findClosestValueInBst(test, 29749), 4500)
