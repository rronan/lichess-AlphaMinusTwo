import backoff
import chess
import chess.uci

import engines


@backoff.on_exception(backoff.expo, BaseException, max_time=120)
def create_engine(config, board):
    return EngineWrapper(config, board)


class EngineWrapper:
    def __init__(self, config, board):
        self.engine = getattr(engines, config["engine"]["name"])(config)
        self.engine.position(board)
        info_handler = chess.uci.InfoHandler()
        self.engine.info_handlers.append(info_handler)
        self.go_commands = {}

    def set_time_control(self, game):
        pass

    def name(self):
        return self.engine.name

    def first_search(self, board, movetime):
        self.engine.position(board)
        best_move, _ = self.engine.go(movetime=movetime)
        return best_move

    def search(self, board, wtime, btime, winc, binc):
        self.engine.position(board)
        cmds = self.go_commands
        best_move, _ = self.engine.go(
            wtime=wtime,
            btime=btime,
            winc=winc,
            binc=binc,
            depth=cmds.get("depth"),
            nodes=cmds.get("nodes"),
            movetime=cmds.get("movetime"),
        )
        return best_move

    def stop(self):
        self.engine.stop()

    def print_stats(self):
        self.print_handler_stats(
            self.engine.info_handlers[0].info,
            ["string", "depth", "nps", "nodes", "score"],
        )

    def get_stats(self):
        return self.get_handler_stats(
            self.engine.info_handlers[0].info, ["depth", "nps", "nodes", "score"]
        )

    def print_handler_stats(self, info, stats):
        for stat in stats:
            if stat in info:
                print("    {}: {}".format(stat, info[stat]))

    def get_handler_stats(self, info, stats):
        stats_str = []
        for stat in stats:
            if stat in info:
                stats_str.append("{}: {}".format(stat, info[stat]))

        return stats_str

    def quit(self):
        self.engine.quit()
