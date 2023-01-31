import time

from robot_hat import Motor

motor1 = 0
motor2 = 1

speed = 10

motor = Motor()
motor = motor.wheel(speed, motor1)
motor = Motor()
motor = motor.wheel(-speed, motor2)

time.sleep(0.25)

speed = 0

motor = Motor()
motor = motor.wheel(speed, motor1)
motor = Motor()
motor = motor.wheel(speed, motor2)
