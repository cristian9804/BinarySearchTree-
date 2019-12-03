

class BTNode:
    def __init__(self,d,l,r):
        self.data = d
        self.left = l
        self.right = r
          
    def updateChild(self, oldChild, newChild):
        if self.left == oldChild:
            self.left = newChild
        elif self.right == oldChild:
            self.right = newChild
        else: raise Exception("updateChild error")

    # prints the node and all its children in a string
    def __str__(self):  
        st = str(self.data)+" -> ["
        if self.left != None:
            st += str(self.left)
        else: st += "None"
        if self.right != None:
            st += ", "+str(self.right)
        else: st += ", None"
        return st + "]"

# iterative version of main functions
class BST:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def __str__(self):
        return str(self.root)
        
    def add(self, d):
        if self.root == None:
            self.root = BTNode(d,None,None)
        else:
            ptr = self.root
            while True:
                if d < ptr.data:
                    if ptr.left == None:
                        ptr.left = BTNode(d,None,None)
                        break
                    ptr = ptr.left
                else:
                    if ptr.right == None:
                        ptr.right = BTNode(d,None,None)
                        break
                    ptr = ptr.right
        self.size += 1

    def _searchNode(self, ptr, d):
        while ptr != None:
            if d == ptr.data:
                return ptr
            if d < ptr.data:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return None
        
    def isIn(self, d):
        ptr = self._searchNode(self.root,d)
        if ptr == None:
            return False
        return True
    
    def count(self, d):
        ptr = self.root
        count = 0
        while ptr != None:
            ptr = self._searchNode(ptr,d)
            if ptr != None:
                count += 1
                ptr = ptr.right
        return count
    
    def remove(self,d):
        if self.root == None:
            return
        if self.root.data == d: 
            return self._removeRoot()
        parentNode = None
        currentNode = self.root
        while currentNode != None and currentNode.data !=d:
            if d < currentNode.data:
                parentNode = currentNode
                currentNode = currentNode.left
            else:
                parentNode = currentNode
                currentNode = currentNode.right
        if currentNode != None:
            return self._removeNode(currentNode,parentNode)
    
    # removes the node currentNode from the tree altogether
    def _removeNode(self,currentNode,parentNode):
        self.size -= 1
        # there are 3 cases to consider:
        # 1. the node to be removed is a leaf (no children)
        if currentNode.left == currentNode.right == None:
            parentNode.updateChild(currentNode,None)
        # 2. the node to be removed has exactly one child
        elif currentNode.left == None or currentNode.right == None:
            if currentNode.left != None:
                parentNode.updateChild(currentNode,currentNode.left)
            else:
                parentNode.updateChild(currentNode,currentNode.right)
        # 3. the node to be removed has both children
        else:
            parentMinNode = currentNode
            minNode = currentNode.right
            while minNode.left != None:
                parentMinNode = minNode
                minNode = minNode.left
            parentMinNode.updateChild(minNode,minNode.right)
            parentNode.updateChild(currentNode,minNode)
            minNode.left = currentNode.left
            minNode.right = currentNode.right
        
    def _removeRoot(self):
        # this is essentially a hack: we are adding a dummy node at 
        # the root and call the previous method -- it allows us to
        # re-use code
        parentNode = BTNode(None,self.root,None)
        self._removeNode(self.root,parentNode)
        self.root = parentNode.left
    

   
    def inOrderPrint(self):
        ptr=self.root
        self.inOrder(ptr)
    def inOrder(self,ptr):
        tree = ptr
        if tree!=None:
            self.inOrder(tree.left)
            print(tree.data)
            self.inOrder(tree.right)


#Question 3            
#t= BST()
#t.add(51)
#t.add(42)
#t.add(18)
#t.add(21)
#t.add(72)
#print(t)
#t.inOrderPrint()
