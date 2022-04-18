list1 = ['-', '-', '-']
list2 = ['-', '-', '-']
list3 = ['-', '-', '-']
board = [list1, list2, list3]

def main():

  #Initializing row, col, player_id
  row = int(0)
  col = int(0)
  player_id = int(1)
  cont = 'n'

  while cont == 'n':
    print_board()
  #Ask row and col
    row = int(input('Player ' + str(player_id) +', pick a row.'))
    row -= 1
    col = int(input('Player ' + str(player_id) +', pick a column.'))
    col -= 1

  #Validating input
    while row not in range(0, 3) or col not in range(0, 3):
      print("Error: Can't find row or col")
      row = int(input('Player ' + str(player_id) +', pick a row.'))
      row -= 1
      col = int(input('Player ' + str(player_id) +', pick a column.'))
      col -= 1
  #Check to see if space is taken
    space_available = check_mark(row, col)

  #If space is taken
    while space_available == False:
      print("Space has been taken. Please choose another space.")
      row = int(input('Player ' + str(player_id) +', pick a row.'))
      row -= 1
      col = int(input('Player ' + str(player_id) +', pick a column.'))
      col -= 1
      space_available = check_mark(row, col)

  #Place mark and see if player won
    place_mark(row, col, player_id)
    winner = check_win(player_id)
    if winner == True:
      cont = 'Y'
    elif player_id == 1:
      player_id = 2
    elif player_id == 2:
      player_id = 1

  print_board()
  print('Winner: Player ' + str(player_id))



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
    for x in range(0, 3):
        if list1[x] == 'X' and list2[x] == 'X' and list3[x] == 'X':
          return True
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
    for x in range(0, 3):
        if list1[x] == 'O' and list2[x] == 'O' and list3[x] == 'O':
          return True
    if list1[0] == 'O' and list2[1] == 'O' and list3[2] == 'O':
        return True
    elif list1[2] == 'O' and list2[1] == 'O' and list3[0] == 'O':
        return True
    else:
        return False

main()
