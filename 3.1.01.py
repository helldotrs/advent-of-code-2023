
"""The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?"""

input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def print_list(in_list, divider=False):
    for item in in_list:
        print(item)
        if divider:
            print("!!")

### start creating data_raw[]
data_raw = input.split("\n") #tested. works.

data_raw = ["." + item + "." for item in data_raw] #tested. works.

data_raw = ["." * len(data_raw[0])] + data_raw + ["." * len(data_raw[0])] #tested. works.
### end creating data_raw[]

### create data_map. e for empty, d for digit, o for other. future: x for eXtracted. n for number
data_map    = ["".join(
            "e" if element == "."
            else
            "d" if element.isdigit()
            else
            "o"
            for element in row)
            for row in data_raw] #tested. works.

#create data_nums
data_nums = []

for iterator, item in enumerate(data_raw): #tested. works.
    jterator = 0
    num_len = 0

    for jterator, jtem in enumerate(item):
        if jtem.isdigit():
            num_len += 1
        else:
            if num_len > 0:
                data_nums.append([iterator, jterator - num_len, num_len])
                num_len = 0

    if num_len > 0:
        data_nums.append([iterator, jterator - num_len, num_len])


###tests
print(data_raw)
print_list(data_map)
print(data_nums)
