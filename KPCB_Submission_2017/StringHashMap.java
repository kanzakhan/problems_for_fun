import java.util.Arrays;

public class StringHashMap <V> {
	
	int maxSize;
	int currentSize;
	HashedList<V>[] hashMap;

	// Constructor 
	StringHashMap(int mapSize) {

		currentSize = 0;
		maxSize = mapSize;
		hashMap = new HashedList[maxSize];

		// Populate the HashedList with linked lists
		for (int i = 0; i < maxSize; i++)
			hashMap[i] = new HashedList<V>();
	}

	// Set the key and its corresponding value
	public boolean set(String key, V value) {

		// Check that map is not at capacity before insertion
		// If key is already in map, then value can be updated since
		// map size is not changing
		if (currentSize >= maxSize && get(key) == null) 
			return false;

		boolean insertDone;
		// Call the hash function to get hash index
		int hashIndex = index(key);

		// insertNode takes the new key and value as input param
		insertDone = hashMap[hashIndex].insertNode(key, value);
		
		// Note: currentSize should only increase when new node added, 
		// not when an existing node's value is updated
		if (insertDone)
			currentSize++;

		return true;
	}

	// Get function that returns value associated with the key
	public V get(String key) {
		return hashMap[index(key)].peekNode(key);
	}

	// Delete function removes the value assocated with given key
	// Value is returned upon success, or null if there was no value
	public V delete(String key) {

		V nodeValue = hashMap[index(key)].deleteNode(key);
		if (nodeValue != null) 
			currentSize--;
		return nodeValue;

	}

	// Find the current maxSize of the hash map
	public float load() {

		float loadFactor = (float)currentSize / (float)maxSize;

		if (loadFactor > 1)
			System.out.println("Error, load factor > 1");

		return loadFactor;

	}

	// The Hash Function takes in the string key and returns the index for the hash map
	private int index(String key) {

		return Math.abs(key.hashCode()) % maxSize;
	}


	// Separate node class to create a node object for linked list
	class Node <V> {

		public String key;
		public V value;
		public Node<V> nextNode;

		// Node<V> constructor
		public Node(String key, V value) {

			this.key = key;
			this.value = value;

			// Default: set pointer to the next node to null...
			nextNode = null;
		}

	}

	// Singley-linked list for separate chaining in the hash map entries
	class HashedList <V> {

		public int currentSize;
		public Node<V> head;	// List Head

		//List Constructor
		HashedList() {

			currentSize = 0;
			head = null;	// First node in list is null by default

		}

		// Method to insert node into list; returns true only when a new node is created
		public boolean insertNode(String key, V value) {

			Node<V> currentNode = head;

			// Check through entire list to see if new key matches an existing one
			while (currentNode != null) {

				// If there is a matching key, update the old node value with new value
				// Note the list currentSize and map currentSize both do not change in this case
				if (currentNode.key.equals(key)) {

					currentNode.value = value;
					return false;

				} else
					currentNode = currentNode.nextNode;
				
			}

			// If the key does not already exist in the list or head is null
			// then create a new node with the given key/value pair
			Node<V> newNodeObject = new Node<V>(key, value);
			newNodeObject.nextNode = head;
			head = newNodeObject;
			currentSize++;
			return true;

		}

		// Method to peek at node in list; returns value on success
		public V peekNode(String matchKey) {

			V tempValue = null;
			// Set a dummy current node to the first node in the list
			Node<V> currentNode = head;

			// Add loop to traverse the linked list and find matching key
			while (currentNode != null) {

				// Check if keys match at each node, if not move to next node
				if (currentNode.key.equals(matchKey))
					return currentNode.value;
				else 
					currentNode = currentNode.nextNode;
					
			}

			if (tempValue == null)
				System.out.println("No such object found in the map to view");
			return tempValue; // Null returned if no match found (key/value pair DNE)
		}

		// Method to delete node in list; returns value on success
		public V deleteNode(String matchKey) {

			V tempValue = null;
			Node<V> currentNode = head;
			Node<V> priorNode = head;

			// Retrieve the value of the node to be deleted
			// Loop to traverse the linked list and find matching key
			while (currentNode != null) {

				if (currentNode.key.equals(matchKey)) {

					tempValue = currentNode.value;

					// Remove the current node from the list
					// Delete Node<V> Object from list by rearranging pointers
					if (currentNode == head)
						head = head.nextNode;
					else
						priorNode.nextNode = currentNode.nextNode;
					
					// Must also decrement total list items
					currentSize--;
					return tempValue;		//return currentNode.value;

				} else {

					priorNode = currentNode;
					currentNode = currentNode.nextNode;

				}
			}

			if (tempValue == null)
				System.out.println("No such object found in the map to delete");
			return tempValue;

		}
	}

	public static void main(String[] args) {

		// Main will only be running the tests to confirm
		// that both the linked list and hash map are working
		TestHashMap.runMapTest();
		TestHashMap.runListTest();
		return;
	}
}

