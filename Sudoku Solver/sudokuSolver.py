# Name: Mohammad Khan
# Project: Sudoku Board Solver
# Goal: To learn and emphasize the usage of the Backtracking Algorithm

# These are a few test boards that are used to see if the algorithm works

sudoTestBoardOne = [ [7,8,0,4,0,0,1,2,0],
                     [6,0,0,0,7,5,0,0,9],
                     [0,0,0,6,0,1,0,7,8],
                     [0,0,7,0,4,0,2,6,0],
                     [0,0,1,0,5,0,9,3,0],
                     [9,0,4,0,6,0,0,0,5],
                     [0,7,0,3,0,0,0,1,2],
                     [1,2,0,0,0,7,4,0,0],
                     [0,4,9,2,0,6,0,0,7] ]

sudoTestBoardTwo = [ [0,0,0,2,6,0,7,0,1],
                     [6,8,0,0,7,0,0,9,0],
                     [1,9,0,0,0,4,5,0,0],
                     [8,2,0,1,0,0,0,4,0],
                     [0,0,4,6,0,2,9,0,0],
                     [0,5,0,0,0,3,0,2,8],
                     [0,0,9,3,0,0,0,7,4],
                     [0,4,0,0,5,0,0,3,6],
                     [7,0,3,0,1,8,0,0,0] ]

sudoTestBoardThree = [ [1,0,0,4,8,9,0,0,6],
                     [7,3,0,0,0,0,0,4,0],
                     [0,0,0,0,0,1,2,9,5],
                     [0,0,7,1,2,0,6,0,0],
                     [5,0,0,7,0,3,0,0,8],
                     [0,0,6,0,9,5,7,0,0],
                     [9,1,4,6,0,0,0,0,0],
                     [0,2,0,0,0,0,0,3,7],
                     [8,0,0,5,1,2,0,0,4] ]

def solve(board):
    # Base Case
    finder = emptyFinder(board)
    if not finder:
        return True
    else:
        row, col = finder

    for i in range (1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            # Recursive Case
            if solve(board):
                return True

            board[row][col] = 0

    return False

def valid(board, num, pos):
    # Checking for the row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Checking for the column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Checking each box

    xBox = pos[1] // 3
    yBox = pos[0] // 3

    for i in range (yBox * 3, yBox * 3 + 3):
        for j in range (xBox * 3, xBox * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def displayBoard(board):
    # Displays an organized sudoku board given a 2D array


    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def emptyFinder(board):
    for i in range (len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # Returns in the format (row, col)

# Testing each of the sample boards to see if algorithm works by display how the board
# looks before the algorithm is used and after once the solve function is called

print("\nTest Board One: \n")
displayBoard(sudoTestBoardOne)
print("\nSolving Test Board One ... ")
solve(sudoTestBoardOne)
print("Solved! \n")
displayBoard(sudoTestBoardOne)

print("\nTest Board Two: \n")
displayBoard(sudoTestBoardTwo)
print("\nSolving Test Board Two ... ")
solve(sudoTestBoardTwo)
print("Solved! \n")
displayBoard(sudoTestBoardTwo)

print("\nTest Board Three: \n")
displayBoard(sudoTestBoardThree)
print("\nSolving Test Board Three ... ")
solve(sudoTestBoardThree)
print("Solved! \n")
displayBoard(sudoTestBoardThree)

