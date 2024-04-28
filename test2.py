\
import threading
from pynput import keyboard,mouse

class Hook:
    Thread_List = []
    
    def __init__(self, HookType):
        if((1 & HookType) != 0):
           Keyboard_Thread = threading.Thread(target = self.Start_Keyboard_Lsisten)
           Keyboard_Thread.start()
           self.Thread_List.append(Keyboard_Thread)
        if((2 & HookType) != 0):
            Mouse_Thread = threading.Thread(target = self.Start_Mouse_Listen)
            Mouse_Thread.start()
            self.Thread_List.append(Mouse_Thread)
        for i in range(len(self.Thread_List)):
            self.Thread_List[i].join()


    def Start_Mouse_Listen(self):
        with mouse.Listener(on_move=self.mouse_on_move, on_click=self.mouse_on_click, on_scroll=self.mouse_on_scroll) as MouseListener:
            MouseListener.join()

    def Start_Keyboard_Lsisten(self):
        with keyboard.Listener(on_press=self.keyboard_on_press, on_release=self.keyboard_on_release) as KeyboardListener:
            KeyboardListener.join()

    def keyboard_on_press(self, key): # 键盘按下时的操作
        try:
            print('{0} press'.format(key.char))
        except AttributeError:
            if key == keyboard.Key.esc:
                return False
            print(key)

    def keyboard_on_release(self, key):# 键盘弹起时的操作
        try:
            print('{0} release'.format(key.char))
        except AttributeError:
            print(key)

    def mouse_on_move(self, x, y): # 鼠标移动时的操作
        print('Pointer moved to {0}'.format((x, y)))

    def mouse_on_click(self, x, y, button, pressed): # 鼠标点击时的操作
        # if(button == mouse.Button.middle):
        print(button)
        print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))

    def mouse_on_scroll(self, x, y, dx, dy): # 鼠标滚轮时的操作
        print('Scrolled {0}'.format((dx, dy)))

if __name__ == '__main__':
    Hooks = Hook(3)# 1键盘钩子 2鼠标钩子 3=1+2