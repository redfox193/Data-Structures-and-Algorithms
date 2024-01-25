from typing import Any


class TreeNode:
    
    def __init__(self, val: Any, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    
    def __init__(self, root: TreeNode = None) -> None:
        self.root = root
        
    def add(self, value: Any) -> None:
        node = TreeNode(value)
        if self.root is None:
            self.root = node
        else:
            parent = self.root

            while parent.val != node.val:
                if parent.val > node.val:
                    next_node = parent.left
                else:
                    next_node = parent.right

                if next_node is None:
                    break
                parent = next_node
            
            if parent.val == node.val:
                return
            if parent.val > node.val:
                parent.left = node
            else:
                parent.right = node
                
    def delete(self, value: Any) -> None:
        parent = self.root
        node = self.root
        
        while node is not None and node.val != value:
            if node.val > value:
                parent, node = node, node.left
            else:
                parent, node = node, node.right
                
        if node is None:
            return
        
        if node.right is None and node.left is None:
            self.__delete_leaf(parent, node)
        elif node.right is None or node.left is None:
            self.__delete_node_with_one_child(parent, node)
        else:
            self.__delete_node_with_children(parent, node)
        
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
            
    def __delete_node_with_children(self, parent: TreeNode, node: TreeNode) -> None:
        replace_parent, replace_node = node, node.right
        while replace_node.left is not None:
            replace_parent, replace_node = replace_node, replace_node.left
        
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