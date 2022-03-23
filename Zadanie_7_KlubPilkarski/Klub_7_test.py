from Klub_7 import KlubPilkarski 
import unittest
import os

class TestPlikTxt(unittest.TestCase):

	def setUp(self):
		self.test_dane = KlubPilkarski("Bayern", "klub.txt")

	def test_txt(self):
		self.zmienna = self.test_dane.create_klubPilkarski()
		self.assertEqual(self.zmienna,"Bayern")

	def test2_txt(self):
		self.zmienna2 = self.test_dane.delete_klubPilkarski()
		self.assertEqual(self.zmienna2,"klub.txt")



if __name__ == '__main__':
    unittest.main()