import sys

from robot_hat import TTS

tts = TTS()

text = sys.argv[1]

tts.say(text)
