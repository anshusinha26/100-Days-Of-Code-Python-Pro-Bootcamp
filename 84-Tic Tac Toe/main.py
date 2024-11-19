# Initialize the board as a list
board = [" " for _ in range(9)]

def print_board():
    # Function to print the current board
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def check_winner(player):
    # Check all possible winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_tie():
    # Check for a tie (no empty spaces)
    return " " not in board

def tic_tac_toe():
    current_player = "X"
    while True:
        print_board()
        try:
            # Ask the player for their move
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = current_player
                # Check if the player has won
                if check_winner(current_player):
                    print_board()
                    print(f"Player {current_player} wins!")
                    break
                # Check if there's a tie
                if check_tie():
                    print_board()
                    print("It's a tie!")
                    break
                # Switch player
                current_player = "O" if current_player == "X" else "X"
            else:
                print("That spot is taken, try another one.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number from 1 to 9.")

# Run the game
tic_tac_toe()
