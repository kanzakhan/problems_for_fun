import java.util.*;

class LinkedList<T> {

	Node head;
	int size;


	public LinkedList() {

		this.head = NULL;
		this.size = 0;
	}

	public T addNode(T data) {

		Node<T> temp;
		if (size == 0) {

			temp = new Node<T>(data);
			head = temp; 
			size++;
			return data;
		}

		temp = head;
		while (temp.next != null) {

			temp = temp.next;

		}
		Node<T> newNode = new Node<T>(data);
		temp.next = newNode;
		newNode.previous = temp;
		size++;
	}

	public T deleteNode(T data) {

		if (size == 0) {

			return NULL;
		}

		Node<T> temp = head;
		while(temp.data != data) {

			temp = temp.next;
		}

		temp.previous.next = temp.next;
		temp.next.previous = temp.previous;
		size--;
		return data;
	}

	public boolean findNode(T data) {

		if (size == 0) {

			return false;
		}

		Node<T> temp = head;
		while(temp.data != data) {

			temp = temp.next;
		}

		if(temp.data == data)
			return true;
		else
			return false;
	}
	
	class Node<T> {

		Node<T> previous;
		Node<T> next;
		T data;

		public Node(T data) {

			this.data = data;
			this.previous = NULL;
			this.next = NULL;

		}


	}


}