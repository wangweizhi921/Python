from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
 
class CustomButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
    def event(self, event):
        # 重写鼠标按下事件
        if event.type() == event.MouseButtonPress:
            if event.button() == Qt.LeftButton:
                QMessageBox.information(self, 'Clicked', 'Mouse Left Button Clicked')
                return True  # 事件处理完毕，返回True
        
        # 重写鼠标释放事件
        elif event.type() == event.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                QMessageBox.information(self, 'Released', 'Mouse Left Button Released')
                return True  # 事件处理完毕，返回True
        
        # 对其它事件调用父类的event方法进行处理
        return super().event(event)
 
 
def main():
    app = QApplication([])
    window = QWidget()
    button = CustomButton(window)
    button.setText('Click Me')
    button.resize(200, 60)
    window.show()
    app.exec_()
 
 
if __name__ == '__main__':
    main()