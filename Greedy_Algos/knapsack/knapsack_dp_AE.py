'''
# the columns  of table are all the weights knapsack can have
# the rows represent each additional item that can be added to sack
# the entries of the table are the value of the knapsack, given the
# current capacity of the knapsack (column) and the available items
# to add to the sack (the row). More items available with increasing row index

item_index  [p,w]   ____0_______1______2______3______4_______5____
n/a    |    []     |    0   |   0  |   0  |   0  |   0   |   0   |
0      |    [1,2]  |    0   |      |      |      |       |       |
1      |    [3,4]  |    0   |      |      |      |       |       |
2      |    [4,3]  |    0   |      |      |      |       |   *   |

* = final knapsack value

'''
import unittest

def find_knapsack_value(prices, weights, max_capacity):
    # +1 to len of prices to include 'None' item [] (the base case)
    num_items = len(prices) + 1
    knapsack_value = [[0 for j in range(max_capacity + 1)] for i in range(num_items)]

    # base cases: when 0 items to put in knapsack
    # or, weight available in knapsack is 0
    # so the first row and column are already all 0, can skip in for loops

    for current_item in range(1, num_items):
        current_item_weight = weights[current_item - 1]
        current_item_price = prices[current_item - 1]
        
        for knapsack_capacity in range(1, max_capacity + 1):
            prev_item = current_item - 1
            # current item weighs less than knapsack capacity
            if current_item_weight <= knapsack_capacity:
                # value will be max of either:
                # 1) not adding the current item at all, even if it fits
                # 2) adding the current item's value to the prev max
                #       value the knapsack had -- subtract the weight of current item
                #       to accomodate adding it to sack
                knapsack_value[current_item][knapsack_capacity] = \
                    max(
                        knapsack_value[prev_item][knapsack_capacity],
                        knapsack_value[prev_item][knapsack_capacity - current_item_weight] \
                            + current_item_price
                    )
            # current item weighs more than knapsack capacity - wont fit
            else:
                  knapsack_value[current_item][knapsack_capacity] = \
                      knapsack_value[prev_item][knapsack_capacity]  
    
    return knapsack_value

# find items put in sack by backtracking and removing items if the knapsack's value
# changed (based on knapsack table) after the item was added to sack
def get_knapsack_items(knapsack_value, weights, max_capacity):
    items_in_sack = []
    sack_item_index = len(knapsack_value) - 1
    current_capacity = max_capacity
    # > 0 b/c 0th ithem is just [] in the sack
    while sack_item_index > 0 and current_capacity > 0:
        # if knapsack value didnt change, then item was not added
        if knapsack_value[sack_item_index][current_capacity] == \
            knapsack_value[sack_item_index - 1][current_capacity]:
            sack_item_index -= 1
        else:
            items_in_sack.append(sack_item_index - 1)
            current_capacity -= weights[sack_item_index - 1]
            sack_item_index -= 1
    return list(reversed(items_in_sack))
        
def knapsackProblem(items, capacity):
    # items = [[value, weight]]
    prices = [item[0] for item in items]
    weights = [item[1] for item in items]
    knapsack_value = find_knapsack_value(prices, weights, capacity)
    knapsack_items = get_knapsack_items(knapsack_value, weights, capacity)
    return [knapsack_value[-1][-1], knapsack_items]

# ----------------------------------------------------------------------------------

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10), [10, [1, 3]])

    def test_case_2(self):
        self.assertEqual(
            knapsackProblem(
                [
                    [465, 100],
                    [400, 85],
                    [255, 55],
                    [350, 45],
                    [650, 130],
                    [1000, 190],
                    [455, 100],
                    [100, 25],
                    [1200, 190],
                    [320, 65],
                    [750, 100],
                    [50, 45],
                    [550, 65],
                    [100, 50],
                    [600, 70],
                    [240, 40],
                ],
                200,
            ),
            [1500, [3, 12, 14]],
        )

test = TestProgram()
test.test_case_1()
test.test_case_2()

'''
Practice Problem from Algo Expert
'''