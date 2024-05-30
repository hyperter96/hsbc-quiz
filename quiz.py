def reverse_list(l:list):

    """
    TODO: Reverse a list without using any built in functions
    The function should return a sorted list.

    Input l is a list which can contain any type of data.

    """
    return reverse_list(l[1:]) + l[:1] if l else l

def findNextCellToFill(matrix, i, j):
        for x in range(i,9):
                for y in range(j,9):
                        if matrix[x][y] == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if matrix[x][y] == 0:
                                return x,y
        return -1,-1

def isValid(matrix, i, j, e):
        rowOk = all([e != matrix[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != matrix[x][j] for x in range(9)])
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if matrix[x][y] == e:
                                                return False
                        return True
        return False

def solve_sudoku_helper(matrix, i,j):
    i,j = findNextCellToFill(matrix, i, j)
    if i == -1:
        return True
    for e in range(1,10):
        if isValid(matrix,i,j,e):
            matrix[i][j] = e
            if solve_sudoku_helper(matrix, i, j):
                return True
            # Undo the current cell for backtracking
            matrix[i][j] = 0
    return False
     
def solve_sudoku(matrix):

    """

    TODO: Write a programme to solve 9x9 Sudoku board.

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 matrix with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.

 
    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """
    return solve_sudoku_helper(matrix, 0, 0)
    
def test_passing():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    
    input = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
    res = solve_sudoku(input)
    assert res == True
    assert input == [[5, 1, 7, 6, 9, 8, 2, 3, 4], [2, 8, 9, 1, 3, 4, 7, 5, 6], [3, 4, 6, 2, 7, 5, 8, 9, 1], [6, 7, 2, 8, 4, 9, 3, 1, 5], [1, 3, 8, 5, 2, 6, 9, 4, 7], [9, 5, 4, 7, 1, 3, 6, 8, 2], [4, 9, 5, 3, 6, 2, 1, 7, 8], [7, 2, 3, 4, 8, 1, 5, 6, 9], [8, 6, 1, 9, 5, 7, 4, 2, 3]]

if __name__ == "__main__":
    reversed_l = reverse_list([1,2,3])
    print(reversed_l)
    input = [[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
    solve_sudoku(input)
    print(input)