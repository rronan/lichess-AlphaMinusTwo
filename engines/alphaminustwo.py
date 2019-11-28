import random


class AlphaMinusTwo:
    def __init__(self, config):
        self.config = config
        self.board = None
        self.info_handlers = []
        self.name = "AlphaMinusTwo"

    def position(self, board):
        self.board = board

    def go(
        self,
        wtime=None,
        btime=None,
        winc=None,
        binc=None,
        depth=None,
        nodes=None,
        movetime=None,
    ):
        return random.choice(list(self.board.legal_moves)), None

    def stop(self):
        pass

    def quit(self):
        pass
