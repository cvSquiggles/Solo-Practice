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
        