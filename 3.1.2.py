input_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

input_data = input_data.split("\n")

total = 0

#add a dot at the beginning and end of each row
for i in range(len(input_data)):
    input_data[i] = "." + input_data[i] + "."

#add a dot at the beginning and end of each column
input_data.insert(0, "." * len(input_data[0]))

#every number (number is defined as a full number, NOT a single digit) in the grid that is next to atleast one non-dot should be added to total
for i in range(len(input_data)):
    for j in range(len(input_data[i])):
        if input_data[i][j] != ".":
            if input_data[i][j-1] != "." or input_data[i][j+1] != "." or input_data[i-1][j] != "." or input_data[i+1][j] != ".":
                total += int(input_data[i][j])



print(total)