__author__ = 'michaeljyan'

class Node():
    def __init__(self, value, leftChild, rightChild):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild

    def visited(self):
        print self.value

def preOrderRecursion(node):
    if not node:
        return

    node.visited()
    preOrderRecursion(node.leftChild)
    preOrderRecursion(node.rightChild)

def inOrderRecursion(node):
    if not node:
        return

    inOrderRecursion(node.leftChild)
    node.visited()
    inOrderRecursion(node.rightChild)

def postOrderRecursion(node):
    if not node:
        return

    postOrderRecursion(node.leftChild)
    postOrderRecursion(node.rightChild)
    node.visited()

def preOrderNoRecursion(node):
    stack=[]
    while(len(stack)!=0 or node):
        if node:
            node.visited()
            stack.append(node.rightChild)
            node=node.leftChild
        else:
            node=stack.pop()

def inOrderNoRecursion(node):
    stack=[]
    while(len(stack)!=0 or node):
        if node:
            stack.append(node)
            node = node.leftChild
        else:
            node = stack.pop()
            node.visited()
            node = node.rightChild

def postOrderNoRecursion(node):
    if not node:
        return

    stack = [node]
    prevNode = None
    while(len(stack)!=0):
        currNode=stack[-1]
        if not prevNode or prevNode.leftChild==currNode or prevNode.rightChild==currNode:
            if currNode.leftChild:
                stack.append(currNode.leftChild)
            elif currNode.rightChild:
                stack.append(currNode.rightChild)
            else:
                pass
        elif currNode.leftChild==prevNode:
            if currNode.rightChild:
                stack.append(currNode.rightChild)
        else:
            currNode.visited()
            stack.pop()

        prevNode = currNode



if __name__=="__main__":

    '''
                   1
                   
                /     \
               2       3
              / \     /
             4   5   6
            /       / \
           7       8   9
    '''
    node_7 = Node(7, None, None)
    node_8 = Node(8, None, None)
    node_9 = Node(9, None, None)

    node_4 = Node(4, node_7, None)
    node_5 = Node(5, None, None)
    node_6 = Node(6, node_8, node_9)

    node_2 = Node(2, node_4, node_5)
    node_3 = Node(3, node_6, None)

    node_1 = Node(1, node_2, node_3)

#    print "+++++++++++++++++++++++++++"
#    preOrderRecursion(node_1)
#    print "+++++++++++++++++++++++++++"
#    inOrderRecursion(node_1)
#    print "+++++++++++++++++++++++++++"
#    postOrderRecursion(node_1)
#    print "+++++++++++++++++++++++++++"
#    preOrderNoRecursion(node_1)
#    print "+++++++++++++++++++++++++++"
#    inOrderNoRecursion(node_1)
#    print "+++++++++++++++++++++++++++"
    postOrderNoRecursion(node_1)




