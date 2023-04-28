from Node import BinarySearchTree

def list_to_bst(func):
    def wrapper(*args):
        source = func(*args)
        root = source[len(source)//2]
        source.remove(root)
        bst = BinarySearchTree(root)
        for num in source:
            bst.add_node(num)
        print(f'\nRoot = {bst.root.value}\n')
        print(f'Minimum = {bst.get_min()}\n')
        print(f'Maximum = {bst.get_max()}\n')
    return wrapper



@list_to_bst
def create_list(num):
    num_list = []
    for i in range(num + 1):
        num_list.append(i)
    return num_list

my_bst = create_list(10)
