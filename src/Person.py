#----------------------------------------------
#--- Author         : Ahmet Özlü
#--- Mail           : ahmetozlu93@gmail.com
#--- Date           : 1st August 2017
#----------------------------------------------

class Person(object):

    # initialization to calculate total people in the family
    person = 0

    def __init__(self, name=None, surName=None, gender=None, birthDate=None, deadDate=None, father=None, mother=None, children=0):
        self.name = name
        self.surName = surName
        self.gender = gender
        self.birthDate = birthDate
        self.deadDate = deadDate
        self.father = father
        self.mother = mother
        self.children = children
        Person.person += 1

    def displayCount(self):
        print("Total Person %d" % Person.person)

    def displayPerson(self):
        print("Name : ", self.name, ", Surname: ", self.surName, ", Father: ", self.father, ", Mother: ", self.mother,", Children: ", self.children)

