from unittest.case import TestCase

from 數字 import 整理羅馬字


class Sooji(TestCase):
    def test_全小寫(self):
        self.assertEqual(整理羅馬字('Tsa̍p-it'), 'tsa̍p-it')
        
    def test_99以下連字符(self):
        self.assertEqual(整理羅馬字('la̍k tsa̍p-it'), 'la̍k-tsa̍p-it')