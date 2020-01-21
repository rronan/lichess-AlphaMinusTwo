import random

from engines.alphaminustwo import AlphaMinusTwo


class Random(AlphaMinusTwo):
    def __init__(self, config):
        super().__init__(config)

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
