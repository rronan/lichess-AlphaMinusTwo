#!/usr/bin/env python3

import chess
import chess.uci


class Engine:
    def __init__(self):
        self.board = chess.Board()


def main():
    engine = chess.uci.popen_engine("/usr/games/stockfish")
    board = chess.Board()
    while not board.is_game_over():
        command = engine.go(movetime=1000, async_callback=True)
        move, _ = command.result()
        print(move)
        board.push(move)
    engine.quit()


main()
