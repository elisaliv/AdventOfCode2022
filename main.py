import fileinput
import string


def day_01():
  max_calories = 0
  second_max = 0
  third_max = 0
  calories = 0

  with fileinput.input(files=('calories.txt')) as f:
    for line in f:
      if line != '\n':
        calories += int(line)
      else:
        if calories >= third_max and calories < second_max:
          third_max = calories
        if calories >= second_max and calories < max_calories:
          third_max = second_max
          second_max = calories
        if calories >= max_calories:
          third_max = second_max
          second_max = max_calories
          max_calories = calories

        print('Calories carried by elf:', calories)
        print('Max calories so far:', max_calories)
        print('Second max:', second_max)
        print('Third max:', third_max)
        calories = 0

  print('Max calories:', max_calories)
  print('Total top three calories:', max_calories + second_max + third_max)


def day_02():
  score = 0
  new_score = 0
  
  with fileinput.input(files=('rps.txt')) as f:
    for line in f:
      opponent_move = line[0]
      my_move = line[2]
      
      if my_move == 'X':  # rock... OR I lose
        score = score + 1
        # new_score += 0
        if opponent_move == 'A':  # rock
          score = score + 3
          new_score = new_score + 3  # I am scissors
        elif opponent_move == 'B':  # paper
          # score += 0
          new_score = new_score + 1  # I am rock
        elif opponent_move == 'C':  # scissors
          score = score + 6
          new_score = new_score + 2  # I am paper
          
      elif my_move == 'Y':  # paper... OR draw
        score = score + 2
        new_score = new_score + 3
        if opponent_move == 'A':  # rock
          score = score + 6
          new_score = new_score + 1  # I am rock
        elif opponent_move == 'B':  # paper
          score = score + 3
          new_score = new_score + 2  # I am paper
        elif opponent_move == 'C':  # scissors
          # score += 0
          new_score = new_score + 3  # I am scissors
          
      elif my_move == 'Z':  # scissors... OR I win
        score = score + 3
        new_score = new_score + 6
        if opponent_move == 'A':  # rock
          # score += 0
          new_score = new_score + 2  # I am paper
        elif opponent_move == 'B':  # paper
          score = score + 6
          new_score = new_score + 3  # I am scissors
        elif opponent_move == 'C':  # scissors
          score = score + 3
          new_score = new_score + 1  # I am rock

    print('Score for part one:', score)
    print('Score for part two:', new_score)


def day_03():
  priorities_dict = dict(zip(
    list(string.ascii_lowercase) + list(string.ascii_uppercase), 
    range(1, 53)))
  sum_priorities = 0
  
  with open('rucksacks.txt') as file:
    rucksacks = file.readlines()
    
  for rucksack in rucksacks:
    rucksack = rucksack.strip()
    rucksack_size = len(rucksack)
    compartment_size = int(rucksack_size / 2)
    # ! I am assuming that all string lengths are even
    first_compartment = rucksack[:compartment_size]
    second_compartment = rucksack[compartment_size:]
    common_item_types = set(first_compartment)\
      .intersection(second_compartment)
    for type in common_item_types:
      sum_priorities += priorities_dict.get(type)
  print('Part one:', sum_priorities)


def main():
  day_03()


if __name__ == "__main__":
  main()
