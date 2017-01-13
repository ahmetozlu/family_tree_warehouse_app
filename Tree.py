from Person import Person

class Tree(object):
    peopleList = []
    childList = []
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    list=[]

    level0=[]
    level1=[]
    level2 = []
    level3 = []
    level4 = []

    def addPerson(self,newPerson):
        if(newPerson.birthDate and newPerson.deadDate):
            if(newPerson.birthDate < newPerson.deadDate):
                if(newPerson.gender):
                    if(newPerson.gender =="f" or newPerson.gender=="m" or newPerson.gender =="F" or newPerson.gender=="M"):
                        self.peopleList.append(newPerson)
                        print("The person is added!")
                    else:
                        print("The gender which you are entered is wrong!(It must be f or m)")
                        print("The person is NOT added!")
            else:
                print(newPerson.name + " " + newPerson.surName + " is not added because the birth date can not be bigger than dead date!")
        else:
            if (newPerson.gender):
                if (newPerson.gender == "f" or newPerson.gender == "m" or newPerson.gender == "F" or newPerson.gender == "M"):
                    self.peopleList.append(newPerson)
                    print("The person is added!")
                else:
                    print("The gender which you are entered is wrong!(It must be f or m)")

    def deletePerson(self,person):
        self.peopleList.remove(person)

    def setChildren(self):
        for tempPerson in self.peopleList:
            myList = []
            relation = self.getChild(self, tempPerson, myList)
            totalChildNumber = len(myList)
            tempPerson.children = totalChildNumber

    def printTreeAlternatively(self):
        for tempPerson in self.peopleList:
            a = self.getLevel(self,tempPerson)
            if( a == 0 ):
                self.level0.append(tempPerson)
            elif( a == 1 and tempPerson.gender == "f"):
                self.level1.append(tempPerson)
            elif (a == 2 and tempPerson.gender == "f"):
                self.level2.append(tempPerson)
            elif (a == 3 and tempPerson.gender == "f"):
                self.level3.append(tempPerson)
            elif (a == 4 and tempPerson.gender == "f"):
                self.level4.append(tempPerson)

        print("***LEVEL-3***")
        for tempPerson in self.level3:
            relation = self.getChild(self, tempPerson, self.list1)

            if (len(Tree.list1) >= 1):
                if (tempPerson.gender == "f"):
                    child = self.getPerson(self, self.list1[0].name, self.list1[0].surName)
                    del Tree.list1[:]
                    print(
                        tempPerson.name + " " + tempPerson.surName + " & " + child.father + " " + tempPerson.surName)

        print("***LEVEL-2***")
        for tempPerson in self.level2:
            relation = self.getChild(self, tempPerson, self.list1)

            if (len(Tree.list1) >= 1):
                if (tempPerson.gender == "f"):
                    child = self.getPerson(self, self.list1[0].name, self.list1[0].surName)
                    del Tree.list1[:]
                    print(tempPerson.name + " " + tempPerson.surName + " & " + child.father + " " + tempPerson.surName)

        print("***LEVEL 1***")
        for tempPerson in self.level1:
            relation = self.getChild(self, tempPerson, self.list1)

            if (len(Tree.list1) >= 1):
                if (tempPerson.gender == "f"):
                    child = self.getPerson(self, self.list1[0].name, self.list1[0].surName)
                    del Tree.list1[:]
                    print(tempPerson.name + " " + tempPerson.surName + " & " + child.father + " " + tempPerson.surName)

        print("***LEVEL-0***")
        for tempPerson in self.level0:
            if(tempPerson.name and tempPerson.surName):
                print(tempPerson.name + " " + tempPerson.surName)
            elif (tempPerson.name):
                print(tempPerson.name)
            elif (tempPerson.surName):
                print(tempPerson.surName)
        print("LEVEL - 3")
        for tempPerson in self.peopleList:
            a = self.getLevel(self, tempPerson)
            if (a == 3):
                # relation = self.getChild(self, tempPerson)
                relation = self.getChild(self, tempPerson, self.list1)

                if (len(Tree.list1) >= 1):
                    if (tempPerson.gender == "f"):
                        child = self.getPerson(self, self.list1[0].name, self.list1[0].surName)
                        del Tree.list1[:]
                        print(
                            tempPerson.name + " " + tempPerson.surName + " & " + child.father + " " + tempPerson.surName)

        print("LEVEL - 2")
        for tempPerson in self.peopleList:
            a = self.getLevel(self, tempPerson)
            if (a == 2):
                # relation = self.getChild(self, tempPerson)
                relation = self.getChild(self, tempPerson, self.list1)

                if (len(Tree.list1) >= 1):
                    if (tempPerson.gender == "f"):
                        child = self.getPerson(self, self.list1[0].name, self.list1[0].surName)
                        del Tree.list1[:]
                        print(
                            tempPerson.name + " " + tempPerson.surName + " & " + child.father + " " + tempPerson.surName)

        print("LEVEL - 1")
        for tempPerson in self.peopleList:
            a = self.getLevel(self, tempPerson)
            if (a == 1):
                # relation = self.getChild(self, tempPerson)
                relation = self.getChild(self, tempPerson, self.list1)

                if (len(Tree.list1) >= 1):
                    if (tempPerson.gender == "f"):
                        child = self.getPerson(self, self.list1[0].name, self.list1[0].surName)
                        del Tree.list1[:]
                        print(
                            tempPerson.name + " " + tempPerson.surName + " & " + child.father + " " + tempPerson.surName)

        print("LEVEL - 0")
        for tempPerson in self.peopleList:
            a = self.getLevel(self,tempPerson)
            if( a == 0):
                print(tempPerson.name)

    def getLevel(self,person):
        self.getChild(self,person,self.list1)
        totalChildNumber = len(Tree.list1)
        #print("totalChildNumber =" + str(totalChildNumber ))
        if( totalChildNumber == 0 ):
            del Tree.list1[:]
            return 0
        else:
            for tempPerson in self.list1:
                self.getChild(self,tempPerson,self.list2)
            totalChildNumberC1 = len(Tree.list2)
            #print("totalChildNumberC1 =" + str(totalChildNumberC1))
            if( totalChildNumberC1 == 0):
                del Tree.list1[:]
                del Tree.list2[:]
                return 1
            else:
                for tempPerson in self.list2:
                    self.getChild(self, tempPerson,self.list3)
                totalChildNumberC2 = len(Tree.list3)
                #print("totalChildNumberC2 =" + str(totalChildNumberC2))
                if( totalChildNumberC2  == 0 ):
                    del Tree.list1[:]
                    del Tree.list2[:]
                    del Tree.list3[:]
                    return 2
                else:
                    for tempPerson in self.list3:
                        self.getChild(self,tempPerson,self.list4)
                totalChildNumberC3 = len(Tree.list4)
                #print("totalChildNumberC3 =" + str(totalChildNumberC3))
                if( totalChildNumberC3 == 0 ):
                    del Tree.list1[:]
                    del Tree.list2[:]
                    del Tree.list3[:]
                    del Tree.list4[:]
                    return 3
                else:
                    for tempPerson in self.list4:
                        self.getChild(self, tempPerson, self.list5)
                totalChildNumberC4 = len(Tree.list5)
                if (totalChildNumberC3 == totalChildNumberC4):
                    del Tree.list1[:]
                    del Tree.list2[:]
                    del Tree.list3[:]
                    del Tree.list4[:]
                    del Tree.list5[:]
                    return 3
                else:
                    del Tree.list1[:]
                    del Tree.list2[:]
                    del Tree.list3[:]
                    del Tree.list4[:]
                    del Tree.list5[:]
                    return 4

    def getPerson(self,person1Name,person1SurName):
        for TempPerson in self.peopleList:
            if(person1SurName==TempPerson.surName and person1Name==TempPerson.name):
                return TempPerson

    def getChild(self,searchPerson,list=[]):
        for TempPerson in self.peopleList:
            if(searchPerson.gender =="m"):
                if(TempPerson.father==searchPerson.name):
                    list.append(TempPerson)
            elif(searchPerson.gender=="f"):
                if(TempPerson.mother==searchPerson.name):
                    list.append(TempPerson)

    def testMarriageAge(self):
        for tempPerson in self.peopleList:
            relation = self.getChild(self, tempPerson, self.list1)

            if (len(Tree.list1) >= 1):
                if (tempPerson.gender == "f"):
                    child = self.getPerson(self, self.list1[0].name, self.list1[0].surName)
                    father = self.getPerson(self, child.father, child.surName)
                    mother = self.getPerson(self, child.mother, child.surName)
                    del Tree.list1[:]

                    if(mother and father):
                        if( mother.birthDate  and father.birthDate ):
                            if (1998 < int(mother.birthDate) or 1998 < int(father.birthDate)):
                                #print(tempPerson.name + " " + tempPerson.surName)
                                print("***---WARNING---***")
                                print("Unter 18 age marriage: " + mother.name + " " + mother.surName + " & " + father.name + " " + father.surName)
            del Tree.list1[:]

    def testAliveOrDead(self,searchPerson):
        if(searchPerson.deadDate<2016):
            print(searchPerson.name + " is dead!")
        else:
            print(searchPerson.name + " is alive!")

    def getDaughter(self,searchPerson):
        for TempPerson in self.peopleList:
            if(TempPerson.father==searchPerson.name and TempPerson.surName==searchPerson.surName and TempPerson.gender=="f"):
                return TempPerson
        return None

    def getSon(self,searchPerson):
        for TempPerson in self.peopleList:
            if(TempPerson.father==searchPerson.name and TempPerson.surName==searchPerson.surName and TempPerson.gender=="m"):
                return TempPerson
        return None

    def getMother(self,searchPerson):
        mother = self.getPerson(self, searchPerson.mother, searchPerson.surName)
        return mother

    def getFather(self,searchPerson):
        father = self.getPerson(self, searchPerson.father, searchPerson.surName)
        return father

    def getWife(self,searchPerson,list1=[]):
        relation = self.getChild(self, searchPerson, self.list1)
        if (len(Tree.list1) >= 1):
            child = self.getPerson(self, self.list1[0].name, self.list1[0].surName)
            del Tree.list1[:]
            wife = self.getPerson(self, child.mother, child.surName)
            return wife

    def getHusband(self,searchPerson, list1=[]):
        relation = self.getChild(self, searchPerson, self.list1)
        if (len(Tree.list1) >= 1):
            child = self.getPerson(self, self.list1[0].name, self.list1[0].surName)
            del Tree.list1[:]
            husband = self.getPerson(self, child.father, child.surName)
            return husband

    def findRelationship(self,person1, person2):
        #kişiler listede mevcut mu? kontrol ediliyor
        control = 0
        i=0
        l=0
        for tempPerson in self.peopleList:
            if(tempPerson.name==person1.name and tempPerson.surName==person1.surName):
                i=5
            if(tempPerson.name==person2.name and tempPerson.surName==person2.surName):
                l=7

        if(i+l==12):
            if((person1.father==person2.name!=None or person1.mother == person2.name!=None) and person1.gender=="m"):
                print("Son")
                control = 1
            elif ((person1.father == person2.name!=None or person1.mother == person2.name!=None) and person1.gender == "f"):
                print("Sister")
                control = 1
            elif(person1.name==person2.father!=None):
                print("Father")
                control = 1
            elif(person1.name==person2.mother!=None):
                print("Mother")
                control = 1
            elif(person1.father==person2.father!=None and person1.mother == person2.mother!=None and person2.gender=="f" and person1.father!=None and person2.father!=None):
                if (person1.birthDate > person2.birthDate):
                    print("Elder sister")
                    control = 1
                else:
                    print("Sister")
                    control = 1
            elif (person1.father == person2.father!=None and person1.mother == person2.mother!=None and person2.gender == "m"):
                if(person1.birthDate>person2.birthDate):
                    print("Brother")
                    control = 1
                else:
                    print("Brother")
                    control = 1
            else:
                relation = self.getWife(self, person2,self.list1)
                if (relation):
                    if (relation.father == person1.father!=None and relation.mother == person1.mother!=None and person1.gender=="m"):
                        print("Brother-in-law")
                        control = 1
                relation = self.getWife(self, person2,self.list1)
                if (relation):
                    if (relation.father == person1.father!=None and relation.mother == person1.mother!=None and person1.gender == "f" and person2.gender=="m"):
                        print("Sister-in-law")
                        control = 1
                relation = self.getWife(self, person1,self.list1)
                if (relation):
                    if (relation.father == person2.name!=None and person1.gender == "m"):
                        print("Son-in-law")
                        control = 1
                relation = self.getWife(self, person1,self.list1)
                if (relation):
                    if(relation.father==person2.father!=None and relation.mother==person2.mother!=None and person1.gender=="m"):
                        print("Brother-in-law")
                        control = 1
                relation=self.getMother(self,person2)
                if (relation):
                    if(relation.mother==person1.mother!=None and relation.father==person1.father!=None and person1.gender=="m"):
                        print("Uncle")
                        control = 1
                    elif(relation.mother==person1.mother!=None and relation.father==person1.father!=None and person1.gender == "f"):
                        print("Aunt")
                        control = 1
                relation = self.getMother(self, person1)
                if (relation):
                    if(relation.mother==person2.mother!=None and relation.father==person2.father!=None and person2.mother):
                        print("Nephew")
                        control = 1
                relation = self.getMother(self, person1)
                relation1 = self.getMother(self, person2)
                if (relation and relation1):
                    if (relation.mother == relation1.mother!=None and relation.father == relation1.father!=None and relation.name!=relation1.name and relation.surName!=relation1.surName):
                        print("Cousin")
                        control = 1
                relation = self.getFather(self, person2)
                if (relation):
                    if (relation.mother == person1.mother!=None and relation.father == person1.father!=None and person1.gender=="m"):
                        print("Uncle")
                        control = 1
                    if (relation.mother == person1.mother!=None and relation.father == person1.father!=None and person1.gender == "f"):
                        print("Aunt")
                        control = 1
                relation = self.getMother(self, person2)
                relation1 = self.getMother(self, person2)
                relation2 = self.getHusband(self,person1,self.list1)
                if((relation or relation1) and relation2):
                    if((relation2.father==relation.father!=None and person1.gender=="f" and relation2.mother==relation.mother!=None) or (relation2.father==relation1.father!=None and relation2.mother==relation1.mother!=None and person1.gender=="f")):
                        print("Sister-in-law")
                        control = 1
                relation = self.getWife(self,person1,self.list1)
                relation1 = self.getWife(self, person2,self.list1)
                if(relation and relation1):
                    if(relation.father==relation1.father!=None and relation.mother==relation1.mother!=None and person1.gender=="m" and person2.gender=="m"):
                        print("Brother-in-law")
                        control = 1
                relation = self.getHusband(self, person1,self.list1)
                relation1 = self.getHusband(self, person2,self.list1)
                if (relation and relation1):
                    if (relation.father == relation1.father!=None and relation.mother == relation1.mother!=None and person1.gender == "f" and person2.gender == "f"):
                         print("Sister-in-law")
                         control = 1
                relation = self.getHusband(self,person1,self.list1);
                if(relation):
                    if(relation.mother == person2.name!=None and relation.surName ==person2.surName!=None):
                        print("Daughter-in-law")
                        control = 1
                relation = self.getHusband(self, person2,self.list1);
                if (relation):
                   if (relation.mother == person1.name!=None and relation.surName == person1.surName!=None):
                       print("Mother-in-law")
                       control = 1
                relation = self.getWife(self, person2,self.list1)
                if (relation):
                   if (relation.father == person1.name!=None and person1.gender == "m"):
                       print("Father-in-law")
                       control = 1
                relation = self.getHusband(self,person1,self.list1)
                if(relation):
                    if(relation.father==person2.father!=None and relation.mother==person2.mother!=None and person1.gender=="f"):
                        print("Sister-in-law")
                        control=1
                if (control == 0):
                    print("There are not any relation between " + person1.name + " " + person1.surName + " and " + person2.name + " " + person2.surName)
        elif(i==5 and l==0):
            print(person2.name + " is not at the list")

        elif (i == 0 and l == 7):
            print(person1.name + " is not at the list")

        elif(i==0 and l==0):
            print("The both of two person are not at the list")