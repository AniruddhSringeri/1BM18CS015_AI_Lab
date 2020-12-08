import re

def getAttributes(expression):
    expression = expression.split("(")[1:]
    expression = "(".join(expression)
    expression = expression[:-1]
    expression = re.split("(?<!\(.),(?!.\))", expression)
    return expression

def fetchInitialPredicate(expression):
    return expression.split("(")[0]


def isConstant(char):
    return char.isupper() and len(char) == 1

def isVariable(char):
    return char.islower() and len(char) == 1

def replaceAttributes(exp, old, new):
    attributes = getAttributes(exp)
    
    for index, val in enumerate(attributes):
        if val == old:
            attributes[index] = new
    predicate = fetchInitialPredicate(exp)
    return predicate + "(" + ",".join(attributes) + ")"

def apply(exp, substitutions):
    for substitution in substitutions:
        new, old = substitution[0],substitution[2]  # cz substitution is a tuple of 2 values (new, old)
        exp = replaceAttributes(exp, old, new)
    return exp
def checkOccurs(var, exp):
    if exp.find(var) == -1:
        return False
    return True


def fetchFirstPart(expression):
    attributes = getAttributes(expression)
    return attributes[0]


def fetchRemainingPart(expression):
    predicate = fetchInitialPredicate(expression)
    attributes = getAttributes(expression)
    newExpression = predicate + "(" + ",".join(attributes[1:]) + ")"
    return newExpression

def UNIFY(exp1, exp2):
    if exp1 == exp2:
        return []

    if isConstant(exp1) and isConstant(exp2):
        if exp1 != exp2:
            return False

    if isConstant(exp1):
        return [(exp1,'|', exp2)]

    if isConstant(exp2):
        return [(exp2,'|', exp1)]

    if isVariable(exp1):
        if checkOccurs(exp1, exp2):
            
            return False
        else:
            
            return [(exp2,'|', exp1)]

    if isVariable(exp2):
        if checkOccurs(exp2, exp1):
            return False
        else:
            return [(exp1,'|', exp2)]

    if fetchInitialPredicate(exp1) != fetchInitialPredicate(exp2):
        print("Predicates do not match. Cannot be unified")
        return False

    attributeCount1 = len(getAttributes(exp1))

    attributeCount2 = len(getAttributes(exp2))

    if attributeCount1 != attributeCount2:
        return False

    head1 = fetchFirstPart(exp1)
    #print("Head1 ",head1)
    head2 = fetchFirstPart(exp2)
    #print("Head2 ",head2)
    initialSubstitution = UNIFY(head1, head2)
    #print("initial ",initialSubstitution)
    
    if not initialSubstitution:
        return False
    if attributeCount1 == 1:
        return initialSubstitution

    tail1 = fetchRemainingPart(exp1)
    #print("tail1 ",tail1)
    tail2 = fetchRemainingPart(exp2)
    #print("tail2 ",tail2)

    if initialSubstitution != []:
        tail1 = apply(tail1, initialSubstitution)
        #print("tail11 ",tail1)
        tail2 = apply(tail2, initialSubstitution)
        #print("tail21 ",tail2)

    remainingSubstitution = UNIFY(tail1, tail2)
    if not remainingSubstitution:
        return False
    
    initialSubstitution.extend(remainingSubstitution)
    return initialSubstitution

exp1 = input("Exp1:  ")
exp2 = input("Exp2:  ")
substitutions = UNIFY(exp1, exp2)
print("Substitutions:")
print(substitutions)