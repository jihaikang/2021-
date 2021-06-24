import win32gui
import win32con
import time
 #不知道这个咋玩的
def exe_is_active():
    while True:
        time.sleep(0.2)
        try:
            # 关闭文件或目录，使用模糊查询
            hld = FindWinHwnd(u" D:\Android")
            if str(hld) != "0":
                time.sleep(0.2)
                win32gui.PostMessage(hld, win32con.WM_CLOSE, 0, 0)
                time.sleep(0.1)
                print("已关闭txt")

            # 关闭文件或目录，精准查询
            hld = win32gui.FindWindow(None, u"公用")
            if str(hld) != "0":
                time.sleep(0.2)
                win32gui.PostMessage(hld, win32con.WM_CLOSE, 0, 0)
                time.sleep(0.1)
                print("已关闭目录")
        except:
            print("速度过快报错")

# 模糊查询
def FindWinHwnd(title, top=True):
    titles = []
    def foo(hwnd, mouse):
        if top:
            if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                if title in win32gui.GetWindowText(hwnd):
                    titles.append(hwnd)
                    return titles[0]
        else:
            if title in win32gui.GetWindowText(hwnd):
                titles.append(hwnd)
    win32gui.EnumWindows(foo, 0)
    if titles:
        return titles[0]
    else:
        return 0


if __name__ == '__main__':
    exe_is_active()