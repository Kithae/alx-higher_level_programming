#!/usr/bin/python3
"""Solving a puzzle - the N-queens """

import sys


def board_start(n):
    """starts chessboard of size `n`x`n` with zeros."""
    puzzle_board = []
    [puzzle_board.append([]) for a in range(n)]
    [row.append(' ') for a in range(n) for row in puzzle_board]
    return (puzzle_board)


def board_deepcopy(puzzle_board):
    """Return chessboard deepcopy."""
    if isinstance(puzzle_board, list):
        return list(map(board_deepcopy, puzzle_board))
    return (puzzle_board)


def get_solution(puzzle_board):
    """Returns a solved chessboard lists representation."""
    solution = []
    for b in range(len(puzzle_board)):
        for c in range(len(puzzle_board)):
            if puzzle_board[b][c] == "Q":
                solution.append([b, c])
                break
    return (solution)


def xout(puzzle_board, row, col):
    """crosses out non-attacking queens spots on the chessboard.
    Args:
        puzzle_board (list): current chessboard.
        row (int): Last played queen row.
        col (int): Last played queen column.
    """
    # crosses out forward spots
    for c in range(col + 1, len(puzzle_board)):
        puzzle_board[row][c] = "x"
    # crosses out backwards spots
    for c in range(col - 1, -1, -1):
        puzzle_board[row][c] = "x"
    # cross out spots below
    for r in range(row + 1, len(puzzle_board)):
        puzzle_board[r][col] = "x"
    # cross out spots above
    for r in range(row - 1, -1, -1):
        puzzle_board[r][col] = "x"
    # cross out diagonal spots
    c = col + 1
    for r in range(row + 1, len(puzzle_board)):
        if c >= len(puzzle_board):
            break
        puzzle_board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        puzzle_board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(puzzle_board):
            break
        puzzle_board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for b in range(row + 1, len(puzzle_board)):
        if c < 0:
            break
        puzzle_board[b][c] = "x"
        c -= 1


def recursive_solve(puzzle_board, row, queens, solutions):
    """ solves the N-queens puzzle recursively
    Args:
        puzzle_board (list): The chessboard.
        row (int): current row.
        queens (int): current total placed queens.
        solutions (list): solutions list.
    Returns:
        The solutions
    """
    if queens == len(puzzle_board):
        solutions.append(get_solution(puzzle_board))
        return (solutions)

    for c in range(len(puzzle_board)):
        if puzzle_board[row][c] == " ":
            tmp_board = board_deepcopy(puzzle_board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    puzzle_board = board_start(int(sys.argv[1]))
    solutions = recursive_solve(puzzle_board, 0, 0, [])
    for ans in solutions:
        print(ans)
