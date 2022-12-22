import unittest
from main import sum
from main import div
from main import sub
from main import mul
from main import modd

class TestCalculator(unittest.TestCase):
  def test_sum(self):
<<<<<<< HEAD
    self.assertEqual(sum(1,2), 3)
=======
    self.assertEqual(sum(1,2), 88)
>>>>>>> master
  def test_sub(self):
    self.assertEqual(sub(4,5), 1)
  def test_mul(self):
    self.assertEqual(mul(1,2), 2)
  def test_div(self):
    self.assertEqual(div(120,6), 20)
  def test_mod(self):
<<<<<<< HEAD
    self.assertEqual(modd(100,10),0)
=======
    self.assertEqual(modd(110,10),70)
>>>>>>> master
