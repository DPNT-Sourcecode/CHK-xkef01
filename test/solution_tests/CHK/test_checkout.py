from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout_success():
        checkout = checkout_solution.checkout()
        checkout.add_item('A')
        checkout.add_item('B')
        checkout.add_item('C')
        checkout.add_item('D')
        total_price = checkout.calculate_total_price()
        assert total_price == 115

    def test_checkout_failure():
        checkout = checkout_solution.checkout()
        checkout.add_item('A')
        checkout.add_item('B')
        checkout.add_item('C')
        checkout.add_item('D')
        total_price = checkout.calculate_total_price()
        assert total_price != 120
