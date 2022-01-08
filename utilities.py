import re
import ast

variables = []
connectives = ['not', 'and', 'or', 'then', 'iff', 'NOR', 'NAND', 'XOR']


def get_formula_as_list(formula_str):

    formula_str = re.compile(r'(\w+)').sub(r"'\1'", formula_str)
    formula_list = ast.literal_eval('[' + formula_str.replace('(', '[').replace(')', ']') + ']')
    while len(formula_list) == 1 and isinstance(formula_list[0], list):
        formula_list = formula_list[0]

    get_list_of_variables(formula_list)
    return formula_list


def get_list_of_variables(formula):
    if not isinstance(formula, list):
        if not formula in connectives and not formula in variables:
            variables.append(formula)
        return

    get_list_of_variables(formula[0])

    if len(formula) > 1:

        get_list_of_variables(formula[1])

        if len(formula) == 3:
            get_list_of_variables(formula[2])


def get_indexed_formula(formula):
    indexed_formula = formula

    for variable in variables:
        indexed_formula = str(indexed_formula). \
            replace("\'" + variable + "\'", str(variables.index(variable)))

    return ast.literal_eval(indexed_formula)


def valuation(formula, truth_bits):
    formula = get_indexed_formula(formula)

    if isinstance(formula, int):
        return truth_bits[formula]

    elif len(formula) == 1:
        return str(int(valuation(formula[0], truth_bits)))

    elif len(formula) == 2:
            if formula[0] == 'not':
                return str((int(valuation(formula[1], truth_bits)) + 1) % 2)

    elif len(formula) == 3:
        a = valuation(formula[0], truth_bits)
        connective = formula[1]
        b = valuation(formula[2], truth_bits)

        if connective == 'and':
            if a == '1' and b == '1':
                return '1'
            return '0'

        elif connective == 'or':
            if a == '0' and b == '0':
                return '0'
            return '1'

        elif connective == 'then':
            if a == '1' and b == '0':
                return '0'
            return '1'

        elif connective == 'iff':
            if a == b:
                return '1'
            return '0'

        elif connective == 'NOR':
            if a == '0' and b == '0':
                return '1'
            return '0'

        elif connective == 'NAND':
            if a == '1' and b == '1':
                return '0'
            return '1'

        elif connective == 'XOR':
            if a == b:
                return '0'
            return '1'

    else:
        print("error: invalid input.")


def get_trues(formula):
    trues = []

    for i in range(0, pow(2, len(variables))):
        truth_bit = format(i, '#0' + str((len(variables) + 2)) + 'b')[2:]
        if valuation(formula, truth_bit) == '1':
            trues.append(truth_bit)

    return trues


def is_tautology(formula):
    trues = get_trues(formula)
    if len(trues) == pow(2, len(variables)):
        return True
    return False


def print_help():
    print('''
    welcome!
    this is a simple program which converts any propositional formula to its' disjunctive and conjunctive normal forms. 
    the program also prints the formula's truth table. a couple of notes on syntax:
    
    -the program is case sensitive, be careful!
    -list of allowed connectives:
        ['and', 'or', 'then', 'not', 'iff', 'NOR', 'NAND', 'XOR']
    -formulas and connectives should be separated with commas. variables do not need parentheses around them. examples:
        p, then, (q, then, (not, p)) is a valid formula, whereas 
        p, then, (q, then, not, p) & p, then, (q, then, not p) are not.
        A, XOR, (b, NAND, (not, a)) is a valid formula.            
         ''')
