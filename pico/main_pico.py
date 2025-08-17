from machine import Pin,UART,PWM
import uselect, sys, rp2, utime, time

direction_pin = Pin(2, Pin.OUT)  
pwm_pin = Pin(3, Pin.OUT)        
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
led = Pin("LED", Pin.OUT)
counter=0
led_status=0

pwm = PWM(pwm_pin)
pwm.freq(1000)  # 1 kHz frekansta PWM
pwm.duty_u16(0)  # PWM duty cycle başlangıçta 0


def softstart(target_duty, duration,led_status):
    start_time = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start_time) < duration:
        current_duty = int((utime.ticks_diff(utime.ticks_ms(), start_time) / duration) * target_duty)
        pwm.duty_u16(current_duty)
        utime.sleep_us(100)
        led.value(not led_status)
        led_status = not led_status

def control_motor(direction, target_duty, duration,led_status):
    direction_pin.value(direction)
    sstime=200
    softstart(target_duty, sstime,led_status)  # Soft start için 200 milisaniye süre
    pwm.duty_u16(target_duty)
    utime.sleep(abs(duration-(ss/1000)))
    pwm.duty_u16(0)

def ana_dongu_keyboard():
    if uselect.select([sys.stdin], [], [], 1)[0]:
        utime.sleep_ms(250)
        data = sys.stdin.readline()
        if data!="":
            direction, duty_cycle, move_duration = map(int, data.split(","))
            duty_cycle = int(duty_cycle*65536/100)
            direction_pin.value(direction)
            move_duration=move_duration/1000
            control_motor(direction, duty_cycle, move_duration,led_status)
            if direction == 1:
                retmes=b"close\n"
            else:
                retmes=b"openn\n"
            print(retmes)

def ana_dongu():
    if uart.any()>7:
        utime.sleep_ms(250)

        data = uart.readline().decode()
        if data!=" ":
            direction, duty_cycle, move_duration = map(int, data.split(","))
            duty_cycle = int(duty_cycle*65536/100)
            direction_pin.value(direction)
            move_duration=move_duration/1000
            control_motor(direction, duty_cycle, move_duration,led_status)
            if direction == 1:
                retmes=b"close\n"
            else:
                retmes=b"open\n"
            uart.write(retmes)

while True:
    try:
        ana_dongu()
    except:
        pass
    if counter>10000:
        counter=0
        led.value(not led_status)
        led_status = not led_status
    counter+=1
    time.sleep_us(10)
