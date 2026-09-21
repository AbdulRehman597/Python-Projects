import random


def create_board():
    return [" " for _ in range(10)]


def printBoard(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")


def isBoardFull(board):
    return all(square != " " for square in board[1:])


def isWinner(board, letter):
    return (
        (board[1] == letter and board[2] == letter and board[3] == letter)
        or (board[4] == letter and board[5] == letter and board[6] == letter)
        or (board[7] == letter and board[8] == letter and board[9] == letter)
        or (board[1] == letter and board[4] == letter and board[7] == letter)
        or (board[2] == letter and board[5] == letter and board[8] == letter)
        or (board[3] == letter and board[6] == letter and board[9] == letter)
        or (board[1] == letter and board[5] == letter and board[9] == letter)
        or (board[3] == letter and board[5] == letter and board[7] == letter)
    )


def spaceIsFree(board, pos):
    return 1 <= pos <= 9 and board[pos] == " "


def insertLetter(board, letter, pos):
    if spaceIsFree(board, pos):
        board[pos] = letter
        return True
    return False


def selectRandom(moves):
    return random.choice(moves)


def compMove(board):
    possible_moves = [index for index, letter in enumerate(board) if letter == " " and index != 0]

    for letter in ["O", "X"]:
        for move in possible_moves:
            board_copy = board[:]
            board_copy[move] = letter
            if isWinner(board_copy, letter):
                return move

    if 5 in possible_moves:
        return 5

    corner_open = [move for move in possible_moves if move in [1, 3, 7, 9]]
    if corner_open:
        return selectRandom(corner_open)

    edge_open = [move for move in possible_moves if move in [2, 4, 6, 8]]
    if edge_open:
        return selectRandom(edge_open)

    return None


def userMove(board):
    while True:
        user_input = input("Enter a position between 1 and 9 (or Q to quit): ").strip().lower()

        if user_input in {"q", "quit", "exit"}:
            return False

        try:
            pos = int(user_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not 1 <= pos <= 9:
            print("Please enter a number between 1 and 9.")
            continue

        if not spaceIsFree(board, pos):
            print("Sorry, this space is occupied.")
            continue

        insertLetter(board, "X", pos)
        return True


def play_game():
    board = create_board()
    print("Welcome to the Tic-Tac-Toe game\n")
    printBoard(board)

    while True:
        if not userMove(board):
            print("Exiting current game.")
            return False
        printBoard(board)

        if isWinner(board, "X"):
            print("You win!")
            return True

        if isBoardFull(board):
            print("\nGame tied")
            return True

        move = compMove(board)
        if move is None:
            print("\nGame tied")
            return True

        insertLetter(board, "O", move)
        print(f"Computer placed O on position {move}")
        printBoard(board)

        if isWinner(board, "O"):
            print("Sorry, you lose!")
            return True

        if isBoardFull(board):
            print("\nGame tied")
            return True


def main():
    while True:
        choice = input("Do you want to play a game (Y/N): ").strip().lower()
        if choice == "y":
            print("-----------------------------------------")
            should_continue = play_game()
            if not should_continue:
                break
        elif choice == "n":
            print("Goodbye!")
            break
        else:
            print("Please enter Y or N.")


if __name__ == "__main__":
    main()
