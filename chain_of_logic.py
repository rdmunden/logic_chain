""" generate random strings of logic """

# The cycle:
#   1. Start with a True
#       a. keep doing 'and True' to the end
#       b. if you hit an 'or' before then, stop there (before the 'or', with the current True value)
#       c. if you hit 'and False' look for the next 'or'
#           i. if you find one, start the cycle again from there (after the 'or')
#           ii. if you don't then stop there (on that False value)
#
#   2. Start with a False
#       a. look for the next 'or'
#           i. if you find one, start the cycle again from there (after the 'or')
#           ii. if you don't then stop there (on that False value)

import random


def r2():
    return random.randint(0, 1)


def r7():
    return random.randint(0,6)


tv = true_values = ["'a'", "'b'", "'c'", "'d'", "'e'", "'f'", "'g'"]
fv = false_values = ["''", 0, (), [], {}, set(), None]
lv = logic_values = ['and', 'or']

vals = [tv, fv]

n = 5
cont = ''

while cont == '':
    expr = "{}".format(vals[r2()][r7()])

    for i in range(n):
        item = " {} {}".format(lv[r2()], vals[r2()][r7()])
        expr += item

    print('\n' + expr + '\n')
    resp = input("Enter for answer...")
    ans = eval(expr)
    if isinstance(ans, str): ans = ans or "''"
    print(f"result: {ans}")
    cont = input("\nEnter to continue... ")
