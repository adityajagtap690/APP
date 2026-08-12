from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardStrategy(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Credit Card.")


class PayPalStrategy(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using PayPal.")


class PaymentContext:

    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        if self.strategy:
            self.strategy.pay(amount)
        else:
            print("Payment strategy not selected.")


if __name__ == "__main__":

    print("Select Payment Method")
    print("1. Credit Card")
    print("2. PayPal")

    choice = int(input("Enter your choice : "))

    context = PaymentContext()

    if choice == 1:
        context.set_strategy(CreditCardStrategy())
    elif choice == 2:
        context.set_strategy(PayPalStrategy())
    else:
        print("Invalid choice")
        exit()

    amount = float(input("Enter amount : ₹"))

    context.make_payment(amount)