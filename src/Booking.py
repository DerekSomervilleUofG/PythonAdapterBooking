from Confirmation import Confirmation
from EmailConfirmation import EmailConfirmation
from TextConfirmation import TextConfirmation

class Booking:
    confirmation = None;

    def set_confirmation(self,confirmation):
        self.confirmation = confirmation

    def make_a_booking(self,name):
        self.confirmation.confirm(name)

def main():
    booking = Booking()
    booking.set_confirmation(EmailConfirmation())
    booking.make_a_booking("Derek")
    booking.set_confirmation(TextConfirmation())
    booking.make_a_booking("Susan")

if __name__ == "__main__":
    main()