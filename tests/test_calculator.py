import pytest
from app.calculator import Calculator

calc = Calculator

class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_multiply_correctly(self):

        assert self.calc.multiply(self, 2, 2) == 4


    def test_division_correctly(self):

        assert self.calc.division(self, 45, 9) == 5

    def test_subtraction_correctly(self):

        assert self.calc.subtraction(self, 65, 35) == 30

    def teardown(self):
        print('Выполнение метода Teardown')