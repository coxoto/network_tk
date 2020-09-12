# from datetime import datetime

# # current date and time

# timestamp = int(datetime.timestamp(datetime.now()))
# print(int(timestamp))
from tkinter import *


def call_back(event):
    print(event.keysym)


def main():
    root = Tk()

    # 创建一个框架，在这个框架中响应事件
    frame = Frame(root,
                  width=200, height=200,
                  background='green')

    # 这样就不用查看 键盘特殊按键的keysym表了。
    # 试一下就知道了
    frame.bind("<KeyPress>", call_back)
    frame.pack()

    # 当前框架被选中，意思是键盘触发，只对这个框架有效
    frame.focus_set()

    mainloop()


if __name__ == '__main__':
    main()