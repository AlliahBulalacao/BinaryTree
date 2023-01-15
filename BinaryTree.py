class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)

            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)

            else:
                return False

        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

            elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        return elements

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            minimum_val = self.right.minimum()
            self.data = minimum_val
            self.right = self.right

        return self

    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()

    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()

def build_tree(elements):
    print("Full Name: ", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ =='__main__':
    fullname = ['A', 'L', 'L', 'I', 'A', 'H', 'M', 'A', 'E', 'B.', 'B', 'U', 'L', 'A', 'L', 'A', 'C', 'A','O']
    binary_name = build_tree(fullname)

    print("Sorted Order: ", binary_name.in_order_traversal())
    print("Post-Order: ", binary_name.post_order_traversal())
    print("Pre-Order: ", binary_name.pre_order_traversal())
    print("Minimum value on the list: ", binary_name.min())
    print("Maximum value on the list: ", binary_name.max())

    ask = input("\nDo you want to delete letter A from the list? (Y/N) ")
    if ask == 'Y':
        ans = input("What letter do you want to delete? ")
        print("The", ans, "have now deleted")
        binary_name.delete(ans)
        print("New list: ", binary_name.in_order_traversal())







