import unittest
from CatsPartnerFinder import CatsPartnerFinder, Cat

class TestCatsPartnerFinder(unittest.TestCase):
    def setUp(self):
        self.cat1 = Cat("Whiskers", "black")
        self.cat2 = Cat("Fluffy", "white")
        self.cat3 = Cat("Tiger", "orange")
        self.cats_list = [self.cat1, self.cat2, self.cat3]
        self.finder = CatsPartnerFinder(self.cats_list)

    def test_find_best_match_by_color(self):
        result = self.finder.find_best_match("black", [], 25)
        self.assertEqual(result, self.cat1)

    def test_find_best_match_by_animal_preference(self):
        result = self.finder.find_best_match("blue", ["dog", "cat"], 30)
        self.assertEqual(result, self.cat1)

    def test_find_best_match_age_too_old(self):
        result = self.finder.find_best_match("black", ["dog", "cat"], 91)
        self.assertIsNone(result)

    def test_find_best_match_no_match(self):
        result = self.finder.find_best_match("blue", ["dog", "elephant"], 25)
        self.assertIsNone(result)

    def test_find_best_match_multiple_preferences(self):
        result = self.finder.find_best_match("white", ["dog", "bird"], 40)
        self.assertEqual(result, self.cat2)

if __name__ == '__main__':
    unittest.main()