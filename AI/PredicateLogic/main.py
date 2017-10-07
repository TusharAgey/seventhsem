def unify(E1, E2, listE1, listE2): #E1 and E2 are respective elements in predicate logic. listE1 and listE2 are lists of elements in respective predicate logics
    if(len(E1) == 1 and len(E2) == 1): #if both E1 and E2 are constants
        if E1 is E2:
            return {}
        else:
            return -1;
    elif len(E1) == 1 and len(E2) is not 1: #if E1 is a variable:
        if E1 in listE2: #if E1 in E2 then return FAIL
            return -1
        else:
            return [E2+'/'+E1]
    elif len(E2) == 1 and len(E1) is not 1: # E2 is a variable
        if E2 in listE1: #if E2 occurs in E1 then FAIL
            return -1
        else:
            return [E2+'/'+E1]
    elif len(E2) == 0 or len(E1) == 0 : #either E1 or E2 are empty then return FAIL
        return -1
#print unify('x', 'john', ['marry', 'x'], ['marry', 'john'])

def unification(P1, P2):
    predicate1 = P1.split('(')[0]
    predicate2 = P2.split('(')[0]
    if predicate1 != predicate2:
        return -1
    returning = []
    e1 = P1.split('(')[1].split(')')[:1][0].split(',')
    e2 = P2.split('(')[1].split(')')[:1][0].split(',')
    i = 0
    if len(e1) != len(e2):
        return -1
    for i in range(len(e1)):
        returning.append(unify(e1[i], e2[i], e1, e2))
    if -1 in returning:
        return -1
    return returning
P1 = 'loves(tushar,java)'
P2 = 'loves(x,java)'
output = unification(P1, P2)
if output is -1:
    print "unification is not possible"
    exit(0)
print output