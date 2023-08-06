import inspect
from types import MethodType


class SuperObject:
    """
    SuperObject

    support dynamically add methods to base object.

    """

    @staticmethod
    def _is_function_of(func, clz):
        """ whether func is a function defined in cls """
        if hasattr(func, '__qualname__'):
            qualname = func.__qualname__
            if qualname.find(clz.__name__ + '.') == 0:
                if qualname.find('_subclass') < 0:
                    return True
        return False

    @staticmethod
    def merge_methods(dst_obj, src_class):
        """
        read the methods of the src class, add to the object

        :param dst_obj:   the object which need to add method
        :param src_class:  a class which provide methods
        :return: return modified object
        """
        if dst_obj is None or src_class is None:
            return dst_obj

        if inspect.isclass(src_class):
            # analysis each attribute of the src_class
            for name, attr in inspect.getmembers(src_class):
                if isinstance(attr, property) and SuperObject._is_function_of(attr.fget, src_class):
                    # when a property of extend_class is met
                    # dynamically add property getter function as a method to the object
                    if attr.fget and not hasattr(dst_obj, 'get_' + name):
                        setattr(dst_obj, 'get_' + name, MethodType(attr.fget, dst_obj))
                    # dynamically add property setter function as a method to the object
                    if attr.fset and not hasattr(dst_obj, 'set_' + name):
                        setattr(dst_obj, 'set_' + name, MethodType(attr.fset, dst_obj))
                elif inspect.isfunction(attr) and SuperObject._is_function_of(attr, src_class):
                    # when a method is met,  dynamically add method to obj dynamically
                    setattr(dst_obj, name, MethodType(attr, dst_obj))
            return dst_obj
        else:
            raise ValueError('expect class type but %s is found' % repr(type(src_class)))

    def __init__(self, base_obj=None):
        self._methods = {}
        self._properties = {}
        if not hasattr(self, 'base_obj') or base_obj:
            # print('set base_obj')
            self.base_obj = base_obj
            if base_obj is not None:
                self._build_methods()

    def __getattribute__(self, attr):
        """ if self has the attr, return it. else if base_obj has the attr, return it."""

        # get attribute from self
        # http://www.sefidian.com/2021/06/06/python-__getattr__-and-__getattribute__-magic-methods/
        __dict__ = super().__getattribute__('__dict__')
        if attr in __dict__:
            return super().__getattribute__(attr)

        # get attribute from _methods
        if '_methods' in __dict__:
            methods = super().__getattribute__('_methods')
            if methods and attr in methods:
                m = methods[attr]
                return m

        # get attribute from base_obj
        if 'base_obj' in __dict__:
            if hasattr(super().__getattribute__('base_obj'), attr):
                return getattr(super().__getattribute__('base_obj'), attr)

        return super().__getattribute__(attr)

    def __setattr__(self, attr, value):
        """ if base_obj has the attr, set base_obj value. else if self has the attr, set its value."""
        # get dict of self
        __dict__ = super().__getattribute__('__dict__')

        # if value is a function, add it as method
        if inspect.isfunction(value):
            return self.add_method(attr, value)

        # if base_obj has the attribute, set the value to attribute of the base_obj
        if 'base_obj' in __dict__:
            if hasattr(super().__getattribute__('base_obj'), attr):
                setattr(super().__getattribute__('base_obj'), attr, value)
                return

        # set the value of the attribute of self
        super().__setattr__(attr, value)

    def _build_methods(self):
        # get method of base_obj
        if self.base_obj is not None:
            for name, attr in inspect.getmembers(self.base_obj):
                if name.startswith('__'):
                    continue
                if inspect.ismethod(attr) or inspect.isbuiltin(attr):
                    self._methods[name] = attr

        # get method of self
        for name, attr in inspect.getmembers(type(self)):
            if name.startswith('__'):
                continue
            if inspect.isfunction(attr) or inspect.isbuiltin(attr):
                self._methods[name] = MethodType(attr, self)

    @property
    def methods(self):
        """ return the methods """
        if not self._methods:
            self._build_methods()
        return self._methods

    @property
    def properties(self):
        """ return the properties """
        if not self._properties:
            # get properties of self
            for name, attr in inspect.getmembers(type(self)):
                if name.startswith('__'):
                    continue
                if isinstance(attr, property):
                    if name not in ['methods', 'properties', 'attributes']:
                        self._properties[name] = attr

            # get properties of base_obj
            if self.base_obj is not None:
                for name, attr in inspect.getmembers(type(self.base_obj)):
                    if name.startswith('__'):
                        continue
                    if isinstance(attr, property):
                        self._properties[name] = attr

        return self._properties

    @property
    def attributes(self):
        """ return the attributes """
        result = {}

        # get attrs of self
        for name, attr in inspect.getmembers(self):
            if name.startswith('__'):
                continue
            if inspect.isfunction(attr) or inspect.ismethod(attr) or inspect.isbuiltin(attr):
                continue
            result[name] = ''

        # get attrs of base_obj
        if self.base_obj is not None:
            for name, attr in inspect.getmembers(self.base_obj):
                if name.startswith('__'):
                    continue
                if inspect.isfunction(attr) or inspect.ismethod(attr) or inspect.isbuiltin(attr):
                    continue
                result[name] = attr

        return result

    def add_method(self, name, func=None):
        """ dynamically add a method """
        if isinstance(name, str):
            if inspect.isfunction(func):
                m = self.methods
                m[name] = MethodType(func, self)
        elif inspect.isclass(name):
            src_class = name
            # read the methods of the class
            for name, attr in inspect.getmembers(src_class):
                if isinstance(attr, property) and SuperObject._is_function_of(attr.fget, src_class):
                    # when a property of extend_class is met
                    if attr.fget:
                        self.add_method('get_' + name, attr.fget)
                    if attr.fset:
                        self.add_method('set_' + name, attr.fset)
                elif inspect.isfunction(attr) and SuperObject._is_function_of(attr, src_class):
                    # when a method is met
                    self.add_method(name, attr)

        return self
