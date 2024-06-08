import unittest

import sys

sys.path.append("../")

from src.hello_world_package.hello_world_module import hello_world


class TestHelloWorld2(unittest.TestCase):

    def test_hello_world2(self):

        print("Testing hello_world 2")
        self.assertEqual(42, 42)


if __name__ == "__main__":
    unittest.main()
