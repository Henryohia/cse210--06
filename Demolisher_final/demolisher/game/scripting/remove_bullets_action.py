from constants import *
from game.scripting.action import Action


class RemoveBulletsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        bullets = cast.get_actors(BULLET_GROUP)
        for bullet in bullets:
          body = bullet.get_body()
          position = body.get_position()
          if position.get_y() <= 0:
            cast.remove_actor(BULLET_GROUP, bullet)