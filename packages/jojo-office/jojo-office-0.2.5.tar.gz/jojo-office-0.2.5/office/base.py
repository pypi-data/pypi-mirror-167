
import os
import shutil
from .util import Util
from .variable import VarData


class BaseFile:
    """
    Base class for Office files, include .docx, .xlsx, .pptx, .pdf.

    :Chinese: Office 文档基类, 包括：.docx, .xlsx, .pptx, .pdf.
    """
    def __init__(self, filename=None, template=None, **kwargs):
        """
        Init and open file depends on template file.

        :Chinese: 初始化，并打开文件

        :param filename:   file name
        :param template:  (optional) template file name. if template is provided,
            template file is copied to overwrite existing file or create new file.

            :Chinese:(可选)模板文件名。如果模板不为空，则复制模板文件创建文件或覆盖已有文件。
        :return: self
        """
        self.filename = None
        self._obj = None
        self.open(filename, template, **kwargs)

    def open(self, filename, template=None, **kwargs):
        """
        Open file.

        :Chinese: 打开文件

        :param filename:   filename.
        :param template:  (optional) template filename. If template is provided,
            template file is copied to overwrite existing file or create new file.

            :Chinese:(可选)模板文件名。如果模板不为空，则复制模板文件创建文件或覆盖已有文件。
        :return: self
        """
        self.close()

        if filename and template:
            if os.path.exists(template):
                shutil.copyfile(template, filename)
            else:
                raise FileNotFoundError('template file %s not found' % repr(template))

        if filename and os.path.exists(filename):
            self._open(filename, **kwargs)
        else:
            self._new_file(filename, **kwargs)

        return self

    def close(self, **kwargs):
        """
        Close file.

        :Chinese: 关闭文件.

        :return: self
        """
        if self._close(**kwargs):
            self._obj = None
        self.filename = None
        return self

    def save(self, filename=None, **kwargs):
        """
        Save file.

        :Chinese: 保存文件

        :param filename:  filename to save. if None, save to original file.
            :Chinese: (可选)存盘文件名。如果缺省，则保存到原文件名。
        :return: self
        """
        filename = self.filename if filename is None else filename
        self._save_file(filename, **kwargs)
        return self

    def _new_file(self, filename, **kwargs):
        """ Extend class should implement this method """
        raise IOError('new file is not supported')

    def _save_file(self, filename, **kwargs):
        """ Extend class should implement this method """
        raise IOError('save to %s is not supported' % repr(Util.file_ext(filename)))

    def _open(self, filename, **kwargs):
        """ Extend class should implement this method """
        raise IOError('open file is not supported')

    # noinspection PyMethodMayBeStatic
    # noinspection PyUnusedLocal
    def _close(self, **kwargs):
        """ Extend class should implement this method """
        return True

    def fill(self, data):
        """
        Fill data into the document, replace variable tags with its values.

        :Chinese: 将数据填入, 替换变量标签，生成文件内容。

        :param data:  the data to fill with, could be a dict,
                    or an Excel filename, or a DataFrame object.
            :Chinese: dictionary对象 或 excel文件名
        :return: self
        """
        data = VarData.open(data)

        # 填入数据
        self._fill_data(data)

        data.close()

        return self

    def _fill_data(self, data):
        """ Extend class should implement this method to fill data into the file"""
        raise IOError('fill data is not implemented')

    @property
    def _absolute_filename(self):
        """ return file name with absolute path """
        filename = self.filename
        if not Util.is_absolute_path(filename):
            filename = os.path.join(os.getcwd(), filename)
        return filename

    # noinspection PyUnusedLocal
    def print(self, **kwargs):
        """
        Print the file.

        Extend class should implement this method.
        """
        pass
