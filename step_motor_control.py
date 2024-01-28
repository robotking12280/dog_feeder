import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)

# GPIO 핀 설정
ENA = 13
IN1 = 6
IN2 = 5
ENB = 16
IN3 = 21
IN4 = 20
ENC_A = 24  # 엔코더 A 채널
ENC_B = 23  # 엔코더 B 채널
BUTTON_PIN = 25  # 버튼이 연결된 GPIO 핀
BUTTON_PIN_2 = 26  # 두 번째 버튼이 연결된 GPIO 핀



def setup():
    # GPIO 핀 초기화
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(ENB, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)
    GPIO.setup(ENC_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ENC_B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(ENB, GPIO.HIGH)

  # GPIO 설정 및 초기화 코드
    # ...

def cleanup():
    GPIO.cleanup()

def check_switches():
    while True:
        if not GPIO.input(BUTTON_PIN):
            step_motor("forward", 2)
            time.sleep(0.5)  # 디바운싱 대기 시간
        elif not GPIO.input(BUTTON_PIN_2):
            step_motor("backward", 1)
            time.sleep(0.5)  # 디바운싱 대기 시간
        time.sleep(0.1)  # 루프 지연 시간

def start_switch_thread():
    thread = threading.Thread(target=check_switches)
    thread.start()

def step_motor(direction, target_revolutions):
    global encoder_counter
    encoder_counter = 0
    target_counts = target_revolutions * 20

    while encoder_counter < target_counts:
        # 모터 회전 코드
        # ...
        seq = [
            [1,0,1,0], [1,0,0,1], [0,1,0,1], [0,1,1,0]
        ] if direction == "forward" else [
            [0,1,1,0], [0,1,0,1], [1,0,0,1], [1,0,1,0]
        ]

        for halfstep in range(4):
            GPIO.output(IN1, seq[halfstep][0])
            GPIO.output(IN2, seq[halfstep][1])
            GPIO.output(IN3, seq[halfstep][2])
            GPIO.output(IN4, seq[halfstep][3])
            time.sleep(0.001)
            print("Encoder count: ", encoder_counter)  # 엔코더 카운트 출력
        GPIO.output([IN1, IN2, IN3, IN4], GPIO.LOW)
        encoder_counter = encoder_counter + 1
