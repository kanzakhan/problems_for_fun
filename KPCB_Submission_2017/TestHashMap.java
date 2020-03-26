public class TestHashMap {
	
	// Method to test the linked list first separately from the hash map	
	public static void runListTest() {

		System.out.println("Be sure to run program with -ea flag to enable assertions");
		System.out.println("Running linked list tests...");

		// Create a linked list of string values to test
		StringHashMap<String>.HashedList<String> testList = new StringHashMap<String>(10).new HashedList<>();

		// Test List is initialized correctly
		assert testList.currentSize == 0 : "List currentSize should be initialized to 0";
		assert testList.head == null;

		// Add one item to list
		testList.insertNode("key1", "val1");
		assert testList.currentSize == 1 : "list currentSize should be one after single insertion";
		assert testList.peekNode("key1") == "val1" : "value is returned after being inserted";

		testList.insertNode("key2", "val2");
		assert testList.currentSize == 2 : "list currentSize should be two after two insertions";
		assert testList.peekNode("key1") == "val1" : "value is returned after being inserted";
		assert testList.peekNode("key2") == "val2" : "value is returned after being inserted";

		assert testList.deleteNode("key1") == "val1" : "delete should return value deleted";
		assert testList.currentSize == 1;
		assert testList.peekNode("key1") == null : "key should be deleted";
		assert testList.peekNode("key2") == "val2" : "other key should be there";

		testList.deleteNode("key2");
		assert testList.currentSize == 0 : "list should be empty";
		assert testList.peekNode("key2") == null : "key should be deleted";

		assert testList.deleteNode("unknownkey") == null : "returns safely on deleting non existent object";
		 
		System.out.println("All linked list tests passed!\n\n");
	
	}
	
	// Once linked list works properly, the full hash map will be tested
	public static void runMapTest() {

		System.out.println("Be sure to run program with -ea flag to enable assertions");
		System.out.println("Running hash map tests...");

		// Create the hash map of string values to test; map size is 10
		StringHashMap<String> testMap = new StringHashMap<>(10);

		assert testMap.maxSize == 10 : "map max size not set properly";
		assert testMap.currentSize == 0 : "map should be empty so current size must be 0";

		// Add first item to hash map
		assert testMap.set("key1", "val1") == true;
		assert testMap.currentSize == 1 : "incorrect value for current map size";
		assert testMap.get("key1") == "val1" : "should return value being viewed";
		assert testMap.delete("key1") == "val1" : "should return deleted value";
		assert testMap.currentSize == 0 : "incorrect value for current map size";

		// Add two objects with same key to hash map
		assert testMap.set("key1", "val1") == true;
		assert testMap.set("key1", "val2") == true;
		assert testMap.currentSize == 1 : "incorrect value for current map size";
		assert floatEquality(testMap.load(), (float)0.10) : "should return the ratio of current map capacity to max size";
		assert testMap.get("key1") == "val2" : "should return value being viewed";
		assert testMap.delete("key1") == "val2" : "should return deleted value";
		assert testMap.currentSize == 0 : "incorrect value for current map size";

		// Test for handling object number exceeding hash map size
		testMap = new StringHashMap<>(1);
		assert testMap.set("key1", "val1") == true;
		assert testMap.set("key2", "val2") == false : "should return false otherwise map capacity exceeds 1";
		assert testMap.currentSize == 1 : "incorrect value for current map size";
		assert testMap.get("key1") == "val1" : "should return value being viewed";
		assert testMap.get("key2") == null : "should return value being viewed";
		assert testMap.delete("key1") == "val1" : "should return deleted value";
		assert testMap.currentSize == 0 : "incorrect value for current map size";
		assert testMap.delete("key2") == null : "should return deleted value";
		assert testMap.currentSize == 0 : "incorrect value for current map size";

		System.out.println("All hash map tests passed! \n");

	}

	// Helper method to compare float values
	static boolean floatEquality (float loadFactor, float expected) {

		return Math.abs(loadFactor - expected) < 0.0001;
	}

}