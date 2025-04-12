# Tests
import gestor_memoria
from cont_mem_algos import worst_fit

import unittest

class TestBasicFirstFit(unittest.TestCase):

    def test_pass_empty_map(self):
        work_memory = []
        req = 0
        index = 0
        search = worst_fit(work_memory, req, index)
        self.assertEqual(search, None)

    def test_req_highest(self):
        work_memory = [(0x00A00000, 0x000C0000)]
        req = 0x000D0000
        index = 0
        search = worst_fit(work_memory, req, index)
        self.assertEqual(search, None)

    def test_req_highest_list(self):
        work_memory = [(0x00A00000, 0x000C0000), (0x00B00000, 0x000C0000), (0x00C00000, 0x000C0000)]
        req = 0x000D0000
        index = 0
        search = worst_fit(work_memory, req, index)
        self.assertEqual(search, None)


if __name__ == '__main__':
    unittest.main()
