from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout_success(self):
        checkout = checkout_solution.checkout("ABCD")
        assert checkout == 115

    def test_checkout_failure(self):
        checkout = checkout_solution.checkout("ABCD")
        assert checkout != 120

    def test_checkout_special_offer(self):
        checkout = checkout_solution.checkout("AAA")
        assert checkout == 130
    
    def test_checkout_second_special_offer(self):
        checkout = checkout_solution.checkout("AAAAA")
        assert checkout == 200

    def test_checkout_special_offer_and_no_special_offer(self):
        checkout = checkout_solution.checkout("BCB")
        assert checkout == 65
    
    def test_checkout_invalid_input(self):
        checkout = checkout_solution.checkout("ABCD1")
        assert checkout == -1

    def test_checkout_special_offer_with_free_item(self):
        checkout = checkout_solution.checkout("EEB")
        assert checkout == 80

    def test_checkout_special_offer_with_free_item_and_no_special_offer(self):
        checkout = checkout_solution.checkout("EEEB")
        assert checkout == 120