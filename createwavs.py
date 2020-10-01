#!/usr/bin/python3

# Script to process sound files.
from pydub import AudioSegment
import os

for file in os.listdir(os.getcwd()):
    if file.endswith(".wav") and " " in file:
        sound = AudioSegment.from_wav(file)
        sil = AudioSegment.silent(duration=2000)
        toReturn = sound + sil + sound
        toReturn.export("combine_" + file, format="wav")

#sound1 = AudioSegment.from_wav("teen.wav")
#sound2 = AudioSegment.from_wav("tin.wav")
#silence = AudioSegment.silent(duration=1000)
#long_sil = AudioSegment.silent(duration=2000)
#combined_sounds = sound1 + silence + sound2 + long_sil + sound1 + silence + sound2
#combined_sounds.export("combined_teentin.wav", format="wav")
