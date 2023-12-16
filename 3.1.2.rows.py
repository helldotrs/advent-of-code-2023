numbers_2d_list = [[[0],False]]

for row_index, row in enumerate(input_data):
    if row_index == 0 or row_index == len(input_data) - 1:
        continue
    first_digit = True
    for char_index, char in enumerate(row):
        if not char.isdigit():
            first_digit = True
            continue
        if first_digit:
            #create new instance in numbers_2d_list where [[char],False]
            numbers_2d_list.append([[char],False])
        else:
            #append char to last instance in numbers_2d_list
            numbers_2d_list[-1][0].append(char)

        first_digit = False

        #if the same char index in the row above or below is a digit or an x, set the instance in numbers_2d_list to True
        if input_data[row_index-1][char_index].isdigit() or input_data[row_index-1][char_index] == "x":
            numbers_2d_list[-1][1] = True
        elif input_data[row_index+1][char_index].isdigit() or input_data[row_index+1][char_index] == "x":
            numbers_2d_list[-1][1] = True

# in  numbers_2d_list, remove all instances where [1] == False
numbers_2d_list = [number for number in numbers_2d_list if number[1]]

# in numbers_2d_list for each instance, add the numbers together as if strings (e.g. ["1","2","3"] becomes "123") then convert to int
numbers_2d_list = [int("".join(number[0])) for number in numbers_2d_list]

# sum all numbers in numbers_2d_list
subtotal = sum(numbers_2d_list)

total += subtotal