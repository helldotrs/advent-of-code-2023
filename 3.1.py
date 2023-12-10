sample_input = """
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
"""

input = sample_input

blanks = [".",
          " ",
          "\n"]

#function to extract numbers that have a non-blank neighbor and replace them with one x per digit
def vertical_extract_numbers(input):
    output = ""
    for i in range(len(input)):
        if input[i] in blanks:
            output += input[i]
        elif input[i-1] in blanks or input[i+1] in blanks:
            output += input[i]
        else:
            output += "x"*len(input[i])
    return output

print(vertical_extract_numbers(input))