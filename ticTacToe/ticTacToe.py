# --------- Global Variables -----------

# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None

# Tells us who the current player is (C:Computer, H:Human)
current_player = "C"

#Tells us what symbol the current player must put on the board(X or O)
current_symbol = "X"



# ------------- Functions ---------------

# Play a game of tic tac toe
def play_game():
  global current_player
  
  print("Start first:1  Play second:2")
  choice = input()
  
  if choice == '1':
    current_player = "H"
  else:
    current_player = "C"

  # Show the initial game board
  display_board()

  # Loop until the game stops (winner or tie)
  while game_still_going:

    # Handle a turn
    handle_turn(current_player, current_symbol)

    # Check if the game is over
    check_if_game_over()

    # Flip to the other player
    flip_player()
  
  
  # Since the game is over, print the winner or tie
  
  #choice = 2 implies computer played first. winner = X implies the one who played first
  #won. So computer won. Similarly if O won and human played first(choice = 1, human had X) then
  #also conputer is the winner
  if winner == "X" and choice == '2' or winner =="O" and choice == '1':
    print("Computer won, lol noob.")

  elif winner == None:
    print("Tie.")
  #If computer didn't win and it is not a tie then human won
  else:
    print("You won(I lost intentionally)")


# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player, symbol):
  #If it is computer's turn
  if(player == "C"):
    w = stop_win()
    if w!= None:
      board[w] = symbol
      display_board()
      return
    
    w = win_is_present()
    if w != None:
      board[w] = symbol
    else:
      for i in range(9):
        if board[i] == "-":
          board[i] = symbol
          break
  #If it is player's turn 
  else:  


    # Get position from player
    print("Your turn.")
    position = input("Choose a position from 1-9: ")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

      # Make sure the input is valid
      while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Choose a position from 1-9: ")
  
      # Get correct index in our board list
      position = int(position) - 1

      # Then also make sure the spot is available on the board
      if board[position] == "-":
        valid = True
      else:
        print("You can't go there. Go again.")

    # Put the game piece on the board
    board[position] = symbol

    # Show the game board
  display_board()


# Check if the game is over
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# Check to see if somebody has won
def check_for_winner():
  # Set global variables
  global winner
  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check the rows for a win
def check_rows():
  # Set global variables
  global game_still_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Or return None if there was no winner
  else:
    return None


# Check the columns for a win
def check_columns():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # Or return None if there was no winner
  else:
    return None


# Check if there is a tie
def check_for_tie():
  # Set global variables
  global game_still_going
  # If board is full
  if "-" not in board:
    game_still_going = False
    return True
  # Else there is no tie
  else:
    return False


# Flip the current player from C to H, or H to C and do the same for current symbol
def flip_player():
  # Global variables we need
  global current_player
  global current_symbol
  # If the current player was C, make it H
  if current_player == "C":
    current_player = "H"
  # Or if the current player was H, make it C
  elif current_player == "H":
    current_player = "C"
  #Same for current symbol
  if current_symbol == "X":
    current_symbol = "O"
  elif current_symbol == "O":
    current_symbol = "X"

#Check if you can win by marking the symbol in the right place and return the
#index of that place if present, else return none
def win_is_present():
  for i in range(9):
    if board[i] == '-':
      board[i] = current_symbol
      check_if_game_over()
      board[i] = '-'
      if not game_still_going:
        return i

#Check if the opponent(Human) can win during his next turn. Returns the index where the
#computer must put it's symbol to stop the human from winning in his next turn
def stop_win():
  flip_player()
  global game_still_going
  for i in range(9):
    if board[i] == "-":
      board[i] = current_symbol
      w = check_if_game_over()
      board[i] = "-"
      if not game_still_going:
        flip_player()
        w = check_if_game_over()
        game_still_going = True
        return i
  flip_player()
  w = check_if_game_over()

      





# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()