from Confirmation import Confirmation

class EmailConfirmation(Confirmation):

    def confirm(self,name):
        print("Email to",name)