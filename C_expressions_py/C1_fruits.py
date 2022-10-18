"""
The assignment will demonstrate Python's built-in collection types:
- List []: ordered, mutable, duplicates
- Set {}: unordered, mutable, no duplicates
- Tuple (): ordered, imutable, duplicates
- Dictonary[key]: unordered, mutable, no duplicate keys
"""


fruit_List = ['banana', 'apple', 'orange', 'banana', 'pineapple']
fruit_Set  = {'banana', 'apple', 'orange', 'banana', 'pineapple'}
fruit_Tuple= ('banana', 'apple', 'orange', 'banana', 'pineapple')
fruit_Dict = {10: 'banana', 20: 'apple', 30: 'orange', 40: 'banana', 20: 'pineapple'}
fruit_Dict2 = {'banana': 10, 'apple': 20, 'orange': 30, 'banana': 40, 'pineapple': 20}
#
# print(f'fruit_List:  {fruit_List}')
# print(f'fruit_Set:   {fruit_Set}')
# print(f'fruit_Tuple: {fruit_Tuple}')
# print(f'fruit_Dict:  {fruit_Dict}')
# print(f'fruit_Dict2: {fruit_Dict2}')

bag = fruit_List
print(f'bag of fruits of type {str(type(bag))[8:-2].upper()}:')
for fruit in fruit_List:
    num = 0
    for f in bag:
        if f==fruit:
            num += 1
    print(f' - counted {num} x {fruit}')

print()

