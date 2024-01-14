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

def find_stars(input_list):
    stars_coordinates = []

    # Iterate through each row in the input_list
    for row_index in range(len(input_list)):
        # Iterate through each character in the current row
        for char_index in range(len(input_list[row_index])):
            # Check if the current character is '*'
            if input_list[row_index][char_index] == '*':
                # If it's a '*', add its coordinates (row_index, char_index) to the list
                stars_coordinates.append((row_index, char_index))

    # Return the list of coordinates
    return stars_coordinates


star_list = find_stars(data_list)
