import fileinput
import string
import re
import copy


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

  crates_part_two = copy.deepcopy(crates)

  for move in moves:
    for _ in range(move['move']):
      to_be_moved = crates[move['from']].pop()
      crates[move['to']].append(to_be_moved)

    to_be_moved_part_two = crates_part_two[move['from']][-move['move']:]
    for _ in range(move['move']):
      crates_part_two[move['from']].pop()
    crates_part_two[move['to']].extend(to_be_moved_part_two)

  print('Part one:', [item[-1] for item in crates.values()])
  print('Part two:', [item[-1] for item in crates_part_two.values()])
    

def day_06():
  # datastream = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
  with open('datastream.txt') as file:
    datastream = file.readlines()
  datastream = datastream[0].strip()
  
  marker_length = 14  # 4 for part one
  marker = [''] * marker_length
  
  for index, char in enumerate(datastream):
    marker.pop(0)
    marker.append(char)
    if len(set(marker)) == marker_length and '' not in marker:
      break
  
  print('Part two:', index + 1, marker)


def day_07():
  with open('exploring_filesystem.txt') as file:
    lines = file.readlines()
  lines = [line.strip() for line in lines]

  current_directory = None
  upper_level = None
  path = []
  dir_sizes = dict()

  for line in lines:
    if line.startswith('$ cd'):
      current_directory = line.split(' ')[2]
      if current_directory == '..':
        path.pop()
      else:
        path.append(current_directory)
      if '/'.join(path) not in dir_sizes:
        dir_sizes['/'.join(path)] = 0
    elif line[0].isdigit():
      for i in range(len(path)):
          dir_sizes['/'.join(path[:i+1])] += int(line.split(' ')[0])
  print('Part one:', sum([size for size in dir_sizes.values() if size <= 100000]))

  total_disk_space = 70_000_000
  total_needed_disk_space = 30_000_000
  currently_free_space = total_disk_space - dir_sizes['/']
  must_free = total_needed_disk_space - currently_free_space
  size_of_chosen_dir = total_disk_space

  for dir, size in dir_sizes.items():
    if size >= must_free and size < size_of_chosen_dir:
      size_of_chosen_dir = size
  print('Part two:', size_of_chosen_dir)


def day_08():
  with open('trees.txt') as f:
    trees = [[int(num) for num in line.strip()] for line in f]

  all_trees = len(trees) * len(trees[0])
  print(all_trees)
  non_visible_trees = 0

  for i in range(1, len(trees) - 1):
    for j in range(1, len(trees[0]) - 1):
      visible_from_north = any(trees[i][j] <= tree for tree in [row[j] for row in trees[:i]])
      visible_from_south = any(trees[i][j] <= tree for tree in [row[j] for row in trees[i+1:]])
      visible_from_east = any(trees[i][j] <= tree for tree in trees[i][:j])
      visible_from_west = any(trees[i][j] <= tree for tree in trees[i][j+1:])
      if visible_from_north and visible_from_south and \
        visible_from_east and visible_from_west:
          non_visible_trees += 1

  visible_trees = all_trees - non_visible_trees
  print('Part one:', visible_trees)

def main():
  day_08()


if __name__ == "__main__":
  main()
