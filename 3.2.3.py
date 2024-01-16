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

def check_star_neighbors(input_list, stars_coordinates):
    neighbors_info = []

    for star_row, star_col in stars_coordinates:
        star_neighbors = []

        for i in range(star_row - 1, star_row + 2):
            for j in range(star_col - 1, star_col + 2):
                # Check if the neighboring cell contains a digit
                # Note: We include the star's own cell in this check for simplicity. 
                # Since it's always '*', it won't affect our digit search.
                if input_list[i][j].isdigit():
                    star_neighbors.append((i, j, input_list[i][j]))

        neighbors_info.append((star_row, star_col, star_neighbors))

    return neighbors_info

def is_part_of_larger_number(coord, input_list):
    # Extract row and column indices from coord
    row, col = coord

    # Check if the digit is part of a larger number
    # We need to check the cells to the left, right, above, and below the digit
    # Since we're only interested in horizontal or vertical numbers, not diagonal

    # Check left (if not on the left edge and the left cell is a digit)
    if col > 0 and input_list[row][col - 1].isdigit():
        return True  # The digit is part of a larger number

    # Check right (if not on the right edge and the right cell is a digit)
    if col < len(input_list[row]) - 1 and input_list[row][col + 1].isdigit():
        return True

    # Check above (if not on the top edge and the above cell is a digit)
    if row > 0 and input_list[row - 1][col].isdigit():
        return True

    # Check below (if not on the bottom edge and the below cell is a digit)
    if row < len(input_list) - 1 and input_list[row + 1][col].isdigit():
        return True

    # If none of the adjacent cells are digits, the digit is not part of a larger number
    return False


neighbors_list = check_star_neighbors(data_list, star_list)
