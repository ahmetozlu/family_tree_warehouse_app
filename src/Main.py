#----------------------------------------------
#--- Author         : Ahmet Özlü
#--- Mail           : ahmetozlu93@gmail.com
#--- Date           : 1st August 2017
#----------------------------------------------

from Person import Person
from Tree import Tree
import datetime

# !!!
# the default family is created // change it with yours
# !!!
person1 = Person("Ahmet","Özlü","m",1993,2050, "Aziz", "Gülsen")
person2 = Person("Aziz","Özlü","m",1958,2030,"Hasan","Sıdıka")
person3 = Person("Gülsen","Özlü","f",1948,2048)
person4 = Person("Hasan","Özlü","m",1980)
person5 = Person("Öznur","Tanış","f",2000,2060, "Aziz", "Gülsen")
person6 = Person("Hakan","Tanış","m",1980,2044,"Namık Kemal","Saniye")
person7 = Person("Elif","Tanış","f",2015,2080,"Hakan","Öznur")
person8 = Person("Yiğit","Tanış","m",2016,2080,"Hakan","Öznur")
person9 = Person("İlknur","Karabag","f",1983,2058, "Aziz", "Gülsen")
person10 = Person("Abdullah","Karabag","m",1980,2065, "Ekrem", "Neriman")
person11 = Person("Nurullah","Karabag","m",2010,2080, "Abdullah", "İlknur")
person12 = Person("Büşra","Karabag","f",2015,2058, "Abdullah", "İlknur")
person13 = Person("Mehmet","Karabag","m",1988,2022, "Ekrem", "Neriman")
person14 = Person("Filiz","Karabag","f",1990,2036, "Nazif", "Nafiye")
person15 = Person("Numan","Karabag","m",2014,2088, "Mehmet", "Filiz")
person16 = Person("Nazif","Şişli","m",1980,2019)
person17 = Person("Nafiye","Şişli","f",1985,2020)
person18 = Person("Ekrem","Karabag","m",1961,2014)
person19 = Person("Neriman","Karabag","f",1964,2023)
person20 = Person("Fatma","Keser","f",1981,2054,"Ekrem","Neriman")
person21 = Person("Selami","Keser","m",1984,2023)
person22 = Person("Merve","Özlü","f",1991,2028)
person23 = Person("Kuzey","Özlü","m",2018,2099,"Ahmet","Merve")
person24 = Person("İlker","Özlü","m",1990,2099,"Aziz","Gülsen")
person25 = Person("Hatice","Özlü","f",1990,2088)
person26 = Person("Melih","Özlü","m",2015,2025,"İlker","Hatice")
person27 = Person("Sıdıka","Özlü","f",1928,1999)

Tree.addPerson(Tree,person1)
Tree.addPerson(Tree,person2)
Tree.addPerson(Tree,person3)
Tree.addPerson(Tree,person4)
Tree.addPerson(Tree,person5)
Tree.addPerson(Tree,person6)
Tree.addPerson(Tree,person7)
Tree.addPerson(Tree,person8)
Tree.addPerson(Tree,person9)
Tree.addPerson(Tree,person10)
Tree.addPerson(Tree,person11)
Tree.addPerson(Tree,person12)
Tree.addPerson(Tree,person13)
Tree.addPerson(Tree,person14)
Tree.addPerson(Tree,person15)
Tree.addPerson(Tree,person16)
Tree.addPerson(Tree,person17)
Tree.addPerson(Tree,person18)
Tree.addPerson(Tree,person19)
Tree.addPerson(Tree,person20)
Tree.addPerson(Tree,person21)
Tree.addPerson(Tree,person22)
Tree.addPerson(Tree,person23)
Tree.addPerson(Tree,person24)
Tree.addPerson(Tree,person25)
Tree.addPerson(Tree,person26)
Tree.addPerson(Tree,person27)

# test the relations
print("1")
Tree.findRelationship(Tree,person7,person18)
print("2")
Tree.findRelationship(Tree,person2,person1)
print("3")
Tree.findRelationship(Tree,person1,person3)
print("4")
Tree.findRelationship(Tree,person3,person1)
print("5")
Tree.findRelationship(Tree,person1,person5)
print("6")
Tree.findRelationship(Tree,person7,person6)
print("7")
Tree.findRelationship(Tree,person6,person7)
print("8")
Tree.findRelationship(Tree,person6,person8)
print("9")
Tree.findRelationship(Tree,person8,person7)
print("10")
Tree.findRelationship(Tree,person1,person8)
print("11")
Tree.findRelationship(Tree,person8,person9)
print("12")
Tree.findRelationship(Tree,person6,person1)
print("13")
Tree.findRelationship(Tree,person6,person2)
print("14")
Tree.findRelationship(Tree,person1,person6)
print("15")
Tree.findRelationship(Tree,person9,person6)
print("16")
Tree.findRelationship(Tree,person11,person8)
print("17")
Tree.findRelationship(Tree,person13,person11)
print("18")
Tree.findRelationship(Tree,person20,person11)
print("19")
Tree.findRelationship(Tree,person22,person11)
print("20")
Tree.findRelationship(Tree,person6,person10)
print("21")
Tree.findRelationship(Tree,person25,person22)
print("22")
Tree.findRelationship(Tree,person22,person3)
print("23")
Tree.findRelationship(Tree,person3,person22)
print("24")
Tree.findRelationship(Tree,person2,person6)
print("25")
Tree.findRelationship(Tree,person7,person6)
print("26")
Tree.findRelationship(Tree,person9,person14)

ans = True
while ans:
    print("1-)Ask relation")
    print("2-)Add/Delete/Update person")
    print("3-)Get information of any person")
    print("4-)Print the family tree")
    print("5-)Terminate the program")

    ans = input("Please choose an operation!\n")

    Tree.testMarriageAge(Tree)
    Tree.setChildren(Tree)

    if(ans=="1"):
        print("***You chose 'Ask a relation'***")
        person1Name = input("Enter the first person name: ")
        person1SurName = input("Enter the first person surname: ")
        print("First person = " + person1Name + " " + person1SurName + "\n")
        person2Name = input("Enter the second person name: ")
        person2SurName = input("Enter the second person surname: ")
        person1 = Tree.getPerson(Tree,person1Name,person1SurName)
        person2 = Tree.getPerson(Tree, person2Name, person2SurName)
        if(person1 and person2):
            Tree.findRelationship(Tree,person1,person2)
        elif(not person1 or not person2):
            print("The person/persons which you are entered is not in the family tree!")

    elif(ans=="2"):
        print("1-)Add person")
        print("2-)Delete person")
        print("3-)Update person")
        ans = input("Please choose an operation!\n")
        if(ans == "1"):
            print("***You chose 'Add person'***")
            choosePersonTypeToAdd = input("Select person type to add\n1.)Add placeholder person\n2.)I want to add father \n3.)I want to add mother\n4.)I want to add child")
            if(choosePersonTypeToAdd == "1" ):
                name = input("Enter the name: ")
                surName = input("Enter the surname: ")
                gender = input("Enter the gender: ")
                birthDate = input("Enter the birthDate: ")
                deadDate = input("Enter the deadDate: ")

                fatherName = input("Enter the father name: ")
                motherName = input("Enter the mother name: ")
                child = input("Enter the child number: ")

                empx = Person(name, surName, gender, birthDate, deadDate, fatherName, motherName, child)
                empx.displayPerson()
                Tree.addPerson(Tree,empx)

            if(choosePersonTypeToAdd == "2"):
                surName = input("Enter the surname: ")
                fatherName = input("Enter the father name: ")

                childName = input("Enter the child name: ")
                childPerson = Tree.getPerson(Tree, childName, surName)

                if(childPerson):
                    relation = Tree.getFather(Tree,childPerson)
                    if(relation):
                        print("That child has already a father!!")
                    else:
                        childPerson.father = fatherName

                        birthDate = input("Enter the birth date")
                        if(childPerson.birthDate and birthDate):
                            if( childPerson.birthDate<birthDate ):
                                print("The child birthdate can not be bigger than father birthdate!")
                            else:
                                deadDate = input("Enter the dead date")

                                fatherFatherName = input("Enter the father name of the father person")
                                fatherMotherName = input("Enter the mother name of the father person")

                                empx = Person(fatherName, surName, "m", birthDate, deadDate, fatherFatherName, fatherMotherName)
                                Tree.addPerson(Tree, empx)
                                Tree.setChildren(Tree)
                                empx.displayPerson()
                        else:
                            deadDate = input("Enter the dead date")

                            fatherFatherName = input("Enter the father name of the father person")
                            fatherMotherName = input("Enter the mother name of the father person")

                            empx = Person(fatherName, surName, "m", birthDate, deadDate, fatherFatherName,fatherMotherName)
                            Tree.addPerson(Tree, empx)
                            Tree.setChildren(Tree)
                            empx.displayPerson()

                else:
                    print("There are not any child whose name is " + childName + " and surname is " + surName + "!")

            if (choosePersonTypeToAdd == "3"):
                surName = input("Enter the surname: ")
                motherName = input("Enter the mother name: ")

                childName = input("Enter the child name")
                childPerson = Tree.getPerson(Tree, childName, surName)

                if (childPerson):
                    relation = Tree.getMother(Tree, childPerson)
                    if (relation):
                        print("That child has already a mother!!")
                    else:
                        childPerson.mother = motherName

                        birthDate = input("Enter the birth date")
                        if(childPerson.birthDate and birthDate):
                            if(childPerson.birthDate < birthDate):
                                print("The child birthdate can not be bigger than mother birthdate!")
                            else:
                                deadDate = input("Enter the dead date")

                                motherMotherName = input("Enter the father name of the mother person")
                                motherMotherName = input("Enter the mother name of the mother person")

                                empx = Person(motherName, surName, "f", birthDate, deadDate, motherMotherName, motherMotherName)
                                Tree.addPerson(Tree, empx)
                                Tree.setChildren(Tree)
                                empx.displayPerson()
                        else:
                            deadDate = input("Enter the dead date")

                            motherMotherName = input("Enter the father name of the mother person")
                            motherMotherName = input("Enter the mother name of the mother person")

                            empx = Person(motherName, surName, "m", birthDate, deadDate, motherMotherName,motherMotherName)
                            Tree.addPerson(Tree, empx)
                            Tree.setChildren(Tree)
                            empx.displayPerson()
                else:
                    print("There are not any child whose name is " + childName + " and surname is " + surName + "!")

            if(choosePersonTypeToAdd == "4"): #doğru eş seçimleri yapıldımı mesela anne veya baba listede varmı kontrol edilmeli
                surName = input("Enter the surname: ")
                fatherName = input("Enter the father name: ")
                motherName = input("Enter the mother name: ")
                fatherPerson = Tree.getPerson(Tree,fatherName,surName)
                motherPerson = Tree.getPerson(Tree, motherName, surName)
                control =0
                if(fatherPerson and motherPerson):
                    if(motherPerson.father==fatherPerson.name!=None):
                        print("Baba-kız evlenemez")
                        control=1
                    elif(fatherPerson.mother==motherPerson.name!=None):
                        print("Anne-oğul evlenemez")
                        control = 1
                    elif(fatherPerson.father==motherPerson.father!=None and fatherPerson.mother==motherPerson.mother!=None and fatherPerson.father and motherPerson.father and fatherPerson.mother and motherPerson.mother):
                        print("Kardeşler evlenemez")
                        control = 1
                    relation = Tree.getFather(Tree, motherPerson)
                    if (relation):
                        if (relation.mother == fatherPerson.mother!=None and relation.father == fatherPerson.father!=None and fatherPerson.gender == "m"):
                            print("Amca-yeğen evlenemez")
                            control = 1

                    relation = Tree.getFather(Tree,fatherPerson)
                    relation1 = Tree.getHusband(Tree,motherPerson)
                    if(relation and relation1):
                        if(relation.father==relation1.father!=None and relation.mother==relation1.mother!=None and relation.surName==relation1.surName!=None):
                            print("Hala-yeğen evlenemez")
                            control = 1

                    relation = Tree.getFather(Tree,fatherPerson)
                    if(relation):
                        if(motherPerson.name==relation.mother!=None and motherPerson.surName==relation.Surname!=None):
                            print("Büyükanne-torun evlenemez")
                            control = 1

                    relation =Tree.getMother(Tree,fatherPerson)
                    if(relation):
                        if(relation.mother==motherPerson.name!=None):
                            print("Büyükanne-torun evlenemez")
                            control = 1

                    relation =Tree.getMother(Tree,motherPerson)
                    if(relation):
                        if(relation.father==fatherPerson.name!=None):
                            print("Büyükbaba-torun evlenemez")
                            control = 1

                    relation =Tree.getFather(Tree,motherPerson)
                    if(relation):
                        if(relation.father==fatherPerson.name!=None):
                            print("Büyükbaba-torun evlenemez")
                            control = 1

                    relation = Tree.getHusband(Tree, motherPerson, Tree.list1)
                    if (relation):
                        if (relation.father == fatherPerson.father != None and relation.mother == fatherPerson.mother != None and motherPerson.gender == "f"):
                            print("Kişi yengesi ile evlenemez")
                            control = 1

                    if( control != 1):
                        childName = input("Enter the child name: ")
                        childSurName = surName
                        childGender = input("Enter the child gender: ")
                        childBirthDate = input("Enter the child birthday: ")

                        controlChild =0

                        if(fatherPerson.deadDate and childBirthDate):
                            if(int(fatherPerson.deadDate) < int(childBirthDate)):
                                print("A person cannot have a child after he dies")
                                controlChild=1
                        if( fatherPerson.birthDate and childBirthDate ):
                            if(int(fatherPerson.birthDate) > int(childBirthDate)):
                                print("Child birthdate can not be less than father birthdate!")
                                controlChild = 1

                        if (motherPerson.deadDate and childBirthDate):
                            if (int(motherPerson.deadDate) < int(childBirthDate)):
                                print("A person cannot have a child after she dies")
                                controlChild = 1

                        if( motherPerson.birthDate and childBirthDate ):
                            if(int(motherPerson.birthDate) > int(childBirthDate)):
                                print("Child birthdate can not be less than mother birthdate!")
                                controlChild = 1

                        if( controlChild !=1 ):
                            childDeadDate = input("Enter the child dead date: ")

                            print("Father: " + fatherName + " " + surName)
                            print("Mother: " + motherName + " " + surName)
                            childChildrenNumber = input("Enter the child children number: ")
                            empx = Person(childName, surName, childGender, childBirthDate, childDeadDate, fatherName,motherName)
                            empx.displayPerson()
                            Tree.addPerson(Tree, empx)

                    else:
                        if (control != 1):
                            childDeadDate = input("Enter the child dead date: ")

                            print("Father: " + fatherName + " " + surName)
                            print("Mother: " + motherName + " " + surName)
                            childChildrenNumber = input("Enter the child children number: ")
                            empx = Person(childName,surName,childGender,childBirthDate,childDeadDate,fatherName,motherName)
                            empx.displayPerson()
                            Tree.addPerson(Tree, empx)

                else:
                    print("The child is not added because father/mother which you are entered is not in the family tree!")

        elif( ans == "2"):
            print("***You chose 'Delete person'***")
            name = input("Enter the name: ")
            surName = input("Enter the surname: ")
            deletePerson = Tree.getPerson(Tree, name, surName)
            if (deletePerson):
                Tree.deletePerson(Tree, deletePerson)
            else:
                print("The person which you are entered is not in the family tree!")

        elif( ans == "3" ):
            print("***You chose 'Update person'***")
            name = input("Enter the name: ")
            surName = input("Enter the surname: ")
            updatePerson = Tree.getPerson(Tree, name, surName)
            if( updatePerson ):
                print("Now, you should enter person information to update!")
                updatePerson.name = input("Enter the name: ")
                updatePerson.surName = input("Enter the surname: ")
                updatePerson.gender = input("Enter the gender: ")

                try:
                    birthDate = int(input("Enter the birthDate: "))
                    deadDate = int(input("Enter the deadDate: "))

                    if (birthDate > deadDate):
                        print("Birth date can not be bigger than dead date")
                    else:
                        updatePerson.birthDate = birthDate
                        updatePerson.deadDate = deadDate
                        updatePerson.fatherName = input("Enter the father name: ")
                        updatePerson.motherName = input("Enter the mother name: ")
                        updatePerson.child = input("Enter the child number: ")

                except ValueError:
                    print("Birth/Dead date which you are entered is not an int!")
            else:
                print("There are not person whose *name: " + name + " and *surname: " + surName)

    elif(ans == '3'):
        print("***You chose 'Get information of any person'***")
        personName = input("Enter the person name: ")
        personSurName = input("Enter the person surname: ")

        person = Tree.getPerson(Tree, personName, personSurName)
        if(person):
            person.displayPerson()
            now = datetime.datetime.now()
            if( person.deadDate and person.birthDate ):
                age = now.year - int(person.birthDate)
                print("Age: " + str(age))


                now = datetime.datetime.now()
                if( int(person.deadDate) < now.year ):
                    print("ALIVE or DEAD: DEAD")
                else:
                    print("AlIVE or DEAD: ALIVE")
            elif( person.birthDate and not person.deadDate ):
                print("AlIVE or DEAD: ? " + person.name + " was birth at " + str(person.birthDate) + " but dead date is unknown!!!")
            elif (not person.birthDate and person.deadDate):
                print(
                    "AlIVE or DEAD: " + person.name + " was dead at " + str(person.deadDate) + " but birth date is unknown!!!")
            elif( not person.deadDate and not person.birthDate ):
                print("AlIVE or DEAD: The birthdate and dead date is unknown for " + person.name + " " + person.surName)

            print("Total child count: " + str(person.children))

            level = Tree.getLevel(Tree, person)
            print("Level in the tree: " + str(level))
        else:
            print("There are not person whose *name: " + personName + " and *surname: " + personSurName)

    elif( ans == '4'):
        print("***You chose 'Print the family tree'***")
        Tree.printTreeAlternatively(Tree)

    elif( ans == '5' ):
        print("The program was terminated!")
        ans = False