# Read input from STDIN. Print output to STDOUT

class CharNode:

    def __init__(self, chars = '', prevNode = None, nextNode = None):
        self.value = chars
        self.prevNode = prevNode
        self.nextNode = nextNode

    def __str__(self):  
        return "CharNode Object: value: {}".format(self.value)


class TextEditor:

    def __init__(self):

        self.cursor = CharNode()
        self.head = CharNode()
        self.undo_stack = []

        self.operations = {
            '1': self.insert_chars,
            '2': self.delete_chars,
            '3': self.print_chars,
            '4': self.undo
        }

        # set pointers for head and cursor
        self.cursor.prevNode = self.head
        self.head.nextNode = self.cursor

    def insert_chars(self, word):
        newNode = CharNode(word)
        self.cursor.prevNode.nextNode = newNode
        newNode.prevNode = self.cursor.prevNode
        newNode.nextNode = self.cursor
        self.cursor.prevNode = newNode
        self.undo_stack.append(["INSERT", word, newNode])

    def print_chars(self, print_index):
        k = 1
        printNode = ''
        while k <= print_index:
            if k == 1:
                printNode = self.head
            else:
                printNode = printNode.nextNode
            k += 1
        print(printNode.value)

    def delete_chars(self, del_index):
        k = 0
        delNode = ''
        while k <= del_index:
            if k == 0:
                delNode = self.cursor
            else:
                delNode = delNode.prevNode
            k += 1
        
        self.cursor.prevNode = delNode.prevNode
        delNode.prevNode.nextNode = self.cursor

        self.undo_stack.append(["DELETE", del_index, delNode])

    def undo(self):
        # undo stack looks like: [["OPERATION", value, pointer_to_node]]
        to_do = self.undo_stack.pop()

        if to_do[0] == "INSERT":
            self.__undo_delete(to_do)
        elif to_do[0] == "DELETE":
            self.__undo_insert(to_do)

    def __undo_delete(self, to_do):
        pass

    def __undo_insert(self, to_do):
        pass

    def update_stack(self, cmd, arg):
        pass

    def __str__(self):  
        return "TextEditor Object: value of head: {}, value at cursor: {}" \
                    .format(self.head.value, self.cursor.value)


def main():

    no_operations = int(input("Insert # of Operations"))
    operations = [None]*int(no_operations)
    i = 0

    for i in range(0,no_operations):
        operations[i] = input("Insert the Operations").split()
        if operations[i][0] == '2' or operations[i][0] == '3':
            operations[i][1] = int(operations[i][1])
    print(operations)

    # create the empty text editor:
    editor = TextEditor()
    editor.head.value = 'MILO'
    editor.insert_chars('TESTING')
    editor.insert_chars('TESTING AGAIN')

    print("Cursor: ", editor.cursor.prevNode.value)
    editor.delete_chars(1)
    print("Cursor: ", editor.cursor.prevNode.value)

    
    # go through operations to fill it with values:
    for op in operations:
        pass
    
    # create 
    return

def test_classes():
    first_letter = CharNode('K')
    print(first_letter)
    print(first_letter.value == 'K')

    editor = TextEditor()
    editor.head = first_letter
    print(editor)
    print(editor.head.value == 'K')

main()
# test_classes()
