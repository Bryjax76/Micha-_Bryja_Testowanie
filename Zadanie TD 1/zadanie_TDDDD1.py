import unittest
import zadanietd1
import zadanietd1BRAK

class myslnik(unittest.TestCase):
    
    def test_myslnik(self):
        key = "-"
        container = zadanietd1.zdanie("Wystepuje -")
        message = "Nie ma myslnika"
        self.assertIn(key, container, message)

    def test_brakmyslnik(self):
        key = "-"
        container = zadanietd1BRAK.zdanieBrak("Brak ")
        message = "Jest myslnik"
        self.assertNotIn(key, container, message)


if __name__ == '__main__':
    unittest.main() 