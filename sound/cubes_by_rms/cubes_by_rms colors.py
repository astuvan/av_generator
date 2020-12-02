import pygame
import random
import pyaudio
import audioop

class Audio:
    def __init__(self):
        # Py audio objects
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK
        )

    def getInput(self):
        input = self.stream.read(self.CHUNK)
        return(input)

class Cube:
    def __init__(self):
        self.w = 90
        self.h = 90

    def draw(self, surface, x, y, colorVal):
        pygame.draw.rect(surface, colorVal, (x, y, self.w, self.h))

if __name__ == "__main__":
    clock = pygame.time.Clock()
    
    surface = pygame.display.set_mode((1600, 900), 0, 32)
    pygame.display.set_caption("Cubes flickering")

    a = Audio()
    # RMS-VALUE -> COLOR VALUE
    ratio = 0.050806934

    cube = Cube()

    while True:
        clock.tick(100)
        surface.fill((0,0,0))

        # Audio stuff
        input = a.getInput()
        rms = audioop.rms(input, 2)
        # Avoid owerflow and 
        if rms > 4900:
            volume = 4900
        else:
            volume = rms
        colorVal = int(ratio * volume)

        # Draw blocks randomly
        block_coords = []

        block_coords.append((random.randint(0, 1610),random.randint(0, 810)))
        block_coords.append((random.randint(0, 1610),random.randint(0, 810)))
        block_coords.append((random.randint(0, 1610),random.randint(0, 810)))

        for block in block_coords:
            cube.draw(surface, block[0], block[1], (0, colorVal, 255))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()