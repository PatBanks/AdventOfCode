

class Parser():
    def __init__(self, input):
        with open(input, "r") as f:
            self.input = f.readlines()

    def Get_Input(self):
        return self.input