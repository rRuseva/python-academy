class Sample1:
    x= 42

    def get_x(self):
        self.x

    def increment_x(self):
        self.x += 1

class Sample:
    ### staticclass  atribute
    x= 42
    def get_x(self):
        self.__class__.x
    # increments the attribute of the class /it is same for all instances/
    def increment_x(self):
        self.__class__.x += 1

    @staticmethod
    def increment_static(self):
        __class__.x += 1

    @classmethod
    def increment_class(cls):
        cls.x += 1

    def __init__(self, num):
        self.age = num


if __name__ == '__main__':
    # # s = Sample()
    # # print(s.x)
    # # s.increment_x()
    # # print(s.x)
    #
    # s1 = Sample1()
    # print(s1.x)
    # s1.increment_x()
    # print(s1.x)
    #
    # s11 = Sample1()
    # print(s11.x)
    s1 = Sample(25)
    Sample.increment_class()
    Sample.increment_class()
    print(Sample.x)

    Sample.increment_static()
    Sample.increment_class()
    print(Sample.x)
    print(s1.age)

