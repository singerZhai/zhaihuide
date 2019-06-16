# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-04-23 18:47
# @File    : first.py
# @Software: PyCharm
# import collections
#
# Card = collections.namedtuple('Card', ['rank', 'suit'])
#
#
# class FrenchDeck:
#     ranks = [str(i) for i in range(2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'.split()
#
#     def __init__(self):
#         self._card = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
#
#     def __len__(self):
#         return len(self._card)
#
#     def __getitem__(self, item):
#         return self._card[item]
#
#
# french_deck = FrenchDeck()
# # card = Card('7', 'diamonds')
# # print(card)
# # print(len(card))
# # print(card[0])
# # for i in french_deck:
# #     print(i)
# from math import hypot
#
#
# class Vector:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return 'Vector(%r, %r)' % (self.x, self.y)
#
#     def __abs__(self):
#         return hypot(self.x, self.y)
#
#     def __bool__(self):
#         return bool(self.x or self.y)
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#
#     def __mul__(self, other):
#         return Vector(self.x * other, self.y * other)


# demo = '123456'
# demo_list = [ord(i) for i in demo]
# print(demo_list)
# demo1 = '123'
# demo2 = '456'
# demo = [(first, second) for first in demo1 for second in demo2]
# print(demo)
# message = 'Hello World'
# import array
#
# res = array.array('I', (ord(i) for i in message))
# print(res)

# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# for i in ('%s %s' % (c, s) for c in colors for s in sizes):
#     print(i)

# demo = (i for i in range(11))
# print(list(demo))

# demo = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# for country, _ in demo:
#     print(country)
#     print(_)

# print(divmod(20, 8))
import collections
import os

# _, filename = os.path.split(__file__)
# print(_)
# print(filename)
# print(os.path.split(__file__))
# a, b, *args = range(10)
# print(args)

# metro_areas = [
#     ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  # ➊
#     ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
#     ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
#     ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#     ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
# ]
# print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
# fmt = '{:15} | {:9.4f} | {:9.4f}'
# for name, cc, pop, (latitude, longitude) in metro_areas:  # ➋
#     if longitude <= 0:  # ➌
#         print(fmt.format(name, latitude, longitude))

# from collections import namedtuple
# # City = namedtuple('City', 'name country population coordinates')
# # tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# # # print(tokyo.coordinates)
# #
# # # print(City._fields)
# #
# # LatLong = namedtuple('LatLong', 'lat long')
# # delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# # delhi = City._make(delhi_data)
# # print(delhi._asdict())

# l = [1, 2, 3]
# print(l * 5)

# demo = [['_'] * 3 for i in range(3)]
# print(demo)

# demo = ['grape', 'raspberry', 'apple', 'banana']
# print(sorted(demo, key=len))

# import bisect
# import sys
#
# HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
# NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
# ROW_FMT = '{0:2d} @ {1:2d}  {2}{0:<2d}'
#
#
# def demo(bisect_fn):
#     for needle in reversed(NEEDLES):
#         position = bisect_fn(HAYSTACK, needle)
#         offset = position * '  |'
#         print(ROW_FMT.format(needle, position, offset))
#
#
# if __name__ == '__main__':
#     if sys.argv[-1] == 'left':
#         bisect_fn = bisect.bisect_left
#     else:
#         bisect_fn = bisect.bisect
#
#     print('DEMO:', bisect_fn.__name__)
#     print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
#     demo(bisect_fn)

# import bisect
# import random
#
# SIZE = 7
# random.seed(1729)
#
# my_list = []
# for i in range(SIZE):
#     new_item = random.randrange(SIZE * 2)
#     bisect.insort(my_list, new_item)
#     print('%2d ->' % new_item, my_list)
from collections import abc, ChainMap

import numpy as np
from array import array
import random

# floats = array('d', (random.random() for i in range(10 ** 7)))
# print(len(floats))

# res = np.array([[1, 2, 3], [4, 5, 6]])
# print(res)
# print(res.ndim)
# print(res.shape)
# print(res.dtype)
# print(res.size)

# res = np.array([random.randint(1, 10) for _ in range(10)])
# print(res)
# res1 = numpy.zeros((3, 4))
# print(res1)
# print(res.tolist())
# print(res)

# res = array('d', [random.random() for _ in range(10 ** 7)])
# demo1 = open("./data.txt", "wb")
# res.tofile(demo1)
# demo1.close()
# res1 = array('d')
# demo2 = open("./data.txt", "rb")
# res1.fromfile(demo2, 10 ** 7)
# demo2.close()
# print(len(res1))

# numbers = array('h', [-2, -1, 0, 1, 2])
# memv = memoryview(numbers)
# # print(len(memv))
# # print(memv[0])
# memv_oct = memv.cast('B')
# res = memv_oct.tolist()
# print(res)

# a = np.arange(12)
# # print(a)
# a.shape = 3, 4
# print(a)

# from collections import deque
# dq = deque(range(10), maxlen=10)
# print(dq)
# # dq.rotate(3)
# # print(dq)
# dq.rotate(-4)
# print(dq)

# demo = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
# res = sorted(demo, key=int)
# res1 = sorted(demo, key=str)
# print(res)
# print(res1)

# import re
# WORD_RE = re.compile(r'\w+')
# index = {}
# with open(sys.argv[1], encoding='utf-8') as f:


# import sys
# if len(sys.argv) > 1:
#
#     if sys.argv[1] == '--help':
#         sys.exit("帮助信息：exit")
#         # quit('帮助信息：quit')
#
#     else:
#         port = sys.argv[1]
#         sys.exit(port)
#         # quit('还有谁')

# res = np.array([random.random() for _ in range(100)])
# print(res)
# print(random.random())

# my_dict = {}
# print(isinstance(my_dict, abc.Mapping))

# a = dict(one=1, two=2, three=3)
# print(a)
# b = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# print(b)
# res = zip([1, 2, 3], [4, 5, 6])
# print(res)
# print(dict(res))


# DIAL_CODES = [
#     (86, 'China'),
#     (91, 'India'),
#     (1, 'United States'),
#     (62, 'Indonesia'),
#     (55, 'Brazil'),
#     (92, 'Pakistan'),
#     (880, 'Bangladesh'),
#     (234, 'Nigeria'),
#     (7, 'Russia'),
#     (81, 'Japan'),
# ]
#
# country_code = {country: code for code, country in DIAL_CODES}
# print(country_code)

# import sys
# import re
# import collections
#
# WORD_RE = re.compile(r'\w+')
# index = collections.defaultdict(list)
# with open(sys.argv[0], encoding='utf-8') as f:
#     for line_no, line in enumerate(f, 1):
#         for math in WORD_RE.finditer(line):
#             word = math.group()
#             column_no = math.start() + 1
#             location = (line_no, column_no)
#             index[word].append(location)
#
# for word in sorted(index, key=str.upper):
#     print(word, index[word])

# import builtins
# pylookup = ChainMap(locals(), globals(), vars(builtins))
# print(pylookup)

# ct = collections.Counter('asdfaefdsfecxwerecsdfewfsd')
# print(ct)

# class StrKeyDict(collections.UserDict):
#
#     def __missing__(self, key):
#         if isinstance(key, str):
#             raise KeyError(key)
#         return self[str(key)]
#
#     def __contains__(self, item):
#         return str(item) in self.data
#
#     def __setitem__(self, key, value):
#         self.data[str(key)] = value
#
#
# demo = ['spam', 'spam', 'eggs', 'spam']
# res = set(demo)

# a = 100
# b = 1000
# print(b & a)

# def factorial(n):
#     return 1 if n < 2 else n * factorial(n - 1)
#
# print(factorial(42))

# res = lambda x: x[::-1]
# print(res('123'))

# from functools import reduce
# from operator import add
# print(reduce(add, range(100)))
# print(sum(range(100)))

# demo = [callable(obj) for obj in (abs, str, 13)]
# print(demo)

# class BingoCage:
#
#     def __init__(self, items):
#         self._items = list(items)
#         random.shuffle(self._items)
#         print("__init__", end='')
#         print(self._items)
#
#     def pick(self):
#         try:
#             return self._items.pop()
#         except IndexError:
#             raise LookupError('pick from empty BingoCage')
#
#     def __call__(self, *args, **kwargs):
#         print("__call__", end='')
#         print(self._items)
#         return self.pick()


# bingo = BingoCage('123')
# print(bingo.pick())
# print(bingo())
# print(list('123').pop())
# res = list('123')
# res.pop()
# print(res)

# class C: pass
# obj = C()
# def func(): pass
# print(sorted(set(dir(func)) - set(dir(obj))))


# def tag(name, *content, cls=None, **attrs):
#     """生成一个或多个HTML标签"""
#     if cls is not None:
#         attrs['class'] = cls
#
#     if attrs:
#         attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
#
#     else:
#         attr_str = ''
#
#     if content:
#         return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
#
#     else:
#         return '<%s%s />' % (name, attr_str)


# print(tag('br'))
# print(tag('p', 'hello'))
# print(tag('p', 'hello', 'world'))
# print(tag('p', 'hello', id=33))
# print(tag('p', 'hello', 'world', cls='sidebar'))
# print(tag(content='testing', name='img'))
# my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
#           'src': 'sunset.jpg', 'cls': 'framed'}
#
# print(tag(**my_tag))

# def f(a, *, b):
#     return a, b
#
# print(f(1, b=2))


# def clip(text: str, max_len: 'int > 0' = 80) -> str:
#     """
#     在max_len前面或后面的第一个空格处截断文本
#     :param text:
#     :param max_len:
#     :return:
#     """
#     end = None
#     if len(text) > max_len:
#         space_before = text.rfind(' ', 0, max_len)
#         if space_before >= 0:
#             end = space_before
#         else:
#             space_after = text.rfind(' ', max_len)
#             if space_after >= 0:
#                 end = space_after
#     if end is None:  # 没有找到空格
#         end = len(text)
#     return text[:end].rstrip()
#
# print(clip('123'), 3)

import json


def read_login(filename):
    filepath = "data/" + filename
    res_dict = {}
    with open(filepath, "r", encoding="utf-8") as f:
        # res_dict = dict(json.load(f))
        # return res_dict
        return json.load(f)


res_data = read_login('login.json')
print(res_data)

arrs = []
for data in res_data.values():
    print(data)
    arrs.append(data)
    print(arrs)
