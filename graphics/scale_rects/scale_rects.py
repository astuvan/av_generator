import pygame
import random

class Rect:
    def __init__(self):
        self.x = random.randint(200, 1400)
        self.y = random.randint(200, 700)
        self.w = 1
        self.h = 1
        self.maxWidth = random.randint(50, 300)
        self.direction = random.randint(0, 3) # Direction to scale the rect in

        col = random.randint(0,2)
        if col == 0:
            self.color = (255,0,0)
        elif col == 1:
            self.color = (0,255,0)
        elif col == 2:
            self.color = (0,0,255)

    # Scale rect in different directions
    def southeast(self):
        self.h += 3
        self.w += 3
    def southwest(self):
        self.h += 3
        self.x -= 3
        self.w += 3
    def northwest(self):
        self.y -= 3
        self.h += 3
        self.x -= 3
        self.w += 3
    def northeast(self):
        self.x -= 3
        self.h += 3
        self.w += 3

    # Draw the new rect
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.x, self.y, self.w, self.h], 4)

if __name__ == "__main__":
    clock = pygame.time.Clock()
    
    surface = pygame.display.set_mode((1600, 900), 0, 32)
    pygame.display.set_caption("Scale rectangles")

    rects = []

    count = 0
    while True:
        clock.tick(30)
        surface.fill((0,0,0))

        # Create rects
        if count == 5:
            rect = Rect()
            rects.append(rect)

            count = 0
        else:
            count += 1

        # Scale and draw rects
        for rect in rects:
            rect.draw(surface)
            
            if rect.direction == 0:
                rect.southeast()
            if rect.direction == 1:
                rect.southwest()
            if rect.direction == 2:
                rect.northwest()
            if rect.direction == 3:
                rect.northeast()
            # Remove rect from list if it exceeds the maxwidth
            if rect.w >= rect.maxWidth:
                rects.remove(rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()