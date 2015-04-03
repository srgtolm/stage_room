__author__ = 'sereg'

'''class Song(object):

    def __init__(self,lalala):
        self.lyrics = lalala
        print self.lyrics


    def sing_me(self):
        print self
        for i in self.lyrics:
            print i

#happy_day = Song(["Happy birhday to you","I don't want to get sued","So i'll stop right there"])
#happy_day.sing_me()'''

class Person:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split(' ')[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return 'Person: %s, %s' % (self.name, self.pay)
    '''def show(self):
        print self.name, self.job, self.pay'''

class Manager(Person):
    def __init__(self, name , pay):
        Person.__init__(self,name,'manager',pay)

    def giveRaise(self, percent,bonus=1):
        Person.giveRaise(self,percent=percent + bonus)



ivan = Person("Ivan Petrov")
john = Person('John Sidorov',job='developer',pay=7500)

print(ivan)
print(john)

print(ivan.lastname(),john.lastname())
john.giveRaise(.10)

print(john)
tom = Manager("Tom Jackson",50000)

print(tom)
print "Now we give to Tom some bonus"
tom.giveRaise(0.10)

print(tom.lastname())
print(tom)
