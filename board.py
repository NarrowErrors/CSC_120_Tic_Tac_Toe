list1 = ['-', '-', '-']
list2 = ['-', '-', '-']
list3 = ['-', '-', '-']
board = [list1, list2, list3]

def main():
  print_board()
  check_mark(row, col)
  place_mark(row, col, player_id)
  check_win(player_id)



def print_board():
  for x in range(0, len(board)):
      print(board[x])

def check_mark(row, col):
  if board[row][col] == '-':
    return True
  else:
    return False

def place_mark(row, col, player_id): 
  if player_id == 1:
    board[row][col] = 'X'
  if player_id == 2:
    board[row][col] = 'O'

def check_win(player_id):
  if player_id == 1:
    for x in range(0, len(board)):
      if board[x] == ['X', 'X', 'X']:
        return True
      else:
        for x in range(0, len(list1)):
          if list1[x] == 'X' and list2[x] == 'X' and list3[x] == 'X':
            return True
          else: 
            if list1[0] == 'X' and list2[1] == 'X' and list3[2] == 'X':
              return True
            elif list1[2] == 'X' and list2[1] == 'X' and list3[0] == 'X':
              return True
            else: 
              return False 

  if player_id == 2:
    for x in range(0, len(board)):
      if board[x] == ['O', 'O', 'O']:
        return True
      else:
        for x in range(0, len(list1)):
          if list1[x] == 'O' and list2[x] == 'O' and list3[x] == 'O':
            return True
          else: 
            if list1[0] == 'O' and list2[1] == 'O' and list3[2] == 'O':
              return True
            elif list1[2] == 'O' and list2[1] == 'O' and list3[0] == 'O':
              return True
            else: 
              return False 

main()
