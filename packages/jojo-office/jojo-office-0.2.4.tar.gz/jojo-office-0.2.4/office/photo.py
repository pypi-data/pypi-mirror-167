import math
from .util import Util

try:
    import PIL
    from PIL import Image, ImageDraw, ImageEnhance, ImageFont
except ImportError:
    PIL = None
    Image = None
    ImageDraw = None
    ImageEnhance = None
    ImageFont = None


try:
    import numpy
except ImportError:
    numpy = None


class PhotoFont:
    def __init__(self, name='arial', size=20, color='#000'):
        self._name = name
        self._font_file = name + '.ttf'
        self._size = size
        self._color = color
        self._create_obj()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._font_file = self._name + '.ttf'
        self._create_obj()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        self._create_obj()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def _create_obj(self):
        self.font_obj = ImageFont.truetype(self._font_file, self._size)

    # noinspection PyMethodMayBeStatic
    def _get_font_name(self, text: str):
        """ 取得字体名称 """
        if Util.has_chinese(text):
            return 'simhei.ttf'
        else:
            return 'arial.ttf'

    def set_text(self, text):
        self._font_file = self._get_font_name(text)
        self._create_obj()


class PhotoSplitter:
    def __init__(self, photo):
        Util.check_module(PIL, "pillow")
        self.photo = photo
        self.boxes = []
        self.index = 0

    def table(self, rows, cols, spacing=0, border=0):
        """
        划分表格

        :param rows:  表格的行数 (Pixels)
        :param cols:  表格的列数 (Pixels)
        :param spacing: 间隔宽度 (Pixels)
        :param border: 边框宽度 (Pixels)
        :return: self
        """
        width, height = self.photo.size
        spacing = spacing if spacing > 0 else 0

        if not isinstance(rows, int) or not isinstance(cols, int):
            raise ValueError("rows cols should be int")

        # 每个单元表的宽、高
        w = round((width - (cols-1) * spacing - 2 * border) / cols)
        h = round((height - (rows-1) * spacing - 2 * border) / rows)
        if w < 1 or h < 1:
            raise ValueError("cannot split into rows %s and cols %s" % (rows, cols))

        # 清空原数据
        self.boxes = []
        self.index = 0

        # 切分表格
        x = y = border
        for row in range(0, rows):
            for col in range(0, cols):
                rect = (x, y, x + w, y + h)
                self.boxes.append(rect)
                x = x + spacing + w
            y = y + spacing + h
            x = border

        return self

    def table_fill(self, photo, index=None):
        """ fill a photo into current cell """
        if len(self.boxes) == 0:
            raise ValueError("please call table() first")

        index = self.index if index is None else index

        if index >= len(self.boxes) or index < 0:
            index = 0

        if index < len(self.boxes):
            box = self.boxes[index]
            self.photo.draw_photo(photo, box)
            self.index = index + 1 if index < len(self.boxes) else 0
        else:
            raise IndexError("index %s out of bound" % index)


class Photo:
    """

    Photo is an extended class of PIL.Image.


    PIL Image document:
    https://pillow.readthedocs.io/en/stable/reference/Image.html#module-PIL.Image

    """

    # modes
    BIT = '1'
    PALETTE = 'P'
    GRAYSCALE = 'L'
    RGB = 'RGB'
    RGBA = 'RGBA'
    CYMK = 'CYMK'
    YCbCr = 'YCbCr'
    LAB = 'LAB'
    HSV = 'HSV'

    # resize styles
    FIT = "fit"
    STRETCH = "stretch"
    GROW = "grow"
    TILE = "tile"

    # maximum width, height of the photo
    MAX_WIDTH = 50000

    def __init__(self, file_or_size, height=None, **kwargs):
        """
        init instance

        :param file_or_size:  A filename (string), or file object, or size tuple
        :param kwargs: Extra parameters, such as 'mode', 'color'
        """
        self.filename = None
        self._font = PhotoFont()
        self._draw_obj = None
        self._splitter = None
        self.base_obj = None

        color = kwargs.get('color', (255, 255, 255))
        mode = kwargs.get('mode', 'RGB')

        if isinstance(file_or_size, str):
            base_obj = Image.open(file_or_size)
            self.filename = file_or_size
        elif isinstance(file_or_size, tuple):
            base_obj = Image.new(mode, file_or_size, color)
        elif isinstance(file_or_size, int):
            width = file_or_size
            if not isinstance(height, int):
                height = width
            base_obj = Image.new(mode, (width, height), color)
        elif isinstance(file_or_size, Image):
            base_obj = file_or_size
        else:
            raise ValueError("unsupport file type %s" % repr(type(file_or_size)))

        super().__init__()
        self.base_obj = base_obj

        # decorate method of Images
        # self.resize = self._decorate_method(self.base_obj.resize, Image)

    @property
    def im(self):
        return self.base_obj

    def _decorate_method(self, method, cls=None):
        that = self

        def warpper(*args, **kwargs):
            params = args[1:]
            result = method(*params, **kwargs)
            if cls and isinstance(result, cls):
                that.base_obj = result
            return that

        return warpper

    @property
    def width(self):
        return self.base_obj.width

    @property
    def height(self):
        return self.base_obj.height

    @property
    def mode(self):
        return self.base_obj.mode

    @property
    def size(self):
        return self.base_obj.size

    def __repr__(self):
        s = "<Photo %s x %s, %s>" % (self.width, self.height, repr(self.mode))
        return s

    def new(self, width, height, color=(255, 255, 255), mode='RGB'):
        """
        Creates a new image with the given mode and size.
        https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new

        :param width: widtd in pixels.
        :param height: height in pixels.
        :param mode:  The mode to use for the new image, such as:  Photo.RGB, Photo.RGBA, ...
        :param color: What color to use for the image. Default is black. If given, this should be a single integer
        or floating point value for single-band modes, and a tuple for multi-band modes (one value per band).
        :return: self
        """
        self.base_obj = Image.new(mode, (width, height), color)
        return self

    def open(self, file, formats=None):
        """
        Opens and identifies the given image file.
        https://pillow.readthedocs.io/en/stable/reference/Image.html#functions

        :param file:  A filename (string), pathlib.Path object or a file object.
        :param formats: A list or tuple of formats to attempt to load the file in.
        :return: self
        """
        self.base_obj = Image.open(file, 'r', formats)
        return self

    def save(self, file=None, fmt=None, **params):
        """
        Saves this image under the given filename. If no format is specified, the format to use is determined
        from the filename extension, if possible.
        https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save

        :param file:   A filename (string), pathlib.Path object or file object.
        :param fmt: Optional format override. If omitted, the format is determined from the filename extension.
        :param params: Extra parameters to the image writer.
        :return: self
        """
        file = self.filename if file is None else file
        try:
            self.base_obj.save(file, fmt, **params)
            if isinstance(file, str):
                self.filename = file
        except Exception as e:
            err_msg = str(e)
            if err_msg.find('RGBA'):
                self.base_obj = self.base_obj.convert('RGB')
                self.base_obj.save(file, fmt, **params)
                if isinstance(file, str):
                    self.filename = file
        return self

    def clone(self) -> 'Photo':
        """ return a new copy of the photo"""
        new_photo = Photo(self.width, self.height, mode=self.mode)
        new_photo.paste(self)
        return new_photo

    def table_split(self, rows, cols, spacing=0, border=0):
        """ 切分为 多张小图，返回图片列表 """
        splitter = PhotoSplitter(self).table(rows, cols, spacing, border)
        result = []
        for box in splitter.boxes:
            p = self.clone().crop(box)
            result.append(p)
        return result

    def table(self, rows, cols, spacing=0, border=0):
        """
        切分为表格

        :param rows:  表格的行数 (Pixels)
        :param cols:  表格的列数 (Pixels)
        :param spacing: 间隔宽度 (Pixels)
        :param border: 边框宽度 (Pixels)
        :return: self
        """
        self._splitter = PhotoSplitter(self).table(rows, cols, spacing, border)
        return self

    def table_view(self, rows, cols, spacing=0, border=0, fill="#FFF"):
        """
        将图片变成表格状

        :param rows:  表格的行数 (Pixels)
        :param cols:  表格的列数 (Pixels)
        :param spacing: (可选)间隔宽度 (Pixels)
        :param border: (可选)边框宽度 (Pixels)
        :param fill:   (可选)底色
        :return:
        """
        im = self.base_obj
        photos = self.table_split(rows, cols, spacing, border)
        p = Photo(im.size, mode=im.mode, color=fill)
        p.table(rows, cols, spacing, border).table_fill(photos)
        self.base_obj = p.base_obj
        return self

    def table_fill(self, photo, index=None):
        """
        table() 切分为表格后, 填入图片

        :param photo: 图片， Photo对象 或 图片文件名
        :param index: （可选) 表格位置
        :return: self
        """

        if not self._splitter:
            raise ValueError("please call table() first")

        if isinstance(photo, list):
            self._splitter.index = 0
            for p in photo:
                self._splitter.table_fill(p)
        else:
            self._splitter.table_fill(photo, index)

        return self

    def border(self, color, left, top=None, right=None, bottom=None):
        """
        扩大图片，创建边框

        :param color:  边框颜色
        :param left:   左边边框宽度
        :param top:    （可选)上边边框宽度
        :param right:  （可选)右边边框宽度
        :param bottom: （可选)下边边框宽度
        :return: self
        """
        right = left if right is None else right
        top = left if top is None else top
        bottom = top if bottom is None else bottom
        im = self.base_obj
        w, h = im.size
        p = Photo(w + left + right, h + top + bottom, mode=im.mode, color=color)
        box = (left, top, left + w, top + h)
        p.paste(self, box)
        self.base_obj = p.base_obj
        return self

    def _validate_box(self, box, default_width=None, default_height=None):
        """ validate the box """
        if box is None:
            box = (0, 0, self.width, self.height)

        if default_width is None:
            default_width = self.width

        if default_height is None:
            default_height = self.height

        if isinstance(box, tuple):
            if len(box) == 2:
                right = min(box[0]+default_width, self.width)
                bottom = min(box[1]+default_height, self.height)
                box = tuple(list(box).append(right, bottom))
            if len(box) == 4:
                return box

        raise ValueError('box should be a 4-int tuple')

    # noinspection PyMethodMayBeStatic
    def _validate_wh(self, width, height, msg=None):
        """ validate width and height """
        if not isinstance(width, int) or not isinstance(height, int):
            raise ValueError('width and height should be int')

        if width <= 0 or height <= 0:
            msg = 'width or height should large than zero' if msg is None else msg
            raise ValueError(msg)

        if width > Photo.MAX_WIDTH or height > Photo.MAX_WIDTH:
            raise ValueError('width or height is too big')

    # noinspection PyMethodMayBeStatic
    def _get_image(self, photo):
        """ get image obj from photo"""
        if isinstance(photo, Photo):
            return photo.base_obj
        else:
            return photo

    # noinspection PyMethodMayBeStatic
    def _get_photo(self, im):
        """ get image obj from photo"""
        return im if isinstance(im, Photo) else Photo(im)

    def histogram(self, channel='L', mask=None, extrema=None):
        """
        取得直方图数据

        :param channel:  通道， R , G, B, L(灰度), 默认是 L
        :param mask:     （可选)掩膜
        :param extrema:   （可选)
        :return: 返回一个数据列表

        https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.histogram

        """
        mode = str(self.mode).upper()
        channel = str(channel).upper()

        if channel == 'L':
            # convert to grayscale
            p = self.base_obj.convert(Photo.GRAYSCALE)
            return p.histogram(mask, extrema)
        elif mode.find(channel) >= 0:
            offset = mode.find(channel)
            # split and find channel
            channels = self.base_obj.split()
            if offset < len(channels):
                return channels[offset].histogram(mask, extrema)
        elif channel == '' or channel is None:
            # all channel mixed
            return self.im.histogram(mask, extrema)
        else:
            raise ValueError('channel %s not found' % repr(channel))

    def crop(self, box):
        """
        cut down a rectangular region from this image

        SEE: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.crop

        :param box: the crop rectangle, as a (left, upper, right, bottom)-tuple.
        :return: self
        """
        if isinstance(box, tuple) and len(box) == 4:
            self.base_obj = self.base_obj.crop(box)
        else:
            raise ValueError("box should be a 4-tuple of (left, top, right, bottom) ")
        return self

    def flip(self):
        """ 图片左右反转"""
        self.base_obj = self.base_obj.transpose(PIL.Image.Transpose.FLIP_LEFT_RIGHT)
        return self

    def vflip(self):
        """ 图片上下反转"""
        self.base_obj = self.base_obj.transpose(PIL.Image.Transpose.FLIP_TOP_BOTTOM)
        return self

    def rotate(self, degree, fill=None, expand=0, center=None, resample=None, translate=None):
        """
        旋转图像

        https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.rotate

        :param degree:   角度， 0 - 360度
        :param fill:     旋转后产生的空白部分的填充颜色, 默认是黑色
        :param expand:   是否扩大图片，以保证原图全部可见
        :param center:   旋转中心点， tuple (x, y)
        :param resample: 重采样方法
        :param translate: An optional post-rotate translation
        :return:
        """
        resample = PIL.Image.Resampling.BICUBIC if resample is None else resample

        if degree in [-90, -180, -270, -360]:
            degree += 360

        if degree == 0:
            pass
        elif degree == 90:
            self.base_obj = self.base_obj.transpose(PIL.Image.Transpose.ROTATE_90)
        elif degree == 180:
            self.base_obj = self.base_obj.transpose(PIL.Image.Transpose.ROTATE_180)
        elif degree == 270:
            self.base_obj = self.base_obj.transpose(PIL.Image.Transpose.ROTATE_270)
        else:
            self.base_obj = self.base_obj.rotate(degree, resample, expand, center, translate, fill)
        return self

    def resize(self, width, height=None, style='fit', **kwargs):
        """
        resized the image

        :param width:   An int value which is the target width of the photo ,
                        or a float value which is scale ratio
        :param height:  (optional)An int which is target height of the photo.
                        or None when width is float
        :param style:  (optional) A str, style could be Photo.STRETCH, Photo.FIT, Photo.GROW,
                       Photo.STRETCH  means stretch the photo to match the target size.
                       Photo.FIT  means cut down the edges of the photo to match the target size.
                       Photo.GROW  means add edges to the photo to match the target size.
        :param kwargs: (optional) accept resample, reducing_gap, box
                SEE: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.resize
        :return: self
        """
        # get size`
        old_w, old_h = self.size
        self._validate_wh(old_w, old_h, 'photo is empty')
        old_ratio = old_w / old_h

        # get params
        resample = kwargs.pop("resample", None)
        reducing_gap = kwargs.pop("reducing_gap", None)
        scale = kwargs.pop("scale", False)
        box = kwargs.pop("box", None)

        # process the width, height
        if isinstance(width, float) and height is None:
            # width param is a scale ratio
            new_ratio = width
            width = round(self.width * new_ratio)
            height = round(self.height * new_ratio)
            self._validate_wh(width, height)
            self.base_obj = self.base_obj.resize((width, height), resample, reducing_gap)
            return self

        # if width, height is single provided, keep ratio
        if isinstance(width, int) and height is None:
            height = round(width / old_ratio)
        elif isinstance(height, int) and width is None:
            width = round(height * old_ratio)

        self._validate_wh(width, height)
        new_ratio = width / height

        style = str(style).lower().strip()
        if style not in [Photo.STRETCH, Photo.FIT, Photo.GROW]:
            raise ValueError("unknown style %s" % repr(str(style)))

        # if box is specified, crop it
        if box is not None:
            self.crop(box)

        if style == Photo.STRETCH:
            # stretch the photo to match the target size.
            self.base_obj = self.base_obj.resize((width, height), resample, reducing_gap)
        elif style == Photo.FIT:
            # FIT style means cut down the edges of photo outside the target size
            x = y = 0
            if new_ratio < old_ratio:
                new_h = old_h
                new_w = round(new_h * new_ratio)
                x = round((old_w - new_w)/2)
            else:
                new_w = old_w
                new_h = round(new_w / new_ratio)
                y = round((old_h - new_h) / 2)
            box = (x, y, x + new_w, y + new_h)
            self.base_obj = self.base_obj.crop(box)
            if not scale:
                self.base_obj = self.base_obj.resize((width, height), resample, reducing_gap)
        elif style == Photo.GROW:
            # GROW style is to keep all photo, add margins if needed
            if new_ratio > old_ratio:
                new_h = old_h
                new_w = round(new_h * new_ratio)
            else:
                new_w = old_w
                new_h = round(new_w / new_ratio)
            if not scale:
                self.base_obj = self.base_obj.resize((width, height), resample, reducing_gap)
            # create new photo
            new_photo = Photo((new_w, new_h), img=self.base_obj.mode)
            old_photo = self
            x = round((new_photo.width - old_photo.width)/2)
            y = round((new_photo.height - old_photo.height) / 2)
            # paste old_photo into the new photo
            new_photo.paste(old_photo, (x, y))
            self.base_obj = new_photo.base_obj
        return self

    def thumbnail(self, width, height=None, style=None, resample=None, reducing_gap=2.0):
        """
        生成缩略图

        https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.thumbnail

        :param width:  缩略图宽度
        :param height: 缩略图高度
        :param style:  (optional) A str, style could be Photo.STRETCH, Photo.FIT, Photo.GROW,
                       Photo.STRETCH  means stretch the photo to match the target size.
                       Photo.FIT  means cut down the edges of the photo to match the target size.
                       Photo.GROW  means add edges to the photo to match the target size.
        :param resample: 重采样方法
        :param reducing_gap:
        :return:
        """
        resample = PIL.Image.Resampling.BICUBIC if resample is None else resample

        if height is None and isinstance(width, int):
            height = round(width * (self.height / self.width))
        elif width is None and isinstance(height, int):
            width = round(height * (self.width / self.height))

        if style:
            kwargs = {}
            kwargs['resample'] = resample
            kwargs['reducing_gap'] = reducing_gap
            self.resize(width, height, style, **kwargs)
        else:
            self.base_obj.thumbnail((width, height), resample, reducing_gap)

        return self

    def alpha(self, value):
        """
        Adds or replaces the alpha layer in this image. If the image does not have an alpha layer, it’s converted
        to “LA” or “RGBA”. The new layer must be either “L” or “1”.

        :param value: alpha – The new alpha layer. This can either be an “L” or “1” image having the same size
        as this image, or an integer or other color value.

        :return: self
        """
        self.base_obj.putalpha(value)
        return self

    def show(self, title=None):
        """
        Displays this image.

        https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.show

        :param title: window title
        :return: self
        """
        self.base_obj.show(title)
        return self

    # noinspection PyMethodMayBeStatic
    def _angle(self, width, height):
        """ return angle in degree """
        if height == 0:
            return 0
        else:
            return math.atan(height / width) * 180 / math.pi

    def blend(self, photo, alpha):
        """
        Creates a new image by interpolating input image, using a constant alpha.

        https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.blend

        :param photo: The image. Must have the same mode and size as the first image.
        :param alpha: The interpolation alpha factor. If alpha is 0.0, a copy of the first image is returned.
        If alpha is 1.0, a copy of the second image is returned. There are no restrictions on the alpha value.
        If necessary, the result is clipped to fit into the allowed output range.

        :return: self
        """
        self.base_obj = PIL.Image.blend(self.base_obj, self._get_image(photo), alpha)
        return self

    def composite(self, photo, mask):
        """
        Create composite image by blending images using a transparency mask.

        https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.composite

        :param photo:  The image. Must have the same mode and size as the first image.
        :param mask: A mask image. This image can have mode “1”, “L”, or “RGBA”, and must have
        the same size as the other two images.

        :return: self
        """
        self.base_obj = PIL.Image.composite(self.base_obj, self._get_image(photo), mask)
        return self

    def eval(self, func):
        """
        Applies the function (which should take integer argument) to each pixel in the given image.

        :param func:  the function (which should take integer argument)
        :return: self
        """
        self.base_obj = PIL.Image.eval(self.base_obj, func)
        return self

    def convert(self, mode):
        """
        convert to specified mode

        :param mode: the mode to use for the new image, such as:  Photo.RGB, Photo.RGBA, ...
        :return: self
        """
        self.base_obj = self.base_obj.convert(mode)
        return self

    def transparent(self, rgb_color):
        """
        设置透明色

        :param rgb_color:  颜色， tuple like (R, G, B)
        :return: self
        """
        if self.mode != 'RGBA':
            self.convert('RGBA')

        Util.check_module(numpy, 'numpy')

        if numpy:
            # Make transparency using numpy
            arr = numpy.array(self.base_obj)  # convert image to numpy array
            rgb = rgb_color
            mask = (arr[:, :, 0] == rgb[0]) & (arr[:, :, 1] == rgb[1]) & (arr[:, :, 2] == rgb[2])
            arr[mask] = [255, 255, 255, 0]
            # convert the numpy array into image
            self.base_obj = PIL.Image.fromarray(arr)
        else:
            # make transparency using python
            arr = []
            for item in self.base_obj.getdata():
                if item[:3] == rgb_color:
                    arr.append((255, 255, 255, 0))
                else:
                    arr.append(item)
            self.base_obj.putdata(arr)
        return self

    def paste(self, photo, box=None, mask=None):
        """
        Pastes another image into this image

        :param photo:  Source image or pixel value (integer or tuple).
        :param box:    An optional 4-tuple giving the region to paste into. If a 2-tuple is used instead, it’s
        treated as the upper left corner. If omitted or None, the source is pasted into the upper left corner.

        If an image is given as the second argument and there is no third, the box defaults to (0, 0), and the
        second argument is interpreted as a mask image.
        :param mask:   An optional mask image.
        :return:
        """
        self.base_obj.paste(self._get_image(photo), box, self._get_image(mask))
        return self

    def brightness(self, factor):
        """
        调节亮度

        :param factor : 调节系数 float型. 0调至全黑，1 保持原图亮度不变，>1提高亮度, <1降低亮度
        :return: self
        """
        en = ImageEnhance.Brightness(self.base_obj)
        self.base_obj = en.enhance(factor)
        return self

    def color(self, factor):
        """
        调节色彩浓度

        :param factor : 调节系数 float型. 0调至黑白，1 保持原图色彩浓度不变，>1提高色彩浓度, <1降低色彩浓度
        :return: self
        """
        en = ImageEnhance.Color(self.base_obj)
        self.base_obj = en.enhance(factor)
        return self

    def contrast(self, factor):
        """
        调节对比度

        :param factor : 调节系数 float型. 0调至全灰(无对比度)，1 保持原图不变，>1提高对比度, <1降低对比度
        :return: self
        """
        en = ImageEnhance.Contrast(self.base_obj)
        self.base_obj = en.enhance(factor)
        return self

    def sharpness(self, factor):
        """
        调节锐度

        :param factor : 调节系数 float型. <0是模糊化， >0是锐化
        :return: self
        """
        en = ImageEnhance.Sharpness(self.base_obj)
        self.base_obj = en.enhance(factor)
        return self

    @property
    def font(self):
        return self._font

    @property
    def _draw(self):
        """ return the PIL draw object """
        if self._draw_obj is None or self._draw_obj.im != self.base_obj:
            self._draw_obj = ImageDraw.Draw(self.base_obj)
        return self._draw_obj

    def text_size(self, text):
        """ return a tuple (width, height) of the drawing size of text """
        self.font.set_text(text)
        _, _, width, height = self._draw.textbbox((0, 0), text, self.font.font_obj)
        return width, height

    def draw_photo(self, photo: 'Photo', box=None, style="fit", mask=None):
        """ draw a image """
        photo = self._get_photo(photo)
        box = self._validate_box(box, photo.width, photo.height)
        w = box[2] - box[0]
        h = box[3] - box[1]
        p = photo.clone().resize(w, h, style)
        self.paste(p, box=box, mask=mask)
        return self

    def draw_text(self, x, y, text):
        """ draw text on the photo"""
        self.font.set_text(text)
        self._draw.text((x, y), text, font=self.font.font_obj, fill=self.font.color)
        return self

    def watermark(self, mark, box=None):
        """ draw watermark """
        if isinstance(mark, str):
            width, height = self.base_obj.size
            m = Photo((width, height), color=(255, 255, 255))
            m.font.size = 80
            m.font.size = round(min(width, height) / max(len(mark), 6))
            m.font.color = '#666'
            w, h = m.text_size(mark)
            x = (width - w) / 2
            y = (height - h) / 2
            m.draw_text(x, y, mark)
            m.base_obj = m.base_obj.rotate(30, fillcolor=(255, 255, 255))
            m.save("text.png")
            mark = m

        if isinstance(mark, Photo):
            mark.alpha(100).transparent((255, 255, 255))
            self.paste(mark, box=box, mask=mark)
        return self

    # noinspection PyMethodMayBeStatic
    def lost_red(self, pixels, x, y, channels):
        a = 255
        if channels == 3:
            r, g, b = pixels[x, y]
        else:
            r, g, b, a = pixels[x, y]

        if channels == 3:
            return r, 0, b
        else:
            return r, 0, b, a

    def process_pixels(self, func):
        im = self.base_obj
        width, height = im.size
        pixels = im.load()
        channels = len(pixels[0, 0])
        for x in range(width):
            for y in range(height):
                pixels[x, y] = func(pixels, x, y, channels)
