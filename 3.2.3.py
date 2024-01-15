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
    # This will store the results, which could be digits found near each '*'
    neighbors_info = []

    # Iterate through each star coordinate in stars_coordinates
    for star_row, star_col in stars_coordinates:
        # Initialize a list or other structure to hold information about this star's neighbors
        star_neighbors = []

        # Check the neighboring cells around the star
        # Remember to check in a 3x3 grid around the star
        for i in range(star_row - 1, star_row + 2):
            for j in range(star_col - 1, star_col + 2):
                # Skip the cell if it's the star itself
                if (i, j) != (star_row, star_col):
                    # Check if the neighboring cell contains a digit
                    if input_list[i][j].isdigit():
                        # If it's a digit, add its information to star_neighbors
                        # You might want to store the digit itself, its coordinates, or other relevant info
                        star_neighbors.append((i, j, input_list[i][j]))

        # Add the information about this star's neighbors to the overall list
        neighbors_info.append((star_row, star_col, star_neighbors))

    return neighbors_info
