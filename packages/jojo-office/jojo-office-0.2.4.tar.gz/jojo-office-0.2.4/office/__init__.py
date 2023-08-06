# Process .docx, .xlsx, .pptx, .pdf files for office automation

from .util import Util
from .word import Word
from .excel import Excel
from .ppt import PPT
from .pdf import PDF
from .video import Video
import sys

__version__ = '0.2.4'
__author__ = "JoStudio"
__date__ = "2022/9/1"


def open_file(filename, template=None, **kwargs):
    """
    open office file (file extentions are .docx, or .xlsx or .pptx or .pdf)

    :Chinese: 打开office文件 （ .docx 或 .xlsx 或 .pptx 或 .pdf )

    :param filename:  filename
    :param template:  (optional)template filename, copy templated file to create filename
    :return: object
    """
    ext = Util.file_ext(filename)
    if ext in ['.docx']:
        return Word(filename, template, **kwargs)
    elif ext in ['.xlsx']:
        return Excel(filename, template, **kwargs)
    elif ext in ['.pptx']:
        return PPT(filename, template, **kwargs)
    elif ext in ['.pdf']:
        return PDF(filename, template, **kwargs)
    else:
        raise ValueError('file extension % is not supported' % repr(ext))


def print_files(filename_list, **kwargs):
    """
    Use printer to print each file in the list

    :Chinese: 使用打印机逐个打印文件.

    :param filename_list: office filename list
    :param kwargs:  (optional)
    :return: None
    """
    for filename in filename_list:
        try:
            w = open_file(filename)
            w.print(**kwargs)
        except Exception as e:
            print("error print file %s, %s" % (filename, str(e)), file=sys.stderr)
