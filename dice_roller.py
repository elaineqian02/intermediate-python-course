import random

def main():
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  dice_sum = 0

  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll

    if roll == 1:
      print(f'You rolled a {roll}! Critical Fail')
    elif roll == dice_size:
      print(f'You rolled a {roll}! Critical Success!')
    else:
      print(f'You rolled a {roll}')
  
  print(f'You have rolled a total of {dice_sum}')

def main2():
  dice_rolls = 2
  dice_sum, num_rolls = 0, 0

  while True:
    roll = random.randint(1,6)
    dice_sum += roll
    num_rolls += 1
    
    if roll == 1:
      print(f'You rolled a {roll}! Critical Fail')
    elif roll == 6:
      print(f'You rolled a {roll}! Critical Success!')
      break;
    else:
      print(f'You rolled a {roll}')
  
  print(f'You have rolled a total of {dice_sum} in {num_rolls} rolls')

if __name__== "__main__":
  main()