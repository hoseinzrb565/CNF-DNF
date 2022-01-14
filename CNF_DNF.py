import re
import utilities

def DNF(formula_lst):

    trues = utilities.get_trues(formula_lst)

    dnf = ''

    if len(trues) == 0:
        dnf = '(' + utilities.variables[0] + ') and (not ' + utilities.variables[0] + ')'

        for i in range(1, len(utilities.variables)):
            dnf += ' and (' + utilities.variables[i] + ')'

    else:

        for bit in trues:
            dnf += '('

            for j in range(0, len(utilities.variables)):
                if bit[j] == '0':
                    dnf += 'not '
                dnf +=   utilities.variables[j]
                dnf += ' and '
            dnf = dnf[:-5]
            dnf += ') or '

        dnf = dnf[:-4]

    return dnf


def CNF(formula_lst):

    not_formula = []
    not_formula.append('not')
    not_formula.append(formula_lst)
    dnf = DNF(not_formula)


    pattern = re.compile(r'(\s\w[\s)])')
    cnf = pattern.sub(r' not\1', dnf)

    pattern = re.compile(r'\((\w\s)')
    cnf = pattern.sub(r'(not \1', cnf)

    pattern = re.compile(r'\((\w)\)')
    cnf = pattern.sub(r'(not \1)', cnf)

    pattern = re.compile(r'not not ')
    cnf = pattern.sub(r'', cnf)

    pattern = re.compile(r'or')
    cnf = pattern.sub(r'&', cnf)

    pattern = re.compile(r'and')
    cnf = pattern.sub(r'or', cnf)

    pattern = re.compile(r'&')
    cnf = pattern.sub(r'and', cnf)

    return cnf

