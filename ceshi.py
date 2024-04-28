import keyboard
import time

# 定义标志变量
k_pressed = False
u_pressed = False

def on_key_event(event):
    global k_pressed, u_pressed
    if event.name == 'k':
        k_pressed = True
        print("K键被按下")
    elif event.name == 'u':
        u_pressed = True
        print("U键被按下")

# 监听键盘事件
keyboard.on_press(on_key_event)

print("按下'K'或'U'键进行测试，按下'ESC'键退出程序。")

# 循环检查按键状态
while True:
    # 检查是否同时按下了K和U键
    if k_pressed and u_pressed:
        print("K和U键已被按下")
        # 重置按键状态
        k_pressed = False
        u_pressed = False
    
    # 每0.5秒检查一次
    time.sleep(0.5)
    
    # 检查是否按下了ESC键，如果是，则退出程序
    if keyboard.is_pressed('esc'):
        print("退出程序。")
        break
    
    


