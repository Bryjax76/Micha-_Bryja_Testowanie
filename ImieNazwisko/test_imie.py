from imie import Pracownik 
import unittest

class TestImie(unittest.TestCase):
	def test_email(self):
		self.assertEqual(Pracownik.email("Jan","Kowalski"),"Jan.Kowalski@testemail.com")
	def test_nazwa(self):
		self.assertEqual(Pracownik.nazwa("Jan","Kowalski"),"Jan Kowalski")
	def test_wynagrodzenie(self):
		self.assertEqual(Pracownik.wynagrodzenie(2000),4000)

if __name__ == '__main__':  
    unittest.main()
