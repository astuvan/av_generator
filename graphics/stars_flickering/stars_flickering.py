import pygame
import random

class Circle:
    def __init__(self, x, y, existence):
        self.x = x
        self.y = y
        self.rad = random.randint(1, 4)
        self.existence = existence
        self.color = (255, 255, 255)
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.rad)
        self.existence -= 1
        return(self.existence)

# Object containing a line of circles
class Circles:
    def __init__(self):
        # Create circles spawning diagonally downwards on screen
        self.circles = []
        x = random.randint(0, 1400)
        y = random.randint(0, 700)
        existence = 1
        for a in range(20):
            circle = Circle(x, y, existence)
            x += 10
            y += 10
            existence += 1
            self.circles.append(circle)
    def popCircle(self):
        for circle in self.circles:
            circle.draw(surface)
            if circle.existence == 0:
                self.circles.remove(circle)


if __name__ == "__main__":
    surface = pygame.display.set_mode((1600, 900), 0, 32)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Stars flickering")

    circlesList = [] # List of lines with circles
    count = 0

    # Create som circles to begin with
    for x in range(20):
        circles = Circles()
        circlesList.append(circles)

    while True:
        clock.tick(30)

        surface.fill((0,0,0))

        if count == 1:
            circles = Circles()
            circlesList.append(circles)
            circles = Circles()
            circlesList.append(circles)
            circles = Circles()
            circlesList.append(circles)
            circles = Circles()
            circlesList.append(circles)
            circles = Circles()
            circlesList.append(circles)
            count = 0
        else:
            count += 1
        
        for circles in circlesList:
            circles.popCircle()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()