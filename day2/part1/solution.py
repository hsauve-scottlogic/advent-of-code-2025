with open('input.txt', 'r') as my_file:
    puzzle_input = my_file.read()

dups_list = []

for element in puzzle_input.split(','):

    for start, end in [element.split('-')]:

        number_range = range(int(start), (int(end) + 1))

        for each in number_range:
            each_string = str(each)

            if len(each_string) % 2 == 0:

                first_half, second_half = each_string[0:int(len(each_string) / 2)], each_string[int(len(each_string) / 2)::]
                

                if first_half == second_half:
                    dups_list.append(each)

print(sum(dups_list))