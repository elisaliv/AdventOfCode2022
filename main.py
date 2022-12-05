import fileinput
import string
import re


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
  sum_badges = 0
  
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

  for index, rucksack in enumerate(rucksacks):
    rucksack = rucksack.strip()
    if index % 3 == 0:
      first_rucksack = rucksack
    elif index % 3 == 1:
      second_rucksack = rucksack
    else:
      third_rucksack = rucksack
      common_item_in_group = set(first_rucksack)\
        .intersection(second_rucksack)\
        .intersection(third_rucksack)
      for type in common_item_in_group:
        sum_badges += priorities_dict.get(type)
  print('Part two:', sum_badges)


def day_04():
  completely_overlapping_pairs = 0
  overlapping_pairs = 0
  with open('pairs.txt') as file:
    lines = file.readlines()

  for line in lines:
    pairs = line.split(',')
    first_elf_range = list(map(int, pairs[0].split('-')))
    second_elf_range = list(map(int, pairs[1].split('-')))
    if (first_elf_range[0] <= second_elf_range[0] 
        and first_elf_range[1] >= second_elf_range[1]) \
      or (second_elf_range[0] <= first_elf_range[0] 
          and second_elf_range[1] >= first_elf_range[1]):
      completely_overlapping_pairs += 1
            
    first_elf_sections = set(range(first_elf_range[0], first_elf_range[1] + 1))
    second_elf_sections = set(range(second_elf_range[0], second_elf_range[1] + 1))
    if (len(first_elf_sections.intersection(second_elf_sections)) != 0):
      overlapping_pairs += 1

  print('Part one:', completely_overlapping_pairs)
  print('Part two:', overlapping_pairs)


def day_05():
  with open('crates.txt') as file:
    all_file = file.readlines()
  all_file = [line[:-1] for line in all_file]

  blank_index = all_file.index('')
  crates_raw = [line.split(',') for line in all_file[:blank_index]]
  crates_raw = [[line.strip() for line in crate] for crate in crates_raw]
  crates = dict(zip(range(1, len(crates_raw) + 1), crates_raw))
  moves_raw = all_file[blank_index + 1:]
  moves = [dict(zip(['move', 'from', 'to'], re.findall(r'\d+', line))) for line in moves_raw]
  moves = [dict([a, int(x)] for a, x in b.items()) for b in moves]

  for move in moves:
    for crate in range(move['move']):
      to_be_moved = crates[move['from']].pop()
      crates[move['to']].append(to_be_moved)

  print('Part one:', [item[-1] for item in crates.values()])
    

def main():
  day_05()


if __name__ == "__main__":
  main()
