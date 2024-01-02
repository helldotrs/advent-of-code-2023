
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

total    = 0

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

#create data_nums #data_nums[x_pos, y_pos, len]
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


#extract numbers with x neighbors:
for item in data_nums: #tested. works. #FIXME - priority:low - BUT adjusted by MLLM, and uses .isdigit() instead of checking data_map
    digits = ""

    data_char_left = data_map[item[0]][item[1] - 1] if item[1] > 0 else ''
    data_char_right = data_map[item[0]][item[1] + item[2]]

    if data_char_left == "o" or data_char_right == "o":
        digits = ''.join([c if c.isdigit() else 'x' for c in data_raw[item[0]][item[1]:item[1] + item[2]]])
        total += int(digits)

        # Replace digits with 'x' in data_map
        data_map[item[0]] = data_map[item[0]][:item[1]] + 'x' * item[2] + data_map[item[0]][item[1] + item[2]:]

#extract numbers with y neighbors:
for item in data_nums:
    data_char_top = data_map[item[0] - 1][item[1] : item[1] + item[2]] if item[0] > 0 else ''
    data_char_bottom = data_map[item[0] + 1][item[1] : item[1] + item[2]] if item[0] < len(data_map) - 1 else ''

    if any(char != 'e' for char in data_char_top + data_char_bottom):
        number = data_raw[item[0]][item[1] : item[1] + item[2]]
        total += int(number)

        # Replace the entire number with 'x' in data_map
        data_map[item[0]] = data_map[item[0]][:item[1]] + 'x' * item[2] + data_map[item[0]][item[1] + item[2]:]
"""
I got output 2547, doing this math, this was correct: 
35 + 633 + 617 + 664 + 598

this is where I reread and realized we also need to check for diagonals
this is why I have been stuck... ffs.
"""
for item in data_nums:
    x, y, length = item
    first_digit = data_raw[x][y]
    last_digit = data_raw[x][y + length - 1]

    # Check for diagonals only for the first and last digit
    if (
        (x > 0 and y > 0 and data_map[x - 1][y - 1] not in ('e', 'd', 'x')) or
        (x > 0 and y + length < len(data_map[x]) - 1 and data_map[x - 1][y + length] not in ('e', 'd', 'x')) or
        (x + 1 < len(data_map) and y > 0 and data_map[x + 1][y - 1] not in ('e', 'd', 'x')) or
        (x + 1 < len(data_map) and y + length < len(data_map[x]) - 1 and data_map[x + 1][y + length] not in ('e', 'd', 'x'))
    ):
        total += int(data_raw[x][y : y + length])

        # Replace the entire number with 'x' in data_map
        data_map[x] = data_map[x][:y] + 'x' * length + data_map[x][y + length:]





###tests
print_list(data_raw)
print_list(data_map)
print_list(data_nums)

print(f"data_raw = {data_raw}")
print(f"data_map = {data_map}")
print(f"data_nums = {data_nums}")
print(total)