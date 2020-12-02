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
    pygame.display.set_caption("Light on rms")

    clock = pygame.time.Clock()
    a = Audio()

    # RMS-VALUE -> COLOR VALUE
    ratio = 0.050806934

    # Main loop
    while True:
        clock.tick(100)
        input = a.getInput()

        rms = audioop.rms(input, 2)
        # Avoid owerflow and 
        if rms > 4900:
            volume = 4900
        else:
            volume = rms

        colorVal = int(ratio * volume)

        surface.fill((int(colorVal), int(colorVal), int(colorVal)))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()