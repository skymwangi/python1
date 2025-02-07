# list datastructure
# list are mutable
# list are ordered
# list are indexed
fruits=['pear','apple','watermelon','mango','kiwi',
        'grapefruit']
fruits[0]= "kiwi"
numbers=[1,2,3,4,5,6,7,8,9,]
numbers2=[65,90,7.6,21,6,-9,-54,0,333]
numbers2.sort(reverse=True)
print(numbers2)
print(fruits)
numbers.append(11)
print(numbers)
print(f"I love eating {fruits[3]}")
# tuple datastructures
# tuples are immutable(unchanged)
# tuples are ordered
# tuples are indexed
cars=('audi','toyota','subaru','jeep')
print(cars)
nambari=(3,0,-5,-694,88,7,9,1,234566,5,-8,43,112)
print(nambari)
print(sorted(nambari))
# set datastructure
# set are unordered
# set are not indexed

computers={'dell','hp','macbook','lenovo','ibm','acer','toshiba'}
computers.add('google')
computers.remove('hp')

print(computers)
num1={1,2,3}
num2={4,5,6}
union_set=num1.union(num2)
print(union_set)
# dictionaries data structures
student={'Name': 'Joseph', 'Age':43, 'Gender': 'Male',
         'School':"Kenyatta University"}
print(f"Student name: {student['Name']}")
print(f"Student Age:{student['Age']}")
print(f"Student Gender: {student['Gender']}")
print(f"School:{student['School']}")