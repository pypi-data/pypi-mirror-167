import os
import sys
import datetime
from io import BytesIO
import csv
import json
import base64
import pickle
import inspect


class Util:
    IMAGE_EXTS = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.emf',
                  '.wmf', '.jpe', '.tif', '.tiff', '.svg']
    AUDIO_EXTS = ['.wav', '.mp3', '.wma', '.wax', '.au', '.midi', '.au',
                  '.m3u', '.m4a', '.aif', '.aiff']
    VIDEO_EXTS = ['.mp4', '.wmv', '.avi', '.mov', '.m4v', '.asf', '.asx',
                  '.wm', '.wvx', '.mpeg', '.mpg', '.webm', '.flv', '.f4v']

    @staticmethod
    def file_ext(filename, lower=True):
        """ 返回文件扩展名 """
        ext = ''
        if isinstance(filename, str):
            if filename.find('?') >= 0:
                filename = filename[:filename.find('?')]
            offset = filename.rfind('.')
            if offset > 0:
                ext = filename[offset:]
        return ext.lower() if lower else ext

    @staticmethod
    def change_file_ext(filename, new_ext):
        suffix = ''

        if filename.find('?') >= 0:
            suffix = filename[filename.find('?'):]
            filename = filename[:filename.find('?')]

        if not new_ext.startswith('.'):
            new_ext = '.' + new_ext

        offset = filename.rfind('.')
        if offset > 0:
            new_filename = filename[:offset] + new_ext + suffix
        else:
            new_filename = filename + new_ext

        return new_filename

    @staticmethod
    def file_name(filename, lower=True):
        """ 返回文件名(不含路径)"""
        if isinstance(filename, str):
            if filename.rfind('\\') >= 0:
                filename = filename[filename.rfind('\\')+1:]
            if filename.rfind('/') >= 0:
                filename = filename[filename.rfind('/')+1:]
            if lower:
                filename = filename.lower()
        return filename

    @staticmethod
    def file_path(filename):
        """ 返回路径"""
        path = ''
        if isinstance(filename, str):
            offset1 = filename.rfind('\\')
            offset2 = filename.rfind('/')
            offset = max(offset1, offset2)
            if offset >= 0:
                path = filename[:offset+1]
        return path

    @staticmethod
    def find_file(filename, paths):
        """
        查找文件

        :param filename: 文件名
        :param paths:  目录列表
        :return:
        """
        if os.path.exists(filename):
            return filename

        if not Util.is_absolute_path(filename):
            if isinstance(paths, list):
                for path in paths:
                    if path:
                        f = os.path.join(path, filename)
                        if os.path.exists(f):
                            return f

    @staticmethod
    def is_absolute_path(filename):
        if sys.platform == 'win32':
            if filename.find(':') == 1 or filename.startswith('\\\\'):
                return True
        elif filename.startswith("/"):
            return True
        return False

    @staticmethod
    def delete_dir(path):
        """ 删除目录 """
        # noinspection PyBroadException
        try:
            for fn in os.listdir(path):
                # noinspection PyBroadException
                try:
                    os.remove(os.path.join(path, fn))
                except Exception:
                    pass
            os.rmdir(path)
        except Exception:
            pass

    @staticmethod
    def module(module_name: str, error=False):
        # noinspection PyBroadException
        try:
            return __import__(module_name)
        except Exception:
            if error:
                raise ImportError("Cannot import module %s, please install, pip install %s"
                                  % (module_name, module_name))
            else:
                return None

    @staticmethod
    def is_image(filename):
        if Util.file_ext(filename) in Util.IMAGE_EXTS:
            return True
        return False

    @staticmethod
    def is_video(filename):
        if Util.file_ext(filename) in Util.VIDEO_EXTS:
            return True
        return False

    @staticmethod
    def is_audio(filename):
        if Util.file_ext(filename) in Util.AUDIO_EXTS:
            return True
        return False

    @staticmethod
    def is_int(n):
        """ whether n is an integer """
        # noinspection PyBroadException
        try:
            _ = int(n)
            return True
        except Exception:
            return False

    @staticmethod
    def is_list_like(data):
        if isinstance(data, list) or isinstance(data, tuple):
            return True
        return False

    @staticmethod
    def is_table_list(data):
        """ whether the data is a list like table """
        if Util.is_list_like(data):
            for item in data:
                if not Util.is_list_like(item):
                    return False
            return True
        return False

    @staticmethod
    def is_workbook(obj):
        """ whether obj is an Excel object"""
        if type(obj).__name__ == 'Workbook':
            return True
        elif type(obj).__name__ == 'Excel':
            return True
        return False

    @staticmethod
    def has_chinese(s):
        """ 字符串 s 中是否包含中文 """
        if isinstance(s, str):
            for ch in s:
                if u'\u4e00' <= ch <= u'\u9fff':
                    return True
        return False

    @staticmethod
    def common_passwords():
        """ 产生常用密码 """
        def day_words(from_year, to_year):
            # 生日数字
            for y in range(from_year, to_year + 1):
                for month in range(1, 13):
                    for day in range(1, 32):
                        # noinspection PyBroadException
                        try:
                            day = datetime.date(y, month, day)
                            words.append(day.strftime("%Y%m%d"))
                            words.append(day.strftime("%y%m%d"))
                            words.append(day.strftime("%m%d%Y"))
                            words.append(day.strftime("%d%m%y"))
                            words.append(day.strftime("%m%d"))
                            words.append(day.strftime("%d%m"))
                        except Exception:
                            pass

        def most_used_words():
            # most used
            words.append("password")
            words.append("12345")
            words.append("123456")
            words.append("1234567")
            words.append("a12345")
            words.append("a123456")
            words.append("a1234567")
            words.append("aa12345")
            words.append("aa123456")
            words.append("aa1234567")
            words.append("12345678")
            words.append("123456789")
            words.append("1234567890")
            words.append("123123")
            words.append("qwerty")
            words.append("1q2w3e")
            words.append("pass")
            words.append("admin")
            words.append("888")
            words.append("8888")
            words.append("888888")
            words.append("111")
            words.append("1111")
            words.append("111111")
            words.append("000")
            words.append("0000")
            words.append("000000")

        def continuous_words(max_length=6):
            # 连续字符
            for i in range(0, len(chars)):
                for length in range(1, max_length + 1):
                    word = ''
                    for j in range(0, length):
                        if i + j < len(chars):
                            word += chars[i + j]
                    words.append(word)
                    if len(word) <= 4:
                        words.append(word + word)

        def same_words(max_length=8):
            # 相同字符
            for i in range(0, len(chars)):
                for length in range(0, max_length):
                    word = chars[i]
                    for j in range(0, length):
                        if i < len(chars):
                            word += chars[i]
                    words.append(word)

        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
        words = []

        most_used_words()

        continuous_words()

        same_words()

        # 生日数字
        year = datetime.datetime.now().year
        day_words(year, year + 1)
        day_words(year + 2, year + 3)
        day_words(year - 50, year - 1)

        return words

    @staticmethod
    def load_text_file(filename):
        f = open(filename, mode='r')
        content = f.read()
        f.close()
        return content

    @staticmethod
    def save_text_file(filename, content, append=False):
        mode = "a+" if append else "w"
        f = open(filename, mode)
        f.write(str(content))
        f.close()
        return True

    @staticmethod
    def load_csv_file(filename, delimiter=None):
        """ load csv file, return record list """
        result = []
        with open(filename, 'r') as file:
            kwargs = {'dialect': 'excel'}
            if delimiter:
                kwargs['delimiter'] = delimiter
            reader = csv.reader(file, **kwargs)
            for row in reader:
                result.append(row)
        return result

    @staticmethod
    def save_csv_file(filename, record_list, delimiter=None):
        """ save record list to .csv file """
        if not Util.is_table_list(record_list):
            raise ValueError("record_list must be a list of list")
        with open(filename, 'w', newline='') as file:
            kwargs = {'dialect': 'excel'}
            if delimiter:
                kwargs['delimiter'] = delimiter
            writer = csv.writer(file, **kwargs)
            for item in record_list:
                writer.writerow(item)

    @staticmethod
    def load_from_file(filename, **kwargs):
        ext = Util.file_ext(filename)
        if ext == '.json':
            return json.loads(Util.load_text_file(filename))
        elif ext == '.csv':
            return Util.load_csv_file(filename)
        elif ext == '.txt':
            return Util.load_text_file(filename)
        elif ext == '.object':
            # read .object file, return file
            s2 = Util.load_text_file(filename)
            b2 = base64.b64decode(s2)  # base64 decode
            return pickle.loads(b2)
        else:
            return IOError('unknown file extension %s' % repr(ext))

    @staticmethod
    def save_to_file(filename, data, encoding='utf-8'):
        """ 将data存入文件"""
        with open(filename, "wb") as f:
            if isinstance(data, BytesIO):
                f.write(data.getbuffer())
            elif isinstance(data, bytes):
                f.write(data)
            elif isinstance(data, str):
                f.write(data.encode(encoding))
            elif isinstance(data, dict) or isinstance(data, list):
                f.write(json.dumps(data).encode(encoding=encoding))
            elif isinstance(data, str):
                f.write(data.encode(encoding=encoding))
            elif type(data).__name__ == 'DataFrame':
                f.close()
                data.to_csv(filename)
                return
            elif hasattr(data, 'write'):
                data.write(f)
            elif inspect.isclass(type(data)):
                b1 = pickle.dumps(data)  # serialize object
                s1 = str(base64.b64encode(b1), "utf-8")  # base64 encode to string
                f.write(s1.encode(encoding=encoding))
            else:
                f.write(data)
        f.close()

    @staticmethod
    def check_module(module, name):
        if module is None:
            raise ImportError("%s module is required: pip install %s" % (name, name))

