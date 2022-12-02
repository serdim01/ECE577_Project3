import itertools


def Diff(li1, li2):
    """Returns only the difference between two lists and removes the dublicates"""
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif


def PlRes(clause0, KB0, worklist0):
    """Calculates the resolution of given knowledgebase (KB) Returns KB and worklist."""
    for iter in range(0, len(clause0)):
        # Removing dublicates from KB
        KB0.sort()
        KB0 = list(k for k, _ in itertools.groupby(KB0))
        # Removing dublicates from worklist
        worklist0.sort()
        worklist0 = list(k for k, _ in itertools.groupby(worklist0))
        if clause0[iter] == "-" + clause0[iter + index1] or "-" + clause0[iter] == clause0[iter + index1]:
            temp = [clause0[iter]] + [clause0[iter + index1]]
            noclubs = Diff(clause0, temp)
            KB0 = [noclubs] + KB0
            worklist0 = worklist0 + [noclubs]
            # if noclubs==[] or worklist0==[]:
            #     break
    return KB0, worklist0


KB = [['p'], ['-p'], ['-q']] # Resovable
# KB = [['-p', 'r'], ['-q', 'r'], ['p', 'q'], ['-r']] # Resovable
# KB = [['-p', 'q'], ['p'], ['-q']] # Resovable
# KB = [['P', 'Q'], ['-Q', 'R'], ['-P', 'S'], ['-S'], ['-R']] # Resovable
# KB = [['p', 'q'], ['-q', '-s']] # Not Resovable

worklist = KB[::-1]  # reverse order

iscontinued = True
while iscontinued:
    for m in worklist:
        worklist.pop(0)
        for n in KB:
            new_list = m + n
            clause = [*set(new_list)]  # remove the duplicate items from  the list
            index1 = -1
            KB, worklist = PlRes(clause, KB, worklist)
        if [] in KB:
            print(f'knowledgebase: {KB}')
            print(f'worklist: {worklist}')
            print("SUCCESS!")
            iscontinued = False
            break
        elif not worklist:
            print(f'knowledgebase: {KB}')
            print(f'worklist: {worklist}')
            print("FAILURE!")
            iscontinued = False
            break