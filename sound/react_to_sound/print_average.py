import pyaudio
import struct
import pygame

if __name__ == "__main__":
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024 * 2

    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        output=True,
        frames_per_buffer=CHUNK
    )

    data = stream.read(CHUNK)
    data_int = struct.unpack(str(2 * CHUNK) + 'B', data)

    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        total_value = 0
        for byte in data_int:
            total_value += byte
        average = total_value / len(data_int)
        print(f"Total value: {total_value}    Average: {average}")
        print(average)