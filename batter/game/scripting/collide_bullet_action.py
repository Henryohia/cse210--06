from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBulletAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        bullets = cast.get_actors(BULLET_GROUP)
        
        for bullet in bullets:
          ball_body = ball.get_body()
          bullet_body = bullet.get_body()

          if self._physics_service.has_collided(ball_body, bullet_body):
              ball.bounce_bullet()
              sound = Sound(BOUNCE_SOUND)
              self._audio_service.play_sound(sound)
              cast.remove_actor(BULLET_GROUP, bullet)