import math
import random

from pygame.math import Vector2


class Ball:
    """
    base class for bouncing objects
    """

    def __init__(self, bounds, position, velocity, color, radius):
        self.position = position
        self.velocity = velocity
        self.bounds = bounds
        self.color = color
        self.radius = radius

    def update(self):
        # bounce at edges.  TODO: Fix sticky edges
        nextX = self.position.x + self.velocity.x
        nextY = self.position.y + self.velocity.y

        if nextX < 0 + self.radius:
            nextX = self.radius
            self.velocity.x *= -1
        if nextX > self.bounds[0] - self.radius:
            nextX = self.bounds[0] - self.radius
            self.velocity.x *= -1

        if nextY < 0 + self.radius:
            nextY = self.radius
            self.velocity.y *= -1
        if nextY > self.bounds[1] - self.radius:
            nextY = self.bounds[1] - self.radius
            self.velocity.y *= -1

        # if self.position.x < 0 + self.radius or self.position.x > self.bounds[0] - self.radius: # screen width
        # if self.position.y < 0 + self.radius or self.position.y > self.bounds[1] - self.radius: # screen height

        self.position.x = nextX
        self.position.y = nextY

    def draw(self, screen, pygame):
        # cast x and y to int for drawing
        pygame.draw.circle(screen, self.color, [int(
            self.position.x), int(self.position.y)], self.radius)


class BouncingBall(Ball):
    """
    ball effected by gravity
    """
    # TODO:

    def __init__(self, bounds, position, velocity, color, radius, acceleration):
        super().__init__(bounds, position, velocity, color, radius)
        self.acceleration = acceleration
        self.frictionX = 0.01

    def update(self):
        self.velocity.y += self.acceleration

        nextX = self.position.x + self.velocity.x
        nextY = self.position.y + self.velocity.y

        # if ball at bottom
        if self.position.y == self.bounds[1] - self.radius:
            # if ball's velocity.y is near cero.
            if self.velocity.y > -1 and self.velocity.y < 10:
                # if ball's velocity.x is near cero.
                if self.velocity.x > -0.1 and self.velocity.x < 0.1:
                    # STOP movement on X axis.
                    self.velocity.x = 0
                    self.frictionX = 0
                else:
                    # STOP movement on Y axis.
                    self.acceleration = 0
                    self.velocity.y = 0
                    # APLY Friction on X axis.
                    if self.velocity.x > 0:
                        self.velocity.x -= self.frictionX
                    if self.velocity.x < 0:
                        self.velocity.x += self.frictionX
        # If ball hit Y bounds
        elif nextY < 0 + self.radius or nextY > self.bounds[1] - self.radius:
            self.acceleration += self.acceleration * 0.6
            if self.velocity.x > 0:
                self.velocity.x -= self.frictionX
            if self.velocity.x < 0:
                self.velocity.x += self.frictionX

        # print('position',self.position.x)
        # print('velocity',self.velocity.x)

        super().update()


class RainbowBall(Ball):
    """
    Ball that changes colors
    """
    # TODO:

    def update(self):
        r = (self.color[0] + random.randrange(0, 10)) % 256
        g = (self.color[1] + random.randrange(0, 10)) % 256
        b = (self.color[2] + random.randrange(0, 10)) % 256
        self.color = [r, g, b]
        super().update()


class BouncingRainbow(BouncingBall, RainbowBall):
    """
    Ball that changes color and is affected by gravity
    """
    # TODO:
    # def __init__(self, bounds, position, velocity, color, radius, acceleration):
    #     super().__init__(bounds, position, velocity, color, radius, acceleration)
    pass


class KineticBall(Ball):
    """
    A ball that collides with other collidable balls using simple elastic circle collision
    """
    # TODO:

    def collide(self, distanceToObject, sumOfRadius):
        self.velocity *= -1
        print('Collision!')

        self.update()


# class KineticBouncing(???):
#     """
#     A ball that collides with other collidable balls using simple elastic circle collision
#     And is affected by gravity
#     """


# class AllTheThings(???):
#     """
#     A ball that does everything!
#     """
