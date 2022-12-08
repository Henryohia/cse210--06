from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.image import Image
from game.casting.body import Body
from game.casting.bullet import Bullet


class FireBulletsAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        if self._keyboard_service.is_key_down(SPACE): 
          self._fire_bullet(cast, racket)

    def _fire_bullet(self, cast, racket):
      """Fires a bullet from the racket's current position."""
      try:
        old_bullet = cast.get_first_actor(BULLET_GROUP)
        frames = old_bullet.get_age()
        if frames % 15 == 0:
          self._load_bullet(cast, racket, -14)
          self._load_bullet(cast, racket, 10)
      except AttributeError:                           
        # Bullets Group doesn't exist...
        self._load_bullet(cast, racket, -10)
        self._load_bullet(cast, racket, 10)
      except IndexError:
        # No bullest exist...
        self._load_bullet(cast, racket, -10)
        self._load_bullet(cast, racket, 10)
        
    def _load_bullet(self, cast, racket, x_offset):
      """Creates a new bullet."""
      racket_body = racket.get_body()
      racket_position = racket_body.get_position()
      position = Point(racket_position.get_x() + x_offset, racket_position.get_y() + 18)
      size = Point(BULLET_WIDTH, BULLET_HEIGHT)
      image = Image(BULLET_IMAGE)
      velocity = Point(0, -BULLET_VELOCITY)
      body = Body(position, size, velocity)
      bullet = Bullet(body, image, True)
      cast.add_actor(BULLET_GROUP, bullet)

