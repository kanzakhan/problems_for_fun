



public class HashMap<V> {
	public int currentSize;
	public int maxSize;
	LinkedList<V>[] list;

	public HashMap() {}

	public void set(String key, V value) {}

	public V get(String key) {}

	public void delete(String key) {}

	private int hashedIndex(String key) {}
}




class Node<V> {
	public String key;
	public V value;
	public Node<V> nextNode;

	public Node() {

	}
}

class LinkedList<V> {
	public int currentSize;
	public Node<V> head;

	public LinkedList() {}

	public void insert(String key, V value) {}

	public void delete(String key) {}

	public void peek(String key) {}
}