print("|||||||||||||||||||||    CL y cCL   |||||||||||||||||||||||||")

V = {0,1,2,3,4,5}
D = {0,1,2,3,4}

for X in V:
    def neg(X):
        if X == 0:
            return 5
        if X == 1:
            return 4
        if X == 2:
            return 2
        if X == 3:
            return 3
        if X == 4:
            return 1
        if X == 5:
            return 0
        

print("Negation")
for X in V:
    print(str(X) + "--->" + str(neg(X)))

for X in V:
    for Y in V:
        def then(X,Y):
            if X == 0 and Y == 0:
                return 0
            if X == 0 and Y == 1:
                return 5
            if X == 0 and Y == 2:
                return 5
            if X == 0 and Y == 3:
                return 5
            if X == 0 and Y == 4:
                return 5
            if X == 0 and Y == 5:
                return 5
            if X == 1 and Y == 0:
                return 0
            if X == 1 and Y == 1:
                return 4
            if X == 1 and Y == 2:
                return 5
            if X == 1 and Y == 3:
                return 5
            if X == 1 and Y == 4:
                return 5
            if X == 1 and Y == 5:
                return 5
            if X == 2 and Y == 0:
                return 0
            if X == 2 and Y == 1:
                return 2
            if X == 2 and Y == 2:
                return 2
            if X == 2 and Y == 3:
                return 5
            if X == 2 and Y == 4:
                return 5
            if X == 2 and Y == 5:
                return 5
            if X == 3 and Y == 0:
                return 0
            if X == 3 and Y == 1:
                return 3
            if X == 3 and Y == 2:
                return 5
            if X == 3 and Y == 3:
                return 3
            if X == 3 and Y == 4:
                return 5
            if X == 3 and Y == 5:
                return 5
            if X == 4 and Y == 0:
                return 0
            if X == 4 and Y == 1:
                return 1
            if X == 4 and Y == 2:
                return 2
            if X == 4 and Y == 3:
                return 3
            if X == 4 and Y == 4:
                return 4
            if X == 4 and Y == 5:
                return 5
            if X == 5 and Y == 0:
                return 0
            if X == 5 and Y == 1:
                return 0
            if X == 5 and Y == 2:
                return 0
            if X == 5 and Y == 3:
                return 0
            if X == 5 and Y == 4:
                return 0
            if X == 5 and Y == 5:
                return 0
            
print("Conditional CL")
for X in V:
    for Y in V:
        print("(" + str(X) + "," + str(Y) + ")" + "--->" + str(then(X,Y)))

for X in V:
    for Y in V:
        def wedge(X,Y):
            if X == 0 and Y == 0:
                return 0
            if X == 0 and Y == 1:
                return 1
            if X == 0 and Y == 2:
                return 2
            if X == 0 and Y == 3:
                return 3
            if X == 0 and Y == 4:
                return 4
            if X == 0 and Y == 5:
                return 5
            if X == 1 and Y == 0:
                return 1
            if X == 1 and Y == 1:
                return 1
            if X == 1 and Y == 2:
                return 2
            if X == 1 and Y == 3:
                return 3
            if X == 1 and Y == 4:
                return 4
            if X == 1 and Y == 5:
                return 5
            if X == 2 and Y == 0:
                return 2
            if X == 2 and Y == 1:
                return 2
            if X == 2 and Y == 2:
                return 2
            if X == 2 and Y == 3:
                return 4
            if X == 2 and Y == 4:
                return 4
            if X == 2 and Y == 5:
                return 5
            if X == 3 and Y == 0:
                return 3
            if X == 3 and Y == 1:
                return 3
            if X == 3 and Y == 2:
                return 4
            if X == 3 and Y == 3:
                return 3
            if X == 3 and Y == 4:
                return 4
            if X == 3 and Y == 5:
                return 5
            if X == 4 and Y == 0:
                return 4
            if X == 4 and Y == 1:
                return 4
            if X == 4 and Y == 2:
                return 4
            if X == 4 and Y == 3:
                return 4
            if X == 4 and Y == 4:
                return 4
            if X == 4 and Y == 5:
                return 5
            if X == 5 and Y == 0:
                return 5
            if X == 5 and Y == 1:
                return 5
            if X == 5 and Y == 2:
                return 5
            if X == 5 and Y == 3:
                return 5
            if X == 5 and Y == 4:
                return 5
            if X == 5 and Y == 5:
                return 5
            

print("Conjunction")
for X in V:
    for Y in V:
        print("(" + str(X) + "," + str(Y) + ")" + "--->" + str(wedge(X,Y)))

for X in V:
    for Y in V:
        def vee(X,Y):
            if X == 0 and Y == 0:
                return 0
            if X == 0 and Y == 1:
                return 0
            if X == 0 and Y == 2:
                return 0
            if X == 0 and Y == 3:
                return 0
            if X == 0 and Y == 4:
                return 0
            if X == 0 and Y == 5:
                return 0
            if X == 1 and Y == 0:
                return 0
            if X == 1 and Y == 1:
                return 1
            if X == 1 and Y == 2:
                return 1
            if X == 1 and Y == 3:
                return 1
            if X == 1 and Y == 4:
                return 1
            if X == 1 and Y == 5:
                return 1
            if X == 2 and Y == 0:
                return 0
            if X == 2 and Y == 1:
                return 1
            if X == 2 and Y == 2:
                return 2
            if X == 2 and Y == 3:
                return 1
            if X == 2 and Y == 4:
                return 2
            if X == 2 and Y == 5:
                return 2
            if X == 3 and Y == 0:
                return 0
            if X == 3 and Y == 1:
                return 1
            if X == 3 and Y == 2:
                return 1
            if X == 3 and Y == 3:
                return 3
            if X == 3 and Y == 4:
                return 3
            if X == 3 and Y == 5:
                return 3
            if X == 4 and Y == 0:
                return 0
            if X == 4 and Y == 1:
                return 1
            if X == 4 and Y == 2:
                return 2
            if X == 4 and Y == 3:
                return 3
            if X == 4 and Y == 4:
                return 4
            if X == 4 and Y == 5:
                return 4
            if X == 5 and Y == 0:
                return 0
            if X == 5 and Y == 1:
                return 1
            if X == 5 and Y == 2:
                return 2
            if X == 5 and Y == 3:
                return 3
            if X == 5 and Y == 4:
                return 4
            if X == 5 and Y == 5:
                return 5
            
print("Disjunction")
for X in V:
    for Y in V:
        print("(" + str(X) + "," + str(Y) + ")" + "--->" + str(vee(X,Y)))

for X in V:
    for Y in V:
        def iff(X,Y):
            return wedge(then(X,Y),then(Y,X))

print("Biconditional")
for X in V:
    for Y in V:
        print("(" + str(X) + "," + str(Y) + ")" + "--->" + str(iff(X,Y)))

for X in V:
    for Y in V:
        def circ(X,Y):
            return neg(then(X,neg(Y)))

print("Compatibility")
for X in V:
    for Y in V:
        print("(" + str(X) + "," + str(Y) + ")" + "--->" + str(circ(X,Y)))

for X in V:
    for Y in V:
        def hence(X,Y):
            if X in D and Y in D:
                return "valid"
            if X in D and Y not in D:
                return "invalid"

for X in V:
    def taut(X):
        if X not in D:
            return "invalid"
        else:
            return "valid"

print("--------------------------------------Counterexamples------------------------------------------")

print("<<<<<Axioms for R>>>>>:")
print("----Implicative fragment:")

print("Rule transitivity:")
for A in V:
    for C in V:
        for E in V:
            if str(hence(wedge(then(A,C),then(C,E)),then(A,E)))=="invalid":
                print("("+str(A) + "," + str(C) + "," + str(E) + ")")

print("Biconditional reflexivity:")
for A in V:
    if str(taut(iff(A,A)))=="invalid":
        print(str(A))

print("Biconditional symmetry RuleForm:")
for A in V:
    for C in V:
        if str(hence(iff(A,C),iff(C,A)))=="invalid":
            print("("+str(A) + "," + str(C) + ")")

print("Biconditional symmetry ArrowForm:")
for A in V:
    for C in V:
        if str(taut(then(iff(A,C),iff(C,A))))=="invalid":
            print("("+str(A) + "," + str(C) + ")")

print("Biconditional transitivity RuleForm:")
for A in V:
    for C in V:
        for E in V:
            if str(hence(wedge(iff(A,C),iff(C,E)),iff(A,E)))=="invalid":
                print("("+str(A) + "," + str(C) + "," + str(E) + ")")

print("Biconditional transitivity ArrowForm:")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(wedge(iff(A,C),iff(C,E)),iff(A,E))))=="invalid":
                print("("+str(A) + "," + str(C) + "," + str(E) + ")")

print("Rule Residuation L2R:")
for A in V:
    for C in V:
        for E in V:
            if str(hence(then(circ(A,C),E),then(A,then(C,E))))=="invalid":
                print("("+str(A) + "," + str(C) + "," + str(E) + ")")

print("Rule Residuation R2L:")
for A in V:
    for C in V:
        for E in V:
            if str(hence(then(A,then(C,E)),then(circ(A,C),E)))=="invalid":
                print("("+str(A) + "," + str(C) + "," + str(E) + ")")

print("Residuation arrow form L2R:")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(then(circ(A,C),E),then(A,then(C,E)))))=="invalid":
                print("("+str(A) + "," + str(C) + "," + str(E) + ")")
print("Residuation arrow form R2L:")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(then(A,then(C,E)),then(circ(A,C),E))))=="invalid":
                print("("+str(A) + "," + str(C) + "," + str(E) + ")")

print("Reflexivity")

for A in V:
    if str(taut(then(A,A)))=="invalid":
        print(str(A))

print("ARROW Prefixing (se puede cambiar por Suffixing)")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(then(A,C),then(then(E,A),then(E,C))))) == "invalid":
                print("("+ str(A) + "," + str(C) + "," + str(E) + ")")

print("RULE Prefixing (se puede cambiar por Suffixing)")
for A in V:
    for C in V:
        for E in V:
            if str(hence(then(A,C),then(then(E,A),then(E,C)))) == "invalid":
                print("("+ str(A) + "," + str(C) + "," + str(E) + ")")

print("ARROW Suffixing:")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(then(A,C),then(then(C,E),then(A,E))))) == "invalid":
                print("("+ str(A) + "," + str(C) + "," + str(E) + ")")

print("RULE Suffixing:")
for A in V:
    for C in V:
        for E in V:
            if str(hence(then(A,C),then(then(C,E),then(A,E)))) == "invalid":
                print("("+ str(A) + "," + str(C) + "," + str(E) + ")")
                
print("Contraction (se puede cambiar por Self Distribution)")
for A in V:
    for C in V:
        if str(taut(then(then(A,then(A,C)),then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Self Distribution:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,then(E,C)), then(then(A,E),then(A,C))))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Permutation (se puede cambiar por Assertion)")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,then(E,C)),then(E,then(A,C))))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Assertion:")
for A in V:
    for C in V:
        if str(taut(then(A,then(then(A,C),C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Modus Ponens")
for A in V:
    for C in V:
        if str(hence(wedge(A,then(A,C)),C))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("----Positive fragment:")

print("Simplification 1:")
for A in V:
    for C in V:
        if str(taut(then(wedge(A,C),A)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Simplification 2:")
for A in V:
    for C in V:
        if str(taut(then(wedge(A,C),C)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("And-Composition:")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(wedge(then(A,C),then(A,E)),then(A,wedge(C,E)))))=="invalid":
                print("(" + str(A) + "," + str(C) + "," + str(E) + ")")

print("Addition 1:")
for A in V:
    for C in V:
        if str(taut(then(A, vee(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Addition 2:")
for A in V:
    for C in V:
        if str(taut(then(C, vee(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Or-Composition:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(wedge(then(A,C), then(E,C)), then(vee(A,E), C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Distribution:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(wedge(A,vee(E,C)),vee(wedge(A,E),C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("----Negative fragment:")

print("Reductio:")
for A in V:
    if str(taut(then(then(A,neg(A)),neg(A)))) == "invalid":
        print(str(A))

print("Rule Intuitionistic Contraposition:")
for A in V:
    for C in V:
        if str(hence(then(A,neg(C)),then(C,neg(A))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Double Negation Elimination:")
for A in V:
    if str(taut(then(neg(neg(A)),A)))=="invalid":
        print(str(A))

print("Double Negation Introduction (este es innecesario para R pero Nissim lo usa)")
for A in V:
    if str(taut(then(A,neg(neg(A)))))=="invalid":
        print(str(A))

print("De Morgan Law 1:")
for A in V:
    for C in V:
        if str(taut(then(neg(wedge(A,C)),vee(neg(A),neg(C)))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("De Morgan Law 2:")
for A in V:
    for C in V:
        if str(taut(then(vee(neg(A),neg(C)),neg(wedge(A,C)))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("De Morgan Law 3:")
for A in V:
    for C in V:
        if str(taut(then(neg(vee(A,C)),wedge(neg(A),neg(C)))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("De Morgan Law 4:")
for A in V:
    for C in V:
        if str(taut(then(wedge(neg(A),neg(C)),neg(vee(A,C)))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("----Further negative theses")

print("Disjunctive Syllogism counterexamples:")

for A in V:
    for B in V:
        if str(taut(then(wedge(A,(vee(neg(A),B))), B))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Antilogism counterexamples:")

for A in V:
    for B in V:
        for C in V:
            if str(taut(then(then(wedge(A,B), C), then(wedge(A,neg(C)), neg(B))))) == "invalid":
                print("(" + str(A) + "," + str(B) + "," + str(C) + ")")

print("Rule Antilogism counterexamples:")

for A in V:
    for B in V:
        for C in V:
            if str(hence(then(wedge(A,B), C), then(wedge(A,neg(C)), neg(B)))) == "invalid":
                print("(" + str(A) + "," + str(B) + "," + str(C) + ")")

print("Rule Contraposition counterexamples:")

for A in V:
    for B in V:
        if str(hence(then(A,B), then(neg(B), neg(A)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Contraposition counterexamples:")

for A in V:
    for B in V:
        if str(taut(then(then(A,B),then(neg(B), neg(A))))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Rule Intuitionistic Contraposition counterexamples:")

for A in V:
    for B in V:
        if str(hence(then(A,neg(B)),then(B,neg(A)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Intuitionistic Contraposition counterexamples:")

for A in V:
    for B in V:
        if str(taut(then(then(A,neg(B)),then(B, neg(A))))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")



print("----Connexive theses:")


print("Aristotle's Thesis")

for A in V:
    if str(taut(neg(then(A,neg(A)))))=="invalid":
        print(str(A))

print("Aristotle variant")
for A in V:
    if str(taut(neg(then(neg(A),A))))=="invalid":
        print(str(A))

print("Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),neg(then(A,neg(C)))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Symmetry of the Conditional:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),then(C,A)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,neg(C))),then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Variant of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,neg(C)),neg(then(A,C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Variant of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,C)),then(A,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(neg(A),C),neg(then(A,C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Variant of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),neg(then(neg(A),C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,C)),then(neg(A),C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Variant of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(neg(A),C)), then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Aristotle's Second Thesis:")

for A in V:
    for C in V:
        if str(taut(neg(wedge(then(A,C),then(neg(A),C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Abelard's First Principle:")

for A in V:
    for C in V:
        if str(taut(neg(wedge(then(A,C),then(A,neg(C)))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Abelard's Second Principle:")

for A in V:
    for C in V:
        if str(taut(neg(then(A,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")


print("----Paradoxes of implication")

print("Mingle")
for A in V:
    if str(taut(then(A,then(A,A))))=="invalid":
        print(str(A))


print("Linearity counterexamples:")

for A in V:
    for B in V:
        if str(taut(vee(then(A,B),then(B,A)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Positive Paradox")
for A in V:
    for C in V:
        if str(taut(then(A,then(C,A))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Negative Paradox")
for A in V:
    for C in V:
        if str(taut(then(A,then(neg(A),C))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Paradox of Necessity")
for A in V:
    for C in V:
        if str(taut(then(A,then(C,C))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Explosion:")

for A in V:
    for C in V:
        if str(taut(then(wedge(A,neg(A)),C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Implosion:")

for A in V:
    for C in V:
        if str(taut(then(A,vee(C,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Antilogism")
for A in V:
    for E in V:
        for C in V:
            if str(hence(then(wedge(A,E),C),then(wedge(A,neg(C)),neg(E))))=="invalid":
                print("("+str(A)+","+str(E)+","+str(C)+")")

print("False Antecedent:")

for A in V:
    for C in V:
        if str(hence(neg(A),then(A,C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Counterexample:")

for A in V:
    for C in V:
        if str(hence(neg(then(A,C)),wedge(A,neg(C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("True Consequent:")

for A in V:
    for C in V:
        if str(hence(C,then(A,C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")


print("----Other principles")

print("Modus Tollens")
for A in V:
    for C in V:
        if str(hence(wedge(neg(C),then(A,C)),neg(A)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Transitivity (Conjunctive Syllogism)")

for A in V:
    for E in V:
        for C in V:
            if str(taut(then(wedge(then(A,E),then(E,C)),then(A,C))))=="invalid":
                print("("+str(A)+","+str(E)+","+str(C)+")")

print("Monotonicity:")

for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,C),then(wedge(A,E),C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Pseudo Modus Ponens:")

for A in V:
    for C in V:
        if str(taut(then(wedge(then(A,C),A), C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Factor 1 counterexamples:")

for A in V:
    for B in V:
        for C in V:
            if str(taut(then(then(A,B),then(wedge(A,C),wedge(B,C))))) == "invalid":
                print("(" + str(A) + "," + str(B) + "," + str(C) + ")")

print("Factor 2 counterexamples:")

for A in V:
    for B in V:
        for C in V:
            if str(taut(then(then(A,B),then(vee(A,C),vee(B,C))))) == "invalid":
                print("(" + str(A) + "," + str(B) + "," + str(C) + ")")

print("RM3-axiom counterexamples:")

for A in V:
    for B in V:
        if str(taut(vee(A,then(A,B)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("cRM3-axiom counterexamples:")

for A in V:
    for B in V:
        if str(taut(vee(A,neg(then(A,B))))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Assertion counterexamples:")

for A in V:
    for B in V:
        if str(taut(then(A,then(then(A,B),B)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")



print("Rule Affixing:")

for A in V:
    for G in V:
        for C in V:
            for E in V:
                if str(hence(wedge(then(A,G),then(C,E)),then(then(G,C),then(A,E)))) == "invalid":
                    print("(" + str(A) + "," + str(G) + "," + str(C) + "," + str(E) + ")")

print("Affixing:")

for A in V:
    for G in V:
        for C in V:
            for E in V:
                if str(taut(then(wedge(then(A,G),then(C,E)),then(then(G,C),then(A,E))))) == "invalid":
                    print("(" + str(A) + "," + str(G) + "," + str(C) + "," + str(E) + ")")

print("Affixing 2:")

for A in V:
    for G in V:
        for C in V:
            for E in V:
                if str(taut(then(then(A,G),then(then(C,E),then(then(G,C),then(A,E)))))) == "invalid":
                    print("(" + str(A) + "," + str(G) + "," + str(C) + "," + str(E) + ")")

print("Relativity counterexamples:")

for A in V:
    for B in V:
        if str(taut(then((then(then(A,B),B)), A))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Irreflexivity counterexamples:")

for A in V:
    if str(taut(neg(then(A,A)))) == "invalid":
        print(str(A))

print("Centering counterexamples:")

for A in V:
    if str(taut(iff(neg(then(A,A)), then(A,A)))) == "invalid":
        print(str(A))

print("Negated Conditional counterexamples")

for A in V:
    for B in V:
        if str(taut(neg(then(A,B)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")


print("----Tesis que rompen la relevancia profunda----")

print("(t9) counterexamples:")

for A in V:
    for B in V:
        if str(taut(then(then(then(A,A),B),B))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Peirce's Law counterexamples:")

for A in V:
    for B in V:
        if str(taut(then(then(then(A,B),A),A))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Pseudo-Modus Tollens counterexamples:")

for A in V:
    for B in V:
        if str(taut(then(wedge(then(A,B),neg(B)),neg(A)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Hilbert's Reductio counterexample:")

for A in V:
    for B in V:
        if str(taut(then(wedge(then(A,B),then(A,neg(B))),neg(A)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("----Disjunctive rules----")

print("Disj. Modus Ponens counterexample:")

for A in V:
    for B in V:
        for C in V:
            if str(hence(wedge(vee(C,A),vee(C,then(A,B))),vee(C,B))) == "invalid":
                print("(" + str(A) + "," + str(B) + "," + str(C) +")")

print("Disj. Aristotle counterexample:")

for A in V:
    for B in V:
        if str(hence(vee(C,A),vee(C,neg(then(A,neg(A)))))) == "invalid":
            print("(" + str(A) + "," + str(B) +")")

print("Disj. Affixing counterexample:")

for A in V:
    for B in V:
        for C in V:
            for E in V:
                for F in V:
                    if str(hence(wedge(vee(F,then(A,B)),vee(F,then(C,E))),vee(F,then(then(B,C),then(A,E))))) == "invalid":
                        print("(" + str(A) + "," + str(B) + "," + str(C) + "," + str(E) + "," + str(F) + ")")

print("-------- \circ Principles in mixed-Curry ----------")

print("Fusion of assumptions 1 counterexample:")

for A in V:
    for B in V:
        if str(taut(then(A,then(B,circ(A,B))))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Fusion of assumptions 2 counterexample:")

for A in V:
    for B in V:
        for C in V:
            if str(taut(then(then(A,then(B,C)),then(circ(A,B),C)))) == "invalid":
                print("(" + str(A) + "," + str(B) + "," + str(C) + ")")

print("-------- For combinator D --------")

print("(1):")

for A in V:
    for B in V:
        if str(taut(then(then(A,B),then(A,then(B,B))))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("(2):")

for A in V:
    for B in V:
        for C in V:
            if str(taut(then(then(A,C),then(A,then(B,C))))) == "invalid":
                print("(" + str(A) + "," + str(B) + "," + str(C) + ")")

print("(3):")

for A in V:
    for B in V:
        for C in V:
            if str(taut(then(then(C,then(B,C)),then(C,then(then(A,B),then(A,C)))))) == "invalid":
                print("(" + str(A) + "," + str(B) + "," + str(C) + ")")



print("<<<<<<<< Ahora modificamos el condicional >>>>>>>>>")

print("----------------------- cCL -------------------------")

for X in V:
    for Y in V:
        def then(X,Y):
            if X == 0 and Y == 0:
                return 0
            if X == 0 and Y == 1:
                return 5
            if X == 0 and Y == 2:
                return 5
            if X == 0 and Y == 3:
                return 5
            if X == 0 and Y == 4:
                return 5
            if X == 0 and Y == 5:
                return 5
            if X == 1 and Y == 0:
                return 0
            if X == 1 and Y == 1:
                return 4
            if X == 1 and Y == 2:
                return 5
            if X == 1 and Y == 3:
                return 5
            if X == 1 and Y == 4:
                return 5
            if X == 1 and Y == 5:
                return 5
            if X == 2 and Y == 0:
                return 0
            if X == 2 and Y == 1:
                return 2
            if X == 2 and Y == 2:
                return 2
            if X == 2 and Y == 3:
                return 5
            if X == 2 and Y == 4:
                return 5
            if X == 2 and Y == 5:
                return 5
            if X == 3 and Y == 0:
                return 0
            if X == 3 and Y == 1:
                return 3
            if X == 3 and Y == 2:
                return 5
            if X == 3 and Y == 3:
                return 3
            if X == 3 and Y == 4:
                return 5
            if X == 3 and Y == 5:
                return 5
            if X == 4 and Y == 0:
                return 0
            if X == 4 and Y == 1:
                return 1
            if X == 4 and Y == 2:
                return 2
            if X == 4 and Y == 3:
                return 3
            if X == 4 and Y == 4:
                return 4
            if X == 4 and Y == 5:
                return 5
            if X == 5 and Y == 0:
                return 3
            if X == 5 and Y == 1:
                return 3
            if X == 5 and Y == 2:
                return 3
            if X == 5 and Y == 3:
                return 3
            if X == 5 and Y == 4:
                return 3
            if X == 5 and Y == 5:
                return 3
            
print("Conditional cCL")
for X in V:
    for Y in V:
        print("(" + str(X) + "," + str(Y) + ")" + "--->" + str(then(X,Y)))

for X in V:
    for Y in V:
        def iff(X,Y):
            return wedge(then(X,Y),then(Y,X))

print("Biconditional")
for X in V:
    for Y in V:
        print("(" + str(X) + "," + str(Y) + ")" + "--->" + str(iff(X,Y)))

for X in V:
    for Y in V:
        def circ(X,Y):
            return neg(then(X,neg(Y)))

print("Compatibility")
for X in V:
    for Y in V:
        print("(" + str(X) + "," + str(Y) + ")" + "--->" + str(circ(X,Y)))

print("--------------------------------------Counterexamples------------------------------------------")

print("<<<<<Axioms for R>>>>>:")
print("----Implicative fragment:")

print("Rule transitivity:")
for A in V:
    for C in V:
        for E in V:
            if str(hence(wedge(then(A,C),then(C,E)),then(A,E)))=="invalid":
                print("("+str(A) + "," + str(C) + "," + str(E) + ")")

print("Biconditional reflexivity:")
for A in V:
    if str(taut(iff(A,A)))=="invalid":
        print(str(A))

print("Biconditional symmetry RuleForm:")
for A in V:
    for C in V:
        if str(hence(iff(A,C),iff(C,A)))=="invalid":
            print("("+str(A) + "," + str(C) + ")")

print("Biconditional symmetry ArrowForm:")
for A in V:
    for C in V:
        if str(taut(then(iff(A,C),iff(C,A))))=="invalid":
            print("("+str(A) + "," + str(C) + ")")

print("Biconditional transitivity RuleForm:")
for A in V:
    for C in V:
        for E in V:
            if str(hence(wedge(iff(A,C),iff(C,E)),iff(A,E)))=="invalid":
                print("("+str(A) + "," + str(C) + "," + str(E) + ")")

print("Biconditional transitivity ArrowForm:")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(wedge(iff(A,C),iff(C,E)),iff(A,E))))=="invalid":
                print("("+str(A) + "," + str(C) + "," + str(E) + ")")

print("Rule Residuation L2R:")
for A in V:
    for C in V:
        for E in V:
            if str(hence(then(circ(A,C),E),then(A,then(C,E))))=="invalid":
                print("("+str(A) + "," + str(C) + "," + str(E) + ")")

print("Rule Residuation R2L:")
for A in V:
    for C in V:
        for E in V:
            if str(hence(then(A,then(C,E)),then(circ(A,C),E)))=="invalid":
                print("("+str(A) + "," + str(C) + "," + str(E) + ")")

print("Residuation arrow form L2R:")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(then(circ(A,C),E),then(A,then(C,E)))))=="invalid":
                print("("+str(A) + "," + str(C) + "," + str(E) + ")")
print("Residuation arrow form R2L:")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(then(A,then(C,E)),then(circ(A,C),E))))=="invalid":
                print("("+str(A) + "," + str(C) + "," + str(E) + ")")

print("Reflexivity")

for A in V:
    if str(taut(then(A,A)))=="invalid":
        print(str(A))

print("ARROW Prefixing (se puede cambiar por Suffixing)")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(then(A,C),then(then(E,A),then(E,C))))) == "invalid":
                print("("+ str(A) + "," + str(C) + "," + str(E) + ")")

print("RULE Prefixing (se puede cambiar por Suffixing)")
for A in V:
    for C in V:
        for E in V:
            if str(hence(then(A,C),then(then(E,A),then(E,C)))) == "invalid":
                print("("+ str(A) + "," + str(C) + "," + str(E) + ")")

print("ARROW Suffixing:")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(then(A,C),then(then(C,E),then(A,E))))) == "invalid":
                print("("+ str(A) + "," + str(C) + "," + str(E) + ")")

print("RULE Suffixing:")
for A in V:
    for C in V:
        for E in V:
            if str(hence(then(A,C),then(then(C,E),then(A,E)))) == "invalid":
                print("("+ str(A) + "," + str(C) + "," + str(E) + ")")
                
print("Contraction (se puede cambiar por Self Distribution)")
for A in V:
    for C in V:
        if str(taut(then(then(A,then(A,C)),then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Self Distribution:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,then(E,C)), then(then(A,E),then(A,C))))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Permutation (se puede cambiar por Assertion)")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,then(E,C)),then(E,then(A,C))))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Assertion:")
for A in V:
    for C in V:
        if str(taut(then(A,then(then(A,C),C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Modus Ponens")
for A in V:
    for C in V:
        if str(hence(wedge(A,then(A,C)),C))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("----Positive fragment:")

print("Simplification 1:")
for A in V:
    for C in V:
        if str(taut(then(wedge(A,C),A)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Simplification 2:")
for A in V:
    for C in V:
        if str(taut(then(wedge(A,C),C)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("And-Composition:")
for A in V:
    for C in V:
        for E in V:
            if str(taut(then(wedge(then(A,C),then(A,E)),then(A,wedge(C,E)))))=="invalid":
                print("(" + str(A) + "," + str(C) + "," + str(E) + ")")

print("Addition 1:")
for A in V:
    for C in V:
        if str(taut(then(A, vee(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Addition 2:")
for A in V:
    for C in V:
        if str(taut(then(C, vee(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Or-Composition:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(wedge(then(A,C), then(E,C)), then(vee(A,E), C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Distribution:")
for A in V:
    for E in V:
        for C in V:
            if str(taut(then(wedge(A,vee(E,C)),vee(wedge(A,E),C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("----Negative fragment:")

print("Reductio:")
for A in V:
    if str(taut(then(then(A,neg(A)),neg(A)))) == "invalid":
        print(str(A))

print("Rule Intuitionistic Contraposition:")
for A in V:
    for C in V:
        if str(hence(then(A,neg(C)),then(C,neg(A))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Double Negation Elimination:")
for A in V:
    if str(taut(then(neg(neg(A)),A)))=="invalid":
        print(str(A))

print("Double Negation Introduction (este es innecesario para R pero Nissim lo usa)")
for A in V:
    if str(taut(then(A,neg(neg(A)))))=="invalid":
        print(str(A))

print("De Morgan Law 1:")
for A in V:
    for C in V:
        if str(taut(then(neg(wedge(A,C)),vee(neg(A),neg(C)))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("De Morgan Law 2:")
for A in V:
    for C in V:
        if str(taut(then(vee(neg(A),neg(C)),neg(wedge(A,C)))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("De Morgan Law 3:")
for A in V:
    for C in V:
        if str(taut(then(neg(vee(A,C)),wedge(neg(A),neg(C)))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("De Morgan Law 4:")
for A in V:
    for C in V:
        if str(taut(then(wedge(neg(A),neg(C)),neg(vee(A,C)))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("----Further negative theses")

print("Disjunctive Syllogism counterexamples:")

for A in V:
    for B in V:
        if str(taut(then(wedge(A,(vee(neg(A),B))), B))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Antilogism counterexamples:")

for A in V:
    for B in V:
        for C in V:
            if str(taut(then(then(wedge(A,B), C), then(wedge(A,neg(C)), neg(B))))) == "invalid":
                print("(" + str(A) + "," + str(B) + "," + str(C) + ")")

print("Rule Antilogism counterexamples:")

for A in V:
    for B in V:
        for C in V:
            if str(hence(then(wedge(A,B), C), then(wedge(A,neg(C)), neg(B)))) == "invalid":
                print("(" + str(A) + "," + str(B) + "," + str(C) + ")")

print("Rule Contraposition counterexamples:")

for A in V:
    for B in V:
        if str(hence(then(A,B), then(neg(B), neg(A)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Contraposition counterexamples:")

for A in V:
    for B in V:
        if str(taut(then(then(A,B),then(neg(B), neg(A))))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Rule Intuitionistic Contraposition counterexamples:")

for A in V:
    for B in V:
        if str(hence(then(A,neg(B)),then(B,neg(A)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Intuitionistic Contraposition counterexamples:")

for A in V:
    for B in V:
        if str(taut(then(then(A,neg(B)),then(B, neg(A))))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")



print("----Connexive theses:")


print("Aristotle's Thesis")

for A in V:
    if str(taut(neg(then(A,neg(A)))))=="invalid":
        print(str(A))

print("Aristotle variant")
for A in V:
    if str(taut(neg(then(neg(A),A))))=="invalid":
        print(str(A))

print("Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),neg(then(A,neg(C)))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Symmetry of the Conditional:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),then(C,A)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,neg(C))),then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Variant of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,neg(C)),neg(then(A,C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Variant of Boethius' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,C)),then(A,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(neg(A),C),neg(then(A,C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Variant of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(then(A,C),neg(then(neg(A),C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(A,C)),then(neg(A),C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Converse of Variant of Francez' Thesis:")

for A in V:
    for C in V:
        if str(taut(then(neg(then(neg(A),C)), then(A,C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Aristotle's Second Thesis:")

for A in V:
    for C in V:
        if str(taut(neg(wedge(then(A,C),then(neg(A),C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Abelard's First Principle:")

for A in V:
    for C in V:
        if str(taut(neg(wedge(then(A,C),then(A,neg(C)))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Abelard's Second Principle:")

for A in V:
    for C in V:
        if str(taut(neg(then(A,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")


print("----Paradoxes of implication")

print("Mingle")
for A in V:
    if str(taut(then(A,then(A,A))))=="invalid":
        print(str(A))


print("Linearity counterexamples:")

for A in V:
    for B in V:
        if str(taut(vee(then(A,B),then(B,A)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Positive Paradox")
for A in V:
    for C in V:
        if str(taut(then(A,then(C,A))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Negative Paradox")
for A in V:
    for C in V:
        if str(taut(then(A,then(neg(A),C))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Paradox of Necessity")
for A in V:
    for C in V:
        if str(taut(then(A,then(C,C))))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Explosion:")

for A in V:
    for C in V:
        if str(taut(then(wedge(A,neg(A)),C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Implosion:")

for A in V:
    for C in V:
        if str(taut(then(A,vee(C,neg(C))))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Rule Antilogism")
for A in V:
    for E in V:
        for C in V:
            if str(hence(then(wedge(A,E),C),then(wedge(A,neg(C)),neg(E))))=="invalid":
                print("("+str(A)+","+str(E)+","+str(C)+")")

print("Rule False Antecedent:")

for A in V:
    for C in V:
        if str(hence(neg(A),then(A,C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Rule Counterexample:")

for A in V:
    for C in V:
        if str(hence(neg(then(A,C)),wedge(A,neg(C)))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Rule True Consequent:")

for A in V:
    for C in V:
        if str(hence(C,then(A,C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")


print("----Other principles")

print("Modus Tollens")
for A in V:
    for C in V:
        if str(hence(wedge(neg(C),then(A,C)),neg(A)))=="invalid":
            print("("+str(A)+","+str(C)+")")

print("Transitivity (Conjunctive Syllogism)")

for A in V:
    for E in V:
        for C in V:
            if str(taut(then(wedge(then(A,E),then(E,C)),then(A,C))))=="invalid":
                print("("+str(A)+","+str(E)+","+str(C)+")")

print("Monotonicity:")

for A in V:
    for E in V:
        for C in V:
            if str(taut(then(then(A,C),then(wedge(A,E),C)))) == "invalid":
                print("(" + str(A) + "," + str(E) + "," + str(C) + ")")

print("Pseudo Modus Ponens:")

for A in V:
    for C in V:
        if str(taut(then(wedge(then(A,C),A), C))) == "invalid":
            print("(" + str(A) + "," + str(C) + ")")

print("Factor 1 counterexamples:")

for A in V:
    for B in V:
        for C in V:
            if str(taut(then(then(A,B),then(wedge(A,C),wedge(B,C))))) == "invalid":
                print("(" + str(A) + "," + str(B) + "," + str(C) + ")")

print("Factor 2 counterexamples:")

for A in V:
    for B in V:
        for C in V:
            if str(taut(then(then(A,B),then(vee(A,C),vee(B,C))))) == "invalid":
                print("(" + str(A) + "," + str(B) + "," + str(C) + ")")

print("RM3-axiom counterexamples:")

for A in V:
    for B in V:
        if str(taut(vee(A,then(A,B)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("cRM3-axiom counterexamples:")

for A in V:
    for B in V:
        if str(taut(vee(A,neg(then(A,B))))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Assertion counterexamples:")

for A in V:
    for B in V:
        if str(taut(then(A,then(then(A,B),B)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")



print("Rule Affixing:")

for A in V:
    for G in V:
        for C in V:
            for E in V:
                if str(hence(wedge(then(A,G),then(C,E)),then(then(G,C),then(A,E)))) == "invalid":
                    print("(" + str(A) + "," + str(G) + "," + str(C) + "," + str(E) + ")")

print("Affixing:")

for A in V:
    for G in V:
        for C in V:
            for E in V:
                if str(taut(then(wedge(then(A,G),then(C,E)),then(then(G,C),then(A,E))))) == "invalid":
                    print("(" + str(A) + "," + str(G) + "," + str(C) + "," + str(E) + ")")

print("Affixing 2:")

for A in V:
    for G in V:
        for C in V:
            for E in V:
                if str(taut(then(then(A,G),then(then(C,E),then(then(G,C),then(A,E)))))) == "invalid":
                    print("(" + str(A) + "," + str(G) + "," + str(C) + "," + str(E) + ")")

print("Relativity counterexamples:")

for A in V:
    for B in V:
        if str(taut(then((then(then(A,B),B)), A))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Irreflexivity counterexamples:")

for A in V:
    if str(taut(neg(then(A,A)))) == "invalid":
        print(str(A))

print("Centering counterexamples:")

for A in V:
    if str(taut(iff(neg(then(A,A)), then(A,A)))) == "invalid":
        print(str(A))

print("Negated Conditional counterexamples")

for A in V:
    for B in V:
        if str(taut(neg(then(A,B)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("----Tesis que rompen la relevancia profunda----")

print("(t9) counterexamples:")

for A in V:
    for B in V:
        if str(taut(then(then(then(A,A),B),B))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Peirce's Law counterexamples:")

for A in V:
    for B in V:
        if str(taut(then(then(then(A,B),A),A))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Pseudo-Modus Tollens counterexamples:")

for A in V:
    for B in V:
        if str(taut(then(wedge(then(A,B),neg(B)),neg(A)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Hilbert's Reductio counterexample:")

for A in V:
    for B in V:
        if str(taut(then(wedge(then(A,B),then(A,neg(B))),neg(A)))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("----Disjunctive rules----")

print("Disj. Modus Ponens counterexample:")

for A in V:
    for B in V:
        for C in V:
            if str(hence(wedge(vee(C,A),vee(C,then(A,B))),vee(C,B))) == "invalid":
                print("(" + str(A) + "," + str(B) + "," + str(C) +")")

print("Disj. Aristotle counterexample:")

for A in V:
    for B in V:
        if str(hence(vee(C,A),vee(C,neg(then(A,neg(A)))))) == "invalid":
            print("(" + str(A) + "," + str(B) +")")

print("Disj. Affixing counterexample:")

for A in V:
    for B in V:
        for C in V:
            for E in V:
                for F in V:
                    if str(hence(wedge(vee(F,then(A,B)),vee(F,then(C,E))),vee(F,then(then(B,C),then(A,E))))) == "invalid":
                        print("(" + str(A) + "," + str(B) + "," + str(C) + "," + str(E) + "," + str(F) + ")")

print("-------- \circ Principles in mixed-Curry ----------")

print("Fusion of assumptions 1 counterexample:")

for A in V:
    for B in V:
        if str(taut(then(A,then(B,circ(A,B))))) == "invalid":
            print("(" + str(A) + "," + str(B) + ")")

print("Fusion of assumptions 2 counterexample:")

for A in V:
    for B in V:
        for C in V:
            if str(taut(then(then(A,then(B,C)),then(circ(A,B),C)))) == "invalid":
                print("(" + str(A) + "," + str(B) + "," + str(C) + ")")
