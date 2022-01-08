# CNF---DNF
 
welcome!
    this is a simple program which converts any propositional formula to its' disjunctive and conjunctive normal forms. 
    the program also prints the formula's truth table. a couple of notes on syntax:
    
    the program is case sensitive, be careful!
    list of allowed connectives:
        ['and', 'or', 'then', 'not', 'iff', 'NOR', 'NAND', 'XOR']
    formulas and connectives should be separated with commas. variables do not need parentheses around them. examples:
        p, then, (q, then, (not, p)) is a valid formula, whereas 
        p, then, (q, then, not, p) & p, then, (q, then, not p) are not.
        A, XOR, (b, NAND, (not, a)) is a valid formula. 
