from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_invalid(self):
        try:
            sum_solution.compute(-1, 2)
        except ValueError as e:
            assert str(e) == "x and y should be between 0 and 100"
