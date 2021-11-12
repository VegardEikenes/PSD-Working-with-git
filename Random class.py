from random import randint


class Random():

    def __init__(self, intamount, intmin, intmax):
        self.intamount = intamount
        self.intmin = intmin
        self.intmax = intmax

    def randomnumber(self):
        for n in range(self.intamount):
            print(randint(self.intmin, self.intmax))
            
if __name__ == "__main__":
    test = Random(10, 1, 20)
    test.randomnumber()