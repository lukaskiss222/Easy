import unittest
from builder import builder
from ctypes import c_int32, c_bool, c_char, POINTER, c_char_p
import numpy as np
from ctypes import create_string_buffer
import itertools

class TestEvaluator(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.builder = builder()

    def test_add(self):
        fu = "def add:int(a:int, b:int){\n" \
             "return a + b\n" \
             "}\n"
        func = self.builder.compile(fu, "add", c_int32, [c_int32]*2, verbose=False)

        self.assertEqual(func(1, 2), 1 + 2)
        self.assertEqual(func(1003, 2232), 1003 + 2232)


    def test_sub(self):
        fu = "def add:int(a:int, b:int){\n" \
             "return a - b\n" \
             "}\n"
        func = self.builder.compile(fu, "add", c_int32, [c_int32] * 2, verbose=False)
        self.assertEqual(func(1, 2), 1 - 2)
        self.assertEqual(func(1003, 2232), 1003 - 2232)

    def test_combine(self):
        fu = "def add:int(a:int, b:int){\n" \
             "return a + a*b" \
             "}\n"
        func = self.builder.compile(fu, "add", c_int32, [c_int32] * 2, verbose=False)
        self.assertEqual(func(3, 4), 15)

    def test_logical(self):
        fu = "def f:bool(a:bool, b:bool){\n" \
             "return a && b\n" \
             "}\n" \
             "def g:bool(a:bool, b:bool){\n" \
             "f(True, True)\n" \
             "return a || b\n" \
             "}\n" \
             "def t:bool(a:int, b:int, c:int){\n" \
             "d:int\n" \
             "f:bool\n" \
             "d = (b + c)*a\n" \
             "f = g(True, True)" \
             "return (a < d) && f\n" \
             "}\n"
        func = self.builder.compile(fu, "f", c_bool, [c_bool] * 2, verbose=False)
        func2 = self.builder.compile(fu, "g", c_bool, [c_bool] * 2, verbose=False)
        t = self.builder.compile(fu, "t", c_int32, [c_int32] * 3, verbose=False)
        self.assertEqual(func(True, False), False)

        self.assertEqual(func(True, True), True)
        self.assertEqual(func2(False, False), False)

        self.assertEqual(t(1, 2, 3), True)
        self.assertEqual(t(-2, 3, 5), False)

    def test_if(self):
        fu = "def f:int(a:int, b:int){\n" \
             " if a > b {\n" \
             "  return a\n" \
             " }\n" \
             "return b\n" \
             "}\n"
        func = self.builder.compile(fu, "f", c_int32, [c_int32]*2, verbose=False)
        self.assertEqual(func(2, 3), 3)
        self.assertEqual(func(-10, -20), -10)

    def test_while(self):
        fu = "def f:int(n:int){\n" \
             "sum:int = 0\n" \
             "i:int = 0\n" \
             "while i <= n {\n" \
             "sum = sum + i\n" \
             "i = i + 1\n" \
             "}\n" \
             "return sum\n" \
             "}\n"

        func = self.builder.compile(fu, "f", c_int32, [c_int32] * 1, verbose=False)
        self.assertEqual(func(0), 0)
        self.assertEqual(func(1), 1)
        self.assertEqual(func(10), 55)

    def test_my(self):
        fu = "def f:char(){\n" \
             'printf("Print from my test_my of string :D")\n' \
             'g:char*\n' \
             'g = "test1"\n' \
             "g[1] = 'g'\n" \
             'c:char* = "balblabla"\n' \
             "c[0] = 'c'\n" \
             'printf(c)\n' \
             "return g[0]\n" \
             "}\n"

        func = self.builder.compile(fu, "f", c_char, [] * 1, verbose=False)
        self.assertEqual(func(), b't')


    def test_allocate(self):
        fu = "def f:int(){\n" \
             "while 1 < 0 {\n" \
             "return 1" \
             "}\n" \
             "a:char* = calloc(20,20)\n" \
             "free(a)\n" \
             "return 0\n" \
             "}\n"

        func = self.builder.compile(fu, "f", c_int32, [] * 1, verbose=False)
        func()

    def test_array_allocation(self):
        fu = "def f:int(size:int){\n" \
             "a:bool(size)\n" \
             "a[0] = True\n" \
             "b:bool = a[0]" \
             'printf("%d",b)\n' \
             'del a\n' \
             "return 0\n" \
             "}\n"
        func = self.builder.compile(fu, "f", c_int32, [c_int32] * 1, verbose=False)
        self.assertEqual(func(10), 0)

    def test_pointer_as_parameter(self):
        fu = "def f:int(arr:int*){\n" \
             "arr[0] = 0\n" \
             "return arr[1]\n" \
             "}\n"

        func = self.builder.compile(fu, "f", c_int32, [POINTER(c_int32)] * 1, verbose=False)
        arr = (c_int32*3)()
        arr[0] = 1
        arr[1] = 2
        arr[2] = 3
        self.assertEqual(func(arr), 2)
        self.assertEqual(arr[0], 0)

    def test_addres2d(self):
        arr2d = (POINTER(c_int32)*10)()
        for i in range(10):
            arr2d[i] = (c_int32*10)()
        for i, j in itertools.product(range(10), range(10)):
            arr2d[i][j] = i + j
        fu = "def f:int(arr2d:int**, i:int, j:int){\n" \
             "arr2d[i,j] = arr2d[i,j] + arr2d[i,j]\n" \
             "b:int = arr2d[i,j]\n" \
             'printf("%d",b)\n' \
             "return arr2d[i,j]\n" \
             "}\n"
        func = self.builder.compile(fu, "f", c_int32, [POINTER(POINTER(c_int32))] * 1, verbose=False)

        self.assertEqual(func(arr2d, 9, 7), (9 + 7)*2)


    def test_allocation2d(self):

        fu = 'def f:int(){\n' \
             'arr:int*(2)\n' \
             'c:int(10)\n' \
             'd:int(10)\n' \
             'c[0] = 2\n' \
             'd[0] = 2\n' \
             'arr[0] = c\n' \
             'arr[1] = d\n' \
             'del arr\n'  \
             'printf("%d", arr[1,0])\n' \
             'return 0\n' \
             '}\n'
        func = self.builder.compile(fu, "f", c_int32, [] * 1, verbose=False)
        func()

    def test_memoryleak(self):
        fu = 'def f:int(){' \
             'i:int = 200000\n' \
             'while i > 0 {\n' \
             'arr:int*(20)\n' \
             'c:int(20)' \
             'd:int(30)\n' \
             'arr[0] = c\n' \
             'arr[1] = d\n' \
             'del arr[1]\n' \
             'del arr[0]\n' \
             'del arr\n' \
             'i = i - 1' \
             '}\n' \
             'return 0\n' \
             '}\n'
        func = self.builder.compile(fu, "f", c_int32, [] * 1, verbose=False)
        func()

    def test_void(self):
        fu = 'def f:void(){\n' \
             'printf("asd")\n' \
             '}\n'
        func = self.builder.compile(fu, "f", None, [] * 1, verbose=False)
        func()

    def test_for(self):
        fu = 'def f:int(n:int){\n' \
             'sum:int = 0\n' \
             'for i:int from 0 to n by 1 {\n' \
             'sum = sum + i\n' \
             '}\n' \
             'return sum\n' \
             '}\n'
        func = self.builder.compile(fu, "f", c_int32, [c_int32] * 1, verbose=False)
        self.assertEqual(func(12), 6*11)

    def test_return(self):
        fu = 'def f:void(n:int){\n' \
             'if n < 10 {\n' \
             'return' \
             '}\n' \
             'printf("asd")' \
             '}\n'
        func = self.builder.compile(fu, "f", None, [c_int32] * 1, verbose=False)
        func(9)
        func(12)

    def test_string_comparision(self):
        fu = 'def f:void(){\n' \
             'a:str = "asd"\n' \
             'b:str = "asD"\n' \
             r'printf("Vysledok: %d\n", a > b)' \
             '\ntemp:str = a\n' \
             'a = b\n' \
             'b = temp\n' \
             r'printf("A je  %s ::::B je %s\n",a,b)' \
             '\n}\n'
        func = self.builder.compile(fu, "f", None, [] * 1, verbose=False)
        func()

    def test_swap(self):
        fu = 'def swap:void(arr:str*, i:int, j:int){\n' \
             'temp:str = arr[i]\n' \
             'arr[i] = arr[j]\n' \
             'arr[j] = temp\n' \
             '}\n' \
             'def f:void(){\n' \
             'a:str(2)\n' \
             'a[0] = "asd"\n' \
             'a[1] = "bbb"\n' \
             'swap(a,0,1)\n' \
             r'printf("A je  %s ::::B je %s\n",a[0],a[1])' \
             '\ndel a\n' \
             '}\n' \

    def test_string_sort(self):
        fu = 'def swap:void(arr:str*, i:int, j:int){\n' \
             'temp:str = arr[i]\n' \
             'arr[i] = arr[j]\n' \
             'arr[j] = temp\n' \
             '}\n' \
             "def sort:void(arr:str*, n:int){\n" \
             "for i:int from 0 to (n-1) by 1 {\n" \
             "for j:int from 0 to (n -i -1) by 1{\n" \
             "if arr[j] > arr[j+1] {\n" \
             r'printf("Swaping: %d, %d\n", i, j)' \
             "\nswap(arr,j,j+1)\n" \
             "}\n" \
             "}\n" \
             "}\n" \
             "}\n" \
             'def f:void(n:int){\n' \
             'arr:str(n)\n' \
             'for i:int from 0 to n by 1{\n' \
             'temp:char(200)\n' \
             'scanf("%s",temp)\n' \
             'arr[i] = temp\n' \
             '}\n' \
             'sort(arr,n)\n' \
             'for j:int from 0 to n by 1{\n' \
             r'printf("%s\n",arr[j])' \
             '\ndel arr[j]\n' \
             '}\n' \
             'del arr\n' \
             '}\n'

        func = self.builder.compile(fu, "sort", None, [POINTER(c_char_p), c_int32] * 1, verbose=False)
        func2 = self.builder.compile(fu, "f", None, [c_int32] * 1, verbose=False)
        n = 10
        arr = (c_char_p * n)()
        sample = np.random.random_sample(n)
        sample = list(map(lambda x: str(x).encode(), sample))

        for i in range(n):
            arr[i] = c_char_p(sample[i])
        func(arr, n)

        for i in range(n):
            print(arr[i])

        func2(4)


if __name__ == "__main__":
    t = TestEvaluator()
    t.main()
