#!/usr/bin/python

class Person(object):


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

