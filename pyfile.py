class Dog(object):
    def __init__(self):
        self.name = "Boola"

    def bark(self):
        print("How")

dog = Dog()
dog.bark()

dog2 = Dog()
dog.bark()

l = map(lambda x: x*x, range(10))

for item in l:
    print (item)

print(l)


