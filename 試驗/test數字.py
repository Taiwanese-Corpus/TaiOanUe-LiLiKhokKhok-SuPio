from unittest.case import TestCase
from 數字 import 全部漢字

from 數字 import 整理羅馬字


class Sooji(TestCase):
    def test_99以下全小寫(self):
        self.assertEqual(整理羅馬字('Tsa̍p-it'), 'tsa̍p-it')
        
    def test_99以下連字符(self):
        self.assertEqual(整理羅馬字('la̍k tsa̍p-it'), 'la̍k-tsa̍p-it')
    
class 試數字敢有出現(TestCase):
    
    def test_99以下(self):
        self.assertIn('三十三', 全部漢字())
        
    def test_百(self):
        self.assertIn('五百', 全部漢字())