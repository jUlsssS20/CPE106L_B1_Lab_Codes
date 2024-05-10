"""
File: student.py
Resources to manage a student's name and test scores.
"""
import random
class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    def __eq__(self, other):
        return self.name == other.name
    
    def __lt__(self, other):
        return self.name < other.name
    
    def __ge__(self, other):
        return self.name >= other.name

def main():
    listofstudents = []
    """A simple test."""
    Mico = Student("Mico", 4)
    for i in range(1, 5):
        Mico.setScore(i, 100)
    listofstudents.append(Mico)

    Chris = Student("Chris", 4)
    for i in range(1, 5):
        Chris.setScore(i,100)
    listofstudents.append(Chris)
    
    Juls = Student("Juls", 4)
    for i in range(1, 5):
        Juls.setScore(i,100)
    listofstudents.append(Juls)
        
    Nick = Student("Nick", 3)
    for i in range(1, 4):
        Nick.setScore(i,100)
    listofstudents.append(Nick)

    random.shuffle(listofstudents)
    print("shuffled", end="->")
    for student in listofstudents:
        print (student.getName(), end =" ")

    listofstudents.sort()
    print ("Sorted" , end="->")
    for student in listofstudents:
        print (student.getName(), end = " ")
    print("Printing students")
    for persons in listofstudents:
        print(persons)


if __name__ == "__main__":
    main()