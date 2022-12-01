import fileinput

max_calories = 0
calories = 0

with fileinput.input(files=('calories.txt')) as f:
    for line in f:
      if line != '\n':
        calories += int(line)
      else:
        if calories > max_calories:
          max_calories = calories
        print('Calories carried by elf:', calories)
        print('Max calories so far:', max_calories)
        calories = 0

print('Max calories:', max_calories)