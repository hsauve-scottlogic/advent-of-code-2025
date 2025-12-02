with open('input.txt', 'r') as my_file:
    data_into_list = my_file.read().splitlines()


dial=50

count=0

for element in data_into_list:
    rotation_distance = int(element[1:])

    if element.startswith("L"):
        dial = dial - rotation_distance
        if dial % 100 == 0:
            count+=1

    elif element.startswith("R"):
        dial = dial + rotation_distance
        if dial % 100 == 0:
            count+=1

print(count)
