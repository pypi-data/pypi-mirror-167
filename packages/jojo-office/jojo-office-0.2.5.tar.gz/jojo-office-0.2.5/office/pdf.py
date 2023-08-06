import os
import sys
import subprocess
import time
import json
import io
from io import BytesIO
from pathlib import Path
from types import MethodType
from .base import BaseFile
from .util import Util
from .win32 import Win32


try:
    import PyPDF4
    from PyPDF4.pdf import PdfFileReader, PdfFileWriter
    from PyPDF4.generic import TextStringObject
except ImportError:
    PyPDF4 = None
    PdfFileReader = None
    PdfFileWriter = None
    TextStringObject = None


try:
    import reportlab
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
except ImportError:
    reportlab = None
    Canvas = None
    pdfmetrics = None
    TTFont = None


try:
    import PIL
    from PIL import Image, ImageDraw, ImageEnhance
except ImportError:
    PIL = None
    Image = None
    ImageDraw = None
    ImageEnhance = None


class FontLib:
    ChineseFontNames = {
        '黑体': 'SimHei',
        '宋体': 'SimSunB',
        '仿宋': 'SimFang',
        '楷体': 'SimKai',
        '幼圆': 'SimYou',
        '隶书': 'SimLi',
    }
    #  OS Font paths
    MSFolders = r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'

    MSFontDirectories = [
        r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts',
        r'SOFTWARE\Microsoft\Windows\CurrentVersion\Fonts']

    X11FontDirectories = [
        # an old standard installation point
        "/usr/X11R6/lib/X11/fonts/TTF/",
        "/usr/X11/lib/X11/fonts",
        # here is the new standard location for fonts
        "/usr/share/fonts/",
        # documented as a good place to install new fonts
        "/usr/local/share/fonts/",
        # common application, not really useful
        "/usr/lib/openoffice/share/fonts/truetype/",
    ]

    OSXFontDirectories = [
        "/Library/Fonts/",
        "/Network/Library/Fonts/",
        "/System/Library/Fonts/",
        # fonts installed via MacPorts
        "/opt/local/share/fonts",
    ]

    # if not USE_FONTCONFIG and sys.platform != 'win32':
    #     OSXFontDirectories.append(str(Path.home() / "Library/Fonts"))
    #     X11FontDirectories.append(str(Path.home() / ".fonts"))

    @staticmethod
    def win32FontDirectory():
        r"""
        Return the user-specified font directory for Win32.  This is
        looked up from the registry key::

          \\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders\Fonts

        If the key is not found, $WINDIR/Fonts will be returned.
        """
        import winreg
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, FontLib.MSFolders) as user:
                return winreg.QueryValueEx(user, 'Fonts')[0]
        except OSError:
            return os.path.join(os.environ['WINDIR'], 'Fonts')

    @staticmethod
    def get_fontext_synonyms(font_ext):
        """
        Return a list of file extensions that are synonyms for
        the given file extension *file_ext*.
        """
        return {'ttf': ('ttf', 'otf'),
                'otf': ('ttf', 'otf'),
                'afm': ('afm',)}[font_ext]

    @staticmethod
    def list_fonts(directory, extensions):
        """
        Return a list of all fonts matching any of the extensions, found
        recursively under the directory.
        """
        extensions = ["." + ext for ext in extensions]
        return [os.path.join(dirpath, filename)
                # os.walk ignores access errors, unlike Path.glob.
                for dirpath, _, filenames in os.walk(directory)
                for filename in filenames
                if Path(filename).suffix.lower() in extensions]

    @staticmethod
    def win32InstalledFonts(directory=None, font_ext='ttf'):
        """
        Search for fonts in the specified font directory, or use the
        system directories if none given.  A list of TrueType font
        filenames are returned by default, or AFM fonts if *font_ext* ==
        'afm'.
        """
        import winreg

        if directory is None:
            directory = FontLib.win32FontDirectory()

        font_ext = ['.' + ext for ext in FontLib.get_fontext_synonyms(font_ext)]

        items = set()
        for font_dir in FontLib.MSFontDirectories:
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, font_dir) as local:
                    for j in range(winreg.QueryInfoKey(local)[1]):
                        key, direc, tp = winreg.EnumValue(local, j)
                        if not isinstance(direc, str):
                            continue
                        # Work around for https://bugs.python.org/issue25778,
                        # which is fixed in Py>=3.6.1.
                        direc = direc.split("\0", 1)[0]
                        try:
                            path = Path(directory, direc).resolve()
                        except (FileNotFoundError, RuntimeError):
                            # Don't fail with invalid entries (FileNotFoundError is
                            # only necessary on Py3.5).
                            continue
                        if path.suffix.lower() in font_ext:
                            items.add(str(path))
            except (OSError, MemoryError):
                continue
        return list(items)

    @staticmethod
    def OSXInstalledFonts(directories=None, font_ext='ttf'):
        """Get list of font files on OS X."""
        if directories is None:
            directories = FontLib.OSXFontDirectories
        return [path
                for directory in directories
                for path in FontLib.list_fonts(directory, FontLib.get_fontext_synonyms(font_ext))]

    @staticmethod
    def _call_fc_list():
        """Cache and list the font filenames known to `fc-list`.
        """
        # # Delay the warning by 5s.
        # timer = Timer(5, lambda: warnings.warn(
        #     'Matplotlib is building the font cache using fc-list. '
        #     'This may take a moment.'))
        # timer.start()
        # try:
        #     out = subprocess.check_output(['fc-list', '--format=%{file}\\n'])
        # except (OSError, subprocess.CalledProcessError):
        #     return []
        # finally:
        #     timer.cancel()
        # return [os.fsdecode(filename) for filename in out.split(b'\n')]
        return []

    @staticmethod
    def get_fontconfig_fonts(font_ext='ttf'):
        """List the font filenames known to `fc-list` having the given extension.
        """
        font_ext = ['.' + ext for ext in FontLib.get_fontext_synonyms(font_ext)]
        return [fname for fname in FontLib._call_fc_list()
                if Path(fname).suffix.lower() in font_ext]

    @staticmethod
    def findSystemFonts(font_paths=None, font_ext='ttf'):
        """
        Search for fonts in the specified font paths.  If no paths are
        given, will use a standard set of system paths, as well as the
        list of fonts tracked by fontconfig if fontconfig is installed and
        available.  A list of TrueType fonts are returned by default with
        AFM fonts as an option.
        """
        font_files = set()
        font_exts = FontLib.get_fontext_synonyms(font_ext)

        if font_paths is None:
            if sys.platform == 'win32':
                font_paths = [FontLib.win32FontDirectory()]
                # now get all installed fonts directly...
                font_files.update(FontLib.win32InstalledFonts(font_ext=font_ext))
            else:
                font_paths = FontLib.X11FontDirectories
                font_files.update(FontLib.get_fontconfig_fonts(font_ext))
                # check for OS X & load its fonts if present
                if sys.platform == 'darwin':
                    font_files.update(FontLib.OSXInstalledFonts(font_ext=font_ext))

        elif isinstance(font_paths, str):
            font_paths = [font_paths]

        for path in font_paths:
            font_files.update(map(os.path.abspath, FontLib.list_fonts(path, font_exts)))

        return [fname for fname in font_files if os.path.exists(fname)]

    @staticmethod
    def replaceFontName(font_name):
        """ replace font name """
        if font_name in FontLib.ChineseFontNames:
            return FontLib.ChineseFontNames[font_name]
        return font_name

    @staticmethod
    def findFontFile(font_name):
        """ Find font file"""
        font_files = FontLib.findSystemFonts()
        target = (FontLib.replaceFontName(font_name) + '.ttf').lower()
        for f in font_files:
            if f.lower().find(target) >= 0:
                return f


# PPT .pdf 文档类
class PDF(BaseFile):
    FONT_NAME = 'Helvetica-Bold'  # 西文字体(水印)
    CHINESE_FONT_NAME = 'SimHei'  # 中文字体(水印)

    class Pages:
        """ 页面集合类 """
        def __init__(self, pdf):
            self.pdf = pdf

        def __len__(self):
            return self.pdf.page_count

        def _add_page_method(self, page, index):
            """ add method to page object """
            def func_text(this, layout=False):
                # noinspection PyProtectedMember
                return this.pdf_obj._page_text(this.index, layout)

            def func_tables(this):
                # noinspection PyProtectedMember
                return this.pdf_obj._page_tables(this.index)

            # https://www.ianlewis.org/en/dynamically-adding-method-classes-or-class-instanc
            page.index = index
            page.pdf_obj = self.pdf
            page.text = MethodType(func_text, page)
            page.tables = MethodType(func_tables, page)
            return page

        def __getitem__(self, item):
            if 0 <= item < self.pdf.page_count:
                # noinspection PyProtectedMember
                page = self.pdf._obj.getPage(item)
                return self._add_page_method(page, item)
            raise IndexError('Index %s out of bound' % repr(item))

    def __init__(self, filename, template=None, **kwargs):
        self._watermark = None  # 水印pdf
        self._info = None  # pdf 文件信息对象
        self._register_fonts = {}  # 已注册的字体
        self._file_obj = None
        super().__init__(filename, template, **kwargs)

    def _open(self, filename, **kwargs):
        """  kwargs support:  password='xxx' """
        password = kwargs.get('password', None)

        f = open(filename, 'rb')
        self._file_obj = io.BytesIO(f.read())
        f.close()

        self._obj = PdfFileReader(self._file_obj, strict=False)
        self.filename = filename

        if password and self.is_encrypted:
            self._obj.decrypt(password=password)
        return True

    def _close(self, **kwargs):
        self._obj = None
        self._file_obj = None
        return True

    @staticmethod
    def _open_data_file(filename):
        with open(filename, 'rb') as f:
            f.read()

    @staticmethod
    def _save_data_to_file(filename, data, encoding='utf-8'):
        """ 将data存入文件"""
        file = open(filename, "wb")
        if isinstance(data, PdfFileWriter):
            data.write(file)
        elif isinstance(data, BytesIO):
            file.write(data.getbuffer())
        elif isinstance(data, bytes):
            file.write(data)
        elif isinstance(data, str):
            file.write(data.encode(encoding))
        elif isinstance(data, dict) or isinstance(data, list):
            file.write(json.dumps(data).encode(encoding))
        else:
            file.write(data)
        file.close()

    def _save_file(self, filename, **kwargs):
        file_ext = Util.file_ext(filename)
        if file_ext == '.pdf':
            return self._save_pdf(filename, **kwargs)
        else:
            return super()._save_file(filename, **kwargs)

    def _save_pdf(self, filename, **kwargs):
        """
        保存为pdf文件

        :param filename:  pdf文件名
        :param  kwargs:   support:  password='xxx'
        :return: 成功返回True, 失败返回False
        """
        # process parameters
        password = kwargs.get('password', None)
        watermark = kwargs.get('watermark', None)

        if watermark:
            self.watermark(str(watermark))

        pages = kwargs.get('pages', None)
        if isinstance(pages, int):
            pages = [pages]

        filename = self.filename if filename is None else filename

        wm_reader = None if self._watermark is None else PdfFileReader(self._watermark)

        # copy pages
        pdf_writer = PdfFileWriter()
        for idx, page in enumerate(range(self._obj.getNumPages())):
            # filter by pages
            if pages and idx not in pages:
                continue
            page = self._obj.getPage(page)
            # merge watermark
            if wm_reader:
                p = wm_reader.getPage(0)
                page.mergePage(p)
                pdf_writer.addPage(page)
            else:
                pdf_writer.addPage(page)

        # encrypt if needed
        if password:
            pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

        self._save_data_to_file(filename, pdf_writer)
        return True

    @property
    def is_encrypted(self):
        """ pdf是否已加密 """
        return self._obj.isEncrypted

    @property
    def info(self) -> PyPDF4.pdf.DocumentInformation:
        """ 返回 pdf 文件信息对象"""
        if self._info is None:
            if not self.is_encrypted:
                self._info = self._obj.getDocumentInfo()
        return self._info

    @property
    def page_count(self):
        """ 返回页面数量 """
        return self._obj.getNumPages()

    def __len__(self):
        return self.page_count

    @property
    def pages(self):
        """ 返回页面的集合 """
        return PDF.Pages(self)

    def _register_font(self, font_name):
        """ 注册字体 """
        if font_name in self._register_fonts:
            return True

        # https://blog.csdn.net/a_faint_hope/article/details/90084992
        font_file = FontLib.findFontFile(font_name)
        if not font_file:
            raise ValueError('Cannot find font %s' % repr(font_name))
        pdfmetrics.registerFont(TTFont(font_name, font_file))
        self._register_fonts[font_name] = True

    def _get_font_name(self, text: str):
        """ 取得字体名称 """
        if Util.has_chinese(text):
            self._register_font(PDF.CHINESE_FONT_NAME)
            return PDF.CHINESE_FONT_NAME
        else:
            return PDF.FONT_NAME

    def watermark(self, text: str, color=(190, 190, 190), rotate=15, font_size=40):
        """
        加水印文字

        :param text:  水印文字
        :param color: (可选) 颜色, 数据类型是 tuple (r, g, b), 默认值是(190, 190, 190)
        :param rotate: (可选) 文字旋转角度
        :param font_size: (可选) 文字大小, 默认值是40
        :return: self
        """
        if not text:
            self._watermark = None
            return self

        if self.page_count > 0:
            page = self._obj.getPage(0)
            width = page.mediaBox.getWidth()
            height = page.mediaBox.getHeight()
        else:
            # default size is A4
            width = 596
            height = 842

        # https://www.thepythoncode.com/article/watermark-in-pdf-using-python
        # Generate the output to a memory buffer
        output_buffer = BytesIO()
        # Set Page Size
        c = Canvas(output_buffer, pagesize=(width, height))

        # Set the size and type of the font
        c.setFont(self._get_font_name(text), font_size)
        # add image instead of text: c.drawImage("logo.png", X, Y, 160, 160)

        # Set the color
        if isinstance(color, tuple):
            ct = (r / 255 for r in color)
            c.setFillColorRGB(*ct)
        else:
            c.setFillColor(color)

        # set rotation angle in degree
        c.rotate(rotate)

        # draw multiple text
        size = font_size
        for x in range(size, width, (len(text) * 2) * size):
            for y in range(-2 * size, height, 4 * size):
                c.drawString(x, y, text)

        c.save()
        self._watermark = output_buffer
        return self

    def _watermark_real_text(self, wm_text: str):
        # Generate a watermark pdf in output_buffer
        prefix = '_@#%^$_'
        output_buffer = BytesIO()
        c = Canvas(output_buffer, pagesize=(596, 842))
        c.setFont(self._get_font_name(wm_text), 40)
        c.drawString(10, 10, prefix + wm_text)
        c.save()

        # find the watermark text in the pdf
        wm_reader = PdfFileReader(output_buffer)
        page = wm_reader.getPage(0)
        content_object = page["/Contents"].getObject()
        content = PyPDF4.pdf.ContentStream(content_object, wm_reader)
        for operands, operator in content.operations:
            if operator == PyPDF4.utils.b_("Tj"):
                text = operands[0]
                if isinstance(text, str) and text.startswith(prefix):
                    text = text[len(prefix):]
                    return text
        return wm_text

    def _unwatermark(self, save_filename, watermark_text: str, password: str = None):
        """
        删除水印文字

        :param save_filename:  删除水印文字后的存盘 pdf 文件名
        :param watermark_text:  水印文字
        :param password:  (可选)密码
        :return: self
        """
        real_text = self._watermark_real_text(watermark_text)
        pdf_writer = PdfFileWriter()
        # for each page
        for p in range(self._obj.getNumPages()):
            page = self._obj.getPage(p)
            # Get the page content
            content_object = page["/Contents"].getObject()
            content = PyPDF4.pdf.ContentStream(content_object, self._obj)
            # Loop through all the page elements
            for operands, operator in content.operations:
                # Checks the TJ operator and replaces the corresponding string operand (Watermark text) with ''
                if operator == PyPDF4.utils.b_("Tj"):
                    text = operands[0]
                    if isinstance(text, str) and (text == watermark_text or text == real_text):
                        operands[0] = TextStringObject('')
            page.__setitem__(PyPDF4.generic.NameObject('/Contents'), content)
            pdf_writer.addPage(page)
        if password:
            pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)
        self._save_data_to_file(save_filename, pdf_writer)
        return self

    def _page_text(self, page_index, layout=False):
        """
        提取 指定页面中 的文字
        @return:
        """
        pdfplumber = Util.module('pdfplumber', True)

        # https://blog.csdn.net/h123456789999999/article/details/122832328
        with pdfplumber.open(self.filename) as pdf:
            if isinstance(page_index, int):
                page = pdf.pages[page_index]
                return page.extract_text(layout=layout)
            else:
                result = ''
                for page in pdf.pages:
                    result += page.extract_text(layout=layout)
                return result

    def _page_tables(self, page_index):
        """
        提取PDF中的图表数据
        @return:
        """
        pdfplumber = Util.module('pdfplumber', True)

        # https://blog.csdn.net/h123456789999999/article/details/122832328
        with pdfplumber.open(self.filename) as pdf:
            if isinstance(page_index, int):
                page = pdf.pages[page_index]
                tables = page.extract_tables()
                return tables
            else:
                result = []
                for page in pdf.pages:
                    t = page.extract_tables()
                    if isinstance(t, list):
                        result += t
                return result

    def text(self, layout=False):
        """ 返回 pdf 所有页的文本 """
        return self._page_text("all")

    def tables(self):
        """ 返回 pdf 所有页的表格数据 """
        return self._page_tables("all")

    def guess_password(self, words_filename: str = None):
        """
        (猜测) 破解 pdf 文件密码

        :param words_filename: (可选)密码文件名
        :return: 成功则返回密码，密码为空时返回空字符串。失败则返回None
        """
        def test(words, counter):
            for w in words:
                counter += 1
                if counter > 0 and counter % 2000 == 0:
                    print('guessed passwords %s ...' % counter)
                if self._obj.decrypt(password=w):
                    return w, counter
            return None, counter

        if not self.is_encrypted:
            return ''

        counter = 0

        if words_filename:
            # load passwords from file line by line
            f = open(words_filename, "r")
            line = f.readline()
            while line:
                word = line.strip()
                if self._obj.decrypt(password=word):
                    f.close()
                    return word
                line = f.readline()
            f.close()
        else:
            # get common passwords
            passwords = Util.common_passwords()
            password, counter = test(passwords, counter)
            if password is not None:
                return password

    def print(self, **kwargs):
        """ 使用打印机打印文档 """

        def com_object_print():
            """ print PDF by COM object """
            # noinspection PyBroadException
            try:
                # https://community.spiceworks.com/topic/2146606-automatically-printing-pdf-files-re-sizing-print-double-sided
                # http://www.verycomputer.com/340_bbd9c02270bc1c17_1.htm
                app = Win32.create_com_object('AcroExch.App')
                doc = Win32.create_com_object("AcroExch.AVDoc")
                doc.Open(self.filename, "")
                # Get the number of pages for this pdf, Subtract one because the count is 0 based
                max_page = doc.GetPDDoc().GetNumPages() - 1
                # Print Entire Document, Last value is ShrinkToFit
                shrink_to_fit = True
                postscript_level = 2
                doc.PrintPages(0, max_page, postscript_level, True, shrink_to_fit)
                # Print first two pages : doc.PrintPages(0, 1, 2, 1, 1)
                # quit
                app.Exit()
                doc.Close(True)
                return True
            except Exception:
                return False

        def find_acrobat_exe():
            """ find Acrobat executable filename """
            # noinspection PyBroadException
            try:
                import winreg
                exe = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT, 'Software\\Adobe\\Acrobat\\Exe')
                return exe
            except Exception:
                return None

        def command_line_print():
            """ print PDF by command line """
            # https://zgserver.com/pdf-26.html
            acrobat_exe = find_acrobat_exe()
            if not acrobat_exe or not os.path.exists(acrobat_exe):
                raise ValueError("Adobe Acrobat is needed to print .pdf file")

            # noinspection PyBroadException
            try:
                # compose command of acrobat print
                cmd = '"%s" /N /S /T "%s"' % (acrobat_exe, self._absolute_filename)
                proc = subprocess.Popen(cmd)
                # wait for print pdf to the printer.
                time.sleep(6)
                # kill process
                proc.kill()
                # os.system("TASKKILL /F /IM %s" % Util.file_name(acrobat_exe))
                return True
            except Exception:
                return False

        print("printing", self.filename, '...')

        if not com_object_print():
            return command_line_print()
        return True
