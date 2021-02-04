import unittest
import calculator

class TestCaseAddition(unittest.TestCase):
	def testAddition(self):
		self.assertEqual(calculator.addition(2,1), 3)
		self.assertEqual(calculator.addition(-1,5), 4)
		self.assertEqual(calculator.addition(0,0), 0)
		self.assertEqual(calculator.addition(-1,-2), -3)

	def testSubtraction(self):
		self.assertEqual(calculator.subtraction(5,2), 3)
		self.assertEqual(calculator.subtraction(-1,-2), 1)
		self.assertEqual(calculator.subtraction(2,3), -1)
		self.assertEqual(calculator.subtraction(0,0), 0)

	def testMultiplication(self):
		self.assertEqual(calculator.multiplication(-1,-1), 1)
		self.assertEqual(calculator.multiplication(-2, 2), -4)
		self.assertEqual(calculator.multiplication(3, 2), 6)
		self.assertEqual(calculator.multiplication(0,-1), 0)

	def testDivision(self):
		self.assertEqual(calculator.division(0,2), 0)
		self.assertEqual(calculator.division(6,2), 3)
		self.assertEqual(calculator.division(-4,2), -2)
		self.assertEqual(calculator.division(3,-3), -1)


if __name__ == '__main__':
	unittest.main()
