# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:44:18 2021

@author: aklett
"""

from math import floor
from time import time

start = time()

def checkRowColumnGroup(n, row, column, puzzle):
    '''
    Checks a cell to see if a number n appears in either the same row, column,
    or group

    Parameters
    ----------
    n : INT
        Number to check
    row : INT
        Index of row being checked
    column : INT
        Index of column being checked
    puzzle : LIST
        The sudoku puzzle being solved, which is a list of lists containing
        the rows of the puzzle

    Returns
    -------
    BOOLEAN
        A logical AND of a check of the rows, groups, and columns. If the
        number n was not found, then the function will return True

    '''
    if puzzle[row][column] != 0:
        return False
    else:
        checkRow = not n in puzzle[row]
        checkColumn = not(n in [puzzle[i][column] for i in range(9)])

        rows = [[0,1,2],[3,4,5],[6,7,8]][floor(row/3)]
        columns = [[0,1,2],[3,4,5],[6,7,8]][floor(column/3)]
        checkGroup = not(n in [puzzle[r][c] for r in rows for c in columns])

    return checkRow and checkColumn and checkGroup

def calcPossibleValues(puzzle):
    '''
    Calculates a list of possible values that each "cell" could be

    Parameters
    ----------
    puzzle : LIST
        The sudoku puzzle being solved, which is a list of lists containing
        the rows of the puzzle

    Returns
    -------
    possible_values : LIST
        A list of lists for each "cell" in the puzzle that contains all
        values that could be in that spot given the current state of the 
        puzzle

    '''
    possible_values = [[],[],[],[],[],[],[],[],[]]
    for row in range(9):
        for column in range(9):
            myList = []
            for i in range(1,10):
                if checkRowColumnGroup(i, row, column, puzzle):
                    myList.append(i)
            possible_values[row].append(myList)
    return possible_values

def iteration(puzzle, possibilities):
    '''
    A single iteration step that goes through the list of possible values
    and updates the puzzle with values from lists that only contain one
    element

    Parameters
    ----------
    puzzle : LIST
        The sudoku puzzle being solved, which is a list of lists containing
        the rows of the puzzle
    possibilities : LIST
        A list of lists for each "cell" in the puzzle that contains all
        values that could be in that spot given the current state of the 
        puzzle

    Returns
    -------
    puzzle : LIST
        An updated version of the puzzle after the iteration

    '''
    for row in range(9):
        for column in range(9):
            if len(possibilities[row][column]) == 1:
                puzzle[row][column] = possibilities[row][column][0]
    return puzzle

sudoku = [[8,1,0,0,3,0,0,2,7],
          [0,6,2,0,5,0,0,9,0],
          [0,7,0,0,0,0,0,0,0],
          [0,9,0,6,0,0,1,0,0],
          [1,0,0,0,2,0,0,0,4],
          [0,0,8,0,0,5,0,7,0],
          [0,0,0,0,0,0,0,8,0],
          [0,2,0,0,1,0,7,5,0],
          [3,8,0,0,7,0,0,4,2]]

# Iterate to solve puzzle
while any([0 in row for row in sudoku]):
    sudoku = iteration(sudoku, calcPossibleValues(sudoku))

# Print out execution time and finished puzzle
print('Finished in {0:2.1f} ms'.format((time()-start)*1000))
for i,row in enumerate(sudoku):
    print(sudoku[i])
