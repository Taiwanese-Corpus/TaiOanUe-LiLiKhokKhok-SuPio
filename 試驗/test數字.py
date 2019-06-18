from unittest.case import TestCase
from 數字 import 全部漢字

from 數字 import 整理羅馬字


class sooji_format(TestCase):
    def test_99以下全小寫(self):
        self.assertEqual(整理羅馬字('Tsa̍p-it'), 'tsa̍p-it')

    def test_99以下連字符(self):
        self.assertEqual(整理羅馬字('la̍k tsa̍p-it'), 'la̍k-tsa̍p-it')

    def test_第kah數字連字符(self):
        self.assertEqual(整理羅馬字('tē tshit-pah'), 'tē-tshit-pah')
        
    def test_無應該連的(self):
        self.assertNotIn('九千八百', 全部漢字())    


class 試數字敢有出現(TestCase):
    def test_99以下(self):
        self.assertIn('三十三', 全部漢字())

    def test_百(self):
        self.assertIn('五百', 全部漢字())

    def test_千(self):
        self.assertIn('四千', 全部漢字())
         
    def test_萬(self):
        self.assertIn('六萬', 全部漢字())        

    def test_第(self):
        self.assertIn('第二十三', 全部漢字())

    def test_第kah千(self):
        self.assertIn('第九千', 全部漢字())

    def test_億(self):
        self.assertIn('兩億', 全部漢字())        

    def test_兆(self):
        self.assertIn('八兆', 全部漢字())  