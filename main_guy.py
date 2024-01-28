import tkinter as tk
from step_motor_control import setup,step_motor, cleanup, start_switch_thread

def forward():
    step_motor("forward", 2)

def backward():
    step_motor("backward", 1)

# Tkinter GUI 설정
root = tk.Tk()
root.title("Step Motor Control")

# Forward 버튼
btn_forward = tk.Button(root, text="Forward", command=forward)
btn_forward.pack(pady=10)

# Backward 버튼
btn_backward = tk.Button(root, text="Backward", command=backward)
btn_backward.pack(pady=10)

# 메인 루프 실행 전 GPIO 설정
setup()
start_switch_thread()
# 메인 루프 실행
try:
    root.mainloop()
finally:
    cleanup()

