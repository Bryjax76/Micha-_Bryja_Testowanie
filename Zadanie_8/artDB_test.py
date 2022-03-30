from artDB import dataBaseClass
import unittest
import os
import sqlite3


class TestPlikTxt(unittest.TestCase):

	def setUp(self):
		dataBaseClass.create_database()


	def test_select(self):
		self.zmienna = self.test_select.nazwa()
		self.assertEqual(self.zmienna,"AC Milan")

	def tearDown(self):
		os.remove("mydatabase.db")



if __name__ == '__main__':
    unittest.main()
