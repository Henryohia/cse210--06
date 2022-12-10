from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.image import Image
from game.casting.body import Body
from game.casting.bullet import Bullet


class FireBulletsAction(Action):
  LEFT_BULLET_OFFSET = 5
  RIGHT_BULLET_OFFSET = 30
  BULLET_FREQUENCY = 25 #Delay between bullets in frames

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
      if frames % self.BULLET_FREQUENCY == 0: #The number of frames is a multiple of BULLET_FREQUENCY
        self._load_bullet(cast, racket, self.LEFT_BULLET_OFFSET)
        self._load_bullet(cast, racket, self.RIGHT_BULLET_OFFSET)
    except AttributeError:                           
      # Bullets Group doesn't exist...
      self._load_bullet(cast, racket, self.LEFT_BULLET_OFFSET)
      self._load_bullet(cast, racket, self.RIGHT_BULLET_OFFSET)
    except IndexError:
      # No bullets exist...
      self._load_bullet(cast, racket, self.LEFT_BULLET_OFFSET)
      self._load_bullet(cast, racket, self.RIGHT_BULLET_OFFSET)
      
  def _load_bullet(self, cast, racket, x_offset):
    """Creates a new bullet."""
    racket_body = racket.get_body()
    racket_position = racket_body.get_position()
    position = Point(racket_position.get_x() + x_offset, racket_position.get_y() + 18)
    size = Point(BULLET_WIDTH, BULLET_HEIGHT)
    image = Image(BULLET_IMAGE)
    velocity = Point(0, -BULLET_VELOCITY)
    body = Body(position, size, velocity)
    bullet = Bullet(body, image)
    cast.add_actor(BULLET_GROUP, bullet)

