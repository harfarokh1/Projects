def inputRetrieve(_userInput, _n, _m, _itr, _itr9):
  sudokuArray = []
  sudokuBoard = []
  while _n < len(_userInput):
    for i in range(_n, _m):
      if int(_userInput[i]) == 0:
        sudokuArray.append(-1)
      else:
        sudokuArray.append(int(_userInput[i]))
    _n += 9
    _m += 9

  while _itr < len(_userInput):
    sudokuBoard.append(sudokuArray[_itr:_itr9])
    _itr += 9
    _itr9 += 9
  
  return(sudokuBoard)


def find_next_empty(puzzle):


    for r in range(9):
        for c in range(9): 
            if puzzle[r][c] == -1:
                return r, c

    return None, None  

def is_valid(puzzle, guess, row, col):



    row_vals = puzzle[row]
    if guess in row_vals:
        return False 


    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False


    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):

    row, col = find_next_empty(puzzle)

    if row is None:  
        return True 
    

    for guess in range(1, 10): 

        if is_valid(puzzle, guess, row, col):

            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True

        puzzle[row][col] = -1
    return False

def noCommas(_list1):
  transList = ' '.join(str(e) for e in _list1)
  return(transList)

def puzzleQuad(_puzzleBoard):
  col = 0
  row = 0
  while col < 9:

    first = noCommas(_puzzleBoard[col][row:row+3])
    row += 3
    second = noCommas(_puzzleBoard[col][row:row+3])
    row += 3
    third = noCommas(_puzzleBoard[col][row:row+3])

    if row == 6:
      col += 1
      row = 0    

    print(first,"|", second, "|", third)
    
    if col%3 == 0 and col < 9:
      print("- - - + - - - + - - -")

userInput = input()
userInput = userInput.replace(" ", "")

n = 0
m = 9
itr = 0
itr9 = 9

sudokuBoard = inputRetrieve(userInput, n, m, itr, itr9)

if __name__ == '__main__':
    solve_sudoku(sudokuBoard)
    puzzleQuad(sudokuBoard)