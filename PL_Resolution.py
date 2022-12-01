
def getKB():
    KB = []
    print("Create your Knowledge base in CNF")
    print("~ is NOT")
    print("v is OR")
    print("Enter Variables as 1 alphanumeric symbol that is NOT v")
    KB_Len = input("Enter Length of KB: ")
    for i in range(0, int(KB_Len)):
        KB.append(input("Enter KB input " + str(i+1) + ": "))
    print("Done")
    return KB

def printKB_list(KB):
    for items in KB:
        for terms in items:
            if terms == items[-1]:
                if items == KB[-1]:
                    print(terms)
                else:
                    print(terms+", ", end ="")
            else:
                print(terms +"v", end ="")


# Function to Convert String Input to a list of variables 
# Example "~pvqvr" -> [~p, q, r] 
def parseKB(KB):
    KB_return = []
    for items in KB:
        Clause = []
        # Count v's
        v_count = 0
        i =0
        j =0
        for chars in items:
            if (chars == 'v') or (i == len(items)-1):
                if (i == len(items)-1):
                    if (j == 1):
                        Clause.append(items[i-1:i+1])
                        j = 0;
                    else:
                        Clause.append(items[i])
                        j = 0;
               
                else:
                    v_count+=1
                    if (j == 2):
                        Clause.append(items[(i-2):(i)])
                        j = -1;
                    else:
                        Clause.append(items[i-1])
                        j = -1;
            i+=1
            j+=1
        KB_return.append(Clause)
    return KB_return

def PLResolve(Ci, Cj):

        
        # Remove negations of itself
        index1 = -1
        index2 = 0
        flag = 0
        for i in range(0, len(Ci)):
            if (len(Cj)==0) or (len(Ci)==0):
                break
            index2 = 0
            if flag == 1:
                flag = 0
            else:
                index1 +=1
            for j in range(0, len(Cj)):
                if (("~"+Ci[index1]) == Cj[index2])or(Ci[index1] == ("~"+Cj[index2])):
                    Ci.pop(index1)
                    Cj.pop(index2)
                    if (len(Cj)==0) or (len(Ci)==0):
                        break
                    flag = 1
                    if len(Ci) == 1:
                        index1 = 0
                    else:
                        index1-=1
                else:
                    if len(Cj) == 1:
                        index2 = 0
                    else:
                        index2 +=1;
        # Remove duplicates
        index1 = -1
        flag = 0
        j = len(Ci);
        for i in range(0, j):
            if len(Ci) == 0:
                break
            if flag == 1:
                flag = 0
            else:
                if len(Ci) == 1:
                    index1 = 0
                else:
                    index1 +=1
            for j in range(0, len(Cj)):
                if Ci[index1] == Cj[j]:
                    Ci.pop(index1)
                    flag = 1;
                    if index1 == (len(Ci)):
                        index1 -=1
                    if len(Ci) == 1:
                        index1 = 0 
                    if len(Ci) == 0:
                        break
        if len(list(Cj)) > 1:
            Cj.sort()
        if len(list(Ci)) > 1:
            Ci.sort()
        
        if (Ci == []) and (Cj == []):
            return []
        elif Ci == []:
            return Cj
        elif Cj == []:
            return Ci
        else:
            Ci.append(Cj[0])
            Ci.sort()
            return Ci
        

def PLResolution(KB, alpha):
    alpha_parsed = parseKB(alpha)
    for i in range(0, len(alpha)):
        KB.append(alpha_parsed[i])
    clauses = KB
    iteration_count = 0;
    while True:
        i = 0;
        new = []
        for Ci in clauses:
            j = i;
            for index in range(j, len(clauses)):
                Cj = clauses[j]
                if (i != j):
                    resolvents = PLResolve(list(Ci), list(Cj))
                    if resolvents == []:
                        print("Reached Resolution!!")
                        return True
                    else:
                        new.append(resolvents)
                j+=1
            i+=1
        same_count = 0;
        for items in new:
            if items in clauses:
                same_count +=1
            if same_count == (len(new)):
                print("Failure")
                return False
            else:
                if items not in clauses:
                    clauses.append(items)
        iteration_count+=1
        print("Iteration " + str(iteration_count) + " Clasues = ")
        printKB_list(clauses)
                       
def main():
    ## Run this 
    # KB = getKB()
    # print("Initial Knowledge Base is:")
    #alpha = input("Enter negated alpha: ")
    KB = ["~pvq", "p"]
    KB_list = parseKB(KB)
    for items in KB_list:
        items.sort()
    printKB_list(KB_list)
    alpha = ["~q"]
    PLResolution(KB_list, alpha)
    
if __name__ == '__main__':
    main()
             