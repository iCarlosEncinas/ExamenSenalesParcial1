import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

#4
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)

#8
frecuencia852 = SinSignal(freq=852, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)

#5
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)

#3
frecuencia697 = SinSignal(freq=697, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)

#WAVES
#4
wave_770 = frecuencia770.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_1209 = frecuencia1209.make_wave(duration=0.5, start=0.5, framerate=44100)

#8
wave_852 = frecuencia852.make_wave(duration=0.5, start=1, framerate=44100)
wave_1336 = frecuencia1336.make_wave(duration=0.5, start=1, framerate=44100)

#5
wave_770 = frecuencia770.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_1336 = frecuencia1336.make_wave(duration=0.5, start=1.5, framerate=44100)

#3
wave_697 = frecuencia697.make_wave(duration=0.5, start=2, framerate=44100)
wave_1477 = frecuencia1477.make_wave(duration=0.5, start=2, framerate=44100)

#4 #8 #5 #3
wave_sonido = (wave_770 + wave_1209) + (wave_852 + wave_1336) + (wave_770 + wave_1336) + (wave_697 + wave_1477)


#Sé que repetí frecuencias pero quería hacerlo bien organizado jaja

wave_sonido.write("output.wav")
