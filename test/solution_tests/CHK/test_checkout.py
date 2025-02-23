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

    def test_checkout_multiple_special_offer_with_free_item(self):
        checkout = checkout_solution.checkout("EEEEBB")
        assert checkout == 160

    def test_checkout_multiple_E_and_B_item(self):
        checkout = checkout_solution.checkout("BBBEE")
        assert checkout == 125

    def test_checkout_multiple_special_offer(self):
        checkout = checkout_solution.checkout("AAAAAAAA")
        assert checkout == 330

    def test_checkout_double_same_special_offer(self):
        checkout = checkout_solution.checkout("AAAAAAAAAA")
        assert checkout == 400

    def test_checkout_F_offer(self):
        checkout = checkout_solution.checkout("FFF")
        assert checkout == 20

    def test_checkout_F_offer_with_other_item(self):
        checkout = checkout_solution.checkout("FFFA")
        assert checkout == 70

    def test_checkout_F_offer_with_no_offer(self):
        checkout = checkout_solution.checkout("FFFFF")
        assert checkout == 40

    def test_checkout_H_offer(self):
        checkout = checkout_solution.checkout("HHHHH")
        assert checkout == 45
    
    def test_checkout_H_offer_with_no_offer(self):
        checkout = checkout_solution.checkout("HHHHHH")
        assert checkout == 55

    def test_checkout_any_three_items_offer(self):
        checkout = checkout_solution.checkout("XYZ")
        assert checkout == 45

    