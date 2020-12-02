import pygame
import pyaudio
import audioop
from random import random


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

class Blocks:
    def __init__(self):
        self.blocks = [0, 177, 354, 531, 708, 885, 1062, 1239, 1423] # x-position for blocks
        self.size = (177, 900)

    def draw(self, surface):
        for x in range(len(self.blocks)):
            if random() > 0.5:
                pygame.draw.rect(surface, (255,255,255), (self.blocks[x], 0, 184, 900))
            else:
                pygame.draw.rect(surface, (0,0,0), (self.blocks[x], 0, 184, 900))
        
if __name__ == "__main__":
    surface = pygame.display.set_mode((1600, 900), 0, 32)
    pygame.display.set_caption("Audiovisual Generator")

    clock = pygame.time.Clock()
    a = Audio()

    # Blocks-object
    blocks = Blocks()

    # Main loop
    count = 0
    while True:
        clock.tick(100)
        input = a.getInput()
        rms = audioop.rms(input, 2)

        # If sound is above threshold, draw next frame for each 3rd count
        if rms > 1000:
            if count == 3:
                # Fill surface with white
                blocks.draw(surface)
                count = 0
            else:
                count += 1
        else:
            surface.fill((0, 0, 0))

        pygame.display.update()

        # Listen for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()