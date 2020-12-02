import pygame
import random

class Cube:
    def __init__(self):
        self.w = 90
        self.h = 90
        self.color = (255, 255, 255)

    def draw(self, surface, x, y):
        pygame.draw.rect(surface, self.color, (x, y, self.w, self.h))

if __name__ == "__main__":
    clock = pygame.time.Clock()
    
    surface = pygame.display.set_mode((1600, 900), 0, 32)
    pygame.display.set_caption("Cubes flickering")

    cube = Cube()

    while True:
        clock.tick(20)
        surface.fill((0,0,0))

        # Draw blocks randomly
        block_coords = []

        block_coords.append((random.randint(0, 1610),random.randint(0, 810)))
        block_coords.append((random.randint(0, 1610),random.randint(0, 810)))
        block_coords.append((random.randint(0, 1610),random.randint(0, 810)))

        for block in block_coords:
            cube.draw(surface, block[0], block[1])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()