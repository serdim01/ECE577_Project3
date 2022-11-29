
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

def printKB(KB):
    for items in KB:
        if items == KB[-1]:
            print(items) 
        else:
            print(items + ", ", end =" ")

def checkDuplicate(Ci, Cj, OG1, OG2):
    newClause = list([Ci, Cj]);
    newClause.sort()
    OG1.sort()
    OG2.sort()
    if ((newClause == OG1) or (newClause == OG2)):
        return False
    else:
        return True
    
def PLResolve(Ci, Cj):
        subjectsCi = []
        resolvents =[]
        if len(Ci) > 2:
            i = 0;
            for chars in Ci:
                if chars == 'v':
                    subjectsCi.append(Ci[0:i])
                    subjectsCi.append(Ci[(i+1):])
                i+=1
     
        else:
            subjectsCi.append(Ci)
        subjectsCj = []
        if len(Cj) > 2:
            i = 0;
            for chars in Cj:
                if chars == 'v':
                    subjectsCj.append(Cj[0:i])
                    subjectsCj.append(Cj[i+1:])
                i+=1     
        else:
            subjectsCj.append(Cj)
        subjectsCi_OG = list(subjectsCi)
        subjectsCj_OG = list(subjectsCj)
        
        # Remove duplicates
        index1 = -1
        flag = 0
        for i in range(0, len(subjectsCi)):
            if flag == 1:
                flag = 0
            else:
                index1 +=1;
            for j in range(0, len(subjectsCj)):
                if subjectsCi[index1] == subjectsCj[j]:
                    subjectsCi.pop(index1)
                    flag = 1;
        
        # Remove negations of itself
        index1 = -1
        index2 = 0
        flag = 0
        for i in range(0, len(subjectsCi)):
            index2 = 0
            if flag == 1:
                flag = 0
            else:
                index1 +=1
            for j in range(0, len(subjectsCj)):
                if (("~"+subjectsCi[index1]) == subjectsCj[index2])or(subjectsCi[index1] == ("~"+subjectsCj[index2])):
                    subjectsCi.pop(index1)
                    subjectsCj.pop(index2)
                    flag = 1
                    if index1 == 0:
                        index1 = 0
                    else:
                        index1-=1
                else:
                    index2 +=1;
        
        # New Things
        for i in range(0, len(subjectsCi)):
            for j in range(0, len(subjectsCj)):
                if ((subjectsCi[i]) != subjectsCj[j])and(checkDuplicate(subjectsCi[i], subjectsCj[j], subjectsCi_OG, subjectsCj_OG)):
                    resolvents.append(subjectsCi[i]+"v"+subjectsCj[j])
        if len(resolvents) > 1:
            resolvents = []
            uniqueItems = list(subjectsCj)
            uniqueItems.extend(x for x in subjectsCi if x not in uniqueItems)
            finalString = ""
            for i in range(0, len(uniqueItems)-1):
                finalString += uniqueItems[i]+"v"
            finalString+=uniqueItems[-1]
            resolvents.append(finalString)
        return resolvents

def PLResolution(KB):
    clauses =  KB
    new = []
    i = 0;
    for Ci in clauses:
        j = i;
        for index in range(j, len(clauses)):
            Cj = clauses[j]
            if (i != j):
                resolvents = PLResolve(Ci, Cj)
                if resolvents == []:
                    print("Reached Resolution!!")
                    return True
                else:
                    new.append(resolvents)
            j+=1
        i+=1
    print("No Resolution")
    for items in new:
        if items in clauses:
            blah = 1
        else:
            clauses.append(items)
    print("Final Knowledge Base is:")
    printKB(clauses)
    return False
                
                       
def main():
    # KB = getKB()
    # print("Initial Knowledge Base is:")
    # printKB(KB)
#    alpha = "~Q"
    KB = ["PvQ","~QvR", "R"]
    # KB = []
    # KB.append("~PvQ")
    # KB.append("~QvR")
    # KB.append("~QvS")
    # KB2 = KB
    PLResolution(KB)
    
if __name__ == '__main__':
    main()
             