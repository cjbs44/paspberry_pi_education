import numpy
import wave
import pygame

SAMPLERATE = 44100

def createSignal(frequency, duration):
    samples = int(duration*SAMPLERATE)
    period = SAMPLERATE / frequency
    omega = numpy.pi * 2 / period
    xaxis = numpy.arange(samples, dtype=numpy.float) * omega
    yaxis = 16384 * numpy.sin(xaxis)
    return yaxis.astype('int16').tostring()

def createWAVFile(filename, signal):
    file = wave.open(filename, 'wb')
    file.setparams((1, 2, SAMPLERATE, len(signal), 'NONE', 'noncompressed'))
    file.writeframes(signal)
    file.close()

def playWAVFile(filename):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(filename)
    sound.play()
    while pygame.mixer.get_busy():
        pass

filename = '/tmp/440hz.wav'
signal = createSignal(frequency=440, duration=4)
createWAVFile(filename, signal)
playWAVFile(filename)
