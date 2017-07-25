# Author 'Arash'
# Python verion 2.7
from __future__ import division

def knapsack(load, containers):
    """
    Finding a set containers from container list to fullfill requested load

    `containers` is a a tuple or list of numbers separated by comma.
    This varibale filled by getting values from input command.
    'load' is just a number
    Return would be a list of numbers in container that are
    either equal or with minimum of extra space to fill the requestedload.

    >>> containers = (2, 3, 5)
    >>> load = 6
    >>> knapsack(load, containers)
    [3, 3]
    >>> load = 11
    >>> knapsack(load, containers)
    [5, 3, 3]
    """
    solutions = {};
    _min_result =None
    sums = [];
    sorted_containers = sorted(containers, reverse=True)


    for wei in sorted_containers:
        for w in sorted_containers:
            new_sums = [];  # Use a separate array because sums is modified in the loop.
            for s in sums:
                new_sum = w + s;
                # if new_sum > load: continue;
                if not solutions.get(new_sum, None):
                    solutions.update({new_sum: solutions.get(s) + [w]});
                    new_sums = new_sums + [new_sum];

            sums = sums + new_sums;

            if not solutions.get(w, None):
                solutions.update({w:[w]});
                sums = sums + [w];

    result = None
    for solution in solutions:
        filling_degree = ((sum(solutions[solution]) / load))
        if filling_degree == 1.0:
            return solutions[solution]
        elif filling_degree > 1.0:
            if not _min_result or filling_degree < _min_result:
                _min_result = filling_degree
                result = solutions[solution]
    return  sorted(result, reverse=True)

def app():
    print ('========== Lets Begin =============')
    while True:
        while True:
            try:
                containers = input("containers : ")
                break
            except Exception:
                print ("Please enter numbers separated with coma (,) for containers ")

        while True:
            try:
                load = input("load : ")
                break
            except Exception:
                print ("Please enter a number for load")
        print ("load: {}  ==> {}".format(load, knapsack(load, containers)))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    app()
