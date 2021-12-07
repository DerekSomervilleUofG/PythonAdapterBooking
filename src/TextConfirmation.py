from Confirmation import Confirmation

class TextConfirmation(Confirmation):

    def confirm(self,name):
        print("Text to",name)