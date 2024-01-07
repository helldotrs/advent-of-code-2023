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

def pad_list(to_be_padded, padding="."):
    to_be_padded = [padding + item + padding for item in to_be_padded] #tested. works.

    to_be_padded = [padding * len(to_be_padded[0])] + to_be_padded + [padding * len(to_be_padded[0])] #tested. works.

    return to_be_padded

data_list = pad_list(data_list)

numbers_list = []
current_number = ""

for x_pos, x_val in enumerate(data_list):
    for y_pos, y_val in enumerate(x_val):
        if y_val.isdigit():
            current_number += y_val
        elif current_number:
            numbers_list.append([current_number, [x_pos, y_pos - len(current_number)]])
            current_number = ""

# IMPORTANT: datatype for numbers_list[x][0] is STRING

print(data_list)
print(numbers_list)


