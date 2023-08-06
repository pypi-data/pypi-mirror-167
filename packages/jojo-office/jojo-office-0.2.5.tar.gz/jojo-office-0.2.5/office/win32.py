
import os

from .util import Util

try:
    from win32com.client import Dispatch, DispatchEx, CDispatch
except ImportError:
    Dispatch = None
    DispatchEx = None
    CDispatch = None

try:
    import win32gui
    import win32api
    import winsound
except ImportError:
    win32gui = None
    win32api = None
    winsound: None = None


class Win32:

    @staticmethod
    def check():
        if not DispatchEx:
            raise ImportError('win32com module is required')

    @staticmethod
    def create_com_object(clsid, exception=True):
        """ 创建 COM 对象  """
        try:
            app = DispatchEx(clsid)
            return app
        except Exception as e:
            if exception:
                raise ValueError('Cannot create win32 COM object of %s , %s' % (repr(clsid), str(e)))
        return None

    @staticmethod
    def powerpoint_open(filename):
        """
        启动 PowerPoint应用， 并打开文件

        :param filename:  文件名
        :return:  返回(app, presentation)
        """
        Win32.check()

        # https://cloud.tencent.com/developer/article/1907286
        app = Win32.create_com_object('Kwpp.Application', False)  # WPS
        if app is None:
            app = Win32.create_com_object('PowerPoint.Application')

        app.Visible = 1  # 前台运行
        app.DisplayAlerts = 0  # 不显示，不警告
        presentation = None

        # open file
        if filename:
            if filename.find(':') <= 0:
                filename = os.path.join(os.getcwd(), filename)
            presentation = app.Presentations.Open(filename)

        return app, presentation

    @staticmethod
    def powerpoint_close(app, presentation=None):
        """ 关闭 PowerPoint应用 """
        # noinspection PyBroadException
        try:
            if presentation:
                presentation.Saved = True
                presentation.Close()  # 关闭 PowerPoint 文档
        except Exception:
            pass

        # noinspection PyBroadException
        try:
            app.Quit()
        except Exception:
            pass

    @staticmethod
    def _open(clsid, command=None, filename=None, visible=True, current_dir=True):
        """
        打开应用， 打开文件
        :param filename: 文件名
        :return:  返回 tuple (app, file_obj)
        """
        Win32.check()

        clsids = clsid.split('|')
        # 打开应用
        app = Win32.create_com_object(clsids[0], False)
        if app is None and len(clsids) > 1:
            app = Win32.create_com_object(clsids[1])

        if hasattr(app, 'Visible'):
            # noinspection PyBroadException
            try:
                app.Visible = visible
            except Exception:
                pass

        if hasattr(app, 'DisplayAlerts'):
            # noinspection PyBroadException
            try:
                app.DisplayAlerts = 0  # Do not show alert (不警告)
            except Exception:
                pass

        # 打开文件
        file_obj = None
        if filename:
            if current_dir and not Util.is_absolute_path(filename):
                filename = os.path.join(os.getcwd(), filename)
            if hasattr(app, command):
                files = getattr(app, command)
                file_obj = files.Open(filename)
            else:
                raise ValueError('cannot find command %s' % repr(command))

        return app, file_obj

    @staticmethod
    def open_word(filename, visible=True):
        """
        启动 Word应用， 并打开文件

        :param filename:  文件名
        :param visible:  是否显示应用界面
        :return:  返回 (app, document)
        """
        # https://cloud.tencent.com/developer/article/1907286
        return Win32._open('Word.Application|KWPS.Application', 'Documents', filename, visible)

    @staticmethod
    def open_excel(filename, visible=True):
        """
        启动 Excel 应用， 并打开文件

        :param filename:  文件名
        :param visible:  是否显示应用界面
        :return:  返回 (app, document)
        """
        return Win32._open('Excel.Application|KET.Application', 'Workbooks', filename, visible)

    @staticmethod
    def open_powerpoint(filename, visible=True):
        """
        启动 PowerPoint 应用， 并打开文件

        :param filename:  文件名
        :param visible:  是否显示应用界面
        :return:  返回 (app, document)
        """
        return Win32._open('PowerPoint1111.Application|KWPP.Application', 'Presentations', filename, visible)

    @staticmethod
    def open_pdf(filename, visible=True):
        """
        启动 Word应用， 并打开文件

        :param filename:  文件名
        :param visible:  是否显示应用界面
        :return:  返回 (app, document)
        """
        # https://cloud.tencent.com/developer/article/1907286
        return Win32._open('Kwps.Application', 'Documents', filename, visible)

    @staticmethod
    def close(app, file_obj=None):
        """ 关闭文件， 关闭应用 """
        # noinspection PyBroadException
        try:
            if file_obj:
                if hasattr(file_obj, 'Saved'):
                    file_obj.Saved = True
                file_obj.Close()  # 关闭文档
        except Exception:
            pass

        # noinspection PyBroadException
        try:
            if app:
                app.Quit()
        except Exception:
            pass

    @staticmethod
    def find_window(title):
        """
        查找标题包含title字符串的窗口

        :param title: 窗口标题
        :return:  返回 HWND. 失败返回 0
        """
        # https://www.programcreek.com/python/example/10639/win32gui.EnumWindows
        def window_enumeration_handler(hwnd, windows):
            """Add window title and ID to array."""
            windows.append((hwnd, win32gui.GetWindowText(hwnd)))

        top_windows = []
        win32gui.EnumWindows(window_enumeration_handler, top_windows)

        for window in top_windows:
            if window[1].lower().find(title) >= 0:
                return window[0]

        return 0

    @staticmethod
    def bring_to_front(win_app):
        """ 将 app 窗口置于最前 """
        # noinspection PyBroadException
        try:
            if isinstance(win_app, CDispatch):
                title = win_app.Caption
            elif isinstance(win_app, str):
                title = win_app
            else:
                raise ValueError("Expect COM object or str, but %s is found" % repr(type(win_app)))

            hwnd = Win32.find_window(title)
            if hwnd != 0:
                win32gui.SetForegroundWindow(hwnd)
                return True
        except Exception:
            pass

        return False
