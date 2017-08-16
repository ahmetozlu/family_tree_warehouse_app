# Family Tree Warehouse Application

This is a Family Tree Warehouse Application (FTWA) : creates and manages family trees. FTWA keeps a track of the ancestral hierarchy of the user’s family. It was developed with "Pythonic Approach" in Python ([Python 3.0](https://www.python.org/download/releases/3.0/)) programming language on [PyCharm IDE](https://www.jetbrains.com/pycharm/) .

These several rules that were implemented:

- Users can add new members to the family tree and update people in family tree.

- It maintains only one family tree.

- Each person keeps the following information: gender [male, female], name [string], surname [string], birth date [date], death date [date], father [one person], mother [one person], children [zero or more child]

- Users can add any person as child, mother, or father. Any other relationship is prohibited while entering. So, you can calculate relationships when asked by the user.

- Users can be create a placeholder person [record] to any place which has no or few available information, e.g. with just the name.

- Users can be reach the following information: alive or dead, age, the level in the family tree. This program will calculate this information when asked by the user.

- Users can ask the relationship between 2 people.

- The application can display the tree as meaningful diagram, when asked. The diagram are informative enough.

- The application can display the relationship types in Turkish (you can use [dictionary](translate.google.com) to get them in English). The following types can be supported.

    - Anne, Baba, Oğul, Kız, Erkek Kardeş, Kız Kardeş, Abla, Abi
    
    - Amca, Hala, Dayı, Teyze

    - Yeğen, Kuzen

    - Enişte, Yenge

    - Kayınvalide, Kayınpeder, Gelin, Damat

    - Bacanak, Baldız, Elti, Kayınbirader
    
- Anyone can marry with anyone in the family tree except father, mother, sibling, uncle, aunt and grandparents

- Birth and death dates are realistic. For instance, a person cannot have a child after he/she dies. The application do not allow non-realistic birth and death dates.

- The application gives warnings when any of the spouse is below 18 years old.

***
See for more technical details to this report: [report-ftwa.pdf](https://github.com/ahmetozlu/FamilyTree/files/1228917/report-ftwa.pdf)
***

## Author
Ahmet Özlü

## License
This system is available under the MIT license. See the LICENSE file for more info.


<p align="center">
  <img src="https://user-images.githubusercontent.com/22610163/29375212-7bd586e4-82b4-11e7-99a2-45f04c282dbf.png">
</p>
