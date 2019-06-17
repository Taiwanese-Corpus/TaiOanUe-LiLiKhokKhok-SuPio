from unittest.case import TestCase


class Sooji(TestCase):
    def test_全小寫(self):
        self.assertEqual('十一', 'tsa̍p-it')()
        
    def test_99以下連字符(self):
        self.assertEqual('六十一', 'la̍k-tsa̍p-it')() 