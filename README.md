# My-first-classes-eritage-cascade-in-pyton
Define the following classes:
1. A Date Birth class with three attributes, day, month, year and a ToString method which converts the date of birth into a character string
2. A Person class with three attributes, last name, first name and date of birth and a polymorphic Show method to display the data for each person.
3. An Employee class which derives from the Person class, with the addition of a Salary attribute and the redefinition of the Show method.
4. A Chef class which derives from the Employee class, with the addition of a Service attribute and the redefinition of the Show method.
Execution example:
P=Person ("ALLAQUI", "ILYAS", Birthdate(1, 7, 1982))
P.display()
E=Employee("NAJAHI", "FATIMA", BirthDate (1,7,1985), 7865.548)
E.display()
Ch=Chief("ELOMARI", "ANAS", BirthDate (1,7,1988), 7865.548, "Resourc
e human")
Ch.display()
