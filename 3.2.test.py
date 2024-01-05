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

