import pygame
from .entity import Entity

class Ball(Entity):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.radius = 15
    self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)
    self.direction = pygame.Vector2(-1, 1)

    self.speed_multiplier = 1
    self.speed = 200 * self.speed_multiplier

  def draw(self, surface, color):
    pygame.draw.rect(surface, color, self.rect)

  def move(self, screen_height, screen_width, delta):
    self.x += (self.direction.x * (self.speed * self.speed_multiplier)) * delta
    if self.x < 0: # hits left wall
        self.direction.x = 1
    if self.x + self.radius > screen_width: # hits right wall
        self.direction.x = -1

    self.y += (self.direction.y * (self.speed * self.speed_multiplier)) * delta
    if self.y < 0: # hits top wall
        self.direction.y = 1
    if self.y + self.radius > screen_height: # hits bottom wall
        self.direction.y = -1

    self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)

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

  # rect getter and setter
  @property
  def rect(self):
     return self._rect
  @rect.setter
  def rect(self, newRect):
     self._rect = newRect

  # direction getter and setter
  @property
  def direction(self):
     return self._direction
  @direction.setter
  def direction(self, newDirection):
     self._direction = newDirection
