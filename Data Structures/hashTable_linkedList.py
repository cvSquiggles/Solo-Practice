class node():
    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next_node = next_node

    def set_next(self, next_node):
        # Moves pointer to next point
        self.next_node = next_node

    def __str__(self):
        # Controls print() behavior
        return f'{self.key, self.value}'
    
class Linked_list():

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, key, value):
        # If no key/value entered
        if not (key and value):
            print('Key and Value are required')
            return
        new_node = node(key, value)
        # If our list is empty, add the initial node...
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            self.size = 1
            print("First item inserted")
            return
        # ...otherwise add the node to the list
        self.head.next_node = new_node
        self.head = new_node
        self.size += 1
        print("Item inserted successfully")
        return
    
    def peek(self):
        print(self.head)

class HashTable():
    def __init__(self):
        self.size = 6
        self.ll_array = [Linked_list() for _ in range(self.size)]
        print("Hash table initialized")

    def _show_sizes(self):
        # Show the length of each linked list within the hashtable
        for l in self.ll_array:
            print(l.size)

    def insert(self, key, value):
        # Insert a node into the hashtable
        key_hash = self.hash(key)
        index = key_hash % self.size
        print(f'{key} kept at index {index}')
        self.insert_on_arr(key, value, index)

    def insert_on_arr(self, key, value, index):
        self.ll_array[index].insert(key, value)
    
    def look_up(self, key):
        # Search a node in the hashtable
        key_hash = self.hash(key)
        index = key_hash % self.size
        print(f'{key} hashes at index {index}')
        ll_size = self.ll_array[index].size
        print(ll_size, ' is the current size')
        if ll_size == 0:
            print(f'{key} has not yet been inserted')
            return
        elif ll_size == 1:
            if self.ll_array[index].head.key == key:
                print(self.ll_array[index].peek())
                return
            else:
                print(f"There was a collision, the hash for '{self.ll_array[index].head.key}' and '{key} are the same")
                return
        else:
            travereser = self.ll_array[index].tail
            # Here's the linear search for the key
            while travereser:
                if traverser.key == key:
                    print(traverser.value)
                    return
                traverser = traverser.next_node

            print(f"There was a collision, the hash for the '{self.ll_array[index].head.key}' and '{key}' are the same")
    
    def hash(self, key):
        # Consistently hashes a provided key
        """
        >>>'amiay'.__hash()
        5169131434226628243
        """
        return key.__hash__()
    
#myTable = HashTable()


#myTable.insert('keyOne','Jon Doe')
#myTable.insert('keyTwo','Jane Doe')
#myTable.insert('keyThree','Ronald Radke')

#print(myTable)