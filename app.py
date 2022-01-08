import utilities
import truth_table
import CNF_DNF

formula_str = input('enter a propositional formula. enter help for syntax. enter exit to quit the program.\n')

while formula_str.casefold() != 'exit'.casefold():
    if formula_str.casefold() == 'help'.casefold():
        utilities.print_help()

    else:

        formula_lst = utilities.get_formula_as_list(formula_str)
        print(f'\ntruth table:\n{truth_table.truth_table(formula_str)}')
        print(f'DNF:{CNF_DNF.DNF(formula_lst)}')
        print(f'CNF:{CNF_DNF.CNF(formula_lst)}')

    utilities.variables = []
    formula_str = input('\nenter a propositional formula. enter help for syntax. enter exit to quit the program.\n')



