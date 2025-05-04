from machine import Pin, PWM, time_pulse_us
import time

trigger = Pin(19, Pin.OUT)
echo = Pin(18, Pin.IN)
servo = PWM(Pin(21))
servo.freq(50)

SERVO_OPEN = 0
SERVO_CLOSED = 150

def measure_distance():
    trigger.low()
    time.sleep(0.1)
    trigger.high()
    time.sleep_us(10)
    trigger.low()
    
    pulse_time = time_pulse_us(echo, 1)
    
    distance_cm = (pulse_time * 0.0343) / 2
    return distance_cm

def move_servo(position):
    duty = int(1638 + (position / 180) * 8192)
    servo.duty_u16(duty)

while True:
    dist = measure_distance()
    print("Distance:", dist, "cm")
    if dist < 5:
        move_servo(SERVO_CLOSED)
        time.sleep(5)
        move_servo(SERVO_OPEN)
    else:
        move_servo(SERVO_OPEN)
    time.sleep(0.01)
        