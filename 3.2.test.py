a = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
*.....755.
...$.*....
.664.598.."""

data_list = a.split("\n")

result_list = []

#find all numbers
for row in data_list:
    current_number = ""

    for char in row:
        if char.isdigit():
            current_number += char
        elif current_number:
            result_list.append(int(current_number))
            current_number = ""

# Check for any remaining number at the end of a row
if current_number:
    result_list.append(int(current_number))

print(result_list)

#psudo
for x in range(first_digit_pos[-1], last_digit_pos[+1]):
    for y in range(first_digit_pos[x][-1], last_digit_pos[x][+1]):
        print(x, y) #ok, tired, continue tomorrow

for x_pos, x in enumerate(data_list):
    for y_pos, y in enumerate(data_list):
        print(ypos, y)