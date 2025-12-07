with open('input.txt', 'r') as my_file:
    puzzle_input = my_file.read()

count = 0

for ranges, ingredient_ids in [puzzle_input.split("\n\n")]:
    ingredient_ids = ingredient_ids.split()
    ingredients_int = list(map(int, ingredient_ids))

    for ingredient in ingredients_int:
        for each_range in ranges.split():
            range_start, range_end = each_range.split("-")
            if int(range_start) <= ingredient <= int(range_end):
                count += 1
                break
            else:
                continue


print(count)


            


