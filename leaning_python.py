print('''the big
black
box''')
value_1 = 'bear'
value_2 = 'cheetah'
print(value_1, value_2)
print(value_1 + value_2)
character_1 = input('Enter the first character: ')
character_2 = input('Name for the second charcter: ')
print(character_1+ ': Hi',character_2,'how are you?')
print(character_2+':',character_1,'I am fine, thank you!')
letter = input('Type a letter to use for the Christmas tree: ')
print('  ' + letter)
print(' ' + letter + letter + letter)
print(letter + letter + letter + letter + letter)
print('  |  ')
name = 'Pierre'
email = 'pierre@gmail.com'
age = 50
height = 72
print('His name is ' + name)
print(name + ' can be contacted at ' + email)
print('He is ' + str(age) + ' years old and is ' + str(height) + ' inches tall')
revenue = int(input('Business revenue: '))
cost = int(input('Business costs: '))
profit = revenue - cost
print('The business profit is: ' + str(profit))
cost_bar = '#' * int((cost / revenue) * 25)
profit_bar = '#' * int((profit / revenue) * 25)
print('  cost: ' + cost_bar)
print('profit: ' + profit_bar)
# String indexing
city = 'San Francisco'
value_index = int(input('Enter an index value: '))
letter = city[value_index]
print(letter)
text = input('Type anything: ')
print('The last two words of you input were: ' + text[-2]+text[-1])
# Doing math in Python
x = 100 + 100
y = 100 / 2
print( type(x) )
print( type(y) )