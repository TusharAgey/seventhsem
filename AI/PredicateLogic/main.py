import nltk
from nltk.tag import pos_tag
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
    return None
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
    	op = unify(e1[i], e2[i], e1, e2)
    	if op:
        	returning.append(op)
    if -1 in returning:
        return -1
    return returning


sentence = raw_input("Enter 1st Sentence:- ") #Taking input of two statements that can be unified
sentence2 = raw_input("Enter 2nd Sentence:- ")
tagged_sent = pos_tag(sentence.split()) #create tagged statements
#print tagged_sent

tagged_sent2 = pos_tag(sentence2.split())
#print tagged_sent2
propernouns1 = [word for word,pos in tagged_sent if ((pos == 'NNP') or (pos == 'NN') or (pos == 'NNPS') or (pos == 'VBP') or (pos == 'PRP') or (pos == 'NNS'))]
propernouns2 = [word for word,pos in tagged_sent2 if ((pos == 'NNP') or (pos == 'NN') or (pos == 'NNPS') or (pos == 'VBP') or (pos == 'PRP') or(pos == 'NNS'))]
predicate1 = [word for word, pos in tagged_sent if ((pos == 'VBZ'))]
predicate2 = [word for word, pos in tagged_sent2 if ((pos == 'VBZ'))]
P1 = predicate1[0] + '('
for elem in propernouns1:
	P1 += elem + ','
P1=P1[:(len(P1) - 1)]
P1 += ')'

P2 = predicate2[0] + '('
for elem in propernouns2:
	P2 += elem + ','
P2=P2[:(len(P2) - 1)]
P2 += ')'
#print P1
#print P2
#P1 = 'loves(tushar,java)'
#P2 = 'loves(x,java)'
output = unification(P1, P2)
if output is -1:
    print "unification is not possible"
    exit(0)
print output