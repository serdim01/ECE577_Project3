
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
                    PostFixTree[-1].children.append(Tree(right))
                    PostFixTree[-1].children.append(Tree(left))
            else:
                if chars == '~':
                    PostFixTree.append(Tree(chars)) 
                    PostFixTree[-1].children.append(PostFixTree[-2])
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
                    PostFixTree[-1].children.append(Tree(right))
                    PostFixTree[-1].children.append(Tree(left))
        
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
            current = current.children[1]
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
    print("---------------------------------")
    printTree(TreeItem, level=0)
    while True:
        if current.is_leaf() is not True:
            # Appending with reference?
            stack.append(current)
            current = current.children[0]
            current = removeIMP(current)
        elif(stack):
            current = stack.pop()
            current = current.children[1]
            current = removeIMP(current)
        else:
            break
    return TreeItem

def removeIMP(TreeIn):
    if TreeIn.data == '>':
        TreeIn.data = "|"
        alpha = TreeIn.children[0].data
        TreeIn.children[0].data = "~"+alpha
    return TreeIn

def removeIFF(returnTree):
        nodes = returnTree
        if returnTree.data == "$":
            alpha = nodes.children[0];
            beta = nodes.children[1];
            Left = (Tree('>'))
            Left.children.append((alpha))
            Left.children.append((beta))
            Right = (Tree('>'))
            Right.children.append((beta))
            Right.children.append((alpha))
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
    #inputString = input("Input Sentence: ")
    postFix = infixToPostfix(remove("~(~A>B)"))
    postFixTree = postfixToTree(postFix)
    printTree(postFixTree[-1])
    # postfixToTreeIFF = TreeTraversalIFF(postFixTree[-1])
    postfixToTreeIMP = TreeTraversalIMP(postFixTree[-1])
    printTree(postfixToTreeIMP)
    
if __name__ == '__main__':
    main()
                
                
            
            
        