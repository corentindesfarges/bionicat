from robot_hat import Pin
from robot_hat import Ultrasonic
from robot_hat import Music

from time import sleep

m = Music()

song = "audio/sonar.mp3"

trig = Pin("D2")
echo = Pin("D3")
ultrasonic = Ultrasonic(trig, echo)

while True:
    distance = ultrasonic.read()
    if distance > 100:
        continue
    delay = distance / 100
    print(str(distance) + " cm")

    m.sound_play(song)
    m.music_set_volume(10)
    if delay < 0.1:
        delay = 0.1
    sleep(delay)
