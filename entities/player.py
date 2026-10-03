import pygame
from .entity import Entity

class Player(Entity):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.width = 100 # change with power ups?
    self.height = 20 # also changes with power ups???? idk what benefit it would have doe. maybe gets skinnier to give more time
    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    # player_direction = pygame.Vector2(0, 0) # 0, 0 not moving - 1, 1 up and right, etc

    self.speed_multiplier = 1
    self.speed = 300 * self.speed_multiplier

  def draw(self, surface, color):
    pygame.draw.rect(surface, color, self.rect)

  def move(self, screen_height, screen_width, delta):
    keys = pygame.key.get_pressed()
    
    #########################################
    # probably wont use these in actual game
    if keys[pygame.K_w]:
        self.y -= self.speed * delta
        if self.y < 0: # prevent ball from going off screen
            self.y = 0
    if keys[pygame.K_s]:
        self.y += self.speed * delta
        if self.y + self.height > screen_height: # prevent ball from going off screen
            self.y = screen_height - self.height
    #########################################

    if keys[pygame.K_a]:
        self.x -= self.speed * delta
        if self.x < 0: # prevent ball from going off screen
            self.x = 0
        
    if keys[pygame.K_d]:
        self.x += self.speed * delta
        if self.x + self.width > screen_width: # prevent ball from going off screen
            self.x = screen_width - self.width

    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

  # x coordinate getter and setter
  @property
  def x(self):
    return self._x
  @x.setter
  def x(self, newX):
    self._x = newX

  # y coordinate getter and setter
  @property
  def y(self):
    return self._y
  @y.setter
  def y(self, newY):
    self._y = newY

  # rect getter
  @property
  def rect(self):
     return self._rect
  @rect.setter
  def rect(self, newRect):
     self._rect = newRect
