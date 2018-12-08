class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, elt):
        self.stack.append(elt)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        elt = self.pop()
        self.push(elt)
        return elt
    
    def is_empty(self):
        return self.stack == []
    
    def decrease_top(self):
        (children, meta) = self.pop()
        self.push((children-1, meta))

class TreeStack:
    def __init__(self):
        self.stack = []
    
    def push(self, elt):
        self.stack.append(elt)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        elt = self.pop()
        self.push(elt)
        return elt
    
    def is_empty(self):
        return self.stack == []
    
    def decrease_top(self):
        (children, meta, tree) = self.pop()
        self.push((children-1, meta, tree))

class Tree:
    def __init__(self):
        self.children = []
        self.metadata = []
    
    def add_meta(self, meta):
        for m in meta:
            self.metadata.append(m)
    
    def add_child(self, child):
        self.children.append(child)

def get_data():
    file = open('input.txt', 'r')
    result = []
    for line in file.readlines():
        # decode the line
        line = line.splitlines()[0]
        for i in line.split(' '):
            result.append(int(i))
    return result

def metadata_sum():
    nums = get_data()
    #nums = [2,3,0,3,10,11,12,1,1,0,1,99,2,1,1,2]
    stack = Stack()
    metadata_sum = 0
    i = 0
    while i < len(nums):
        # see if the stack is empty
        if not stack.is_empty():
            (children_left, meta_to_get) = stack.peek()
            # if there's no more children
            if children_left == 0:
                # then we can get our metadata
                for j in range(i, meta_to_get + i):
                    metadata_sum += nums[j]
                i += meta_to_get
                # and remove this parent from the stack since we're done
                stack.pop()
            # but if there are more children to get
            else:
                stack.decrease_top()
                num_children = nums[i]
                num_metadata = nums[i + 1]
                # if there are no children to get we have a concise unit
                if num_children == 0:
                    # so we add its metadata to the sum
                    for j in range(i+2, i+num_metadata+2):
                        metadata_sum += nums[j]
                    i += 2 + num_metadata
                # but if there are children to get
                else:
                    # we need to add to the stack to keep track of it
                    stack.push((num_children, num_metadata))
                    i += 2
        else:
            num_children = nums[i]
            num_metadata = nums[i + 1]
            if num_children == 0:
                for j in range(i, i+num_metadata):
                    metadata_sum += nums[j]
                i += 2 + num_metadata
            else:
                stack.push((num_children, num_metadata))
                i += 2
    return metadata_sum

def build_tree():
    nums = get_data()
    stack = TreeStack()
    root = Tree()
    metadata = []
    i = 0
    while i < len(nums):
        # see if the stack is empty
        if not stack.is_empty():
            (children_left, meta_to_get, tree_node) = stack.peek()
            # if there's no more children
            if children_left == 0:
                # then we can get our metadata
                metadata = []
                for j in range(i, meta_to_get + i):
                    metadata.append(nums[j])
                tree_node.add_meta(metadata)
                i += meta_to_get
                # and remove this parent from the stack since we're done
                stack.pop()
            # but if there are more children to get
            else:
                stack.decrease_top()
                num_children = nums[i]
                num_metadata = nums[i + 1]
                # if there are no children to get we have a concise unit
                if num_children == 0:
                    tree = Tree()
                    metadata = []
                    # so we add its metadata to the sum
                    for j in range(i+2, i+num_metadata+2):
                        metadata.append(nums[j])
                    tree.add_meta(metadata)
                    tree_node.add_child(tree)
                    i += 2 + num_metadata
                # but if there are children to get
                else:
                    # we need to add to the stack to keep track of it
                    tree = Tree()
                    tree_node.add_child(tree)
                    stack.push((num_children, num_metadata, tree))
                    i += 2
        else:
            num_children = nums[i]
            num_metadata = nums[i + 1]
            stack.push((num_children, num_metadata, root))
            i += 2
    return root

def get_root_value():
    tree = build_tree()
    def get_meta_sum(subtree):
        children = subtree.children
        metadata = subtree.metadata
        metadata_sum = 0
        if children == []:
            for m in metadata:
                metadata_sum += m
        else:
            for index in metadata:
                if index-1 < len(children):
                    metadata_sum += get_meta_sum(children[index-1])
        return metadata_sum
    return get_meta_sum(tree)
    


print(metadata_sum())
print(get_root_value())
