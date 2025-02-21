from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout_success(self):
        checkout = checkout_solution.checkout("ABCD")
        assert checkout == 115

    def test_checkout_failure(self):
        checkout = checkout_solution.checkout("ABCD")
        assert checkout != 120

