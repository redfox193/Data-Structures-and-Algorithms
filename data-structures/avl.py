from typing import Any


class TreeNode:
    
    def __init__(self, val: Any, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1


class AvlTree:
    
    def __init__(self, root: TreeNode = None) -> None:
        self.root = root
        
    def add(self, node: TreeNode) -> None:
        if self.root is None:
            self.root = node
        else:
            parent = self.root
            st = [self.root]

            while parent.val != node.val:
                if parent.val > node.val:
                    next_node = parent.left
                else:
                    next_node = parent.right

                if next_node is None:
                    break
                parent = next_node
                st.append(parent)
            
            if parent.val == node.val:
                return
            if parent.val > node.val:
                parent.left = node
            else:
                parent.right = node
            

            while len(st) != 1:
                parent = st.pop()
                self.__balance(st[-1], parent)
            self.__balance(self.root, st.pop())

    def delete(self, value: Any) -> None:
        parent = self.root
        node = self.root
        st = [self.root]

        while node is not None and node.val != value:
            if node.val > value:
                parent, node = node, node.left
            else:
                parent, node = node, node.right
            st.append(parent)
                
        if node is None:
            return
        
        if node.right is None and node.left is None:
            self.__delete_leaf(parent, node)
        elif node.right is None or node.left is None:
            self.__delete_node_with_one_child(parent, node)
        else:
            self.__delete_node_with_children(parent, node, st)

        if self.root is None:
            return
        
        while len(st) != 1:
            parent = st.pop()
            self.__balance(st[-1], parent)
        self.__balance(self.root, st.pop())
        
    def __delete_leaf(self, parent: TreeNode, leaf: TreeNode):
        if self.root is leaf:
            self.root = None
            return
        
        if parent.val > leaf.val:
            parent.left = None
        else:
            parent.right = None
    
    def __delete_node_with_one_child(self, parent: TreeNode, node: TreeNode):
        if self.root is node:
            self.root = node.left if node.left is not None else node.right
            return
        
        if parent.val > node.val:
            parent.left = node.left if node.left is not None else node.right
        else:
            parent.right = node.left if node.left is not None else node.right
            
    def __delete_node_with_children(self, parent: TreeNode, node: TreeNode, stack: list) -> None:
        replace_parent, replace_node = node, node.right
        new_stack = []
        while replace_node.left is not None:
            replace_parent, replace_node = replace_node, replace_node.left
            new_stack.append(replace_parent)
        
        stack.append(replace_node)
        stack += new_stack

        if replace_node.right is None:
            self.__delete_leaf(replace_parent, replace_node)
        else:
            self.__delete_node_with_one_child(replace_parent, replace_node)
        
        replace_node.left, replace_node.right = node.left, node.right
        
        if self.root is node:
            self.root = replace_node
            return
        
        if parent.val > node.val:
            parent.left = replace_node
        else:
            parent.right = replace_node

    def __ll(self, parent: TreeNode, node: TreeNode) -> None:
        new_node = node.left
        node.left, new_node.right = node.left.right, node
        self.__update_height(node)
        self.__update_height(new_node)

        if node == self.root:
            self.root = new_node
            return
        if parent.left == node:
            parent.left = new_node
        else:
            parent.right = new_node

    def __rr(self, parent: TreeNode, node: TreeNode) -> None:
        new_node = node.right
        node.right, new_node.left = node.right.left, node
        self.__update_height(node)
        self.__update_height(new_node)

        if node == self.root:
            self.root = new_node
            return
        if parent.left == node:
            parent.left = new_node
        else:
            parent.right = new_node

    def __lr(self, parent: TreeNode, node: TreeNode) -> None:
        new_node = node.left.right
        new_node_left = node.left
        new_node_right = node
        new_node_left.right, new_node_right.left = new_node.left, new_node.right
        new_node.left, new_node.right = new_node_left, new_node_right
        self.__update_height(new_node_left)
        self.__update_height(new_node_right)
        self.__update_height(new_node)

        if node == self.root:
            self.root = new_node
            return
        if parent.left == node:
            parent.left = new_node
        else:
            parent.right = new_node

    def __rl(self, parent: TreeNode, node: TreeNode) -> None:
        new_node = node.right.left
        new_node_left = node
        new_node_right = node.right
        new_node_left.right, new_node_right.left = new_node.left, new_node.right
        new_node.left, new_node.right = new_node_left, new_node_right
        self.__update_height(new_node_left)
        self.__update_height(new_node_right)
        self.__update_height(new_node)

        if node == self.root:
            self.root = new_node
            return
        if parent.left == node:
            parent.left = new_node
        else:
            parent.right = new_node

    def __balance(self, parent: TreeNode, node: TreeNode) -> None:
        if node is None:
            return
        
        self.__update_height(node)

        left_h = self.__height(node.left)
        right_h = self.__height(node.right)
        if left_h > right_h + 1:
            left_h1 = self.__height(node.left.left)
            right_h1 = self.__height(node.left.right)
            if left_h1 > right_h1:
                self.__ll(parent, node)
            else:
                self.__lr(parent, node)
        elif right_h > left_h + 1:
            left_h1 = self.__height(node.right.left)
            right_h1 = self.__height(node.right.right)
            if right_h1 > left_h1:
                self.__rr(parent, node)
            else:
                self.__rl(parent, node)
        else:
            return
        
        self.__update_height(parent)

    def __height(self, node: TreeNode) -> int:
        return 0 if node is None else node.height
    
    def __update_height(self, node: TreeNode) -> None:
        if node is None:
            return
        node.height = max(self.__height(node.left), self.__height(node.right)) + 1