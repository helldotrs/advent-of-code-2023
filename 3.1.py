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

input = input.split("\n")

blanks = [".",
          " ",
          "\n"]

#psudo code:
def check_rows(input):
    output = []
    for row in input:
        if row not in blanks:
            output.append(row)

#psudo code:
solution = 0
def rows(input)
    output = """"""

    for number in row(input)
        #number is defined as a full number, NOT a single digit
        if number has x-axis-neighboring non-blanks
        solution += number
        output.replace number with "x"
    return output

def columns(input):
    output = """"""
    for number in column(input)
        #number is defined as a full number, NOT a single digit
        if number has y-axis-neighboring non-blanks
        solution += number
        output.replace number with "x"
    return output

print(solution)