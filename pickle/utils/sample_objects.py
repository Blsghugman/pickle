import math
import collections
import threading  # 新增导入


# 自定义类（带 __init__）
class SampleClass:
    def __init__(self):
        self.x = 10
        self.y = [1, 2, 3]


# 带 __slots__ 的类
class SlotClass:
    __slots__ = ['x', 'y']

    def __init__(self):
        self.x = "slot"
        self.y = 123


# 自引用结构
recursive_list = []
recursive_list.append(recursive_list)

# 共享引用结构
shared = [42]
shared_ref = [shared, shared]

# 主测试对象列表
sample_objects = [
    2 ** 16,  # int
    3.14159,  # float
    "hello world",  # string
    [1, 2, 3],  # list
    {"a": 1, "b": 2},  # dict
    ["cherry", "banana", "apple"],  # additional list
    (None, True, False),  # tuple
    {1, 2, 3},  # set
    SampleClass(),  # custom object ✅
    [],  # empty list
    {},  # empty dict
    SlotClass(),  # class with __slots__ ✅
    recursive_list,  # recursive structure
    shared_ref,  # shared object reference
    float('inf'),  # float infinity
    float('-inf'),  # float negative infinity
    float('nan'),  # float NaN
    collections.OrderedDict([('a', 1), ('b', 2)]),  # Ordered dict
    collections.defaultdict(int, a=1),  # default dict
    collections.deque([1, 2, 3]),  # deque
    Exception("error"),  # exception object

    threading.Lock(),
]
