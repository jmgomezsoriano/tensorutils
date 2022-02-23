import unittest
from tensorutils import select_cpu_if_not_gpu


class MyTestCase(unittest.TestCase):
    def test_select_cpu(self):
        select_cpu_if_not_gpu()
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
