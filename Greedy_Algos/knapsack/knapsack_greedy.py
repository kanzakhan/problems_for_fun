'''
Greedy approach does not always guarantee an optimal solution
'''

def knapsackProblem(items, capacity):
	# items = [[value, weight]]
    selectedItems = []
    currentCapacity = capacity
    profit = 0
	# find value per unit weight and sort
    valuePerUnitWeight = getValuePerWeight(items)
	
    i = 0
    while currentCapacity > 0 and i < len(items):
		
		nextBestItemIndex = valuePerUnitWeight[i][0]
		nextBestItemWeight = items[nextBestItemIndex][1]
		nextBestItemValuePerUnitWeight = valuePerUnitWeight[i][1]
		
		if nextBestItemWeight >= currentCapacity:
			profit += nextBestItemValuePerUnitWeight * currentCapacity
			currentCapacity -= currentCapacity
		else:
			profit += nextBestItemValuePerUnitWeight * nextBestItemWeight
			currentCapacity -= nextBestItemWeight
			
		i += 1
		selectedItems.append(nextBestItemIndex)
		
    print([profit, selectedItems])
	# return maximum combined value, array of item indices
    return [int(profit), selectedItems]

def getValuePerWeight(items):
	valuePerUnitWeight = []
	for i, item in enumerate(items):
		valuePerUnitWeight.append([i,item[0]/item[1]])
	# sort in descending order with key being the 2nd item:
	valuePerUnitWeight.sort(reverse=True, key=takeSecond)
	return valuePerUnitWeight

# return 2nd item
def takeSecond(elem):
    return elem[1]

print(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10))