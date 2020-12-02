import pygame

class Line:
    def __init__(self, y):
        self.x = 0
        self.y = y
        self.w = 1600
        self.h = 30
        self.color = (255,255,255)
        self.speed = 5

    def move(self):
        self.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.w, self.h))

if __name__ == "__main__":
    clock = pygame.time.Clock()
    
    surface = pygame.display.set_mode((1600, 900), 0, 32)
    pygame.display.set_caption("Sliding lines")

    # Create the first 8 lines
    lines = []
    y = 100
    for x in range(8):
        line = Line(y)
        lines.append(line)
        y += 100

    count = 19
    while True:
        clock.tick(60)
        surface.fill((0,0,0))

        if count == 19:
            line = Line(0)
            lines.append(line)
            count = 0
        else:
            count += 1

        for line in lines:
            line.move()
            line.draw(surface)
            if line.y > 950:
                lines.remove(line)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()