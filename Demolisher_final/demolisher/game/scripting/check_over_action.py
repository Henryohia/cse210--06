from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        bricks = cast.get_actors(BRICK_GROUP)
        if len(bricks) == 0:
            try:
                stats = cast.get_first_actor(STATS_GROUP)
                stats.next_level()
                callback.on_next(NEXT_LEVEL)
            except FileNotFoundError:
                #The player has completed all the levels
                callback.on_next(VICTORY)