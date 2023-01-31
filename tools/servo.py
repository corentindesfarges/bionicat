import sys

from robot_hat import Servo, PWM

selectedPin = sys.argv[1]
angle = int(sys.argv[2])

pin = PWM(selectedPin)
miniServo = Servo(pin)

miniServo.angle(angle)
