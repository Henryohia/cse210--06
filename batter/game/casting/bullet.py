import random
from constants import *
from game.casting.actor import Actor


class Bullet(Actor):
    """A solid object that is fired from the player ship or enemies."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new bullet.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self._age = 0

    def get_body(self):
        """Gets the bullet's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the bullet's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_older(self):
      """Updates the bullet's age."""
      self._age = self._age + 1
    
    def get_age(self):
      """Gets the bullet's age."""
      return self._age
        