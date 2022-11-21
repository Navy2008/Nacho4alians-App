#!/usr/bin/env python3

import unittest
import smtmain


class TestSmtmain(unittest.TestCase):
    """Unittest for smtmain"""

    def setUp(self):
        self.smtmain = smtmain.hellofunction()

    def test_validate_hellofunction(self):
        self.assertEqual(smtmain.hellofunction(z=32), 32)


if __name__ == '__main__':
    unittest.main()
