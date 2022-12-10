from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBulletAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        racket = cast.get_first_actor(RACKET_GROUP)
        bullets = cast.get_actors(BULLET_GROUP)
        
        for bullet in bullets:
            racket_body = racket.get_body()
            ball_body = ball.get_body()
            bullet_body = bullet.get_body()
            image = bullet.get_image()

            if self._physics_service.has_collided(ball_body, bullet_body):
                if image.get_filename() == BULLET_IMAGES[1]:
                    pass
                else:
                    ball.bounce_bullet()
                    sound = Sound(BOUNCE_SOUND)
                    self._audio_service.play_sound(sound)
                    cast.remove_actor(BULLET_GROUP, bullet)

            if self._physics_service.has_collided(racket_body, bullet_body):
                if image.get_filename() == BULLET_IMAGES[1]:
                    over_sound = Sound(OVER_SOUND)
                    stats = cast.get_first_actor(STATS_GROUP)
                    stats.lose_life()

                    if stats.get_lives() > 0:
                        callback.on_next(TRY_AGAIN) 
                    else:
                        callback.on_next(GAME_OVER)
                        self._audio_service.play_sound(over_sound)