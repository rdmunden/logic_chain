# logic_chain

This is a brain teaser puzzle designed to test your knowledge of [Short-circuit evaluation](https://en.wikipedia.org/wiki/Short-circuit_evaluation) in Python.

## How to evaluate
The cycle:
1. Start with a True
    1. keep doing 'and True' to the end
    1. if you hit an 'or' before then, stop there (before the 'or', with the current True value)
    1. if you hit 'and False' look for the next 'or'
        1. if you find one, start the cycle again from there (after the 'or')
        1. if you don't then stop there (on that False value)
1. Start with a False
    1. look for the next 'or'
        1. if you find one, start the cycle again from there (after the 'or')
        1. if you don't then stop there (on that False value)

