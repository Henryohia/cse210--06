from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.image import Image
from game.casting.body import Body
from game.casting.bullet import Bullet


class FireBulletsAction(Action):
  BULLET_FREQUENCY = 25 #Delay between bullets in frames
  ALIEN_BULLET_FREQUENCY = 80 #Delay between bullets in frames

  def __init__(self, keyboard_service):
    self._keyboard_service = keyboard_service
      
  def execute(self, cast, script, callback):
    racket = cast.get_first_actor(RACKET_GROUP)
    bricks = cast.get_actors((BRICK_GROUP))

    self._fire_alien_bullets(cast, bricks)

    if self._keyboard_service.is_key_down(SPACE): 
      self._fire_player_bullets(cast, racket)

  def _fire_player_bullets(self, cast, object):
    """Fires bullets from the Player's current position."""
    try:
      oldest_bullet = cast.get_first_actor(BULLET_GROUP)
      frames = oldest_bullet.get_age()
      if frames % self.BULLET_FREQUENCY == 0: #Check if the number of frames is a multiple of BULLET_FREQUENCY
        self._load_bullet(cast, object, 5, BULLET_IMAGES[0], PLAYER_BULLET_VELOCITY)
        self._load_bullet(cast, object, 30, BULLET_IMAGES[0], PLAYER_BULLET_VELOCITY)
    except AttributeError:                           
      # Bullets Group doesn't exist...
      self._load_bullet(cast, object, 5, BULLET_IMAGES[0], PLAYER_BULLET_VELOCITY)
      self._load_bullet(cast, object, 30, BULLET_IMAGES[0], PLAYER_BULLET_VELOCITY)
    except IndexError:
      # No bullets exist...
      self._load_bullet(cast, object, 5, BULLET_IMAGES[0], PLAYER_BULLET_VELOCITY)
      self._load_bullet(cast, object, 30, BULLET_IMAGES[0], PLAYER_BULLET_VELOCITY)

  def _fire_alien_bullets(self, cast, bricks):
    """Fires bullets for enemies"""
    for brick in bricks:
      image = brick.get_image()
      if image.get_filename() == BRICK_IMAGES["a"]:
        try:
          oldest_bullet = cast.get_first_actor(BULLET_GROUP)
          frames = oldest_bullet.get_age()
          if frames % self.ALIEN_BULLET_FREQUENCY == 0: #Check if the number of frames is a multiple of ALIEN_BULLET_FREQUENCY
            self._load_bullet(cast, brick, 15, BULLET_IMAGES[1], ALIEN_BULLET_VELOCITY)
        except AttributeError:                           
          # Bullets Group doesn't exist...
          self._load_bullet(cast, brick, 15, BULLET_IMAGES[1], ALIEN_BULLET_VELOCITY)
        except IndexError:
          # No bullets exist...
          self._load_bullet(cast, brick, 15, BULLET_IMAGES[1], ALIEN_BULLET_VELOCITY)

      
  def _load_bullet(self, cast, object, x_offset, image, velocity):
    """Creates a new bullet."""
    object_body = object.get_body()
    object_position = object_body.get_position()
    position = Point(object_position.get_x() + x_offset, object_position.get_y())
    size = Point(BULLET_WIDTH, BULLET_HEIGHT)
    image = Image(image)
    velocity = Point(0, velocity)
    body = Body(position, size, velocity)
    bullet = Bullet(body, image)
    cast.add_actor(BULLET_GROUP, bullet)

