import re

data_str = """Game 1: 4 blue, 4 red, 16 green; 14 green, 5 red; 1 blue, 3 red, 5 green
Game 2: 3 green, 8 red, 1 blue; 5 green, 6 blue; 4 green, 4 blue, 10 red; 2 green, 6 red, 4 blue; 8 red, 11 blue, 4 green; 10 red, 10 blue"""

#snip

"""Game 3: 7 blue, 2 green; 9 blue, 2 green, 4 red; 5 blue, 2 red; 1 red, 1 green, 10 blue; 1 green, 5 blue, 1 red
Game 4: 5 green, 4 blue, 15 red; 1 green, 5 blue, 2 red; 14 red, 3 blue, 2 green; 6 red, 12 green, 1 blue; 1 blue, 6 green, 16 red
Game 5: 1 red, 1 blue, 4 green; 3 blue, 2 green, 4 red; 4 blue, 1 red, 2 green; 1 green, 3 red, 4 blue; 1 green, 2 blue
Game 6: 17 red, 2 blue, 18 green; 4 green, 10 blue, 14 red; 10 blue, 15 green, 14 red; 6 blue, 9 red; 5 blue, 7 red, 10 green
Game 7: 2 green, 3 red, 14 blue; 3 red, 2 green, 6 blue; 3 blue, 1 red; 10 blue, 1 green; 3 green, 17 blue
Game 8: 9 blue, 13 green, 2 red; 3 red, 10 green, 18 blue; 8 blue, 8 green
Game 9: 11 red, 2 blue; 1 blue, 9 green, 13 red; 2 blue, 17 red, 6 green
Game 10: 13 green, 8 red, 8 blue; 10 red, 5 blue, 9 green; 3 blue, 2 green, 1 red; 5 blue, 1 red, 10 green; 10 red, 8 blue; 8 blue, 1 green
Game 11: 14 red, 19 green; 2 blue, 6 red, 17 green; 12 green, 9 red, 6 blue"""

data_list = data_str.split("\n")
print(11111111)
print(data_list)

data_list = [ item.split(": ")[1] for item in data_list ]
print(22222222)
print(data_list)

data_list = [ re.split("; |, ", item) for item in data_list ]
print(33333333)
print(data_list)

for row in data_list:
    for col in row: 
     print(col[0] + col[2])

print('---')
print(data_list)
