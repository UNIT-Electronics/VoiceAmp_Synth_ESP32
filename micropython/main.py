from machine import DAC, Pin, SPI
import os
from dualmcu import sdcard
import time

spi = SPI(2, baudrate=1000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
cs = Pin(5, Pin.OUT)
sd = sdcard.SDCard(spi, cs)
os.mount(sd, '/sd')

print("Archivos en la SD:")
print(os.listdir('/sd'))

def play_wav(filename, volume=1.0):
    dac = DAC(Pin(25))
    try:
        with open(filename, 'rb') as f:
            f.seek(44)  # Saltar el encabezado WAV
            while True:
                data = f.read(1024)
                if not data:
                    break
                for byte in data:
                    adjusted_value = int(min(max(byte * volume, 0), 255))
                    dac.write(adjusted_value)
                    time.sleep_us(125)
    except OSError as e:
        print("Error al abrir el archivo:", e)

play_wav('/sd/output_8bit_mono.wav', volume=0.9)

