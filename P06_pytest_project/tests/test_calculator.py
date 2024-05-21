from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
    def test_sub(self):
        # arrange
        a = 3321
        b = 1220
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 2101
        assert result == expected
    def test_mul(self):
        # arrange
        a = 33
        b = 22
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 726
        assert result == expected
    def test_div(self):
        # arrange
        a = 33
        b = 11
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 3
        assert result == expected
