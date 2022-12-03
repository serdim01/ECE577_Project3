
def precedence(Char):
    if Char == "$":
        return 1
    elif Char == ">":
        return 2
    elif Char == "|":
        return 3
    elif Char == "^":
        return 4
    elif Char == "~":
        return 5
    else: 
        return 0 

def infixToPostfix(infix):
    # ~ Negation
    # ^ and
    # | or
    # > if then
    # <> if and only if 
    postfixStack = [];
    postfixExpression = [];
    i = -1;
    while(i< (len(infix)-1)):
        i+=1
        char = infix[i]    
        if char.isalnum():
            postfixExpression.append(char)
        elif char == '(':
            postfixStack.append('(')
        elif char == '~':
            postfixStack.append('~')
        elif char == ')':
            while ((len(postfixStack) > 0) and (postfixStack[-1] != "(")):
                postfixExpression.append(postfixStack.pop(-1))
            postfixStack.pop(-1) # Pop the (
        else:
            while ((len(postfixStack) > 0) and (precedence(char) <= precedence(postfixStack[-1]))):        
                postfixExpression.append(postfixStack.pop(-1))
            postfixStack.append(char)
   
    while (len(postfixStack) > 0):
        postfixExpression.append(postfixStack.pop(-1))
        
    ''.join(str(e) for e in postfixExpression)
    return postfixExpression

def remove(string):
    return string.replace(" ", "")

# https://stackoverflow.com/questions/41760856/most-simple-tree-data-structure-in-python-that-can-be-easily-traversed-in-both
class Tree(object):
    def __init__(self, data, children=None, parent=None):
        self.children = children or []
        self.parent = parent
        self.data = data
    
    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.children

    def __str__(self):
        if self.is_leaf():
            return str(self.data)
        return '{data} [{children}]'.format(data=self.data, children=', '.join(map(str, self.children)))  
      
def postfixToTree(postFix):
    stack = []
    PostFixTree = []
    flag = 0;
    for chars in postFix:
        if (precedence(chars) == 0): 
            stack.append(chars)
        else:
            if len(PostFixTree) == 0:
                left = stack.pop(-1)
                if len(stack) == 0:
                    left_tree = Tree(left)
                    PostFixTree.append(Tree(chars))
                    PostFixTree[0].children.append(left_tree)
                else:
                    right = stack.pop(-1)
                    PostFixTree.append(Tree(chars))
                    PostFixTree[-1].children.append(Tree(left))
                    PostFixTree[-1].children.append(Tree(right))
            else:
                if chars == '~':
                    if len(stack) == 1:
                        left = stack.pop(-1)
                        PostFixTree.append(Tree(chars)) 
                        PostFixTree[-1].children.append(Tree(left))
                        flag = 1;
                    elif (flag==1) and (len(stack) == 0):
                        PostFixTree.append(Tree(chars)) 
                        PostFixTree[-1].children.append((PostFixTree[-2]))
                        flag = 0
                    else:
                        PostFixTree.append(Tree(chars)) 
                        PostFixTree[-1].children.append((PostFixTree[-2]))
                elif len(stack) == 0:
                    PostFixTree.append(Tree(chars)) 
                    PostFixTree[-1].children.append((PostFixTree[-2]))
                    if len(PostFixTree) > 2:
                        PostFixTree[-1].children.append((PostFixTree[-3]))
                elif len(stack) == 1:
                    right = stack.pop(-1)
                    PostFixTree.append(Tree(chars))
                    PostFixTree[-1].children.append(Tree(right))
                    PostFixTree[-1].children.append((PostFixTree[-2]))
                elif ((precedence(stack[-1]) == 0) and (precedence(stack[-2]) == 0)):
                    left = stack.pop(-1)
                    right = stack.pop(-1)
                    PostFixTree.append(Tree(chars))
                    PostFixTree[-1].children.append(Tree(left))
                    PostFixTree[-1].children.append(Tree(right))
        
    return PostFixTree

def TreeTraversalIFF(TreeItem):
    # Reference to root
    current = TreeItem
    stack = []
    # Changing Root Directly
    current = removeIFF(current)
    while True:
        if current.is_leaf() is not True:
            # Appending with reference?
            stack.append(current)
            current = current.children[0]
            current = removeIFF(current)
        elif(stack):
            current = stack.pop()
            if len(current.children) > 1:    
                current = current.children[1]
                current = removeIFF(current)
            else:
                current = current.children[0]
                current = removeIFF(current)
        else:
            break
    return TreeItem

def TreeTraversalIMP(TreeItem):
    # Reference to root
    current = TreeItem
    stack = []
    # Changing Root Directly
    current = removeIMP(current)

    while True:
        if current.is_leaf() is not True:
            # Appending with reference?
            stack.append(current)
            current = current.children[0]
            current = removeIMP(current)
        elif(stack):
            current = stack.pop()
            if len(current.children) > 1:    
                current = current.children[1]
                current = removeIMP(current)
            else:
                current = current.children[0]
                current = removeIMP(current)
        else:
            break
    return TreeItem

def DistributeOR(TreeItem):
    # Reference to root
    current = TreeItem
    stack = []
    # Changing Root Directly
    current = distOR(current)

    while True:
        # print("---------------------------------")
        # printTree(TreeItem, level=0)
        if current.is_leaf() is not True:
            # Appending with reference?
            stack.append(current)
            current = current.children[0]
            current = distOR(current)
        elif(stack):
            current = stack.pop()
            if len(current.children) > 1:    
                current = current.children[1]
                current = distOR(current)
            else:
                current = current.children[0]
                current = removeIMP(current)
        else:
            break
    return TreeItem

def distOR(TreeIn):
    if (TreeIn.data == '|') and (TreeIn.children[1].data == "^") and (TreeIn.children[0].data == "^"):
        TreeIn.data = "^"
        TreeIn.children[0].data = "|"
        TreeIn.children[1].data = "|"
    elif (TreeIn.data == '|') and (TreeIn.children[0].data == "^"):
        TreeIn.data = "^"
        TreeIn.children[0].data = "|"
        TreeIn.children[0]
    elif (TreeIn.data == '|') and (TreeIn.children[1].data == "^"):
        TreeIn.data = "^"
        TreeIn.children[1].data = "|"
    return TreeIn
def TreeTraversalNEG(TreeItem):
    # Reference to root
    current = TreeItem
    stack = []
    # Changing Root Directly
    current = removeNEG(current)
    # print("---------------------------------")
    # printTree(TreeItem, level=0)
    while True:
        # print("--------------START--------------")
        # printTree(TreeItem, level=0)
        if current != []:
            if current.is_leaf() is not True:
            # Appending with reference?
                stack.append(current)
                current = current.children[0]
                current = removeNEG(current)
            elif (stack):
                current = stack.pop()
                if len(current.children) > 1:    
                    current = current.children[1]
                    current = removeNEG(current)
                else:
                    current = current.children[0]
                    current = removeNEG(current)
            else:
                break
        elif (stack):
            current = stack.pop(0)
            if len(current.children) > 1:    
                current = current.children[1]
                current = removeNEG(current)
            else:
                current = current.children[0]
                current = removeNEG(current)
        else:
            break
        # print("--------------AFTER--------------")
        # printTree(TreeItem, level=0)
    return TreeItem

def removeIMP(TreeIn):
    if TreeIn.data == '>':
        TreeIn.data = "|"
        alpha = list(TreeIn.children)
        TreeIn.children[1].data = "~"+alpha[1].data
    return TreeIn

def removeNEG(TreeIn):
    if TreeIn != []:
        if TreeIn.data == '~~':
            TreeIn.data = TreeIn.children[0].data
            TreeIn.children = list(TreeIn.children[0].children)
        elif (TreeIn.data[0] == '~'):
            if TreeIn.data == '~~':
                TreeIn.data = TreeIn.children[0].data
                TreeIn.children = list(TreeIn.children[0].children)
            if len(TreeIn.data) > 1:
                if TreeIn.data[1].isalnum() is False:
                    if (TreeIn.data[1] == '|'):
                            TreeIn.data = '^'
                            TreeIn.children = list(TreeIn.children)
                            for kiddos in TreeIn.children:
                                if (kiddos.data[0] == "~") and (kiddos.data[1] == "~") and (len(kiddos) > 2):
                                    kiddos.data = kiddos.data[3]
                    elif (TreeIn.data[1] == '^'):
                                TreeIn.data = '|'
                                TreeIn.children = list(TreeIn.children[0].children)
                                for kiddos in TreeIn.children:
                                    if (kiddos.data[0] == "~") and (kiddos.data[1] == "~") and (len(kiddos) > 2):
                                        kiddos.data = kiddos.data[3]
            else:
                if (TreeIn.children[0].data == '|'):
                        TreeIn.data = '^'
                        TreeIn.children = list(TreeIn.children[0].children)
                        for kiddos in TreeIn.children:
                            kiddos.data = "~"+kiddos.data
                            if (kiddos.data[0] == "~") and (kiddos.data[1] == "~") and (len(kiddos) > 2):
                                kiddos.data = kiddos.data[3]
                elif (TreeIn.children[0].data == '^'):
                        TreeIn.data = '|'
                        TreeIn.children = list(TreeIn.children[0].children)
                        for kiddos in TreeIn.children:
                            kiddos.data = "~"+kiddos.data
                            if (kiddos.data[0] == "~") and (kiddos.data[1] == "~") and (len(kiddos) > 2):
                                kiddos.data = kiddos.data[3]
    return TreeIn



def removeIFF(returnTree):
        nodes = returnTree
        if returnTree.data == "$":
            alpha = nodes.children[0];
            beta = nodes.children[1];
            Left = (Tree('>'))
            Left.children.append((Tree(alpha.data, list(alpha.children))))
            Left.children.append((Tree(beta.data, list(beta.children))))
            Right = (Tree('>'))
            Right.children.append((Tree(beta.data, list(beta.children))))
            Right.children.append((Tree(alpha.data, list(alpha.children))))
            returnTree.data = "^"
            returnTree.children[0] = Left
            returnTree.children[1] = Right
        return returnTree


def printTree(node, level=0):
    if (node):
        if (node.is_leaf()):
            print(' ' * 4 * level + '  ' + node.data)
        else:
            if len(node.children) == 1:
                printTree(node.children[0], level + 1)
                print(' ' * 4 * level + '  ' + node.data)
            else:
                printTree(node.children[0], level + 1)
                print(' ' * 4 * level + '  ' + node.data)
                printTree(node.children[1], level + 1)


        
def main():
    inputString = input("Input Sentence: ")
    postFix = infixToPostfix(remove(inputString))
    postFixTree = postfixToTree(postFix)
    print("------------ Initial Input ---------------")
    printTree(postFixTree[-1])
    postfixToTreeIFF = TreeTraversalIFF(postFixTree[-1])
    print("----------- Replace IFF -----------------")
    printTree(postfixToTreeIFF)
    postfixToTreeIMP = TreeTraversalIMP(postfixToTreeIFF)
    print("------------ Replace -> ----------------------")
    printTree(postfixToTreeIMP)
    postfixToTreeNEG = TreeTraversalNEG(postfixToTreeIMP)
    postfixToTreeNEG = TreeTraversalNEG(postfixToTreeIMP)
    postfixToTreeNEG = TreeTraversalNEG(postfixToTreeIMP)
    print("--------------Propagate Negation -----------------------")
    printTree(postfixToTreeNEG)
    print("---------------- Distribute OR over AND -----------------")
    postfixToTreeOR = DistributeOR(postfixToTreeIMP)
    printTree(postfixToTreeOR)
    print("Final in CNF")
if __name__ == '__main__':
    main()
                
                
            
            
        