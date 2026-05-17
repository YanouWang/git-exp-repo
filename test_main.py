# 测试文件
import unittest
from main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), 0)
