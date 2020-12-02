import pygame
import random

class Circle:
    def __init__(self):
        self.x = random.randint(100, 1500)
        self.y = random.randint(100, 800)
        self.max_rad = random.randint(20, 100)
        self.rad = 1
        self.rising = True
        self.color = (255, 255, 255)

    def scale(self):
        if self.rising == True:
            self.rad += 3
            
            if self.rad >= self.max_rad:
                self.rising = False

        else:
            self.rad -= 3

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.rad)

if __name__ == "__main__":
    clock = pygame.time.Clock()
    
    surface = pygame.display.set_mode((1600, 900), 0, 32)
    pygame.display.set_caption("Circles resizing")

    circles = []

    while True:
        clock.tick(30)
        surface.fill((0,0,0))

        numCircles = 0
        for circle in circles:
            numCircles += 1

        max_allowed_circles = 10 # Max number of allowed blockes on screen at the same time
        chanceForAppearance = 1 - (numCircles / max_allowed_circles)

        if random.random() < chanceForAppearance:
            circle = Circle()
            circles.append(circle)

        for circle in circles:
            circle.scale()
            circle.draw(surface)
            if circle.rad <= 0:
                circles.remove(circle)


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()