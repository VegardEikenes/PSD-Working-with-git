from random import randint


class Random():

    def randomnumber(self, intamount, intmin, intmax):
        for n in range(intamount):
            print(randint(intmin, intmax))

if __name__ == "__main__":
    test = Random()
    test.randomnumber(10, 1, 10)