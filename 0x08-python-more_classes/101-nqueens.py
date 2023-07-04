#!/usr/bin/python3
import sys


def init_board(n):
    board = [[' '  for i in range(n)] for i in range(n)]
    return board


def get_solution(board):
    solution = []
    for r in range(len(board)):
        solution = []
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == "Q":
                    solution.append([r, c])
                    break
    return solution


def xout(board, row, col):
    n = len(board)
    directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1)
            ]
    for dx, dy in directions:
        r, c = row + dx, col + dy
        while 0 <= r < n and 0 <= c < n:
            board[r][c] = "x"
            r += dx
            c += dy


def recursive_solve(board, row, queens, solutions):
    n = len(board)
    if queens == n:
        solutions.append(get_solution(board))
        return solutions
    for c in range(n):
        if board[row][c] == " ":
            tmp_board = [row[:] for row in board]
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(
                    tmp_board, row + 1, queens + 1, solutions
                    )
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
