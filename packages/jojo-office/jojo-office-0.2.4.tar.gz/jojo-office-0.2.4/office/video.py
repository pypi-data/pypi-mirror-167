import os
import subprocess
import json
import sys
import glob
import re

# document: https://ffmpeg.org/ffmpeg-filters.html
# chinese document:


def _run_command(*args, **kwargs):
    """
    run command line, return stdout output string

    :param args:    command line arguments
    :param kwargs:  options, such as 'charset', 'err_msg'
    :return:  return stdout output string
    """
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if not kwargs.get('error', False):
        if p.returncode != 0:
            msg = kwargs.get('err_msg', '')
            if msg.find('%s') < 0:
                msg = msg + ' return code %s'
            raise ValueError(msg % repr(p.returncode))
        charset = kwargs.get('charset', 'utf-8')
        out_str = out.decode(charset)
    else:
        charset = kwargs.get('charset', 'utf-8')
        out_str = err.decode(charset)
    return out_str


def _run_process(*args, pipe_stdin=False, pipe_stdout=False, pipe_stderr=False):
    stdin_stream = subprocess.PIPE if pipe_stdin else None
    stdout_stream = subprocess.PIPE if pipe_stdout else None
    stderr_stream = subprocess.PIPE if pipe_stderr else None
    return subprocess.Popen(args, stdin=stdin_stream, stdout=stdout_stream, stderr=stderr_stream)


def _run_command_each_line(*cmd):
    popen = subprocess.Popen(cmd, stderr=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stderr.readline, ""):
        yield stdout_line
    if popen.stderr:
        popen.stderr.close()
    return_code = popen.wait()
    yield "@returncode@" + str(return_code)


# 文件信息类
class Info:
    """ 文件信息类 """
    # command line: ffprobe -v quiet -print_format json -show_format -show_streams '/path/media/video.mp4'
    class _Stream:
        def __init__(self, stream, filename=None):
            self.filename = filename
            self.data = stream if isinstance(stream, dict) else {}

        def is_empty(self):
            return len(self.data) == 0

        def get(self, key, default=''):
            return self.data.get(key, default)

        def _get_int(self, key):
            """ get an integer value """
            s = self.get(key)
            # noinspection PyBroadException
            try:
                return int(s)
            except Exception:
                return

        def _get_float(self, key):
            """ get a float value """
            s = self.get(key)
            # noinspection PyBroadException
            try:
                if s.find('/') > 0:
                    num = s[:s.find('/')].strip()  # num是numerator，分子
                    den = s[s.find('/') + 1:].strip()  # den是denominator，分母
                    num = int(num)
                    den = int(den)
                    rate = round(num / den, 2)
                    rate = int(rate) if rate == int(rate) else rate
                    return rate
                else:
                    num = round(float(s), 2)
                    return num
            except Exception:
                return

        @property
        def codec(self):
            """ 压缩编码 """
            return self.get('codec_name')

        @property
        def bit_rate(self):
            """ 码率 （单位: bps，每秒比特数） """
            return self._get_int('bit_rate')

        @property
        def duration(self):
            """ 时长(秒) """
            return self._get_float('duration')

        @property
        def length(self):
            """ 时长(秒) , （length 是 duration的别名）"""
            return self._get_float('duration')

        def __repr__(self):
            return repr(self.data)

    class _AudioInfo(_Stream):
        @property
        def sample_rate(self):
            """ 采样率 (单位: Hz 赫兹) """
            return self._get_int('sample_rate')

        @property
        def channels(self):
            """
            音频通道数量 (单位: 个)

            例如： channels=1 表示是单声道
            """
            return self._get_int('channels')

    class _VideoInfo(_Stream):
        @property
        def width(self):
            """ 画面宽度 (单位: pixel, 像素点) """
            return self._get_int('width')

        @property
        def height(self):
            """ 画面高度 (单位: pixel, 像素点) """
            return self._get_int('height')

        @property
        def pixel_format(self):
            """ 像素格式 """
            return self.get('pix_fmt')

        @property
        def frame_rate(self):
            """ 帧率，每秒多少帧 """
            return self._get_float('r_frame_rate')  # avg_frame_rate 是平均值

        @property
        def fps(self):
            """ 帧率，每秒多少帧。 fps 是 frame_rate 的别名 """
            return self.frame_rate

        @property
        def frame_count(self):
            """ 总帧数 """
            return self._get_int('nb_frames')

        def key_frames(self):
            # use ffprobe to find key frames
            # ffprobe -loglevel error -select_streams v:0 -show_entries packet=pts_time,flags
            # -of csv=print_section=0 input.mp4
            args = ('ffprobe', '-loglevel', 'error', '-select_streams', 'v:0', '-show_entries',
                    'packet=pts_time,flags', '-of', 'csv=print_section=0', self.filename)
            s = _run_command(*args)
            lines = s.split("\n")
            result = []
            for index, line in enumerate(lines):
                if line.find('K') > 0:
                    result.append(index)
            return result

    def __init__(self, filename):
        self.info = {}
        self.filename = filename
        self._probe()

    def _probe(self):
        filename = self.filename
        if not os.path.exists(filename):
            raise FileExistsError(filename)
        # run ffprobe command:
        # ffprobe -v quiet -print_format json -show_format -show_streams '/path/media/video.mp4'
        args = list()
        ffprobe = 'ffprobe'
        args += [ffprobe, '-v', 'quiet', '-print_format', 'json', '-show_format', '-show_streams', filename]
        out_str = _run_command(*args, err_msg='cannot open file %s, ' % repr(filename))
        self.info = json.loads(out_str)

    def _find_stream(self, codec_type, index):
        index = index if isinstance(index, int) else 0
        index = 0 if index < 0 else index

        count = 0
        if isinstance(self.info, dict):
            streams = self.info.get('streams', [])
            for stream in streams:
                if stream.get('codec_type', '') == codec_type:
                    if count == index:
                        return stream
        return {}

    def _count(self, codec_type):
        count = 0
        if isinstance(self.info, dict):
            streams = self.info.get('streams', [])
            for stream in streams:
                if stream.get('codec_type', '') == codec_type:
                    count += 1
        return count

    @property
    def audio_count(self):
        """
        :return: 音频流的数量
        """
        return self._count('audio')

    @property
    def video_count(self):
        """
        :return: 视频流的数量
        """
        return self._count('video')

    def audio(self, index=0):
        """
        取得音频流

        :param index: (可选)第几路，默认值是0
        :return:
        """
        stream = self._find_stream('audio', index)
        return Info._AudioInfo(stream)

    def video(self, index=0):
        """
        取得视频流

        :param index: (可选)第几路，默认值是0
        :return:
        """
        stream = self._find_stream('video', index)
        return Info._VideoInfo(stream, self.filename)

    @property
    def acodec(self):
        """ 音频压缩编码 """
        return self.audio().codec

    @property
    def vcodec(self):
        """ 视频压缩编码 """
        return self.video().codec

    @property
    def sample_rate(self):
        """ 音频采样率 (单位: Hz 赫兹) """
        return self.audio().sample_rate

    @property
    def channels(self):
        """
        音频通道数量 (单位: 个)

        例如： channels=1 表示是单声道
        """
        return self.audio().channels

    @property
    def bit_rate(self):
        """ 码率 （单位: bps，每秒比特数） """
        if not self.video().is_empty():
            return self.video().bit_rate
        else:
            return self.audio().bit_rate

    @property
    def duration(self):
        """ 时长(秒) """
        if not self.video().is_empty():
            return self.video().duration
        else:
            return self.audio().duration

    @property
    def length(self):
        """ 时长(秒) , （length 是 duration的别名）"""
        if not self.video().is_empty():
            return self.video().length
        else:
            return self.audio().length

    @property
    def width(self):
        """ 画面宽度 (单位: pixel, 像素点) """
        return self.video().width

    @property
    def height(self):
        """ 画面高度 (单位: pixel, 像素点) """
        return self.video().height

    @property
    def pixel_format(self):
        """ 像素格式 """
        return self.video().pixel_format

    @property
    def frame_rate(self):
        """ 帧率，每秒多少帧 """
        return self.video().frame_rate

    @property
    def fps(self):
        """ 帧率，每秒多少帧。 fps 是 frame_rate 的别名 """
        return self.video().fps

    @property
    def frame_count(self):
        """ 总帧数 """
        return self.video().frame_count

    def key_frames(self):
        """ 返回一个关键帧的序列号列表"""
        return self.video().key_frames()

    def print(self):
        """ 打印简要信息 """
        print('filename:', self.filename)

        for i in range(self.audio_count):
            s = '' if self.audio_count == 1 else str(i)
            print('  audio', s, ':  codec:', repr(self.audio(i).codec),
                  ',  sample rate:', "{:,}".format(self.audio(i).sample_rate),
                  'HZ , channels:', self.audio(i).channels, ', bit rate: ',
                  "{:,}".format(self.audio(i).bit_rate), 'bps')

        for i in range(self.video_count):
            s = '' if self.video_count == 1 else str(i)
            print('  video', s, ':  codec:', repr(self.video(i).codec),
                  ', width: ', self.video(i).width, ', height: ', self.video(i).height,
                  ', length: ', self.video(i).duration, 'seconds',
                  ', frame rate:', "{:,}".format(self.video(i).frame_rate),
                  ', pixel format:', self.video(i).pixel_format,
                  )


class VCodec:
    H264 = 'h264'
    H265 = 'libx265'
    MPEG2 = 'mpeg2video'
    MPEG4 = 'mpeg4'
    VP8 = 'libvpx'
    VP9 = 'libvpx-vp9'


class ACodec:
    AAC = "aac"  # AAC (Advanced Audio Coding)
    ADPCM = "adpcm_ms"  # ADPCM Microsoft
    G726 = "g726"  # G.726 ADPCM (codec adpcm_g726)
    G711 = "pcm_alaw"  # PCM A-law / G.711 A-law
    MP3 = "mp3_mf"  # MP3 via MediaFoundation (codec mp3)


class Codec:
    def __init__(self, name, codec_type, comment):
        self.name = name
        self.type = codec_type
        self.comment = str(comment).replace('\r', '')

    def __repr__(self):
        return repr(self.comment)


class Format:
    def __init__(self, file_ext, name, demuxing, muxing, comment):
        self.file_ext = file_ext
        self.name = name
        self.demuxing = demuxing
        self.muxing = muxing
        self.comment = str(comment).replace('\r', '')

    def __repr__(self):
        return repr(self.comment)


class PixelFormat:
    YUV420P = 'yuv420p'
    RGB24 = 'rgb24'
    GRAY = 'gray'
    BGR24 = 'bgr24'


class Preset:
    ultrafast = 'ultrafast'  # 编码速度最快, 压缩率低，生成文件很大
    superfast = 'superfast'
    veryfast = 'veryfast'
    faster = 'faster'
    fast = 'fast'
    medium = 'medium'   # x264默认标准
    slow = 'slow'
    slower = 'slower'
    veryslow = 'veryslow'
    placebo = 'placebo '  # 编码速度最慢，压缩率高，生成文件小


class FilterInfo:
    class Types:
        def __init__(self, s):
            self.video = 0
            self.audio = 0
            self.number = 0
            self.source = 0
            self.count = 0
            if isinstance(s, str):
                for c in s:
                    if c == 'V':
                        self.video += 1
                    elif c == 'A':
                        self.audio += 1
                    elif c == 'N':
                        self.number += 1
                    elif c == '|':
                        self.source += 1
            self.count = self.video + self.audio

        def __repr__(self):
            return repr(['V' * self.video, 'A' * self.audio, 'S' * self.source, 'N' * self.number])

    def __init__(self, name, inputs, outputs, comment, timeline=False):
        self.name = name
        self.inputs = FilterInfo.Types(inputs)
        self.outputs = FilterInfo.Types(outputs)
        self.timeline = timeline
        self.comment = str(comment).replace('\r', '')

    def __repr__(self):
        return repr(self.comment)


# Capacity of ffmpeg
class Capacity:
    _formats = None
    _vcodecs = None
    _acodecs = None
    _scodecs = None
    _filters = None

    @staticmethod
    def _array_strip(arr):
        """ delete empty item in the array """
        ret = []
        for item in arr:
            if item:
                ret.append(item)
        return ret

    @staticmethod
    def _get_formats():
        """ get ffmpeg supported file formats """
        s = _run_command('ffmpeg', '-formats')
        lines = s.split('\n')
        started = False
        Capacity._formats = {}
        for line in lines:
            if started:
                words = Capacity._array_strip(line.split(' '))
                if len(words) >= 2 and words[1]:
                    demuxing = words[0].find('D') >= 0
                    muxing = words[0].find('E') >= 0
                    name = words[1]
                    file_ext = '.' + name.lower()
                    Capacity._formats[file_ext] = Format(file_ext, name, demuxing, muxing, ' '.join(words[2:]))
            elif line.find('--') >= 0:
                started = True

    @staticmethod
    def _get_codecs():
        """ get ffmpeg support codecs """
        s = _run_command('ffmpeg', '-codecs')
        lines = s.split('\n')
        started = False
        Capacity._vcodecs = {}
        Capacity._acodecs = {}
        Capacity._scodecs = {}
        for line in lines:
            if started:
                words = Capacity._array_strip(line.split(' '))
                if len(words) >= 2:
                    name = words[1]
                    if words[0].find('V') >= 0:
                        Capacity._vcodecs[name] = Codec(name, 'video', ' '.join(words[2:]))
                    elif words[0].find('A') >= 0:
                        Capacity._acodecs[name] = Codec(name, 'audio', ' '.join(words[2:]))
                    elif words[0].find('S') == 0:
                        Capacity._scodecs[name] = Codec(name, 'subtitle', ' '.join(words[2:]))
            elif line.find('----') >= 0:
                started = True

    @staticmethod
    def _get_filters():
        """ get ffmpeg support codecs """
        s = _run_command('ffmpeg', '-filters')
        lines = s.split('\n')
        started = False
        Capacity._filters = {}
        for line in lines:
            if started:
                words = Capacity._array_strip(line.split(' '))
                if len(words) >= 3:
                    timeline = True if words[0].find('T') >= 0 else False
                    name = words[1]
                    arr = words[2].split('->')
                    comment = ' '.join(words[3:])
                    if len(arr) == 2:
                        inputs = arr[0]
                        outputs = arr[1]
                        info = FilterInfo(name, inputs, outputs, comment, timeline)
                        Capacity._filters[name] = info
            elif line.find('or sink filter') >= 0:
                started = True

    @staticmethod
    def vcodecs():
        if not Capacity._vcodecs:
            Capacity._get_codecs()
        return Capacity._vcodecs

    @staticmethod
    def acodecs():
        if not Capacity._acodecs:
            Capacity._get_codecs()
        return Capacity._acodecs

    @staticmethod
    def scodecs():
        if not Capacity._scodecs:
            Capacity._get_codecs()
        return Capacity._scodecs

    @staticmethod
    def formats():
        if not Capacity._formats:
            Capacity._get_formats()
        return Capacity._formats

    @staticmethod
    def filters():
        if not Capacity._filters:
            Capacity._get_filters()
        return Capacity._filters

    @staticmethod
    def get_filter_info(name) -> FilterInfo:
        if name in Capacity.filters():
            return Capacity.filters()[name]

    @staticmethod
    def devices():
        lines = _run_command('ffmpeg', '-devices').split('\n')
        result = {}
        started = False
        for line in lines:
            if started:
                words = line.split(" ")
                words = Capacity._array_strip(words)
                if len(words) > 2:
                    result[words[1]] = ' '.join(words[1:])
            elif line.find("--") >= 0:
                started = True
        return result

    @staticmethod
    def dshow_devices():
        result = {}
        if 'dshow' in Capacity.devices():
            # ffmpeg -list_devices true -f dshow -i dummy
            args = ('ffmpeg', '-list_devices', '1', '-f', 'dshow', '-i', 'dummy')
            p = _run_command(*args, error=True)
            lines = p.split('\n')
            found = False
            for line in lines:
                line = line.replace('\r', '')
                if found:
                    if line.find('Alternative name') >= 0:
                        p1 = line.find('"')
                        if p1 > 0:
                            line = line[p1+1:]
                            p2 = line.find('"')
                            name = line[:p2]
                            if name:
                                result[found] = name
                    found = False
                elif line.find('(video)') >= 0:
                    found = 'video'
                elif line.find('(audio)') >= 0:
                    found = 'audio'
        return result


class Position:
    @staticmethod
    def validate(s):
        """
        Whether the string is a valid time string

        :param s: the string
        :return: True of False
        """
        if isinstance(s, str):
            for c in s:
                if ('0' <= c <= '9') or c == ':' or c == '.':
                    pass
                else:
                    return False
            arr = s.split(':')
            if len(arr) <= 3:
                return True
        elif isinstance(s, int) or isinstance(s, float):
            return True
        return False

    def __init__(self, val=None):
        self._seconds = 0
        self.load(val)

    def load(self, s):
        if s is None:
            return

        if isinstance(s, int) or isinstance(s, float):
            self._seconds = s
            return

        if not isinstance(s, str) or not Position.validate(s):
            raise ValueError("expect 'hh:mm:ss' or int, but %s is met" % repr(s))

        arr = s.split(':')
        if len(arr) == 1:
            arr.insert(0, '0')
            arr.insert(0, '0')
        elif len(arr) == 2:
            arr.insert(0, '0')

        hour = minute = second = 0
        for index, item in enumerate(arr):
            if index == 0:
                hour = int(item)
            elif index == 1:
                minute = int(item)
            elif index == 2:
                if item.find('.') >= 0:
                    second = float(item)
                else:
                    second = int(item)
        self._seconds = hour * 3600 + minute * 60 + second

    def from_frame(self, frame, frame_rate):
        seconds = frame / frame_rate
        self.load(seconds)
        return self

    def to_frame(self, frame_rate):
        return round(self.seconds * frame_rate)

    @property
    def seconds(self):
        return self._seconds

    def __repr__(self):
        n = int(self._seconds)
        f = self._seconds - n
        hour = n // 3600
        n = n % 3600
        minute = n // 60
        n = n % 60
        if f != 0:
            n = n + f
        if isinstance(self._seconds, int):
            return '%02d:%02d:%02d' % (hour, minute, int(n))
        else:
            return '%02d:%02d:%04.2f' % (hour, minute, n)


class Time:
    def __init__(self, start_time, end_time):
        self.start = Position(start_time).seconds
        self.end = Position(end_time).seconds

    def expr(self):
        return "enable='between(t,{},{})'".format(self.start, self.end)


class Util:
    @staticmethod
    def is_http_url(s):
        s = s.lower().strip()
        if s.startswith('http://') or s.startswith('https://'):
            return True
        return False

    @staticmethod
    def replace_key(dict1, old_key, new_key):
        if old_key in dict1:
            dict1[new_key] = dict1[old_key]
            del dict1[old_key]

    @staticmethod
    def has_chinese(s):
        for ch in s:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

    @staticmethod
    def to_frame(time, frame_rate):
        if isinstance(time, int):
            return time
        elif Position.validate(time):
            t = Position(time)
            return round(t.seconds * frame_rate)
        else:
            raise ValueError('time format is invalid : %s' % repr(time))

    @staticmethod
    def options_to_args(options):
        result = []
        for item in options:
            if isinstance(item, list) or isinstance(item, tuple):
                if len(item) == 2:
                    key = item[0]
                    value = str(item[1])  # TODO escape
                    # if index is not None:
                    #     key += ':' + str(index)
                    result.append(key)
                    if value:
                        result.append(value)
        return result

    @staticmethod
    def escape(s, escape_chars):
        ret = ''
        for c in s:
            if escape_chars.find(c) >= 0:
                ret += '\\' + c
            else:
                ret += c
        return ret

    @staticmethod
    def get_file_ext(filename):
        if filename.rfind('.') > 0:
            return filename[filename.rfind('.'):].lower()
        return ''

    @staticmethod
    def is_audio_only(file_ext):
        if file_ext in ['.wav', '.flac', '.ac3', '.ape', '.ast', '.binka', '.g722', '.g726',
                        '.g729', '.gsm', '.mca', '.mp2', '.mp3', '.oga', '.pcm']:
            return True
        return False

    @staticmethod
    def is_video_only(file_ext):
        """ 根据文件扩展名判断 该类型文件只能包含图像，不能包含声音 """
        if file_ext in ['.gif', '.cdg', '.ico', '.jpg', '.jpeg', '.ogv', '.png', '.pcx', '.webp']:
            return True
        return False

    @staticmethod
    def is_picture(file_ext):
        if file_ext in ['.jpg', '.jpeg', '.png', '.gif']:
            return True
        return False


class Filter:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.in_tags = []
        self.out_tags = []
        self.arguments = ''
        self.args = None
        self.kwargs = None
        self.enable_time = None
        self.load(*args, **kwargs)

    def load(self, *args, **kwargs):
        params = []
        for item in args:
            if isinstance(item, Time):
                self.enable_time = item
            else:
                params.append(item)
        self.args = params
        self.kwargs = kwargs

    def expr(self):
        ret = ''

        # write in_labels
        for label in self.in_tags:
            ret += '[' + label + ']'

        ret += self.name
        if len(self.args) > 0 or len(self.kwargs) > 0:
            ret += '='

        # write enable
        count = 0
        if isinstance(self.enable_time, Time):
            ret += self.enable_time.expr()
            count += 1

        # write args
        for arg in self.args:
            if count > 0:
                ret += ':'
            s = str(arg)
            if s.find(' ') >= 0:
                s = '"' + s + '"'
            ret += Util.escape(s, ":,\\")
            count += 1

        # write kwargs
        for key in self.kwargs:
            val = self.kwargs[key]
            if count > 0:
                ret += ':'
            count += 1
            ret += key
            if val is not None:
                ret += '='
                s = str(val)
                if s.find(' ') >= 0:
                    s = "'" + s + "'"
                ret += Util.escape(s, ":,\\")

        # write out_labels
        for label in self.out_tags:
            ret += '[' + label + ']'

        return ret


class Task:

    def __init__(self):
        self.counter = {}
        self.inputs = []
        self.outputs = []
        self.output_options = []
        self.overwrite = True
        self.filter_records = []

    def append_output_options(self, key, value=None, prefix='-'):
        """
        增加一个设置项

        :param key:    键名
        :param value:  键值
        :param prefix: （可选)前缀字符
        :return: self
        """
        if prefix and not key.startswith(prefix):
            key = prefix + key
        self.output_options.append((key, value))
        return self

    def get_output_options(self, key, default=None):
        for item in self.output_options:
            if item[0] == key:
                return item[1]
        return default

    def set_output_options(self, key, value=None, prefix='-'):
        if prefix and not key.startswith(prefix):
            key = prefix + key
        for item in self.output_options:
            if item[0] == key:
                item[1] = value
                return self
        return self.append_output_options(key, value, prefix)

    def remove_output_options(self, key):
        for item in self.output_options:
            if item[0] == key:
                self.output_options.remove(item)
                break

    def new_label(self, tag):
        n = self.counter.get(tag, 0)
        self.counter[tag] = n + 1
        return 's' + tag + str(n)

    def input(self, filename, **kwargs):
        i = InputStream(filename, **kwargs)
        i.task = self
        i.tag = str(len(self.inputs))
        self.inputs.append(i)
        return i

    def merge_input(self, stream):
        if isinstance(stream, InputStream):
            if stream not in self.inputs:
                self.inputs.append(stream)
                stream.tag = str(len(self.inputs)-1)
                stream.task = self
        return stream

    def save(self, stream, filename, *args, **kwargs):
        if 'run' in kwargs:
            run = kwargs.pop('run')
        else:
            run = True

        ext = Util.get_file_ext(filename)
        if Util.is_audio_only(ext):
            self.append_output_options('vn')
        elif Util.is_video_only(ext):
            if Util.is_picture:
                self.append_output_options('format', 'image2')
                self.append_output_options('vcodec', 'mjpeg')
            self.append_output_options('an')
        else:
            # self.output = ffmpeg.output(self.audio, self.video, save_filename, **opts)
            pass

        output = OutputStream(stream, filename, **kwargs)
        output.overwrite = self.overwrite
        output.task = self
        for item in self.output_options:
            key, value = item[0], item[1]
            output.append_option(key, value, '')
        self.outputs.append(output)

        args = self.compile()

        if run:
            return self.run(args, run=run)
        else:
            # print(args)
            s = ' '.join(args)
            print(s)
            return s

    def create_filter(self, in_streams, name, *args, **kwargs):
        info = Capacity.get_filter_info(name)
        if info is None:
            raise ValueError('filter %s is not supported' % repr(name))

        f = Filter(name, *args, **kwargs)

        if in_streams is None:
            in_streams = []
        elif isinstance(in_streams, BaseStream):
            in_streams = [in_streams]

        if info.inputs.number > 0:
            pass
        elif len(in_streams) != info.inputs.count:
            raise ValueError('filter %s accept %s input streams, but %s is found'
                             % (repr(name), info.inputs.count, len(in_streams)))

        for item in in_streams:
            f.in_tags.append(item.tag)

        if info.outputs.video > 0:
            for i in range(info.outputs.video):
                f.out_tags.append(self.new_label('v'))
        elif info.outputs.audio > 0:
            for i in range(info.outputs.audio):
                f.out_tags.append(self.new_label('v'))
        elif info.outputs.number > 0:
            if name in ['select', 'concat']:
                count = 1
            else:
                count = 2
                if len(args) == 1 and isinstance(args[0], int):
                    count = args[0]
            for i in range(count):
                f.out_tags.append(self.new_label('n'))

        self.filter_records.append(f)

        ret = []
        for tag in f.out_tags:
            s = Stream(tag)
            s.task = self
            ret.append(s)

        if len(ret) == 1:
            return ret[0]
        else:
            return ret

    def run(self, args, **kwargs):
        r = kwargs.get('run', True)
        if isinstance(r, str):
            pipe_stdout = False
            pipe_stdin = False
            pipe_stderr = False
            if r.find('pipe_stdout') >= 0:
                pipe_stdout = True
            if r.find('pipe_stdin') >= 0:
                pipe_stdin = True
            if r.find('pipe_stderr') >= 0:
                pipe_stderr = True
            return _run_process(*args, pipe_stdin=pipe_stdin, pipe_stdout=pipe_stdout, pipe_stderr=pipe_stderr)

        print(' '.join(args))
        status = 0
        return_code = 0
        for line in _run_command_each_line(*args):
            if line.find('@returncode@') == 0:
                return_code = line[len('@returncode@')]
                break
            if status == 0:
                if line.find('frame=') >= 0:
                    status = 1
                elif line.find('Error') >= 0:
                    print(line, end='')
                    status = 2
            elif status == 1:
                line = line.strip()
                print('\r'+line, end='')
            elif status == 2:
                print(line, end='')
        if return_code == '0':
            print('\nSuccess!')
            if len(self.outputs) > 0 and os.path.exists(self.outputs[0].filename):
                return Video(self.outputs[0].filename)
        else:
            print('\nFailed, return code = ' + str(return_code))

    def compile(self):
        args = []
        ffmpeg = 'ffmpeg'
        args += [ffmpeg]

        for item in self.inputs:
            args += item.cmd_args()

        if len(self.filter_records) > 0:
            s = ''
            for f in self.filter_records:
                if isinstance(f, Filter):
                    if len(s) > 0:
                        s += ';'
                    s += f.expr()
            if len(s) > 0:
                args += ['-filter_complex', s]

        for item in self.outputs:
            args += item.cmd_args()

        return args


class BaseStream:
    # noinspection PyTypeChecker
    def __init__(self):
        self._options = []
        self.tag = None
        self.task: Task = None

    def append_option(self, key, value=None, prefix='-'):
        """
        增加一个设置项

        :param key:    键名
        :param value:  键值
        :param prefix: （可选)前缀字符
        :return: self
        """
        if prefix and not key.startswith(prefix):
            key = prefix + key
        self._options.append((key, value))
        return self

    def cmd_args(self):
        """ 返回命名行参数列表"""
        result = []
        for item in self._options:
            if isinstance(item, list) or isinstance(item, tuple):
                if len(item) == 2:
                    key = item[0]
                    value = item[1]
                    result.append(key)
                    if value is not None:
                        value = Util.escape(str(value), ' -')  # TODO escape
                        result.append(value)
        return result

    def _short_hash(self):
        return '{:x}'.format(abs(hash(self)))[:12]

    def __repr__(self):
        name = self.__class__.__name__
        return '%s(tag=%s)@%s' % (name, self.tag, self._short_hash())


class Curves:
    Vintage = 'vintage'
    Negative = 'negative'
    ColorNegative = 'color_negative'

    @staticmethod
    def lighter(strength=1, channel='all'):
        return {channel: 0.5 + strength * 0.05}

    @staticmethod
    def contrast(strength=1, channel='all'):
        delta = strength * 0.025
        return {channel: [0, 0.25-delta,  0.5, 0.75+delta, 1]}

    class Curve:
        def __init__(self):
            self.points = {}

        def __getitem__(self, item):
            if item in self.points:
                return self.points[item]
            return item

        def __setitem__(self, key, value):
            self.points[key] = value

        def set_values(self, values):
            if values is None:
                return

            if isinstance(values, int) or isinstance(values, float):
                values = [0, values, 1]
            elif isinstance(values, str):
                self.from_str(values)
                return

            if isinstance(values, list) or isinstance(values, tuple):
                if len(values) == 1:
                    self.points[0.5] = values[0]
                    return

                delta = round(1.0 / (len(values) - 1), 3)
                i = 0
                for v in values:
                    if i >= 1:
                        i = 1
                    self.points[i] = v
                    i += delta

        def from_str(self, s):
            arr = s.split(' ')
            for a in arr:
                if a == '':
                    continue
                pos = a.find('/')
                if pos >= 0:
                    key = float(a[:pos])
                    value = float(a[pos+1:])
                else:
                    key = value = float(a)
                self.points[key] = value

        def to_str(self):
            s = ''
            for key in self.points:
                if len(s) > 0:
                    s += ' '
                s += str(key) + '/' + str(self.points[key])
            return s

        def __repr__(self):
            return self.to_str()

        def is_empty(self):
            return len(self.points) == 0

    def __init__(self, all=None, r=None, g=None, b=None):
        self.all = Curves.Curve()
        self.r = Curves.Curve()
        self.g = Curves.Curve()
        self.b = Curves.Curve()
        if isinstance(all, dict):
            self.from_dict(all)
        else:
            self.all.set_values(all)
        self.r.set_values(r)
        self.g.set_values(g)
        self.b.set_values(b)

    def to_dict(self, dict1=None):
        if dict1 is None:
            dict1 = {}
        if not self.all.is_empty():
            dict1['all'] = self.all.to_str()
        if not self.r.is_empty():
            dict1['r'] = self.r.to_str()
        if not self.g.is_empty():
            dict1['g'] = self.g.to_str()
        if not self.b.is_empty():
            dict1['b'] = self.b.to_str()
        return dict1

    def from_dict(self, dict1):
        for item in dict1:
            if item == 'all':
                self.all.set_values(dict1[item])
            elif item == 'r':
                self.r.set_values(dict1[item])
            elif item == 'g':
                self.g.set_values(dict1[item])
            elif item == 'b':
                self.b.set_values(dict1[item])
        return self


class SelectiveColor:
    def __init__(self):
        pass

    def to_dict(self, dict1=None):
        return {}  # Todo

    def from_dict(self, dict1):
        pass  # Todo
        return self


class Transition:
    Fade = 'fade'
    WipeLeft = 'wipeleft'
    WipeRight = 'wiperight'
    WipeUp = 'wipeup'
    WipeDown = 'wipedown'
    SlideLeft = 'slideleft'
    SlideRight = 'slideright'
    SlideUp = 'slideup'
    SlideDown = 'slidedown'
    CircleCrop = 'circlecrop'
    RectCrop = 'rectcrop'
    Distance = 'distance'
    FadeBlack = 'fadeblack'
    FadeWhite = 'fadewhite'
    Radial = 'radial'
    SmoothLeft = 'smoothleft'
    SmoothRight = 'smoothright'
    SmoothUp = 'smoothup'
    SmoothDown = 'smoothdown'
    CircleOpen = 'circleopen'
    CircleClose = 'circleclose'
    VertOpen = 'vertopen'
    VertClose = 'vertclose'
    HorzOpen = 'horzopen'
    HorzClose = 'horzclose'
    DisSolve = 'dissolve'
    Pixelize = 'pixelize'
    Diagtl = 'diagtl'
    Diagtr = 'diagtr'
    Diagbl = 'diagbl'
    Diagbr = 'diagbr'
    Hlslice = 'hlslice'
    Hrslice = 'hrslice'
    Vuslice = 'vuslice'
    Vdslice = 'vdslice'
    Hblur = 'hblur'
    FadeGrays = 'fadegrays'
    Wipetl = 'wipetl'
    Wipetr = 'wipetr'
    Wipebl = 'wipebl'
    Wipebr = 'wipebr'
    Squeezeh = 'squeezeh'
    Squeezev = 'squeezev'
    ZoomIn = 'zoomin'


class Stream(BaseStream):
    def __init__(self, tag, task=None):
        super().__init__()
        self.tag = tag
        if task:
            self.task = task

    def _sub_stream(self, type_str, index=None):
        if self.tag:
            index = ':'+str(index) if index else ''
            arr = self.tag.split(':')
            if len(arr) == 1:
                return Stream(self.tag + ':' + type_str + index, self.task)
            elif len(arr) >= 1:
                if arr[1] != type_str:
                    raise ValueError('cannot extract' + type_str)
                else:
                    return Stream(arr[0] + ':' + type_str + index, self.task)
        raise ValueError('stream without tag')

    def audio(self, index=None):
        """ 取得音频流 """
        return self._sub_stream('a', index)

    def video(self, index=None):
        """ 取得视频流 """
        return self._sub_stream('v', index)

    def input(self, filename, start_time=None, end_time=None, **kwargs):
        """
        增加一个输入文件

        :param filename: 文件名
        :param start_time:    (可选)开始时间， 如: "01:13:23.45" 表示1小时13分23.45秒
        :param end_time:      (可选)结束时间
        :param kwargs:   (可选)选项
        :return:  返回新文件的流 ( Stream object )
        """
        if not isinstance(self.task, Task):
            raise ValueError('task not defined')

        if start_time is not None:
            if isinstance(start_time, str):
                kwargs['ss'] = str(Position(start_time))
            else:
                raise ValueError("start position expect time string or int, but %s is found" % repr(start_time))

        if end_time is not None:
            if isinstance(end_time, str):
                kwargs['to'] = end_time
            elif isinstance(end_time, int):
                kwargs['t'] = end_time
            else:
                raise ValueError("end position expect time string or int, but %s is found" % repr(end_time))

        return self.task.input(filename, **kwargs)

    def save(self, filename, *args, **kwargs):
        """
        将流保存为文件

        :param filename:  文件名
        :param args:      （可选)参数，如果需要多个流合并保存，请将它写入args中
        :param kwargs:    （可选)命名参数， 如果只是测试不需要运行，请设置 run=False
        :return:
        """
        if not isinstance(self.task, Task):
            raise ValueError('task not defined')
        in_streams = [self]
        params = []
        for arg in args:
            if isinstance(arg, BaseStream):
                in_streams.append(arg)
            else:
                params.append(arg)
        return self.task.save(in_streams, filename, *params, **kwargs)

    def _select_frames(self, frame, interval=None, times=None):
        """
        选择帧

        :param frame:           帧号（整数)
        :param interval:       (可选) 间隔帧数 或 时间
        :param times:          (可选) 重复多少次
        :return: self
        """
        if not isinstance(self.task, Task) or len(self.task.inputs) == 0:
            raise ValueError('task not defined')

        info = Info(self.task.inputs[0].filename)
        frame = Util.to_frame(frame, info.frame_rate)
        interval = Util.to_frame(interval, info.frame_rate)

        if not isinstance(frame, int):
            raise ValueError("expect frame in integer")

        if isinstance(interval, int) or isinstance(interval, float):
            # 间隔XX帧选择一帧
            if times:
                max_frame = round(frame + interval * times)
                condition = 'between(n,{},{})*not(mod(n,{}))'.format(frame, max_frame, round(interval))
            else:
                condition = 'get(n,{})*not(mod(n,{}))'.format(frame, round(interval))
            # select filter
            # between(n\,84\,208) 表示 帧号介于 84 到 208之间
            # not(mod(n\,20)) 表示 间隔20帧
            self.task.append_output_options('vsync', 0)
            return self.filter('select', condition)

        else:
            # 只选择一帧
            self.task.append_output_options('frames:v', 1)
            return self.filter('select', 'gte(n,{})'.format(frame))

    def snapshot(self, save_filename, start_time=0, interval=None, times=None):
        """
        截屏 （截屏一次或多次)

        :param save_filename: 存盘文件名， 例如: image_%3d.png
        :param start_time:   （可选)开始时间， 例如:  '00:13:22.5' 表示 13分22.5秒
        :param interval:     （可选)间隔时间， 例如:  '00:30' 表示 30秒, 如此参数缺省，则截屏一次
        :param times:        （可选)截屏次数, 如此参数缺省，则一直截屏到片尾
        :return:  self
        """
        if start_time == 0 and interval is None:
            v = self
            self.task.append_output_options('frames:v', 1)
        else:
            v = self._select_frames(start_time, interval, times)
        v.save(save_filename)
        self.task.remove_output_options('frames:v')
        self.task.remove_output_options('vsync')
        self.task.remove_output_options('format')
        self.task.remove_output_options('vcodec')
        return self

    def bit_rate(self, average_rate, max_rate, min_rate, buffer_size):
        """
        详细设置输出码率

        :param average_rate: 平均码率,  例如：'2200k'
        :param max_rate:     最大码率,  例如：'2200k'
        :param min_rate:     最小码率,  例如：'2200k'
        :param buffer_size:  缓冲区大小,  例如：'2200k'
        :return: self
        """
        if not isinstance(self.task, Task):
            raise ValueError('task not defined')

        self.task.append_output_options('b:v', average_rate)
        self.task.append_output_options('maxrate', max_rate)
        self.task.append_output_options('minrate', min_rate)
        self.task.append_output_options('bufsize', buffer_size)
        return self

    def cbr(self, bit_rate):
        """
        设置输出为固定码率

        :param bit_rate: 固定码率,  例如：'2200k'
        :return: self
        """
        return self.bit_rate(bit_rate, bit_rate, bit_rate, bit_rate)

    def crf(self, factor):
        """
        设置输出为固定速率系数(只适合H264编码)，用于保障画质.

        :param factor: 系数， 取值范围从 0(最好画质) 到 51(最坏画质)， 一般画质取 30
        :return: self
        """
        if not isinstance(self.task, Task):
            raise ValueError('task not defined')
        self.task.append_output_options('crf', factor)
        return self

    def vcodec(self, codec):
        """ 设置输出的视频编码 """
        if not isinstance(self.task, Task):
            raise ValueError('task not defined')
        self.task.append_output_options('vcodec', codec)
        return self

    def acodec(self, codec):
        """ 设置输出的音频编码 """
        if not isinstance(self.task, Task):
            raise ValueError('task not defined')
        self.task.append_output_options('acodec', codec)
        return self

    def filter(self, name, *args, **kwargs):
        """
        创建一个滤镜，返回滤镜产生的流

        :param name:  滤镜名称， 完整列表请参看: Capacity.filters()
        :param args:  滤镜所需的参数。如果滤镜需要多个输入流，请将它写入args中
        :param kwargs: 滤镜所需的命名参数
        :return:  返回滤镜产生的流。如果该滤镜产生多个流，则返回一个列表，每一个元素是一个流
        """
        if not isinstance(self.task, Task):
            raise ValueError('task not defined')

        in_streams = [self]
        params = []
        for arg in args:
            if isinstance(arg, BaseStream):
                in_streams.append(arg)
            else:
                params.append(arg)
        return self.task.create_filter(in_streams, name, *params, **kwargs)

    def hflip(self):
        """ 水平翻转, 返回新的流 """
        return self.filter('hflip')

    def vflip(self):
        """ 上下翻转, 返回新的流 """
        return self.filter('vflip')

    def pixel_format(self, pix_fmts):
        """ 更改 pixel format"""
        return self.filter('format', pix_fmts=pix_fmts)

    def _scale(self, ratio_or_width, height=None):
        """ 缩放 """
        # https://ffmpeg.org/ffmpeg-filters.html#Examples-106
        if height is None:
            sw = "iw*" + str(ratio_or_width)
            sh = "ih*" + str(ratio_or_width)
        else:
            sw = str(ratio_or_width)
            sh = str(height)
        return self.filter("scale", w=sw, h=sh)

    def scale(self, ratio):
        """
        比例缩放

        :param ratio: 缩放比例, 数据类型为float, 例如： 1.5 表示 150%
        :return: self
        """
        return self._scale(ratio)

    def resize(self, width, height):
        """
        调整图像大小

        :param width: 图像宽度(像素)
        :param height: 图像高度(像素)
        :return: self
        """
        return self._scale(width, height)

    def sharpen(self, strength="normal", size=None, *args):
        """
        视频锐化

        :param  strength: 强度, 可以是str 或 float
                 如为str, 可选值为 "super", "strong", "normal", "light".
                 如为float，取值范围为-4到4，正数为锐化，负数为模糊化，大小为强度
        :param  size:  (可选) 卷积子大小，取值为奇数、正整数， 如：3， 5， 7， 9
        :return: self
        """
        #
        # Example: Apply strong luma sharpen effect
        # SEE: https://ffmpeg.org/ffmpeg-filters.html#unsharp-1
        # 'unsharp=luma_msize_x=7:luma_msize_y=7:luma_amount=2.5'
        if isinstance(strength, int):
            amount = strength
            if isinstance(size, int):
                x = y = size
            else:
                x = y = 5
        elif isinstance(strength, str):
            if strength == "super":
                x = y = 9
                amount = 3
            elif strength == "strong":
                x = y = 7
                amount = 2.5
            elif strength == "light":
                x = y = 5
                amount = 0.5
            else:
                x = y = 5
                amount = 1
        else:
            raise ValueError('invalid strength %s' % strength)

        return self.filter('unsharp', *args, luma_msize_x=x, luma_msize_y=y, luma_amount=amount)

    def curves(self, *args, **kwargs):
        """ 曲线调整 """
        if not self.task:
            raise ValueError('task not defined')

        params = []
        for arg in args:
            if isinstance(arg, str):
                kwargs['preset'] = arg
            elif isinstance(arg, dict):
                Curves().from_dict(arg).to_dict(kwargs)
            elif isinstance(arg, Curves):
                arg.to_dict(kwargs)
            else:
                params.append(arg)

        f = self.filter('curves', *params, **kwargs)

        if len(self.task.inputs) > 0:
            info = Info(self.task.inputs[0].filename)
            pix_fmt = info.pixel_format
        else:
            pix_fmt = 'yuv420p'
        return f.pixel_format(pix_fmt)

    def selective_color(self, *args, **kwargs):
        """ 可选颜色调整 """
        if not self.task:
            raise ValueError('task not defined')

        params = []
        for arg in args:
            if isinstance(arg, dict):
                SelectiveColor().from_dict(arg).to_dict(kwargs)
            elif isinstance(arg, SelectiveColor):
                arg.to_dict(kwargs)
            else:
                params.append(arg)

        f = self.filter('selectivecolor', *params, **kwargs)

        if len(self.task.inputs) > 0:
            info = Info(self.task.inputs[0].filename)
            pix_fmt = info.pixel_format
        else:
            pix_fmt = 'yuv420p'
        return f.pixel_format(pix_fmt)

    def split(self, count=2):
        """ 将视频分成多路（默认是2路），返回一个Stream数组 """
        return self.filter('split', count)

    def asplit(self, count=2):
        """ 将音频分成多路（默认是2路），返回一个Stream数组 """
        return self.filter('asplit', count)

    def concat(self, *args, **kwargs):
        """ 将多路Stream首尾相连 """
        if 'fade' in kwargs:
            fade = kwargs.pop('fade')
        else:
            fade = False

        params = []
        if fade:
            for index, arg in enumerate(args):
                if isinstance(arg, Stream):
                    arg = arg.fade(0, fade)
                params.append(arg)
        else:
            params = args

        return self.filter('concat', *params, **kwargs)

    def crop(self, x, y, width, height):
        """ 截取视频画面 """
        return self.filter('crop', x=x, y=y, w=width, h=height)

    def drawbox(self, x, y, width, height, color, thickness=1, *args, **kwargs):
        """ 在视频画面上画一个方形 """
        return self.filter('drawbox', x=x, y=y, w=width, h=height, color=color, thickness=thickness, **kwargs)

    def drawtext_ex(self, *args, **kwargs):
        """
        在视频画面上打印文字
        Official Document:  https://ffmpeg.org/ffmpeg-filters.html#drawtext
        """
        return self.filter('drawtext', *args, **kwargs)

    def drawtext(self, text='', x=0, y=0, color="white", size=16, font='Sans',
                 shadowcolor="black", shadowx=1, shadowy=1, *args, **kwargs):
        """ 在视频画面上打印一串文字 """
        if Util.has_chinese(text) and font == 'Sans':
            font = '宋体' if sys.platform == 'win32' else 'simsun'

        return self.filter('drawtext', text=text, x=x, y=y, fontcolor=color, fontsize=size, font=font,
                           shadowcolor=shadowcolor, shadowx=shadowx, shadowy=shadowy,
                           *args, **kwargs)

    def hue(self, h=0, s=1, b=0, *args):
        """
        调整 h(hues)色相，s(saturation)饱和度，b（brightness）亮度

        :param h:  指定色度角的度数，默认为0
        :param s:  指定饱和度，范围[-10,10]，默认为”1”.
        :param b:  指定亮度，范围[-10,10]。默认为”0”.
        :return: self
        """
        return self.filter('hue', *args, h=h, s=s, b=b)

    def overlay(self, overlay_stream, *args, x=0, y=0, eof_action="repeat", **kwargs):
        """
        把一个图片或视频覆盖在上面

        :param overlay_stream:  被覆盖的视频
        :param x:        （可选）x坐标
        :param y:        （可选）y坐标
        :param eof_action: （可选） 遇到第二路输入结束的处理方式。接受下面的值之一：
            repeat  重复最后一帧（默认）
            endall    同时结束两个流
            pass   把第一路输入作为输出
        :param kwargs:      （可选）
        :return:
        """
        if isinstance(overlay_stream, str):
            if os.path.exists(overlay_stream):
                overlay_stream = self.task.input(overlay_stream)
        overlay_stream = self.task.merge_input(overlay_stream)
        return self.filter('overlay', overlay_stream, x=x, y=y, eof_action=eof_action, *args, **kwargs)

    def transition(self, next_stream, transition_style, **kwargs):
        if isinstance(next_stream, str):
            if os.path.exists(next_stream):
                next_stream = self.task.input(next_stream)
        next_stream = self.task.merge_input(next_stream)
        if 'duration' not in kwargs:
            kwargs['duration'] = 0.5
        if 'offset' not in kwargs:
            kwargs['offset'] = 4
        return self.filter('xfade', next_stream, transition=transition_style, **kwargs)

    def fade(self, start_time, duration, type='in', color="black"):
        start_time = Position(start_time).seconds
        duration = Position(duration).seconds
        d = {'st': start_time, 'd': duration}
        if type != 'in':
            d['t'] = type
        if color != 'black':
            d['c'] = color
        return self.filter('fade', **d)

    def get_input(self, index):
        """  取得第 index 个输入， 返回Stream """
        if not isinstance(self.task, Task):
            raise ValueError('task not defined')
        return self.task.inputs[index]

    def setpts(self, pts):
        """
         Change the PTS (presentation timestamp) of the input frames

        :param pts: 当pts为数字时， 0.5表示2倍速快动作， 2 表示2倍速慢动作，依次类推

        :return:
        """
        if isinstance(pts, int):
            if pts == 0:
                pts = "PTS-STARTPTS"
            else:
                pts = str(pts) + "*PTS"
        return self.filter('setpts', pts)

    def trim(self, start, end):
        """
        截取视频的一部分

        :param start:  开始时间, 或秒数
        :param end:    结束时间, 或秒数
        :return: self
        """
        if isinstance(start, str):
            start = Position(start).seconds
        if isinstance(end, str):
            end = Position(end).seconds
        return self.filter('trim', start=start, end=end)

    def zoompan(self, factor, **kwargs):
        """
        应用放大和摇镜头效

        :param factor: 缩放比例，默认是1
        :return: self
        """
        # x = 'if(lte(on,-1),(iw-iw/zoom)/2,x+3)'
        # y = 'if(lte(on,1),(ih-ih/zoom)/2, y)'
        x = 'x+3'
        y = '-10'
        # ffmpeg -i input.mp4 -vf "zoompan=z='if(lte(mod(time,10),3),2,1)':
        # d=1:x=iw/2-(iw/zoom/2):y=ih/2-(ih/zoom/2):fps=30" output.mp4
        # return self.filter('zoompan', z=factor, x=x, y=y, d=150)
        # z = 'if(lte(mod(time,10),3),2,1)'
        # x = 'iw/2-(iw/zoom/2)'
        # y = 'ih/2-(ih/zoom/2)'
        # https://blog.csdn.net/qq_21275565/article/details/103671164
        return self.filter('zoompan', z=factor, x=x, y=y, d=150, **kwargs)

    def color(self, c, alpha=None, **kwargs):
        if alpha is not None:
            c = str(c) + '@' + str(alpha)
        return self.task.create_filter([], 'color', c=c, **kwargs)


class OutputStream(BaseStream):
    def __init__(self, in_streams, filename, **kwargs):
        super().__init__()
        self.in_streams = []
        self.filename = filename
        self.overwrite = True
        for key in kwargs:
            self.append_option(key, kwargs[key])

        if isinstance(in_streams, BaseStream):
            in_streams = [in_streams]
        if isinstance(in_streams, tuple):
            in_streams = list(in_streams)

        if not isinstance(in_streams, list):
            raise ValueError('output must has in streams')

        self.in_streams = in_streams

    def cmd_args(self):
        result = []
        if self.filename != 'pipe:':
            for stream in self.in_streams:
                if stream.tag:
                    if '0' <= stream.tag[0] <= '9':
                        tag = stream.tag
                    else:
                        tag = '[%s]' % stream.tag
                    result += ['-map', tag]
                else:
                    raise ValueError('stream has not tag')

        result += super().cmd_args()
        if self.overwrite and self.filename != 'pipe:':
            result += ['-y']
        result += [self.filename]
        return result

    def __repr__(self):
        name = self.__class__.__name__
        return '%s(tag=%s, file=%s)@%s' % (name, self.tag, repr(self.filename), self._short_hash())


class InputStream(Stream):
    def __init__(self, filename, **kwargs):
        super().__init__(None)
        if filename == 'camera':
            # open camera
            self._load_camera()
        elif filename == 'desktop':
            # open camera
            self._load_desktop()
        elif filename is None:
            self.filename = None
        else:
            # open file
            if filename == 'pipe:' or os.path.exists(filename):
                self.filename = filename
            else:
                raise FileExistsError('file %s not exists' % repr(filename))

        # set options
        Util.replace_key(kwargs, 'time', 't')
        Util.replace_key(kwargs, 'size', 's')
        Util.replace_key(kwargs, 'frame_rate', 'r')
        Util.replace_key(kwargs, 'start_time', 'ss')
        for key in kwargs:
            self.append_option(key, kwargs[key])

    def _load_desktop(self):
        if sys.platform == 'win32':
            if 'gdigrab' in Capacity.devices():
                self.filename = 'desktop'
                self.append_option('f', 'gdigrab')
                self.append_option('r', 20)
            else:
                raise ValueError('cannot find gdigrab')
        else:
            raise ValueError('camera not supported in current OS')

    def _load_camera(self):
        if sys.platform == 'win32':
            if 'vfwcap' in Capacity.devices():
                self.filename = '0'
                self.append_option('f', 'vfwcap')
            else:
                raise ValueError('cannot find vfwcap')
        else:
            raise ValueError('camera not supported in current OS')

    def cmd_args(self):
        result = super().cmd_args()
        if self.filename is not None:
            result += ['-i', self.filename]
        return result

    def __repr__(self):
        name = self.__class__.__name__
        return '%s(tag=%s, file=%s)@%s' % (name, self.tag, repr(self.filename), self._short_hash())


class Video(InputStream):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        self.task = Task()
        self.task.inputs.append(self)
        self.tag = '0'

    def play(self, win_width=None, win_height=None):
        args = ['ffplay']
        args += self.cmd_args()
        if win_width:
            args += ['-x', str(win_width)]
        if win_height:
            args += ['-y', str(win_height)]
        _run_command(*args)

    def process_each_frame(self, func, save_filename=None):
        """
        逐帧处理视频图像

        :param func:   处理函数。当遇到每一帧图像，将调用此函数一次，传入 RGA形式的图像数据(bytes) 和 size(tuple)。
                       该函数必须返回图像数据(bytes). <br>
             该函数示例： <br>
             def process_func(frame_rgb_bytes, size_tuple):
                 # use PIL to process image
                 img = Image.frombytes('RGB', size, rgb_bytes)
                 draw = ImageDraw.Draw(img)
                 draw.line((0, 0) + img.size, fill="blue")
                 return frame_rgb_bytes
            <br>
        :param save_filename: (可选) 处理后的视频存盘文件名
        :return: None
        """
        if not isinstance(self.task, Task):
            raise ValueError('task not defined')

        if len(self.task.inputs) > 0:
            # get information from input 0
            info = Info(self.task.inputs[0].filename)
            width = info.video().width
            height = info.video().height
            pix_fmt = info.pixel_format
        else:
            raise ValueError("no input")

        # create process
        process_in = self.save('pipe:', f='rawvideo', pix_fmt='rgb24', run='pipe_stdout')

        # create output process if save_filename is specified
        process_out = None
        if save_filename is not None:
            v = Video('pipe:', f='rawvideo', pix_fmt='rgb24', s='{}x{}'.format(width, height))
            process_out = v.save(save_filename, pix_fmt=pix_fmt, run='pipe_stdin, pipe_stderr')

        # process frames one by one
        while True:
            # get frame byte from process_in stdout
            frame_bytes = process_in.stdout.read(width * height * 3)
            if not frame_bytes:
                break    # exit when no data
            # call func
            if callable(func):
                frame_bytes = func(frame_bytes, (width, height))
            # write to process_out stdin
            if process_out and process_out.stdin and frame_bytes:
                process_out.stdin.write(frame_bytes)

        if process_out:
            if process_out.stdin:
                process_out.stdin.close()
            if process_out.stderr:
                process_out.stderr.close()

        process_in.wait()

        if process_out:
            process_out.wait()


class Photos:
    def __init__(self, filename):
        self.task = Task()
        self.load_files(filename)
        self.zoompans = []

    def load_files(self, filenames):
        if isinstance(filenames, str):
            filenames = [filenames]

        for filename in filenames:
            if filename.find('*') >= 0:    # such as 'image_*.jpg'
                file_list = glob.glob('*.jpg')
                for f in file_list:
                    self.task.input(f)
            elif re.search(r'%\d*d', filename):  # such as 'image_%3d.jpg'
                m = re.search(r'%\d*d', filename)
                prefix = filename[:m.span()[0]]
                suffix = filename[m.span()[1]:]
                formats = m.group()
                if len(formats) > 2 and formats[1:2] != '0':
                    formats = formats[:1] + '0' + formats[1:]
                i = 0
                while True:
                    filename = prefix + (formats % i) + suffix
                    if os.path.exists(filename):
                        self.task.input(filename)
                        i = i + 1
                    elif os.path.exists(prefix + (formats % (i + 1)) + suffix):
                        i = i + 1
                    else:
                        break
            else:
                if os.path.exists(filename):  # a single file
                    self.task.input(filename)
                else:
                    raise FileNotFoundError('file %s not found' % repr(filename))

    def zoompan(self, index):
        s = self.task.inputs[index]
        z = s.zoompan(1.5, s='hd720')
        self.zoompans.append(z)

    def z(self):
        for i in range(len(self.task.inputs)):
            self.zoompan(i)
        return self

    def save(self, filename):
        s = self.zoompans[0]
        args = []
        for index, item in enumerate(self.zoompans):
            if index > 0:
                args.append(item)
        s = s.concat(*args)
        s = s.pixel_format('yuv420p')
        self.task.save(s, filename)


class Source:
    DESKTOP = 'desktop'
    CAMERA = 'camera'
