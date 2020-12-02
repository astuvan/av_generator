import pygame
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

if __name__ == "__main__":
    surface = pygame.display.set_mode((1600, 900), 0, 32)
    pygame.display.set_caption("Light on sound")

    clock = pygame.time.Clock()
    a = Audio()

    # Main loop
    while True:
        clock.tick(100)
        input = a.getInput()
        rms = audioop.rms(input, 2)

        if rms > 1000:
            # Fill surface with white
            surface.fill((255, 255, 255))
        else:
            surface.fill((0, 0, 0))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()