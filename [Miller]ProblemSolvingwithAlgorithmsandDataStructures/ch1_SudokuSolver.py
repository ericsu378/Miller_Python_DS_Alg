__author__ = 'ESU_2'

# Problem Solving with Algorithms and Data Structures Release 3.0
# Brad Miller, David Ranum
# September 22, 2013

# 1.7 Programming Exercises

# 11. Find a Sudoku puzzle in the local newspaper. Write a program to solve the puzzle.
# Ref: http://norvig.com/sudoku.html

# Definitions:
# A Sudoku Grid consists of 81 squares
# Square Labels: | Column: 1-9  |  Row: A-I  |
# Unit: a collection of 9 squares (1 column, 1 row, or 1 box)
# Peers: Squares that share a unit

# Goal: A digit (1-9) can only appear once in each unit.

# Grid Construction:
#  A1 A2 A3| A4 A5 A6| A7 A8 A9
#  B1 B2 B3| B4 B5 B6| B7 B8 B9
#  C1 C2 C3| C4 C5 C6| C7 C8 C9
# ---------+---------+---------
#  D1 D2 D3| D4 D5 D6| D7 D8 D9
#  E1 E2 E3| E4 E5 E6| E7 E8 E9
#  F1 F2 F3| F4 F5 F6| F7 F8 F9
# ---------+---------+---------
#  G1 G2 G3| G4 G5 G6| G7 G8 G9
#  H1 H2 H3| H4 H5 H6| H7 H8 H9
#  I1 I2 I3| I4 I5 I6| I7 I8 I9

# Methodology:
# (1) If a square has only one possible value, then eliminate that value from the square's peers.
# (2) If a unit has only one possible place for a value, then put the value there.

# Methodology Part 2:
# Search for a solution
# 'Constraint Propagation' helps us reduce the number of possibilities once we try one possibility
# Algorithm:
#    First make sure we haven't already found a solution or a contradiction
#    Next, choose an unfilled square and consider all possible values
#       If search fails, go back and consider another value
#    ** Note: each new search spawns a new branch as to not pollute the master branch if failure
#    Terminology: 'recursive search' 'depth-first search'
# Two Search Decisions:
# Variable Ordering (which square do we try first): Pick the square that has the minimum number of possible values
#   ('minimum remaining values')
# Value ordering (which digit to try first): Due to 'Variable Ordering', we just go down in numeric order

# Grid Representation
# Textual representation ('0' or '.') represent unknowns
# Internal representation { square : string of all possible values }

# Input:
# grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
# search(parse_grid(grid1))



import pprint as pp

def test():
    "A set of unit tests."
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    print 'All tests pass.'

# Construct grid
def cross(A, B):
    "Cross product of elements in A and elements in B"
    return [a+b for a in A for b in B]


digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows, cols)
# All possible units (27)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123','456','789')]
            )
# {square: list of valid unit lists} --> units is a dictionary where each square maps to the list of units that contain the square
# dict((s, [...]) for s in squares) --> creates a dictionary which maps each square s to a value in list [...]
# [u for u in unitlist if s in u] --> this value is the list of units u such that the square s is a member of u
units = dict((s, [u for u in unitlist if s in u]) for s in squares)
# {square: set of all valid peers} --> peers is a dictionary where each square s maps to the set of squares formed by
# the union of the squares in the units of s, but not s itself
# set(sum(units[s],[]))-set([s])
# units[s] is 3 lists, sum() joins all elements of units[s] into one list minus set([s]) and 'set' makes it unique
# sets are unique, but you need to subtract 's'
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)

def parse_grid(grid):
    """
    Convert grid to a dict of possible values
    :param grid: user entered grid
    :return: dict { squares : possible values }
    """
    # Initialize values {'A1': '123456789, ...}
    values = dict((s, digits) for s in squares)
    for s,d in grid_values(grid).items():
        # print "s, d = | %s | %s |" % (s, d)
        if d in digits and not assign(values, s, d):
            return False # fail if we can't assign d to square s
    return values

def grid_values(grid):
    """
    Convert 'grid' into a dict of {square : char} with '0' or '.' for empties."
    :param grid: user entered grid
    :return: dict {square : char}
    """
    # Turn grid (input) into a list with sanitation (only digits, 0, or . and total length is 81)
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars)) # for each item in squares, assign respective item in chars

def assign(values, s, d):
    """
    Eliminate all the other values (except d) from values[s] and propagate.
    :param values:
    :param s:
    :param d:
    :return:
    """
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    """
    Eliminate d from values[s]; propagate when values or places <=2.
    :param values:
    :param s:
    :param d:
    :return:
    """
    if d not in values[s]:
        return values # Already eliminated
    values[s] = values[s].replace(d,'')
    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers
    if len(values[s]) == 0:
        return False # Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    ## (2) if a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]: # for each unit list that holds 's'...
        dplaces = [s for s in u if d in values[s]] # create a list with each square that has value 'd'
        if len(dplaces) == 0:
            return False # Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d):
                return False
    return values

def display(values):
    "Display these values as a 2-D grid"
    width = 1+max(len(values[s]) for s in squares) # incase solver has more than 1 possible value per square
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print ''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols)
        if r in 'CF': print line
    print

def solve(grid):
    return search(parse_grid(grid))

def search(values):
    "Use depth-first search and then propagation, try all possible values."
    if values is False:
        return False # Failed earlier
    if all(len(values[s]) ==1 for s in squares):
        return values # Sudoku is already solved
    ## Chose the unfilled square s with the fewest possibilities
    # loop through all squares, return square with smallest number of digits. n = number of digits, s = respective square
    n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    # Do Constraint Propagation with new digit in new branch
    return some(search(assign(values.copy(), s, d)) for d in values[s])

def some(seq):
    "Return some element of seq that is true."
    # seq would be false if branch failed
    for e in seq:
        if e:
            return e
    return False


def main():
    grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
    grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    # search(parse_grid(grid1))
    search(parse_grid(grid2))

if __name__ == '__main__': main()