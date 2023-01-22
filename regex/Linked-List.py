class Node:
    def __int__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


def linked_list():
    ll = Node()
    ll.element = 5
    ll.next_node = Node()


if __name__ == "__main__":
    linked_list()
