import win32clipboard as w
import win32con


class Clipboard(object):
    '''模拟Windows设置剪贴板
    '''
    # 读取剪贴板
    @staticmethod
    def getText():
        # 打开剪贴板
        w.OpenClipboard()
        # 获取剪贴板中的数据
        d = w.GetClipboardData(
            win32con.CF_TEXT
        )
        # 关闭剪贴板
        w.CloseClipboard()
        return d

    # 设置剪贴板内容
    @staticmethod
    def setText(aString):
        # 打开剪贴板，清空
        w.OpenClipboard()
        w.EmptyClipboard()
        # 写入数据到剪贴板
        w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
        # 关闭剪贴板
        w.CloseClipboard()

