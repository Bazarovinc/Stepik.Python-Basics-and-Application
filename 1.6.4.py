class ExtendedStack(list):
    def sum(self):
        n1 = self.pop()
        n2 = self.pop()
        self.append(n1 + n2)

    def sub(self):
        n1 = self.pop()
        n2 = self.pop()
        self.append(n1 - n2)

    def mul(self):
        n1 = self.pop()
        n2 = self.pop()
        self.append(n1 * n2)

    def div(self):
        n1 = self.pop()
        n2 = self.pop()
        self.append(n1 // n2)
