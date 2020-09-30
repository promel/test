from person import Person
from datetime import datetime
try:
    file = open('file.txt', 'r'); 
    persons = []
    for line in file: 
        data = line.split('|')
        name  =  data[0]
        person = Person(name,data[1].replace('\n',''))
        persons.append(person)

    for index in range(len(persons)-1):
        if  persons[index].days > persons[index + 1].days:
            temp = persons[index]
            persons[index] = persons[index + 1]
            persons[index + 1] = temp    
    sum = 0
    for person in persons:
        print(person.name, person.date_of_birth, person.age) 
        sum += person.age
    print('Average:',round(sum/len(persons)))

except FileNotFoundError :
    print('File not found')
except ValueError :
    print('Date of birth incorrect')
except:
    print('Something went wrong')